import json

import numpy as np
import pytest

from rag_gdb.checklist import render
from rag_gdb.consolidation import group, load_observations, read_decisions, read_overrides, summarize
from rag_gdb.normative_links import group_key


def _unit(*rows):
    m = np.array(rows, dtype=float)
    return m / np.linalg.norm(m, axis=1, keepdims=True)


# a≈b (0.95), b≈c (0.95) pero a y c lejos (0.8): sin piso se encadenarían.
V = _unit([1, 0, 0], [0.95, 0.31, 0], [0.8, 0.6, 0], [0, 0, 1])
KEYS = ["a", "b", "c", "d"]


def test_floor_prevents_chaining_and_reports_review_pair():
    groups, review = group(V, KEYS, auto=0.9, floor=0.85)
    assert sorted(map(sorted, groups)) == [[0, 1], [2], [3]]
    assert [(i, j) for i, j, _ in review] == [(1, 2)]


def test_manual_decisions_force_or_block_merges():
    # la unión forzada se aplica primero; después el piso impide sumar b (lejano de d)
    groups, _ = group(V, KEYS, {frozenset(("a", "d")): "si"}, auto=0.9, floor=0.85)
    assert sorted(map(sorted, groups)) == [[0, 3], [1, 2]]
    groups, _ = group(V, KEYS, {frozenset(("a", "b")): "no"}, auto=0.9, floor=0.85)
    assert [0, 1] not in map(sorted, groups)


def test_decision_and_override_files_are_validated(tmp_path):
    path = tmp_path / "pares.csv"
    path.write_text("clave_a,clave_b,decision,nota\na,b,quizas,x\n")
    with pytest.raises(ValueError):
        read_decisions(path)
    themes = [{"tema": "T01"}]
    over = tmp_path / "temas.csv"
    over.write_text("clave,tema,nota\na,T99,x\n")
    with pytest.raises(ValueError):
        read_overrides(over, themes)


def _obs(clave, ruta, autor, radicado, resumen="Requisito de prueba"):
    return {"clave": clave, "ruta": ruta, "id": "obs-001", "autor": autor, "radicado_origen": radicado,
            "pagina": 1, "cita": f"Cita literal de {clave} en el documento", "resumen": resumen,
            "estado_en_documento": "sin_estado"}


def test_frequency_counts_distinct_idu_radicados_not_copies():
    obs = [_obs("a", "IDU/memo.pdf", "idu", "DTE 1"), _obs("b", "IDU/copia.pdf", "idu", "DTE 1"),
           _obs("c", "IDU/otro.pdf", "idu", "DTE 2"), _obs("d", "IDU/c1443.pdf", "interventoria", None)]
    themes = [{"tema": "T01", "nombre": "Uno"}, {"tema": "T02", "nombre": "Dos"}]
    tv = _unit([1, 0, 0], [0, 1, 0])
    vectors = _unit([1, 0.1, 0], [1, 0.1, 0], [1, 0.2, 0], [1, 0, 0.1])
    (g,) = summarize(obs, vectors, [[0, 1, 2, 3]], themes, tv, {"d": "T02"})
    assert g["frecuencia_idu"] == 2 and g["documentos"] == 4 and g["documentos_interventoria"] == 1
    assert g["tema"] == "T02" and g["tema_manual"] and g["miembros"][0]["autor"] == "idu"
    md = render({"temas": themes, "grupos": [g]}, today="2026-11-17")
    assert "IDU ×2 · interventoría ×1" in md and md.count("  - «") == 2  # ejemplos de radicados distintos
    key = group_key(g)
    md = render({"temas": themes, "grupos": [g]}, today="2026-11-17",
                normative_links={key: [{"id": "N1", "tipo": "directo", "texto": "Regla oficial"}]},
                reviewed_links={key})
    assert "Normativa directo: **N1**" in md and "los demás quedan marcados" not in md


def test_load_observations_skips_state_and_gives_stable_keys(tmp_path):
    doc = {"version": 1, "documento": {"ruta": "IDU/x.pdf", "sha256": "f" * 64}, "extraido_por": "t",
           "observaciones": [_obs("a", "", "idu", None) | {"cita": "Una cita literal suficientemente larga"}]}
    (tmp_path / "IDU").mkdir()
    (tmp_path / "IDU/x.json").write_text(json.dumps(doc))
    (tmp_path / "estado.json").write_text("{}")
    first = load_observations(tmp_path)
    assert len(first) == 1 and first[0]["ruta"] == "IDU/x.pdf"
    assert load_observations(tmp_path)[0]["clave"] == first[0]["clave"]


def test_no_between_two_members_closes_review_between_their_groups():
    v = _unit([1, 0, 0], [1, 0.05, 0], [0.9, 0.44, 0], [0.9, 0.45, 0])
    keys = ["a", "b", "c", "d"]
    _, review = group(v, keys, auto=0.99, floor=0.85)
    assert review  # {a,b} y {c,d} quedan por revisar
    _, review = group(v, keys, {frozenset(("a", "c")): "no"}, auto=0.99, floor=0.85)
    assert review == []


def test_editorial_wording_merges_groups_into_one_requirement(tmp_path):
    from rag_gdb.checklist import read_editorial
    themes = [{"tema": "T01", "nombre": "Uno"}, {"tema": "T02", "nombre": "Dos"}]
    g1 = {"grupo": "G001", "tema": "T01", "representante": "uno", "frecuencia_idu": 1, "documentos": 1,
          "documentos_interventoria": 0, "miembros": [_obs("a", "IDU/m1.pdf", "idu", "DTE 1") | {"clave": "a"}]}
    g2 = {"grupo": "G002", "tema": "T01", "representante": "dos", "frecuencia_idu": 1, "documentos": 1,
          "documentos_interventoria": 0, "miembros": [_obs("b", "IDU/m2.pdf", "idu", "DTE 2") | {"clave": "b"}]}
    path = tmp_path / "redaccion.csv"
    path.write_text("clave_grupo,grupo,tema_grupo,requisito_id,tema,requisito\n"
                    f"{group_key(g1)},G001,T01,R-T02-01,T02,Requisito único\n"
                    f"{group_key(g2)},G002,T01,R-T02-01,T02,Requisito único\n", encoding="utf-8")
    editorial = read_editorial(path)
    md = render({"temas": themes, "grupos": [g1, g2]}, today="2026-11-18",
                normative_links={group_key(g1): [{"id": "N1", "tipo": "directo", "texto": "Regla"}]},
                reviewed_links={group_key(g1), group_key(g2)}, editorial=editorial)
    assert "**R-T02-01** Requisito único. — IDU ×2 `G001` `G002`" in md
    assert "## T02. Dos" in md and "Normativa directo: **N1**" in md and "Práctica" not in md
    md = render({"temas": themes, "grupos": [g1, g2]}, today="2026-11-18", normative_links={},
                reviewed_links={group_key(g1), group_key(g2)}, editorial=editorial)
    practices = md.split("## Prácticas observadas sin respaldo escrito localizado")
    assert len(practices) == 2 and "**R-T02-01** (T02) Requisito único" in practices[1]
    assert "## T02. Dos" not in md
    bad = tmp_path / "mal.csv"
    bad.write_text("clave_grupo,grupo,tema_grupo,requisito_id,tema,requisito\n"
                   "k1,G001,T01,R1,T01,Texto A\nk2,G002,T01,R1,T01,Texto B\n", encoding="utf-8")
    with pytest.raises(ValueError, match="distintos"):
        read_editorial(bad)
