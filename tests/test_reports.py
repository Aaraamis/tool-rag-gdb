from rag_gdb.reports import build_informe, contract_of, date_of, render_informe, render_matriz


def test_contract_and_date_come_only_from_the_file_name():
    assert contract_of("IDU/2021-02-12_R-IDU1385-0014-21 RTA.pdf") == "1385"
    assert contract_of("IDU/2023-03-29_1443_443723_070700.pdf") == "1443"
    assert contract_of("IDU/2021-01-22_167_anexo_20212150011573_SI.pdf") == "sin determinar"
    assert date_of("IDU/2021-01-22_x.pdf") == "2021-01-22"
    assert date_of("IDU/x.pdf") == "sin fecha"


def test_matriz_lists_every_member_under_its_theme():
    member = {"ruta": "IDU/2023-03-29_1443_1.pdf", "id": "obs-001", "autor": "idu",
              "radicado_origen": "DTE 1", "pagina": 2, "resumen": "a | b"}
    grupos = {"temas": [{"tema": "T01", "nombre": "Uno"}, {"tema": "T02", "nombre": "Dos"}],
              "grupos": [{"tema": "T01", "miembros": [member, {**member, "id": "obs-002"}]}]}
    text = render_matriz(grupos, today="2026-01-01")
    assert "2 observaciones de 1 documentos" in text
    assert text.count("| 2023-03-29 | 1443 | idu |") == 2
    assert "a \| b" in text


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
