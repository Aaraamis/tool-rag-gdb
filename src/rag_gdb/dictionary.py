"""Diccionario de atributos de la BDG desde `Productos_BDG_valores.ods` (exportación de Productos_BDG).

En la plantilla del IDU la marca «X» distingue por color: roja es atributo obligatorio y verde es
atributo según alcance del contrato. Este módulo conserva esa distinción leyendo el estilo de la celda.
"""

from __future__ import annotations

import difflib
import hashlib
import unicodedata
import zipfile
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

TABLE = "{urn:oasis:names:tc:opendocument:xmlns:table:1.0}"
TEXT = "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}"
STYLE = "{urn:oasis:names:tc:opendocument:xmlns:style:1.0}"
FO = "{urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0}"
CELLS = (TABLE + "table-cell", TABLE + "covered-table-cell")
MAX_REPEAT = 60
MARK_BY_COLOR = {"#ff0000": "obligatorio", "#00b050": "según alcance"}
SKIP_SHEETS = {"CATALOGO_BDG", "VALIDACIONES_BDG", "REGLAS_TOPOLOGICAS"}
# Nombres del catálogo que no coinciden con la hoja de la plantilla.
CATALOG_ALIASES = {"Provedoores": "Proveedores"}


def _text(cell: ET.Element) -> str:
    return " ".join(" ".join("".join(p.itertext()) for p in cell.iter(TEXT + "p")).split())


def _colors(root: ET.Element) -> dict[str, str]:
    colors = {}
    for style in root.iter(STYLE + "style"):
        props = style.find(STYLE + "text-properties")
        color = props.get(FO + "color") if props is not None else None
        if color:
            colors[style.get(STYLE + "name", "")] = color.lower()
    return colors


def _column_styles(sheet: ET.Element) -> list[str | None]:
    styles: list[str | None] = []
    for column in sheet.iter(TABLE + "table-column"):
        repeat = min(int(column.get(TABLE + "number-columns-repeated", "1")), MAX_REPEAT)
        styles += [column.get(TABLE + "default-cell-style-name")] * repeat
    return styles


def _rows(sheet: ET.Element, colors: dict[str, str]) -> list[list[tuple[str, str]]]:
    """Filas como listas de (texto, color de fuente); se recortan las celdas vacías finales.

    Una celda sin estilo propio toma el estilo por defecto de su columna.
    """
    defaults = _column_styles(sheet)
    rows = []
    for row in sheet.iter(TABLE + "table-row"):
        values: list[tuple[str, str]] = []
        for cell in row:
            if cell.tag in CELLS:
                repeat = min(int(cell.get(TABLE + "number-columns-repeated", "1")), MAX_REPEAT)
                for _ in range(repeat):
                    index = len(values)
                    style = cell.get(TABLE + "style-name") or (defaults[index] if index < len(defaults) else None)
                    values.append((_text(cell), colors.get(style or "", "")))
        while values and not values[-1][0]:
            values.pop()
        rows.append(values)
    return rows


def _normal(text: str) -> str:
    text = unicodedata.normalize("NFKD", text.lower())
    return "".join(ch for ch in text if ch.isalpha())


def _project_column(header: list[str], project: str) -> int | None:
    """Columna «Proyecto: <etapa>»; tolera erratas de la plantilla («Consrucción», «Contrucción»)."""
    target = _normal(project)
    for index, name in enumerate(header):
        if name.startswith("Proyecto") and ":" in name:
            stage = _normal(name.split(":", 1)[1])
            if difflib.SequenceMatcher(None, stage, target).ratio() >= 0.85:
                return index
    return None


def _criteria_columns(header: list[str]) -> list[int]:
    """Columnas de criterio entre «Tipo de dato» y «Contratista» cuando no son etapas (p. ej. Exploración)."""
    if "Tipo de dato" not in header:
        return []
    start = header.index("Tipo de dato") + 1
    end = header.index("Contratista") if "Contratista" in header else len(header)
    return [i for i in range(start, end) if header[i] and header[i] != "N / A"]


def _mark(value: str, color: str) -> str:
    if value.strip().upper() != "X":
        return ""
    return MARK_BY_COLOR.get(color, "X sin convención de color")


