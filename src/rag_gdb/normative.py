"""Normativa (RF7): catálogo de requisitos oficiales desde el alistamiento del IDU."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import openpyxl

from .pipeline import _run

PARAGRAPH = 700  # tamaño máximo de un fragmento de la guía en el catálogo
GUIDE_NOISE = re.compile(r"^(?:GUÍA|GUÍA ENTREGA DE PRODUCTOS|REALIZADOS EN LA INFRAESTRUCTURA|ESPACIO PÚBLICO$|"
                         r"CÓDIGO\s+PROCESO|GU-IC-06\s+INNOVACIÓN|Página \d+ de \d+|Formato: FO-|"
                         r"FO-DE-|Clasificación de la información)", re.I)


def read_register(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def digest_path(path: Path) -> str:
    """SHA-256 de un archivo o de un árbol, incluyendo rutas relativas."""
    if path.is_file():
        return hashlib.sha256(path.read_bytes()).hexdigest()
    digest = hashlib.sha256()
    for item in sorted(p for p in path.rglob("*") if p.is_file()):
        digest.update(str(item.relative_to(path)).encode())
        digest.update(hashlib.sha256(item.read_bytes()).digest())
    return digest.hexdigest()


def verify_register(register: list[dict], root: Path) -> None:
    """Comprueba que cada entrada existe y coincide con el hash confirmado."""
    errors = []
    for row in register:
        path = root / row["ruta"]
        if not path.exists():
            errors.append(f"{row['codigo']}: no existe {row['ruta']}")
        elif digest_path(path) != row["sha256"]:
            errors.append(f"{row['codigo']}: SHA-256 no coincide para {row['ruta']}")
    if errors:
        raise ValueError("Registro normativo inválido:\n- " + "\n- ".join(errors))


def guide_sections(pdf: Path, code: str) -> list[dict]:
    """Fragmentos de una guía por numeral, usando su tabla de contenido."""
    text = _run("pdftotext", "-layout", str(pdf), "-")
    lines = text.splitlines()
    toc = []
    for line in lines[:200]:
        found = re.match(r"^\s*(\d+(?:\.\d+)*)\s+([A-ZÁÉÍÓÚÑ][^.]{2,90}?)\s*\.*\s*\d*\s*$", line)
        if found and (not toc or found[1] != toc[-1][0]):
            toc.append((found[1], " ".join(found[2].split()).rstrip(":")))
    starts = []  # primera aparición de cada numeral después de la tabla de contenido
    cursor = 0
    for number, title in toc:
        pattern = re.compile(rf"^\s*{re.escape(number)}\.?\s+{re.escape(title.split()[0])}", re.I)
        for k in range(max(cursor, 120), len(lines)):
            if pattern.match(lines[k]):
                starts.append((k, number, title))
                cursor = k + 1
                break
    out = []
    for idx, (k, number, title) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        body = [" ".join(l.split()) for l in lines[k + 1:end]]
        body = [l for l in body if l and not GUIDE_NOISE.match(l)]
        paragraphs, current = [], ""
        for line in body:  # agrupa en fragmentos de tamaño acotado
            if current and len(current) + len(line) > PARAGRAPH:
                paragraphs.append(current)
                current = line
            else:
                current = f"{current} {line}".strip()
        if current:
            paragraphs.append(current)
        for n, para in enumerate(paragraphs or [""], 1):
            out.append({"id": f"{code} §{number}" + (f" ¶{n}" if len(paragraphs) > 1 else ""),
                        "fuente": code, "seccion": f"§{number} {title}", "texto": para})
    return out


def _sheet_rows(path: Path, sheet: str) -> list[list[str]]:
    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    rows = []
    for row in workbook[sheet].iter_rows(values_only=True):
        values = [" ".join(str(v).split()) for v in row if v not in (None, "")]
        if values:
            rows.append(values)
    return rows


def checklist_items_xlsx(xlsx: Path) -> list[dict]:
    """Ítems de la hoja Instrucciones de FO-IC-05 ya convertida a XLSX."""
    rows = _sheet_rows(xlsx, "Instrucciones")
    out, block, component, component_added = [], None, None, False
    for values in rows:
        first = values[0]
        if re.match(r"^[AB]\.\s", first):
            block = first[0]
            component = None
            continue
        header = re.match(r"^(\d)\.\s+(.+)$", first)
        if header and block:
            component = f"{header[1]}. {header[2].title()}"
            component_added = False
            if len(values) > 1:  # componente con su propia descripción (p. ej. meta física)
                out.append({"id": f"FO-IC-05 {block}.{header[1]}", "fuente": "FO-IC-05",
                            "seccion": f"{block}.{component}", "texto": " ".join(values[1:])})
                component_added = True
            continue
        item = re.match(r"^([a-z])\.\s+(.+)$", first)
        if item and block and component:
            text = item[2] + (f": {' '.join(values[1:])}" if len(values) > 1 else "")
            out.append({"id": f"FO-IC-05 {block}.{component[0]}.{item[1]}", "fuente": "FO-IC-05",
                        "seccion": f"{block}.{component}", "texto": text})
            component_added = True
            continue
        noise = {"CUMPLE", "PRESENTA", "CONTENIDO"}
        if block and component and not component_added and len(values) > 1 and first not in noise:
            out.append({"id": f"FO-IC-05 {block}.{component[0]}", "fuente": "FO-IC-05",
                        "seccion": f"{block}.{component}", "texto": " ".join(values)})
            component_added = True
    return out


def checklist_items(xls: Path) -> list[dict]:
    """Ítems de FO-IC-05; convierte el XLS sin alterar el original."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        source = tmp_path / "in" / "foic05.xls"
        output = tmp_path / "out"
        profile = tmp_path / "profile"
        runtime = tmp_path / "runtime"
        config = tmp_path / "config"
        source.parent.mkdir()
        for directory in (output, profile, runtime, config):
            directory.mkdir()
        runtime.chmod(0o700)
        shutil.copyfile(xls, source)
        env = os.environ.copy()
        env.update({"XDG_RUNTIME_DIR": str(runtime), "XDG_CONFIG_HOME": str(config)})
        command = ["soffice", f"-env:UserInstallation=file://{profile}", "--headless", "--norestore",
                   "--convert-to", "xlsx", "--outdir", str(output), str(source)]
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=180, env=env)
        except FileNotFoundError as exc:
            raise RuntimeError("FO-IC-05 requiere LibreOffice (comando soffice)") from exc
        converted = output / "foic05.xlsx"
        if result.returncode or not converted.exists():
            detail = (result.stderr or result.stdout).strip() or f"código {result.returncode}"
            raise RuntimeError(f"No se pudo convertir FO-IC-05 con LibreOffice: {detail}")
        return checklist_items_xlsx(converted)


