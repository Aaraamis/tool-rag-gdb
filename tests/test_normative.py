from pathlib import Path

import openpyxl
import pytest

from rag_gdb.normative import (checklist_items_xlsx, digest_path, products_dwg_items,
                               render_normative, verify_register)


def test_verify_register_checks_file_hash(tmp_path: Path):
    source = tmp_path / "guia.pdf"
    source.write_bytes(b"norma")
    row = {"codigo": "G", "ruta": "guia.pdf", "sha256": digest_path(source)}

    verify_register([row], tmp_path)
    source.write_bytes(b"alterada")

    with pytest.raises(ValueError, match="SHA-256 no coincide"):
        verify_register([row], tmp_path)


def _products_workbook(path: Path) -> None:
    workbook = openpyxl.Workbook()
    construction = workbook.active
    construction.title = "ElementosConstruccion (Récord)"
    construction.append(["ELEMENTOS MÍNIMOS A PRESENTAR EN LOS PLANOS"])
    construction.append(["VIAL"])
    construction.append(["Georreferenciación"])

    layers = workbook.create_sheet("LAYERCAD")
    layers.append(["#", "ELEMENTO", "NOMBRE LAYER", "ESQUEMA", "REPRESENTACIÓN",
                   "NOMBRE LAYER CAD", "ESTADO"])
    layers.append([1, "Andén", "Anden", "EspacioPublico", "POLÍGONO", "ANDEN",
                   "E: EXISTENTE"])

    for name in ("INSTRUCTIVO_NUEVOSLAYERS", "INSTRUCTIVO_LAYOUT_CIV"):
        sheet = workbook.create_sheet(name)
        sheet.append(["CAMPO"])
        sheet.append(["Descripción oficial"])

    scales = workbook.create_sheet("EscalasPlanos")
    scales.append(["ESCALA DE PLANOS PRESENTADOS AL IDU"])
    scales.append(["TIPO DE PLANO", "1 : 50", "1 : 100"])
    scales.append(["1. GENERAL"])
    scales.append(["1.1. Carátula", "X", None])

    names = workbook.create_sheet("NomenclaturaPlano")
    names.append(["Tipo Proyecto", "Código", None, "Especialidad", "Código", None,
                  "Nomenclatura Plano", "Código"])
    names.append(["Construcción Vial", "CV", None, "Pavimentos", "PV", None,
                  "Planta", "PL"])
    workbook.save(path)


def test_products_dwg_extracts_construction_rules(tmp_path: Path):
    path = tmp_path / "Productos_DWG.xlsx"
    _products_workbook(path)

    catalog = products_dwg_items(path)
    texts = [item["texto"] for item in catalog]

    assert "Georreferenciación" in texts
    assert any("layer CAD ANDEN" in text for text in texts)
    assert any("1 : 50" in text for text in texts)
    assert any("Código de tipo de proyecto CV" in text for text in texts)


def test_foic05_includes_direct_components_and_short_topology_items(tmp_path: Path):
    path = tmp_path / "foic05.xlsx"
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Instrucciones"
    sheet.append(["A. REVISIÓN INFORMACIÓN CAD"])
    sheet.append(["1. META FÍSICA"])
    sheet.append(["No. CIVs reportados", "Segmentos presentados"])
    sheet.append(["B. REVISIÓN INFORMACIÓN GEODATABASE"])
    sheet.append(["4. TOPOLOGÍA"])
    sheet.append(["La cartografía cumple las reglas", "SI", "NO"])
    sheet.append(["a. Superposición elementos"])
    workbook.save(path)

    catalog = checklist_items_xlsx(path)

    assert [item["id"] for item in catalog] == ["FO-IC-05 A.1", "FO-IC-05 B.4",
                                                  "FO-IC-05 B.4.a"]


def test_render_normative_separates_sources():
    register = [{"codigo": "G", "nombre": "Guía", "version": "1", "tipo": "guia",
                 "aplica_construccion": "si", "nota": ""}]
    catalog = [{"id": "G §1", "fuente": "G", "seccion": "§1 Alcance", "texto": "Entregar."}]

    rendered = render_normative(register, catalog, "contrato 348")

    assert "# Normativa vigente — contrato 348" in rendered
    assert "### G" in rendered
    assert "**G §1** — Entregar." in rendered
