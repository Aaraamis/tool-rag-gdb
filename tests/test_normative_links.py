from pathlib import Path

import numpy as np
import pytest

from rag_gdb.normative_links import propose_links, rank_links, read_link_decisions, review_links


def test_rank_links_orders_cosine_similarity():
    groups = np.array([[1.0, 0.0], [0.0, 1.0]])
    requirements = np.array([[1.0, 0.0], [0.6, 0.8], [0.0, 1.0]])

    ranked = rank_links(groups, requirements, top_k=2)

    assert [index for index, _ in ranked[0]] == [0, 1]
    assert [index for index, _ in ranked[1]] == [2, 1]


def test_rank_links_rejects_empty_limit():
    with pytest.raises(ValueError, match="positivo"):
        rank_links(np.eye(1), np.eye(1), top_k=0)


def test_propose_links_writes_auditable_csv(tmp_path: Path):
    groups = tmp_path / "groups.json"
    catalog = tmp_path / "catalog.json"
    groups.write_text('{"grupos":[{"grupo":"G001","tema":"T01","representante":"carpetas",'
                      '"miembros":[{"clave":"abc"}]}]}', encoding="utf-8")
    catalog.write_text('[{"id":"N1","fuente":"Guía","seccion":"S1","texto":"carpetas"}]',
                       encoding="utf-8")

    result = propose_links(groups, catalog, tmp_path / "links.csv", tmp_path / "cache.json",
                           lambda texts: [[1.0, 0.0] for _ in texts], "fake", top_k=1)

    output = (tmp_path / "links.csv").read_text(encoding="utf-8")
    assert result["candidatos"] == 1
    assert "clave_grupo,grupo,tema" in output
    assert "N1" in output


def test_review_links_filters_invalid_choices_and_resumes(tmp_path: Path):
    candidates = tmp_path / "candidates.csv"
    candidates.write_text(
        "clave_grupo,grupo,tema,resumen_grupo,rango,fuente,requisito_id,seccion,texto_normativo,similitud,decision\n"
        "key,G001,T01,Entregar carpetas,1,Guía,N1,S1,Entregar estructura,0.8,\n"
        "key,G001,T01,Entregar carpetas,2,Guía,N2,S2,Otro requisito,0.7,\n", encoding="utf-8")
    calls = []

    def ask(prompt):
        calls.append(prompt)
        return ('{"grupos":[{"clave_grupo":"key","enlaces":['
                '{"requisito_id":"N1","tipo":"directo","motivo":"Coincide."},'
                '{"requisito_id":"inventado","tipo":"directo","motivo":"No."}]}]}')

    output, state = tmp_path / "review.csv", tmp_path / "state.json"
    result = review_links(candidates, output, state, "Casos: {casos}", ask, "fake")
    review_links(candidates, output, state, "Casos: {casos}", ask, "fake")

    assert result["enlaces_sugeridos"] == 1
    assert len(calls) == 1
    assert "N1,directo" in output.read_text(encoding="utf-8")


def test_review_links_records_service_failure_for_retry(tmp_path: Path):
    candidates = tmp_path / "candidates.csv"
    candidates.write_text(
        "clave_grupo,grupo,tema,resumen_grupo,rango,fuente,requisito_id,seccion,texto_normativo,similitud,decision\n"
        "key,G001,T01,Carpetas,1,Guía,N1,S1,Regla,0.8,\n", encoding="utf-8")

    result = review_links(candidates, tmp_path / "out.csv", tmp_path / "state.json",
                          "{casos}", lambda prompt: (_ for _ in ()).throw(OSError("servicio")),
                          "fake")

    assert result["errores"] == 1


def test_read_link_decisions_validates_and_returns_confirmed(tmp_path: Path):
    path = tmp_path / "links.csv"
    path.write_text("clave_grupo,grupo,requisito_id,decision,tipo,nota\n"
                    "key,G001,N1,si,directo,confirmado\n"
                    "key,G001,N2,no,,descartado\n", encoding="utf-8")
    links, reviewed = read_link_decisions(path, [
        {"id": "N1", "fuente": "G", "seccion": "S", "texto": "Uno"},
        {"id": "N2", "fuente": "G", "seccion": "S", "texto": "Dos"},
    ])

    assert reviewed == {"key"}
    assert links["key"][0]["tipo"] == "directo"


def test_decisions_follow_groups_after_reconsolidation(tmp_path: Path):
    from rag_gdb.normative_links import current_keys, group_key, register_groups, remap_decisions
    import json
    old = [{"miembros": [{"clave": "a"}, {"clave": "b"}]}, {"miembros": [{"clave": "c"}, {"clave": "d"}]}]
    path = tmp_path / "grupos.json"
    path.write_text(json.dumps({"grupos": old}), encoding="utf-8")
    registry = tmp_path / "registro.csv"
    assert register_groups(path, registry) == {"grupos": 2, "registrados": 2}
    assert register_groups(path, registry)["registrados"] == 0
    grown = {"miembros": [{"clave": "a"}, {"clave": "b"}, {"clave": "nueva"}]}
    split = [{"miembros": [{"clave": "c"}]}, {"miembros": [{"clave": "d"}]}]
    from rag_gdb.normative_links import read_group_registry
    mapping = current_keys([grown, *split], read_group_registry(registry))
    k1, k2 = group_key(old[0]), group_key(old[1])
    links, reviewed = remap_decisions({k1: [{"id": "N1"}]}, {k1, k2}, mapping)
    assert links == {group_key(grown): [{"id": "N1"}]}
    assert reviewed == {group_key(grown)}