def bdg_validations(xlsx: Path) -> list[dict]:
    out, section = [], ""
    for values in _sheet_rows(xlsx, "VALIDACIONES_BDG"):
        if len(values) == 1:
            if re.match(r"^[\d.]+\s", values[0]) or re.match(r"^[a-z]\.\s", values[0]):
                section = values[0]
            continue
        out.append({"id": f"VALIDACIONES_BDG {section.split()[0]} {values[0][:40]}", "fuente": "Productos_BDG",
                    "seccion": f"VALIDACIONES_BDG {section}", "texto": f"{values[0]}: {' '.join(values[1:])}"})
    return out


def topology_rules(xlsx: Path) -> list[dict]:
    rows = _sheet_rows(xlsx, "REGLAS_TOPOLOGICAS")
    names = next(r for r in rows if r[0] == "NOMBRE")[1:]
    descriptions = next(r for r in rows if r[0].startswith("DESCRIP"))[1:]
    return [{"id": f"REGLAS_TOPOLOGICAS {name.split('.')[0]}", "fuente": "Productos_BDG",
             "seccion": "REGLAS_TOPOLOGICAS", "texto": f"{name}: {desc} (aplica por elemento según la hoja)"}
            for name, desc in zip(names, descriptions)]


def _clean(value: object) -> str:
    return " ".join(str(value).split()) if value not in (None, "") else ""


def products_dwg_items(xlsx: Path) -> list[dict]:
    """Requisitos de las hojas aplicables a construcción de Productos_DWG."""
    workbook = openpyxl.load_workbook(xlsx, read_only=True, data_only=True)
    out = []

    sheet = workbook["ElementosConstruccion (Récord)"]
    section = ""
    headings = {"ESTUDIO TOPOGRAFICO", "VIAL", "ARQUITECTÓNICO ESPACIO PÚBLICO Y PAISAJISTICO",
                "PAVIMENTOS", "GEOTECNIA", "ESTRUCTURAS"}
    for row_number, row in enumerate(sheet.iter_rows(values_only=True), 1):
        text = _clean(row[0])
        if not text or text == "ELEMENTOS MÍNIMOS A PRESENTAR EN LOS PLANOS":
            continue
        if text in headings:
            section = text.title()
        elif section and not text.startswith("*"):
            out.append({"id": f"Productos_DWG Récord F{row_number}", "fuente": "Productos_DWG",
                        "seccion": f"ElementosConstruccion (Récord) — {section}", "texto": text})

    sheet = workbook["LAYERCAD"]
    out.append({"id": "Productos_DWG LAYERCAD regla", "fuente": "Productos_DWG",
                "seccion": "LAYERCAD",
                "texto": "Representar cada elemento en el layer CAD, tipo de geometría y estado definidos en LAYERCAD."})
    for row_number, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), 2):
        values = [_clean(value) for value in row]
        if not values or not values[0].isdigit() or len(values) < 7:
            continue
        element, geometry, layer, state = values[1], values[4], values[5], values[6]
        text = f"{element}: layer CAD {layer}"
        if geometry:
            text += f", geometría {geometry}"
        if state:
            text += f", estados {state}"
        out.append({"id": f"Productos_DWG LAYERCAD {values[0]}", "fuente": "Productos_DWG",
                    "seccion": "LAYERCAD", "texto": text})

    for sheet_name in ("INSTRUCTIVO_NUEVOSLAYERS", "INSTRUCTIVO_LAYOUT_CIV"):
        sheet = workbook[sheet_name]
        nonempty = [[_clean(value) for value in row] for row in sheet.iter_rows(values_only=True)
                    if any(_clean(value) for value in row)]
        headers, descriptions = nonempty[:2]
        for column, (header, description) in enumerate(zip(headers, descriptions), 1):
            if header and description:
                out.append({"id": f"Productos_DWG {sheet_name} C{column}", "fuente": "Productos_DWG",
                            "seccion": sheet_name, "texto": f"{header}: {description}"})

    sheet = workbook["EscalasPlanos"]
    rows = [(number, [_clean(value) for value in row])
            for number, row in enumerate(sheet.iter_rows(values_only=True), 1)
            if any(_clean(value) for value in row)]
    scales = rows[1][1]
    section = ""
    for row_number, values in rows[2:]:
        name = values[0]
        if not name:
            continue
        if re.match(r"^\d+\.\s*[A-ZÁÉÍÓÚÑ ]+$", name):
            section = name
            continue
        allowed = [scales[i] for i, value in enumerate(values) if i and value == "X" and i < len(scales)]
        note = next((value for value in values[1:] if value and value != "X"), "")
        if allowed or note:
            text = f"{name}: " + (", ".join(allowed) if allowed else note)
            out.append({"id": f"Productos_DWG Escalas F{row_number}", "fuente": "Productos_DWG",
                        "seccion": f"EscalasPlanos — {section}".rstrip(" —"), "texto": text})

    sheet = workbook["NomenclaturaPlano"]
    for row_number, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), 2):
        for label, name_col, code_col in (("tipo de proyecto", 0, 1), ("especialidad", 3, 4),
                                          ("plano", 6, 7)):
            name, code = _clean(row[name_col]), _clean(row[code_col])
            if name and code and code.lower() != "código":
                out.append({"id": f"Productos_DWG Nomenclatura {label} F{row_number}",
                            "fuente": "Productos_DWG", "seccion": "NomenclaturaPlano",
                            "texto": f"Código de {label} {code}: {name}"})
    workbook.close()
    return out


