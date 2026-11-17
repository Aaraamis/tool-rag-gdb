from rag_gdb.classification import apply_manual_reviews, classify_name, text_relevance


def test_issuer_uses_document_code_not_referenced_code():
    issuer, kind, relevance, _ = classify_name(
        "2025-10-16_E-IDU-348-0995-24 Rta. C.1443 Traslado STEST 2024 GDB.pdf"
    )
    assert (issuer, kind, relevance) == ("obra", "traslado", "si")


def test_known_interventoria_and_designs():
    assert classify_name("2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf")[:3] == (
        "interventoria", "revision_observaciones", "si")
    assert classify_name("2021-03-15_MI-DIS-IDU-1383-006-21_Rta GDB.pdf")[:3] == (
        "disenos", "respuesta", "si")
    assert classify_name("2021-01-06_MI-DIS-IDU1385-001-21_ GDB.pdf")[:3] == (
        "disenos", "comunicado", "si")
    assert classify_name("2021-02-22_MAB-1-1463-0013-21-Respuesta GDB.pdf")[:3] == (
        "interventoria", "respuesta", "si")
    assert classify_name("2021-06-16_MV2-025-21 observ SIG CAD.pdf")[:2] == (
        "interventoria", "revision_observaciones")
    assert classify_name("2020-04-21_MAB-2-1558-0238-20.pdf")[0] == "por_revisar"


def test_ambiguous_name_is_kept_for_review():
    assert classify_name("2021-03-19_20213560460121.pdf", "Entrega de GDB")[:3] == (
        "por_revisar", "por_revisar", "por_revisar")


def test_known_gdb_guide_is_relevant():
    assert classify_name("2021-08-31_GUIC06_GUÍA ENTREGA DE PRODUCTOS.pdf")[:3] == (
        "idu", "guia_instructivo", "si")


def test_pdf_text_signals_are_ranked_without_excluding_unknowns():
    assert text_relevance("La geodatabase se entregó en la GDB") == "probable"
    assert text_relevance("Se revisaron archivos CAD") == "posible"
    assert text_relevance("Acta de reunión de obra") == "por_revisar"


def test_traslado_after_radicado_number_stays_traslado():
    assert classify_name("2021-02-12_MAB-1-1463-0012-21Traslado oficio STMSV observaciones GDB.pdf")[1] == "traslado"


def test_manual_review_keeps_evidence_and_updates_one_field(tmp_path):
    path = tmp_path / "revisiones.csv"
    path.write_text("sha256,emisor,tipo,gdb,justificacion\nabc,interventoria,,,PDF p. 1\n")
    rows = [{"sha256": "abc", "estado_inventario": "coincidente", "emisor": "por_revisar",
             "tipo": "traslado", "gdb": "si", "revisar": "si", "evidencia_manual": ""}]
    apply_manual_reviews(rows, path)
    assert (rows[0]["emisor"], rows[0]["revisar"], rows[0]["evidencia_manual"]) == (
        "interventoria", "no", "PDF p. 1")


def test_manual_no_gdb_closes_irrelevant_review(tmp_path):
    path = tmp_path / "revisiones.csv"
    path.write_text("sha256,emisor,tipo,gdb,justificacion\nabc,,,no,PDF p. 1 solo trata accidentalidad\n")
    rows = [{"sha256": "abc", "estado_inventario": "coincidente", "emisor": "por_revisar",
             "tipo": "por_revisar", "gdb": "por_revisar", "revisar": "si", "evidencia_manual": ""}]
    apply_manual_reviews(rows, path)
    assert (rows[0]["gdb"], rows[0]["revisar"]) == ("no", "no")
