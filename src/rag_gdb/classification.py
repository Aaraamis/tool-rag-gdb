"""Primera clasificación conservadora, basada en nombres e inventario."""

from __future__ import annotations

import csv
import re
import subprocess
from collections import Counter
from pathlib import Path

from .inventory import read_inventory

DATE_PREFIX = re.compile(r"^\d{4}-\d{2}-\d{2}_")
GDB = re.compile(r"(?:^|[^A-Z0-9])(?:GDB|BDG)(?=$|[^A-Z0-9])|GEODATABASE|BASE\s+DE\s+DATOS\s+GEOGR|SIG[\s_-]*CAD", re.I)
TEXT_GDB = re.compile(r"\b(?:GDB|BDG)\b|GEODATABASE|BASE\s+DE\s+DATOS\s+GEOGR", re.I)
TEXT_SIG_CAD = re.compile(r"\b(?:SIG|CAD)\b|SISTEMA\s+DE\s+INFORMACI[OÓ]N\s+GEOGR", re.I)


def classify_name(filename: str, subject: str = "") -> tuple[str, str, str, list[str]]:
    name = DATE_PREFIX.sub("", filename)
    upper = name.upper()
    reasons = []
    if re.match(r"MI-DIS-IDU[-_ ]?\d", upper):
        issuer = "disenos"
        reasons.append("codigo_inicial:MI-DIS-IDU")
    elif re.match(r"E-IDU[-_ ]?\d", upper):
        issuer = "obra"
        reasons.append("codigo_inicial:E-IDU")
    elif re.match(r"(?:C[.\s-]*1443|1443_)", upper):
        issuer = "interventoria"
        reasons.append("codigo_inicial:1443")
    elif re.match(r"MAB-[12]-1463\b|MV2-\d", upper):
        issuer = "interventoria"
        reasons.append("codigo_inicial:MAB-1463/MV2")
    elif re.match(r"(?:\d{1,2}[\s_-]+)?(?:STEST|STMST)\b", upper):
        issuer = "idu"
        reasons.append("codigo_inicial:STEST/STMST")
    elif re.match(r"GUIC\d+", upper):
        issuer = "idu"
        reasons.append("codigo_inicial:GUIC")
    else:
        issuer = "por_revisar"

    if re.search(r"GUIC\d+|(?<![A-Z0-9])GU[IÍ]A(?![A-Z0-9])|(?<![A-Z0-9])INSTRUCTIVO(?![A-Z0-9])", upper):
        kind = "guia_instructivo"
    elif "TRASLADO" in upper:
        kind = "traslado"
    elif re.search(r"(?<![A-Z0-9])(?:RTA|RESPUESTA)(?![A-Z0-9])", upper):
        kind = "respuesta"
    elif re.search(r"(?<![A-Z0-9])(?:ACTA|REUNI[OÓ]N)(?![A-Z0-9])", upper):
        kind = "acta"
    elif re.search(r"OBSERV|REVISI[OÓ]N|\bREV[_ .-]", upper):
        kind = "revision_observaciones"
    elif issuer != "por_revisar":
        kind = "comunicado"
    else:
        kind = "por_revisar"
    if kind != "por_revisar":
        reasons.append(f"nombre_tipo:{kind}")

    if GDB.search(name) or upper.startswith("GUIC06"):
        relevance = "si"
        reasons.append("nombre_gdb")
    elif GDB.search(subject):
        relevance = "por_revisar"
        reasons.append("solo_asunto_gdb")
    else:
        relevance = "por_revisar"
    return issuer, kind, relevance, reasons


def text_relevance(text: str) -> str:
    if TEXT_GDB.search(text):
        return "probable"
    if TEXT_SIG_CAD.search(text):
        return "posible"
    return "por_revisar"