def build_catalog(register: list[dict], root: Path) -> list[dict]:
    by_code = {r["codigo"]: root / r["ruta"] for r in register}
    catalog = guide_sections(by_code["GU-IC-06"], "GU-IC-06")
    catalog += checklist_items(by_code["FO-IC-05"])
    catalog += bdg_validations(by_code["Productos_BDG"])
    catalog += topology_rules(by_code["Productos_BDG"])
    catalog += products_dwg_items(by_code["Productos_DWG"])
    seen = set()
    for entry in catalog:  # ids únicos
        base, n = entry["id"], 2
        while entry["id"] in seen:
            entry["id"] = f"{base} ({n})"
            n += 1
        seen.add(entry["id"])
    return catalog


def render_register(register: list[dict], project: str) -> str:
    lines = [f"# Normativa vigente — {project}", "",
             "> Paquete de alistamiento oficial de 2020 entregado por el IDU para los contratos 348 y 351.",
             "> Para la entrega de construcción del 348 rige este paquete, no versiones posteriores.", "",
             "| Código | Documento | Versión | Tipo | Aplica a construcción (récord) | Nota |",
             "|---|---|---|---|---|---|"]
    order = {"si": 0, "parcial": 1, "no": 2}
    for r in sorted(register, key=lambda r: (order.get(r["aplica_construccion"], 3), r["codigo"])):
        lines.append(f"| {r['codigo']} | {r['nombre']} | {r['version'] or '—'} | {r['tipo']} | "
                     f"{r['aplica_construccion']} | {r['nota']} |")
    return "\n".join(lines) + "\n"


def render_normative(register: list[dict], catalog: list[dict], project: str) -> str:
    """Inventario confirmado y catálogo legible de requisitos oficiales."""
    text = render_register(register, project).rstrip()
    lines = [text, "", "## Catálogo de requisitos oficiales", "",
             "Cada entrada conserva la fuente y sección de la que fue extraída. El enlace con las",
             "observaciones se confirma por separado; una coincidencia semántica no sustituye la revisión."]
    sources = []
    for entry in catalog:
        if entry["fuente"] not in sources:
            sources.append(entry["fuente"])
    for source in sources:
        lines += ["", f"### {source}", ""]
        section = None
        for entry in (item for item in catalog if item["fuente"] == source):
            if entry["seccion"] != section:
                section = entry["seccion"]
                lines += [f"#### {section}", ""]
            lines.append(f"- **{entry['id']}** — {entry['texto']}")
    return "\n".join(lines) + "\n"


def write_normative(register_path: Path, root: Path, catalog_output: Path,
                    markdown_output: Path, project: str) -> dict:
    register = read_register(register_path)
    verify_register(register, root)
    catalog = build_catalog(register, root)
    catalog_output.parent.mkdir(parents=True, exist_ok=True)
    markdown_output.parent.mkdir(parents=True, exist_ok=True)
    catalog_output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_output.write_text(render_normative(register, catalog, project), encoding="utf-8")
    return {"documentos": len(register), "requisitos": len(catalog),
            "catalogo": str(catalog_output), "salida": str(markdown_output)}
