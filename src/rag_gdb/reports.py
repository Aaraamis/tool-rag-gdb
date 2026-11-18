"""Entregables de inventario: `matriz-observaciones.md` e `informe-corpus.md`."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

SIN_CONTRATO = "sin determinar"
QUOTE_CHARS = 200


def read_contracts(path: Path) -> dict[str, str]:
    """Contrato de obra por ruta, según `config/contratos-documentos.csv` (revisión manual con evidencia)."""
    if not path.exists():
        return {}
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["ruta"]: row["contrato"] for row in csv.DictReader(handle) if row["contrato"]}


def date_of(ruta: str) -> str:
    """Fecha `AAAA-MM-DD` que prefija el nombre del archivo, o `sin fecha`."""
    found = re.match(r"(\d{4}-\d{2}-\d{2})_", ruta.rsplit("/", 1)[-1])
    return found.group(1) if found else "sin fecha"


def _cell(text: str, limit: int | None = None) -> str:
    text = " ".join(text.split()).replace("|", "\\|")
    if limit and len(text) > limit:
        text = text[:text.rfind(" ", 0, limit)] + " …"
    return text


def render_matriz(grupos: dict, contracts: dict[str, str], today: str | None = None,
                  themes_by_group: dict[str, str] | None = None) -> str:
    contract_of = lambda ruta: contracts.get(ruta, SIN_CONTRATO)  # noqa: E731
    themes = {t["tema"]: t["nombre"] for t in grupos["temas"]}
    rows: dict[str, list[tuple]] = {code: [] for code in themes}
    for group in grupos["grupos"]:
        for m in group["miembros"]:
            rows[(themes_by_group or {}).get(group["grupo"], group["tema"])].append((date_of(m["ruta"]), m["ruta"], m["id"], m))
    total = sum(len(r) for r in rows.values())
    docs = len({m["ruta"] for g in grupos["grupos"] for m in g["miembros"]})
    unknown = sum(contract_of(r[1]) == SIN_CONTRATO for r in sum(rows.values(), []))
    lines = [
        "# Matriz de observaciones GDB — borrador",
        "",
        f"> Generado por `rag-gdb matriz` el {today or date.today().isoformat()}: {total} observaciones de "
        f"{docs} documentos, agrupadas por tema (`config/temas.csv`, pendiente de validación de Aramis; "
        "el tema es el del requisito redactado en `config/requisitos-redaccion.csv` cuando existe).",
        "> **Contrato:** contrato de obra según `config/contratos-documentos.csv`, revisado por documento "
        "con su evidencia (asunto, texto o respuesta que cita el mismo radicado); "
        f"{unknown} de {total} observaciones quedan «{SIN_CONTRATO}» hasta revisar la primera página del PDF. "
        "**Fecha:** la del prefijo del nombre del archivo (fecha de envío), no la del oficio.",
        "",
        "## Resumen por tema",
        "",
        "| Tema | Observaciones |",
        "|---|---:|",
    ]
    lines += [f"| {code}. {themes[code]} | {len(rows[code])} |" for code in themes]
    for code in themes:
        lines += ["", f"## {code}. {themes[code]}", "",
                  "| Fecha | Contrato | Autor | Referencia | Observación |", "|---|---|---|---|---|"]
        for fecha, ruta, _, m in sorted(rows[code], key=lambda r: (r[0], r[1], r[2])):
            origin = m["radicado_origen"] or "sin radicado"
            lines.append(f"| {fecha} | {contract_of(ruta)} | {m['autor']} | "
                         f"{_cell(origin)}, `{_cell(ruta)}`, p. {m['pagina']}, {m['id']} | "
                         f"{_cell(m['resumen'], QUOTE_CHARS)} |")
    return "\n".join(lines) + "\n"


def write_matriz(grupos_path: Path, output: Path, contracts_path: Path,
                 themes_by_group: dict[str, str] | None = None) -> dict:
    grupos = json.loads(grupos_path.read_text(encoding="utf-8"))
    if not grupos.get("temas"):
        raise ValueError("grupos.json no tiene temas: ejecuta `rag-gdb consolidar` con config/temas.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_matriz(grupos, read_contracts(contracts_path), themes_by_group=themes_by_group), encoding="utf-8")
    return {"observaciones": sum(len(g["miembros"]) for g in grupos["grupos"]),
            "documentos": len({m["ruta"] for g in grupos["grupos"] for m in g["miembros"]})}


def _pending_reason(row: dict) -> str:
    """Motivo por el que un archivo aún no tiene extracción, según su clasificación."""
    if row["gdb"] == "no":
        return "no trata de la GDB (sin extracción prevista)"
    if row["gdb"] in {"si", "probable"}:
        return "relevante para la GDB; extracción pendiente"
    return "relevancia por revisar; extracción pendiente"


def build_informe(manifest: dict, profiles: dict, classification: list[dict],
                  converted: dict, extracted: dict[str, int]) -> dict:
    """Cuenta cada archivo del manifiesto en exactamente una categoría."""
    by_path = {row["ruta"]: row for row in classification}
    files = []
    for item in manifest["archivos"]:
        ruta = item["ruta"]
        if item.get("motivo_exclusion"):
            status, reason = "descartado", item["motivo_exclusion"]
        elif ruta in extracted:
            status = "procesado"
            reason = (f"{extracted[ruta]} observaciones extraídas" if extracted[ruta]
                      else "revisado; sin observaciones extraíbles")
        else:
            status, reason = "pendiente", _pending_reason(by_path[ruta])
        files.append({"ruta": ruta, "estado": status, "motivo": reason})
    profile_docs = profiles["documentos"]
    return {
        "archivos": files,
        "ocr": sorted(r for r, p in profile_docs.items() if p.get("necesita_ocr")),
        "sin_perfil": sorted(i["ruta"] for i in manifest["archivos"] if i["ruta"] not in profile_docs),
        "convertidos": sum(v["estado"] == "ok" for v in converted["documentos"].values()),
        "ausentes": manifest["ausentes"],
        "inventario": manifest["resumen"],
    }


def render_informe(data: dict, today: str | None = None) -> str:
    files = data["archivos"]
    status = Counter(f["estado"] for f in files)
    reasons = Counter((f["estado"], f["motivo"]) for f in files if f["estado"] != "procesado")
    ocr = data["ocr"]
    pending_ocr = [r for r in ocr if any(f["ruta"] == r and f["estado"] == "pendiente" for f in files)]
    lines = [
        "# Informe del corpus GDB — borrador",
        "",
        f"> Generado por `rag-gdb informe` el {today or date.today().isoformat()}. "
        f"Cada uno de los {len(files)} PDF del manifiesto aparece una sola vez en el apéndice.",
        "",
        "## Resumen",
        "",
        "| Estado | Archivos |",
        "|---|---:|",
        f"| Procesado (con JSON validado en `03_extraido`) | {status['procesado']} |",
        f"| Descartado por reglas de ruido (RF2) | {status['descartado']} |",
        f"| Pendiente | {status['pendiente']} |",
        f"| **Total en disco** | **{len(files)}** |",
        "",
        "## Entrada",
        "",
        f"- Archivos PDF en disco: {data['inventario']['archivos_pdf']}; "
        f"coincidentes con la hoja de Batea: {data['inventario']['coincidentes']}; "
        f"huérfanos: {data['inventario']['huerfanos']}.",
        f"- Filas descargadas de la hoja sin archivo en disco (ausentes): {len(data['ausentes'])}.",
        "",
        "## Descartados y pendientes",
        "",
        "| Estado | Motivo | Archivos |",
        "|---|---|---:|",
    ]
    lines += [f"| {s} | {r} | {n} |" for (s, r), n in sorted(reasons.items())] or ["| — | — | 0 |"]
    lines += [
        "",
        "## OCR y conversión",
        "",
        f"- Documentos que necesitan OCR según el perfil técnico: {len(ocr)}; "
        f"de ellos, {len(pending_ocr)} siguen pendientes.",
        f"- PDF convertidos con Docling (JSON + Markdown): {data['convertidos']}.",
        f"- Archivos sin perfil técnico: {len(data['sin_perfil'])}.",
        "",
        "## Apéndice: estado por archivo",
        "",
        "| Estado | Archivo | Detalle |",
        "|---|---|---|",
    ]
    for f in sorted(files, key=lambda f: (f["estado"], f["ruta"])):
        lines.append(f"| {f['estado']} | `{_cell(f['ruta'])}` | {_cell(f['motivo'])} |")
    lines += ["", "## Ausentes (en la hoja, sin archivo)", "", "| Nombre | Motivo |", "|---|---|"]
    lines += [f"| {_cell(a['nombre'])} | {_cell(a['motivo'])} |" for a in data["ausentes"]]
    return "\n".join(lines) + "\n"


def write_informe(manifest_path: Path, profiles_path: Path, classification_path: Path,
                  converted_path: Path, extract_dir: Path, output: Path) -> dict:
    load = lambda p: json.loads(p.read_text(encoding="utf-8"))  # noqa: E731
    extracted = {}
    for path in sorted(extract_dir.rglob("*.json")):
        if path.name == "estado.json":
            continue
        data = load(path)
        extracted[data["documento"]["ruta"]] = len(data["observaciones"])
    with classification_path.open(encoding="utf-8", newline="") as handle:
        classification = list(csv.DictReader(handle))
    data = build_informe(load(manifest_path), load(profiles_path), classification,
                         load(converted_path), extracted)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_informe(data), encoding="utf-8")
    counts = Counter(f["estado"] for f in data["archivos"])
    return {"archivos": len(data["archivos"]), **counts}
