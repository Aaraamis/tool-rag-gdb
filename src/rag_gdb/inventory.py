"""Cruce de PDF originales con la hoja Inventario de Batea."""

from __future__ import annotations

import hashlib
import json
import re
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

TABLE = "{urn:oasis:names:tc:opendocument:xmlns:table:1.0}"
TEXT = "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}"


def _cell_text(cell: ET.Element) -> str:
    return " ".join("".join(p.itertext()) for p in cell.iter(TEXT + "p")).strip()


def read_inventory(path: Path) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("content.xml"))
    sheet = next(
        (s for s in root.iter(TABLE + "table") if s.get(TABLE + "name") == "Inventario"),
        None,
    )
    if sheet is None:
        raise ValueError("El ODS no contiene la pestaña Inventario")
    rows = []
    for row in sheet.iter(TABLE + "table-row"):
        values = []
        for cell in row:
            if cell.tag not in (TABLE + "table-cell", TABLE + "covered-table-cell"):
                continue
            repeat = int(cell.get(TABLE + "number-columns-repeated", "1"))
            values.extend([_cell_text(cell)] * min(repeat, 20))
        if values and values[0]:
            rows.append(values)
    if not rows:
        raise ValueError("La pestaña Inventario está vacía")
    headers = rows[0]
    required = {"clave", "tipo", "nombre", "sha256", "estado"}
    if not required.issubset(headers):
        raise ValueError(f"Faltan columnas: {sorted(required - set(headers))}")
    return [dict(zip(headers, values)) for values in rows[1:]]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _exclusion(row: dict[str, str], rules: dict) -> str | None:
    for field, key in (("remitente", "remitentes"), ("asunto", "asuntos")):
        for pattern in rules.get(key, []):
            if re.search(pattern, row.get(field, ""), re.IGNORECASE):
                return f"{field}:{pattern}"
    return None


def build_manifest(pdf_dir: Path, ods: Path, rules: dict | None = None) -> dict:
    if not pdf_dir.is_dir():
        raise ValueError(f"No existe la carpeta de PDF: {pdf_dir}")
    rows = read_inventory(ods)
    rules = rules or {}
    by_hash: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        if row.get("sha256"):
            by_hash.setdefault(row["sha256"].lower(), []).append(row)
    files = []
    found_hashes = set()
    for path in sorted(pdf_dir.rglob("*.pdf")):
        digest = sha256(path)
        matches = by_hash.get(digest, [])
        found_hashes.add(digest)
        reasons = [_exclusion(r, rules) for r in matches]
        excluded = bool(matches) and all(reasons)
        files.append({
            "ruta": str(path.relative_to(pdf_dir)), "sha256": digest,
            "estado": "excluido" if excluded else "coincidente" if matches else "huerfano",
            "motivo_exclusion": "; ".join(sorted(set(x for x in reasons if x))) if excluded else None,
            "claves_inventario": [r["clave"] for r in matches],
        })
    absent = [
        {"clave": r["clave"], "nombre": r.get("nombre", ""),
         "sha256": r.get("sha256", ""), "estado_inventario": r.get("estado", ""),
         "motivo": "sin_archivo; pendiente_de_confirmacion"}
        for r in rows if r.get("tipo", "").lower() == "pdf"
        and r.get("estado") == "DESCARGADO" and r.get("sha256", "").lower() not in found_hashes
    ]
    return {
        "version": 1, "directorio_pdf": str(pdf_dir.resolve()),
        "inventario_ods": str(ods.resolve()),
        "resumen": {"archivos_pdf": len(files),
                    "coincidentes": sum(f["estado"] == "coincidente" for f in files),
                    "huerfanos": sum(f["estado"] == "huerfano" for f in files),
                    "excluidos": sum(f["estado"] == "excluido" for f in files),
                    "ausentes_descargados": len(absent),
                    "estados_inventario": dict(Counter(r.get("estado", "") for r in rows))},
        "archivos": files, "ausentes": absent,
    }


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)