def _row_mark(row: list[tuple[str, str]], column: int | None, criteria: list[int], header: list[str]) -> str:
    if column is not None:
        return _mark(*row[column]) if column < len(row) else ""
    if not criteria:
        return "sin columna de etapa: ver plantilla"
    found: dict[str, list[str]] = {}
    for i in criteria:
        if i < len(row) and (mark := _mark(*row[i])):
            found.setdefault(mark, []).append(header[i])
    return "; ".join(f"{mark} ({', '.join(names)})" for mark, names in found.items())


def parse_sheet(rows: list[list[tuple[str, str]]], sheet: str, project: str) -> list[dict]:
    """Tablas de una hoja: la clase de entidad y sus tablas relacionadas, cada una con sus campos."""
    tables: list[dict] = []
    pending = {"nombre": sheet, "alias": sheet, "relacionada_de": None}
    current = header = None
    column = None
    criteria: list[int] = []
    for index, row in enumerate(rows):
        cells = [text for text, _ in row]
        first = cells[0] if cells else ""
        if first == "Nombre de la Tabla":
            parent = next((c for c in cells[2:] if c), "")
            parent = parent.split('"')[1] if '"' in parent else (sheet if tables else None)
            following = [t for t, _ in rows[index + 1]] if index + 1 < len(rows) else []
            pending = {"nombre": following[0] if following else "", "relacionada_de": parent or sheet,
                       "alias": following[1] if len(following) > 1 else ""}
            current = None
            continue
        if first == "Nombre_Campo":
            header, column = cells, _project_column(cells, project)
            criteria = [] if column is not None else _criteria_columns(cells)
            current = {**pending, "campos": []}
            tables.append(current)
            continue
        if current is None or header is None or not any(cells):
            continue
        get = dict(zip(header, cells, strict=False))
        if first:
            current["campos"].append({
                "campo": first, "alias": cells[1] if len(cells) > 1 else "",
                "descripcion": cells[2] if len(cells) > 2 else "",
                "tipo": get.get("Tipo de dato", ""),
                "unidad": get.get("Unidad") or get.get("Unidades", ""),
                "rango": [get.get("Rango Mínimo", ""), get.get("Rango Máximo", "")],
                "dominio": [], "marca": _row_mark(row, column, criteria, header)})
        code = cells[4] if len(cells) > 4 else ""
        if current["campos"] and code:
            label = cells[5] if len(cells) > 5 else ""
            current["campos"][-1]["dominio"].append((code, label))
    return tables


def _catalog(rows: list[list[tuple[str, str]]]) -> dict[str, dict]:
    """Feature dataset, geometría y definición por hoja, según CATALOGO_BDG."""
    start = next(i for i, row in enumerate(rows) if any(t == "FEATURE CLASS" for t, _ in row))
    header = [t for t, _ in rows[start]]
    col = {name: header.index(name) for name in header if name}
    result: dict[str, dict] = {}
    dataset = ""
    for row in rows[start + 1:]:
        cells = [t for t, _ in row] + [""] * len(header)
        name = cells[col["FEATURE CLASS"]]
        if not name:
            continue
        dataset = cells[col["FEATURE DATASET"]] or dataset
        geometry = cells[col["TIPO DE GEOMETRÍA"]]
        sheet = CATALOG_ALIASES.get(name, name)
        if name == "ElementoPuenteLinea":  # el catálogo nombra así ambas hojas de elementos de puente
            sheet = "PuenteElementoPoligono" if geometry.startswith("POL") else "PuenteElementoLinea"
        entry = result.setdefault(sheet, {"dataset": dataset, "geometria": geometry, "elementos": [],
                                          "definicion": cells[col["DEFINICIÓN"]]})
        entry["elementos"].append(cells[col["ELEMENTO"]])
    return result


def read_dictionary(ods: Path, project: str = "Construcción") -> dict:
    with zipfile.ZipFile(ods) as archive:
        root = ET.fromstring(archive.read("content.xml"))
    colors = _colors(root)
    sheets = {s.get(TABLE + "name", ""): s for s in root.iter(TABLE + "table")}
    if "CATALOGO_BDG" not in sheets:
        raise ValueError("El ODS no tiene la hoja CATALOGO_BDG: ¿es la exportación de Productos_BDG?")
    catalog = _catalog(_rows(sheets["CATALOGO_BDG"], colors))
    classes = []
    for name, sheet in sheets.items():
        if name in SKIP_SHEETS:
            continue
        info = catalog.get(name, {"dataset": "Sin dataset en el catálogo", "geometria": "", "elementos": [],
                                  "definicion": ""})
        classes.append({"hoja": name, **info, "tablas": parse_sheet(_rows(sheet, colors), name, project)})
    return {"proyecto": project, "clases": classes,
            "sha256": hashlib.sha256(ods.read_bytes()).hexdigest(), "archivo": ods.name}


