"""Perfil técnico y conversión reanudable de PDF."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

from .inventory import sha256, write_json


def _run(*args: str) -> str:
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout


def profile_pdf(path: Path) -> dict:
    info = _run("pdfinfo", str(path))
    match = re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE)
    if not match:
        raise ValueError(f"pdfinfo no devolvió páginas: {path}")
    pages = int(match.group(1))
    chars = []
    for page in range(1, pages + 1):
        extracted = _run("pdftotext", "-f", str(page), "-l", str(page),
                         "-layout", str(path), "-")
        chars.append(len(extracted.strip()))
    return {"paginas": pages, "caracteres_por_pagina": chars,
            "paginas_sin_texto": [i for i, n in enumerate(chars, 1) if n < 40],
            "necesita_ocr": any(n < 40 for n in chars)}


def profile_manifest(manifest: dict, pdf_dir: Path, output: Path) -> dict:
    previous = json.loads(output.read_text()) if output.exists() else {}
    current_paths = {item["ruta"] for item in manifest["archivos"]}
    results = {path: profile for path, profile in previous.get("documentos", {}).items()
               if path in current_paths}
    for item in manifest["archivos"]:
        relative = item["ruta"]
        if (results.get(relative, {}).get("sha256") == item["sha256"]
                and results[relative].get("estado") == "ok"):
            continue
        try:
            results[relative] = {"sha256": item["sha256"], "estado": "ok",
                                 **profile_pdf(pdf_dir / relative)}
        except (subprocess.CalledProcessError, ValueError) as exc:
            results[relative] = {"sha256": item["sha256"], "estado": "error",
                                 "detalle": str(exc)}
        write_json(output, {"version": 1, "documentos": results})
    write_json(output, {"version": 1, "documentos": results})
    return {"version": 1, "documentos": results}


def convert_one(path: Path, json_path: Path, md_path: Path) -> None:
    try:
        from docling.document_converter import DocumentConverter
    except ImportError as exc:
        raise RuntimeError("Instala la dependencia opcional: pip install -e '.[conversion]'") from exc
    document = DocumentConverter().convert(str(path)).document
    write_json(json_path, document.export_to_dict())
    md_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = md_path.with_suffix(".md.tmp")
    temporary.write_text(document.export_to_markdown(), encoding="utf-8")
    temporary.replace(md_path)


def convert_selected(manifest: dict, pdf_dir: Path, output_dir: Path,
                     selected: list[str]) -> dict:
    allowed = {item["ruta"]: item for item in manifest["archivos"]}
    state_path = output_dir / "estado.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {"version": 1, "documentos": {}}
    for relative in selected:
        if relative not in allowed:
            raise ValueError(f"PDF no encontrado en el manifiesto: {relative}")
        item = allowed[relative]
        if item["estado"] == "excluido":
            raise ValueError(f"PDF excluido por las reglas: {relative}")
        stem = Path(relative).with_suffix("")
        json_path = output_dir / stem.with_suffix(".json")
        md_path = output_dir / stem.with_suffix(".md")
        previous = state["documentos"].get(relative, {})
        if (previous.get("estado") == "ok" and previous.get("sha256") == item["sha256"]
                and json_path.exists() and md_path.exists()):
            continue
        if sha256(pdf_dir / relative) != item["sha256"]:
            raise ValueError(f"El PDF cambió después del inventario: {relative}")
        try:
            convert_one(pdf_dir / relative, json_path, md_path)
            state["documentos"][relative] = {"sha256": item["sha256"], "estado": "ok"}
        except Exception as exc:  # noqa: BLE001 — se registra por documento y se reintenta al repetir
            state["documentos"][relative] = {"sha256": item["sha256"], "estado": "error",
                                             "detalle": str(exc)}
        write_json(state_path, state)
    return state
