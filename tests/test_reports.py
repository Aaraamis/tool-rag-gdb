from rag_gdb.reports import build_informe, date_of, read_contracts, render_informe, render_matriz


def test_contracts_come_from_reviewed_csv_and_date_from_name(tmp_path):
    path = tmp_path / "contratos.csv"
    path.write_text("sha256,ruta,contrato,evidencia\nx,IDU/a.pdf,1385,asunto\ny,IDU/b.pdf,,sin señal\n",
                    encoding="utf-8")
    assert read_contracts(path) == {"IDU/a.pdf": "1385"}
    assert read_contracts(tmp_path / "falta.csv") == {}
    assert date_of("IDU/2021-01-22_x.pdf") == "2021-01-22"
    assert date_of("IDU/x.pdf") == "sin fecha"


def test_matriz_lists_every_member_under_its_theme():
    member = {"ruta": "IDU/2023-03-29_1443_1.pdf", "id": "obs-001", "autor": "idu",
              "radicado_origen": "DTE 1", "pagina": 2, "resumen": "a | b"}
    grupos = {"temas": [{"tema": "T01", "nombre": "Uno"}, {"tema": "T02", "nombre": "Dos"}],
              "grupos": [{"grupo": "G001", "tema": "T01", "miembros": [member, {**member, "id": "obs-002"}]}]}
    text = render_matriz(grupos, {"IDU/2023-03-29_1443_1.pdf": "348"}, today="2026-01-01")
    assert "2 observaciones de 1 documentos" in text
    assert text.count("| 2023-03-29 | 348 | idu |") == 2
    assert r"a \| b" in text


def test_informe_counts_each_file_once():
    manifest = {"archivos": [{"ruta": "IDU/a.pdf", "motivo_exclusion": None},
                             {"ruta": "IDU/b.pdf", "motivo_exclusion": None},
                             {"ruta": "IDU/c.pdf", "motivo_exclusion": "remitente"}],
                "ausentes": [], "resumen": {"archivos_pdf": 3, "coincidentes": 3, "huerfanos": 0}}
    profiles = {"documentos": {"IDU/b.pdf": {"necesita_ocr": True}}}
    rows = [{"ruta": "IDU/a.pdf", "gdb": "si"}, {"ruta": "IDU/b.pdf", "gdb": "probable"},
            {"ruta": "IDU/c.pdf", "gdb": "no"}]
    data = build_informe(manifest, profiles, rows, {"documentos": {}}, {"IDU/a.pdf": 0})
    assert [f["estado"] for f in data["archivos"]] == ["procesado", "pendiente", "descartado"]
    assert data["ocr"] == ["IDU/b.pdf"] and data["sin_perfil"] == ["IDU/a.pdf", "IDU/c.pdf"]
    assert render_informe(data, today="2026-01-01").count("`IDU/") == 3


def test_matriz_uses_editorial_theme_when_given():
    member = {"ruta": "IDU/a.pdf", "id": "obs-001", "autor": "idu", "radicado_origen": None,
              "pagina": 1, "resumen": "x"}
    grupos = {"temas": [{"tema": "T01", "nombre": "Uno"}, {"tema": "T02", "nombre": "Dos"}],
              "grupos": [{"grupo": "G001", "tema": "T01", "miembros": [member]}]}
    text = render_matriz(grupos, {}, today="2026-01-01", themes_by_group={"G001": "T02"})
    assert "| T01. Uno | 0 |" in text and "| T02. Dos | 1 |" in text
