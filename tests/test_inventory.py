import json
import zipfile
from pathlib import Path

from rag_gdb.inventory import build_manifest, read_inventory
from rag_gdb.pipeline import convert_selected, profile_manifest


def make_ods(path: Path, digest: str) -> None:
    cells = lambda values: "".join(f'<table:table-cell><text:p>{v}</text:p></table:table-cell>' for v in values)
    headers = ["clave", "tipo", "nombre", "sha256", "estado", "remitente", "asunto"]
    rows = [["a", "pdf", "uno.pdf", digest, "DESCARGADO", "test@ejemplo.com", "Revisión GDB"],
            ["b", "pdf", "dos.pdf", "f" * 64, "DESCARGADO", "", ""]]
    xml = ('<office:document-content xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" '
           'xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" '
           'xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"><office:body>'
           '<office:spreadsheet><table:table table:name="Inventario">'
           + ''.join(f'<table:table-row>{cells(row)}</table:table-row>' for row in [headers, *rows])
           + '</table:table></office:spreadsheet></office:body></office:document-content>')
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("content.xml", xml)


def test_manifest_matches_hash_and_keeps_missing(tmp_path):
    import hashlib

    pdfs = tmp_path / "pdfs"
    pdfs.mkdir()
    (pdfs / "renombrado.pdf").write_bytes(b"documento")
    (pdfs / "huerfano.pdf").write_bytes(b"otro")
    ods = tmp_path / "inventario.ods"
    make_ods(ods, hashlib.sha256(b"documento").hexdigest())
    assert len(read_inventory(ods)) == 2
    result = build_manifest(pdfs, ods)
    assert result["resumen"]["coincidentes"] == 1
    assert result["resumen"]["huerfanos"] == 1
    assert result["resumen"]["ausentes_descargados"] == 1
    assert result["ausentes"][0]["motivo"].endswith("pendiente_de_confirmacion")


def test_conversion_skips_completed_and_retries_failed(tmp_path, monkeypatch):
    from rag_gdb import pipeline

    pdfs = tmp_path / "pdfs"
    pdfs.mkdir()
    (pdfs / "uno.pdf").write_bytes(b"documento")
    ods = tmp_path / "inventario.ods"
    import hashlib
    make_ods(ods, hashlib.sha256(b"documento").hexdigest())
    manifest = build_manifest(pdfs, ods)
    calls = []

    def fake_convert(source, json_path, md_path):
        calls.append(source)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text("{}")
        md_path.write_text("texto")

    monkeypatch.setattr(pipeline, "convert_one", fake_convert)
    out = tmp_path / "convertidos"
    convert_selected(manifest, pdfs, out, ["uno.pdf"])
    convert_selected(manifest, pdfs, out, ["uno.pdf"])
    assert len(calls) == 1
    assert json.loads((out / "estado.json").read_text())["documentos"]["uno.pdf"]["estado"] == "ok"


def test_subject_filter_records_reason(tmp_path):
    import hashlib
    pdfs = tmp_path / "pdfs"
    pdfs.mkdir()
    (pdfs / "uno.pdf").write_bytes(b"documento")
    ods = tmp_path / "inventario.ods"
    make_ods(ods, hashlib.sha256(b"documento").hexdigest())
    result = build_manifest(pdfs, ods, {"remitentes": ["@ejemplo.com"]})
    assert result["archivos"][0]["estado"] == "excluido"
    assert result["archivos"][0]["motivo_exclusion"] == "remitente:@ejemplo.com"


def test_profile_removes_paths_absent_from_current_manifest(tmp_path, monkeypatch):
    from rag_gdb import pipeline

    output = tmp_path / "perfiles.json"
    output.write_text(json.dumps({"documentos": {
        "nombre_alterado.pdf": {"sha256": "abc", "estado": "ok"},
        "nombre_correcto.pdf": {"sha256": "abc", "estado": "ok", "paginas": 1},
    }}))
    monkeypatch.setattr(pipeline, "profile_pdf", lambda path: None)
    manifest = {"archivos": [{"ruta": "nombre_correcto.pdf", "sha256": "abc"}]}

    result = profile_manifest(manifest, tmp_path, output)

    assert list(result["documentos"]) == ["nombre_correcto.pdf"]
    assert list(json.loads(output.read_text())["documentos"]) == ["nombre_correcto.pdf"]