def classify_manifest(manifest: dict, ods: Path, pdf_dir: Path | None = None) -> list[dict[str, str]]:
    by_hash: dict[str, list[dict[str, str]]] = {}
    for row in read_inventory(ods):
        if row.get("sha256"):
            by_hash.setdefault(row["sha256"].lower(), []).append(row)
    result = []
    for item in manifest["archivos"]:
        metadata = by_hash.get(item["sha256"].lower(), [])
        subjects = sorted({row.get("asunto", "") for row in metadata if row.get("asunto")})
        senders = sorted({row.get("remitente", "") for row in metadata if row.get("remitente")})
        issuer, kind, relevance, reasons = classify_name(Path(item["ruta"]).name, " | ".join(subjects))
        excluded = item["estado"] == "excluido"
        if not excluded and pdf_dir is not None and relevance == "por_revisar":
            try:
                extracted = subprocess.run(
                    ["pdftotext", str(pdf_dir / item["ruta"]), "-"],
                    capture_output=True, text=True, timeout=30, check=False,
                )
                if extracted.returncode == 0 and len(extracted.stdout.strip()) >= 100:
                    relevance = text_relevance(extracted.stdout)
                    reasons.append(f"texto_pdf:{relevance}")
                else:
                    reasons.append("texto_pdf:no_disponible")
            except (OSError, subprocess.TimeoutExpired):
                reasons.append("texto_pdf:error")
        result.append({
            "ruta": item["ruta"], "sha256": item["sha256"],
            "estado_inventario": item["estado"],
            "emisor": "no_evaluado" if excluded else issuer,
            "tipo": "no_evaluado" if excluded else kind,
            "gdb": "no_evaluado" if excluded else relevance,
            "revisar": "si" if not excluded and (
                issuer == "por_revisar" or kind == "por_revisar" or relevance != "si") else "no",
            "motivos": "; ".join(reasons),
            "evidencia_manual": "",
            "asunto": " | ".join(subjects), "remitente": " | ".join(senders),
        })
    return result


def apply_manual_reviews(rows: list[dict[str, str]], path: Path) -> None:
    if not path.exists():
        return
    by_hash = {row["sha256"]: row for row in rows}
    seen = set()
    allowed = {
        "emisor": {"idu", "interventoria", "obra", "disenos"},
        "tipo": {"guia_instructivo", "traslado", "respuesta", "acta",
                 "revision_observaciones", "comunicado"},
        "gdb": {"si", "no"},
    }
    with path.open(encoding="utf-8", newline="") as stream:
        for review in csv.DictReader(stream):
            digest = review.get("sha256", "")
            if digest in seen or digest not in by_hash:
                raise ValueError(f"Hash duplicado o ausente del manifiesto en {path}: {digest}")
            seen.add(digest)
            evidence = review.get("justificacion", "").strip()
            values = {field: review.get(field, "").strip() for field in allowed}
            if not evidence or not any(values.values()):
                raise ValueError(f"Revisión manual sin decisión o justificación: {digest}")
            for field, value in values.items():
                if value and value not in allowed[field]:
                    raise ValueError(f"Valor manual inválido para {field}: {value}")
            row = by_hash[digest]
            if row["estado_inventario"] == "excluido":
                raise ValueError(f"No se revisa un PDF excluido: {digest}")
            row.update({field: value for field, value in values.items() if value})
            row["evidencia_manual"] = evidence
            row["revisar"] = "si" if (row["gdb"] != "no" and
                                      (row["emisor"] == "por_revisar" or
                                       row["tipo"] == "por_revisar" or row["gdb"] != "si")) else "no"


def write_classification(path: Path, rows: list[dict[str, str]]) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    fields = ["ruta", "sha256", "estado_inventario", "emisor", "tipo", "gdb",
              "revisar", "motivos", "evidencia_manual", "asunto", "remitente"]
    with temporary.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)
    return {"documentos": len(rows), "emisor": dict(Counter(r["emisor"] for r in rows)),
            "tipo": dict(Counter(r["tipo"] for r in rows)),
            "gdb": dict(Counter(r["gdb"] for r in rows)),
            "por_revisar": sum(r["revisar"] == "si" for r in rows)}
