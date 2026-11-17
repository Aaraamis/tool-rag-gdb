import copy
import json
from pathlib import Path

from rag_gdb import extraction
from rag_gdb.extraction import validate_dir, validate_extraction

SHA = "a" * 64
CITA = "Se solicita incluir el archivo de estructura de carpetas"
MANIFEST = {"archivos": [{"ruta": "IDU/doc.pdf", "sha256": SHA}]}
PAGES = ["Texto de portada sin observaciones.",
         "OBSERVACIÓN IDU: Se solicita incluir el archivo\nde estructura  de “carpetas” en D.23."]


def _data(**changes):
    obs = {"id": "obs-001", "numero": "1", "autor": "idu", "radicado_origen": None,
           "pagina": 2, "cita": CITA, "resumen": "Incluir el reporte de carpetas.",
           "estado_en_documento": "atendida", "requiere_cotejo_visual": False}
    obs.update(changes)
    return {"version": 1, "documento": {"ruta": "IDU/doc.pdf", "sha256": SHA},
            "extraido_por": "prueba", "observaciones": [obs]}


def _validate(data, monkeypatch, pages=PAGES, relative=None):
    monkeypatch.setattr(extraction, "page_texts", lambda pdf: pages)
    return validate_extraction(data, MANIFEST, Path("/pdf"), relative)


def test_valid_extraction_tolerates_line_breaks_quotes_and_case(monkeypatch):
    assert _validate(_data(), monkeypatch) == []


def test_quote_on_another_page_names_the_right_page(monkeypatch):
    errors = _validate(_data(pagina=1), monkeypatch)
    assert errors == ["obs-001: la cita no está en la página 1; aparece en la página 2"]


def test_quote_absent_and_page_out_of_range(monkeypatch):
    assert "no aparece en ninguna página" in _validate(
        _data(cita="Texto que el documento nunca dice"), monkeypatch)[0]
    assert "fuera del PDF" in _validate(_data(pagina=3), monkeypatch)[0]


def test_visual_observation_skips_text_check(monkeypatch):
    assert _validate(_data(pagina=1, requiere_cotejo_visual=True), monkeypatch) == []


def test_schema_rejects_bad_enum_short_quote_and_missing_field(monkeypatch):
    assert _validate(_data(autor="obra"), monkeypatch)
    assert _validate(_data(cita="muy corta"), monkeypatch)
    data = _data()
    del data["observaciones"][0]["pagina"]
    assert any("pagina" in e for e in _validate(data, monkeypatch))


def test_hash_path_and_duplicate_ids_are_checked(monkeypatch):
    data = _data()
    data["documento"]["sha256"] = "b" * 64
    assert _validate(data, monkeypatch) == ["documento.sha256 no coincide con el manifiesto"]
    data = _data()
    data["documento"]["ruta"] = "IDU/otro.pdf"
    assert "no está en el manifiesto" in _validate(data, monkeypatch)[0]
    data = _data()
    data["observaciones"].append(copy.deepcopy(data["observaciones"][0]))
    assert _validate(data, monkeypatch) == ["id repetido: obs-001"]
    assert "debe llamarse IDU/doc.json" in _validate(_data(), monkeypatch, relative="IDU/mal")[0]


def test_validate_dir_reports_per_file(tmp_path, monkeypatch):
    monkeypatch.setattr(extraction, "page_texts", lambda pdf: PAGES)
    (tmp_path / "IDU").mkdir()
    (tmp_path / "IDU/doc.json").write_text(json.dumps(_data()))
    (tmp_path / "IDU/roto.json").write_text("{no es json")
    results = validate_dir(tmp_path, MANIFEST, tmp_path)
    assert results["IDU/doc.json"] == []
    assert "JSON inválido" in results["IDU/roto.json"][0]