def _cell(text: str, limit: int | None = None) -> str:
    text = " ".join(text.split()).replace("|", "\\|")
    if limit and len(text) > limit:
        text = text[:text.rfind(" ", 0, limit)] + " …"
    return text


def _domain(field: dict) -> str:
    low, high = field["rango"]
    parts = [f"`{code}` {label}".strip() for code, label in field["dominio"]]
    if low or high:
        parts.insert(0, f"rango {low or '—'} a {high or '—'}")
    return _cell("; ".join(parts))


def render_dictionary(data: dict, today: str | None = None) -> str:
    project = data["proyecto"]
    classes = sorted(data["clases"], key=lambda c: (c["dataset"], c["hoja"]))
    lines = [
        f"# Diccionario de atributos de la BDG — proyecto de {project.lower()}",
        "",
        (f"> Generado por `rag-gdb diccionario` el {today or date.today().isoformat()} desde "
         f"`{data['archivo']}` (sha256 `{data['sha256'][:16]}…`), exportación a ODS de `Productos_BDG.xlsm` "
         "del alistamiento IDU 2020. La plantilla original rige; este documento la resume para crear y "
         "revisar capas."),
        (f"> **Marca** para «Proyecto: {project}»: **obligatorio** (X roja en la plantilla), **según alcance** "
         "(X verde: obligatorio si el contrato interviene ese elemento) o vacío (no aplica). El color de la "
         "fuente se lee del ODS; «X sin convención de color» indica una marca que hay que confirmar en la "
         "plantilla."),
        "",
        "## Resumen por feature dataset",
        "",
        "| Feature dataset | Clase de entidad | Geometría | Tablas relacionadas | Obligatorios | Según alcance |",
        "|---|---|---|---:|---:|---:|",
    ]
    for c in classes:
        fields = [f for t in c["tablas"] for f in t["campos"]]
        lines.append(f"| {c['dataset']} | [{c['hoja']}](#{c['hoja'].lower()}) | {c['geometria'] or '—'} | "
                     f"{max(len(c['tablas']) - 1, 0)} | {sum(f['marca'].startswith('obligatorio') for f in fields)} | "
                     f"{sum('según alcance' in f['marca'] for f in fields)} |")
    dataset = None
    for c in classes:
        if c["dataset"] != dataset:
            dataset = c["dataset"]
            lines += ["", f"## {dataset}"]
        lines += ["", f"### {c['hoja']}", ""]
        if c["geometria"]:
            elements = ", ".join(e for e in c["elementos"] if e)
            lines.append(f"Geometría **{c['geometria'].lower()}**" + (f"; elementos: {elements}." if elements
                                                                        else "."))
        if c["definicion"]:
            lines.append(f"{_cell(c['definicion'], 400)}")
        for table in c["tablas"]:
            title = (f"Tabla relacionada **{table['nombre']}** ({table['alias']}), de {table['relacionada_de']}"
                     if table["relacionada_de"] else f"Atributos de **{table['nombre']}**")
            lines += ["", title, "", "| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |",
                      "|---|---|---|---|---|---|"]
            for f in table["campos"]:
                lines.append(f"| `{_cell(f['campo'])}` | {_cell(f['alias'])} | {_cell(f['tipo'])} | "
                             f"{_cell(f['unidad'])} | {_domain(f)} | {f['marca']} |")
    return "\n".join(lines) + "\n"


def write_dictionary(ods: Path, output: Path, project: str = "Construcción") -> dict:
    data = read_dictionary(ods, project)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_dictionary(data), encoding="utf-8")
    fields = [f for c in data["clases"] for t in c["tablas"] for f in t["campos"]]
    return {"clases": len(data["clases"]), "tablas": sum(len(c["tablas"]) for c in data["clases"]),
            "campos": len(fields), "obligatorios": sum(f["marca"].startswith("obligatorio") for f in fields),
            "segun_alcance": sum("según alcance" in f["marca"] for f in fields),
            "sin_convencion": sum("sin convención" in f["marca"] for f in fields),
            "sin_etapa": sum(f["marca"].startswith("sin columna") for f in fields),
            "sin_dataset": sorted(c["hoja"] for c in data["clases"] if c["dataset"].startswith("Sin"))}
