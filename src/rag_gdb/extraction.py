"""Validación de las observaciones extraídas por el agente."""

from __future__ import annotations

import json
import re
import unicodedata
from importlib import resources
from pathlib import Path

from jsonschema import Draft202012Validator

from .pipeline import _run


def load_schema() -> dict:
    return json.loads(resources.files(__package__).joinpath("observaciones.schema.json")
                      .read_text(encoding="utf-8"))


def page_texts(pdf: Path) -> list[str]:
    """Texto de cada página del PDF (índice 0 = página 1)."""
    match = re.search(r"^Pages:\s+(\d+)", _run("pdfinfo", str(pdf)), re.MULTILINE)
    if not match:
        raise ValueError(f"pdfinfo no devolvió páginas: {pdf}")
    return [_run("pdftotext", "-f", str(n), "-l", str(n), str(pdf), "-")
            for n in range(1, int(match.group(1)) + 1)]


def _norm(text: str) -> str:
    """Letras y dígitos sin tildes ni mayúsculas: tolera saltos de línea y comillas."""
    decomposed = unicodedata.normalize("NFKD", text).casefold()
    return "".join(c for c in decomposed if c.isalnum())


def validate_extraction(data: dict, manifest: dict, pdf_dir: Path,
                        relative: str | None = None,
                        cache: dict[str, list[str]] | None = None) -> list[str]:
    """Errores de una extracción; lista vacía si es válida.

    `relative` es la ruta del JSON bajo `03_extraido/` sin extensión, para
    comprobar que el archivo está donde la reanudación lo buscará.
    """
    errors = [f"esquema: {'/'.join(map(str, e.absolute_path)) or '(raíz)'}: {e.message}"
              for e in Draft202012Validator(load_schema()).iter_errors(data)]
    if errors:
        return errors
    cache = {} if cache is None else cache
    document = data["documento"]
    known = {item["ruta"]: item for item in manifest["archivos"]}
    item = known.get(document["ruta"])
    if item is None:
        return [f"documento.ruta no está en el manifiesto: {document['ruta']}"]
    if item["sha256"] != document["sha256"]:
        errors.append("documento.sha256 no coincide con el manifiesto")
    if relative is not None and relative != str(Path(document["ruta"]).with_suffix("")):
        errors.append(f"el archivo debe llamarse {Path(document['ruta']).with_suffix('.json')}")
    ids = [o["id"] for o in data["observaciones"]]
    errors += [f"id repetido: {i}" for i in sorted({i for i in ids if ids.count(i) > 1})]
    if document["ruta"] not in cache:
        cache[document["ruta"]] = page_texts(pdf_dir / document["ruta"])
    pages = cache[document["ruta"]]
    normalized = [_norm(text) for text in pages]
    for obs in data["observaciones"]:
        if obs["pagina"] > len(pages):
            errors.append(f"{obs['id']}: página {obs['pagina']} fuera del PDF ({len(pages)} páginas)")
        elif not obs["requiere_cotejo_visual"] and _norm(obs["cita"]) not in normalized[obs["pagina"] - 1]:
            found = [n for n, text in enumerate(normalized, 1) if _norm(obs["cita"]) in text]
            hint = f"; aparece en la página {found[0]}" if found else "; no aparece en ninguna página"
            errors.append(f"{obs['id']}: la cita no está en la página {obs['pagina']}{hint}")
    return errors


def validate_dir(extract_dir: Path, manifest: dict, pdf_dir: Path) -> dict[str, list[str]]:
    """Valida todos los JSON de `extract_dir`; devuelve los errores por archivo."""
    cache: dict[str, list[str]] = {}
    results = {}
    for path in sorted(extract_dir.rglob("*.json")):
        relative = str(path.relative_to(extract_dir).with_suffix(""))
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            results[str(path.relative_to(extract_dir))] = [f"JSON inválido: {exc}"]
            continue
        results[str(path.relative_to(extract_dir))] = validate_extraction(
            data, manifest, pdf_dir, relative, cache)
    return results
