import csv
import json

import numpy as np
import pytest

from rag_gdb.checklist import render
from rag_gdb.consolidation import group, load_observations, read_decisions, read_overrides, summarize


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
    groups, review = group(V, KEYS, {frozenset(("a", "b")): "no"}, auto=0.9, floor=0.85)
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
    groups, review = group(v, keys, auto=0.99, floor=0.85)
    assert review  # {a,b} y {c,d} quedan por revisar
    _, review = group(v, keys, {frozenset(("a", "c")): "no"}, auto=0.99, floor=0.85)
    assert review == []
