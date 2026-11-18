import json

from rag_gdb import extraction, proposal
from rag_gdb.classification import issuer_from_text
from rag_gdb.extraction import validate_extraction
from rag_gdb.proposal import page_blocks, propose, propose_selected

FOOTER = "Calle 95 No 15 47 Piso 6 Teléfono 622 5099 Bogotá D.C., Colombia"
PAGES = [
    f"Respetados Señores, se remite la revisión de la entrega.\n\n{FOOTER}",
    ("OBSERVACIÓN IDU: Se solicita incluir el archivo de estructura de carpetas.\n\n"
     f"RESPUESTA CONTRATISTA: Se revisa y se ajusta la carpeta indicada.\n\n{FOOTER}"),
    f"- No se incluyen planos PDF en la carpeta de urbanismo.\n\n{FOOTER}",
]
TEMPLATE = "Elige bloques.\n{bloques}"


def _fake(answers):
    calls = []

    def ask(prompt):
        calls.append(prompt)
        return answers[len(calls) - 1]
    return ask, calls


def test_blocks_drop_footer_repeated_on_most_pages():
    blocks = page_blocks(PAGES)
    assert all(FOOTER not in b["texto"] for b in blocks)
    assert [b["pagina"] for b in blocks] == [1, 2, 2, 3]


def test_short_documents_keep_repeated_blocks():
    assert len(page_blocks(PAGES[1:3])) == 5  # dos páginas: el pie no se considera repetido


def test_propose_takes_literal_block_and_coerces_fields():
    ask, calls = _fake([
        '{"observaciones": []}',
        ('{"observaciones": [{"bloque": "B2", "numero": 1, "autor": "IDU", "resumen": "x"},'
         ' {"bloque": "B2"}, {"bloque": "B99"}, {"bloque": "B4"}]}'),
        "esto no es JSON",
    ])
    candidates, failed = propose(PAGES, TEMPLATE, ask)
    assert len(calls) == 3 and "{bloques}" not in calls[0]
    assert failed == [3]
    assert len(candidates) == 1  # repetido, inexistente y de otra página se descartan
    obs = candidates[0]
    assert obs["cita"].startswith("OBSERVACIÓN IDU: Se solicita incluir")
    assert obs["numero"] == "1" and obs["autor"] == "idu" and obs["pagina"] == 2
    assert len(obs["resumen"]) >= 10  # resumen corto se reemplaza por el texto


def test_long_block_is_cut_at_a_word_boundary():
    page = "Se solicita " + "verificar la geometría de cada elemento " * 20
    ask, _ = _fake([('{"observaciones": [{"bloque": "B1", "autor": "interventoria", '
                     '"resumen": "Verificar la geometría."}]}')])
    (obs,), _ = propose([page], TEMPLATE, ask)
    assert len(obs["cita"]) <= proposal.MAX_CITA and page.startswith(obs["cita"])


def test_propose_selected_writes_valid_candidates_and_resumes(tmp_path, monkeypatch):
    pdf = tmp_path / "pdf" / "IDU" / "doc.pdf"
    pdf.parent.mkdir(parents=True)
    pdf.write_bytes(b"%PDF-1.4 prueba")
    manifest = {"archivos": [{"ruta": "IDU/doc.pdf", "sha256": proposal.sha256(pdf)}]}
    monkeypatch.setattr(proposal, "page_texts", lambda path: PAGES)
    monkeypatch.setattr(extraction, "page_texts", lambda path: PAGES)
    ask, calls = _fake(['{"observaciones": []}',
                        ('{"observaciones": [{"bloque": "B2", "autor": "idu", '
                         '"resumen": "Incluir el reporte de carpetas."}]}'),
                        ('{"observaciones": [{"bloque": "B4", "autor": "interventoria", '
                         '"resumen": "Entregar planos en PDF."}]}')])
    out = tmp_path / "cand"
    state = propose_selected(manifest, tmp_path / "pdf", out, ["IDU/doc.pdf"], TEMPLATE, "m", ask)
    assert state["documentos"]["IDU/doc.pdf"]["estado"] == "ok"
    data = json.loads((out / "IDU/doc.json").read_text())
    assert validate_extraction(data, manifest, tmp_path / "pdf") == []
    assert len(data["observaciones"]) == 2
    propose_selected(manifest, tmp_path / "pdf", out, ["IDU/doc.pdf"], TEMPLATE, "m", ask)
    assert len(calls) == 3  # reanudación: no vuelve a llamar al modelo
    propose_selected(manifest, tmp_path / "pdf", out, ["IDU/doc.pdf"], TEMPLATE + " v2",
                     "m", _fake(['{"observaciones": []}'] * 3)[0])
    assert json.loads((out / "estado.json").read_text())["documentos"]["IDU/doc.pdf"]["candidatos"] == 0


def test_issuer_from_first_page_text():
    idu = "*20213560877971*\nSTMSV\n20213560877971\nInformación Pública\nAl responder cite este número"
    assert issuer_from_text(idu) == ("idu", "texto_pdf:radicado_idu")
    assert issuer_from_text("Para contestar cite:\nRadicado ANI No.: 20215000370491") == (
        "por_revisar", "texto_pdf:otra_entidad_ANI")
    assert issuer_from_text("FORMATO\nRADICACIÓN WEB\nFO-DO-42\nAl responder cite este número")[0] == "por_revisar"
    assert issuer_from_text("Señores CONSORCIO, en respuesta a su comunicación") == ("por_revisar", None)


def test_segments_split_bullets_labels_and_long_sentences():
    page = ("REVISIÓN INTERVENTORÍA No. 1: se tienen las siguientes observaciones:\n"
            "- a. Algunos numerales se marcaron como Ok sin estar presentes en la entrega.\n"
            "o Los planos deben incluir el sistema de referencia empleado.\n"
            "o\n"
            "1. OBSERVACIÓN IDU: " + "Se solicita verificar la geometría del elemento. " * 15)
    texts = [b["texto"] for b in page_blocks([page])]
    assert texts[0].startswith("REVISIÓN INTERVENTORÍA")
    assert texts[1].startswith("- a. Algunos numerales")
    assert texts[2].startswith("o Los planos deben incluir")
    assert all(len(t) <= proposal.MAX_BLOCK + 60 for t in texts)  # frases largas partidas
    assert sum(t.count("Se solicita verificar") for t in texts) == 15  # nada se pierde


def test_same_statement_on_two_pages_is_proposed_once():
    pages = ["- No se incluyen planos PDF en la carpeta.", "- No se incluyen planos PDF en la carpeta."]
    ask, _ = _fake(['{"observaciones": [{"bloque": "B1"}]}', '{"observaciones": [{"bloque": "B2"}]}'])
    candidates, _ = propose(pages, TEMPLATE, ask)
    assert len(candidates) == 1 and candidates[0]["pagina"] == 1
