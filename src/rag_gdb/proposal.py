"""Primera pasada local de extracción: un modelo elige bloques, la cita sale del PDF.

El texto de cada página se parte en bloques numerados. El modelo local solo
indica qué bloques son observaciones; la cita es el texto del bloque, así que
siempre es literal y pasa `validar`. El resultado son candidatos sin revisar.
"""

from __future__ import annotations

import hashlib
import json
import re
import urllib.request
from collections import Counter
from collections.abc import Callable
from datetime import date
from pathlib import Path

from .extraction import _norm, page_texts
from .inventory import sha256, write_json

MIN_BLOCK = 25
MAX_BLOCK = 500
MAX_CITA = 600
SEGMENTER = "3"  # cambia la clave de reanudación cuando cambia la segmentación
IDU_MARK = re.compile(r"OBSERVACI[OÓ]N\s+IDU", re.IGNORECASE)
# Una línea que empieza con viñeta, numeral o rótulo abre un enunciado nuevo.
ITEM_START = re.compile(
    r"^\s*(?:[-•·▪◦●]\s*|o\s+(?=[A-ZÁÉÍÓÚÑ])|\(?\d{1,2}[.)]\s+|\(?[a-z][.)]\s+|[ivx]{1,4}[.)]\s+"
    r"|(?:OBSERVACI[OÓ]N|RESPUESTA|VALIDACI[OÓ]N|REVISI[OÓ]N|Seguimiento)\b)")


def _segments(chunk: str) -> list[str]:
    """Parte un párrafo en enunciados: por viñetas o rótulos y, si sigue largo, por frases."""
    items: list[list[str]] = []
    for line in chunk.splitlines():
        if not line.strip():
            continue
        if not items or ITEM_START.match(line):
            items.append([line])
        else:
            items[-1].append(line)
    out = []
    for item in (" ".join(" ".join(lines).split()) for lines in items):
        if len(item) <= MAX_BLOCK:
            out.append(item)
            continue
        piece = ""
        for sentence in re.split(r"(?<=[.;:])\s+(?=[A-ZÁÉÍÓÚÑ¿\"“(-])", item):
            if piece and len(piece) + len(sentence) > MAX_BLOCK:
                out.append(piece)
                piece = sentence
            else:
                piece = f"{piece} {sentence}".strip()
        out.append(piece)
    merged: list[str] = []
    for segment in out:  # un fragmento corto se une al anterior para no perder texto
        if merged and len(segment) < MIN_BLOCK:
            merged[-1] = f"{merged[-1]} {segment}"
        else:
            merged.append(segment)
    return merged


def page_blocks(pages: list[str]) -> list[dict]:
    """Enunciados por página; descarta encabezados y pies que se repiten en la mitad o más de las páginas."""
    split = [[s for c in re.split(r"\n\s*\n", text) for s in _segments(c)] for text in pages]
    split = [[b for b in page if len(b) >= MIN_BLOCK] for page in split]
    seen = Counter(key for page in split for key in {_norm(b) for b in page})
    repeated = {k for k, n in seen.items() if len(pages) >= 3 and n >= max(3, len(pages) / 2)}
    blocks = []
    for number, page in enumerate(split, 1):
        for text in page:
            if _norm(text) not in repeated:
                blocks.append({"id": f"B{len(blocks) + 1}", "pagina": number, "texto": text})
    return blocks


def _cita(text: str) -> str:
    if len(text) <= MAX_CITA:
        return text
    cut = text[:MAX_CITA]
    return cut[:cut.rfind(" ")] if " " in cut[MIN_BLOCK:] else cut


def ollama_ask(model: str, url: str = "http://localhost:11434") -> Callable[[str], str]:
    def ask(prompt: str) -> str:
        body = {"model": model, "stream": False, "think": False, "format": "json",
                "options": {"temperature": 0, "num_ctx": 8192, "num_predict": 3000},
                "messages": [{"role": "user", "content": prompt}]}
        request = urllib.request.Request(f"{url}/api/chat", json.dumps(body).encode(),
                                         {"Content-Type": "application/json"})
        with urllib.request.urlopen(request, timeout=600) as response:
            return json.load(response)["message"]["content"]
    return ask


def propose(pages: list[str], template: str, ask: Callable[[str], str]) -> tuple[list[dict], list[int]]:
    """Candidatos de observación y páginas cuya respuesta no fue JSON válido."""
    blocks = page_blocks(pages)
    by_id = {b["id"]: b for b in blocks}
    candidates, failed, used, texts = [], [], set(), set()
    for number in range(1, len(pages) + 1):
        own = [b for b in blocks if b["pagina"] == number]
        if not own:
            continue
        listing = "\n".join(f"[{b['id']}] {b['texto'][:420]}" for b in own)
        try:
            answer = json.loads(ask(template.replace("{bloques}", listing)))["observaciones"]
        except (ValueError, KeyError, TypeError):
            failed.append(number)
            continue
        for item in answer if isinstance(answer, list) else []:
            block = by_id.get(str(item.get("bloque", ""))) if isinstance(item, dict) else None
            if (block is None or block["pagina"] != number or block["id"] in used
                    or _norm(block["texto"]) in texts):  # mismo enunciado en otra fila o página
                continue
            used.add(block["id"])
            texts.add(_norm(block["texto"]))
            autor = item.get("autor")
            if autor not in ("idu", "interventoria"):
                autor = "idu" if IDU_MARK.search(block["texto"]) else "interventoria"
            numero = item.get("numero")
            resumen = str(item.get("resumen") or "").strip()
            candidates.append({
                "id": f"obs-{len(candidates) + 1:03d}",
                "numero": None if numero in (None, "", "null") else str(numero),
                "autor": autor, "radicado_origen": None, "pagina": number,
                "cita": _cita(block["texto"]),
                "resumen": resumen if len(resumen) >= 10 else _cita(block["texto"])[:200],
                "estado_en_documento": "sin_estado", "requiere_cotejo_visual": False,
            })
    return candidates, failed


def propose_selected(manifest: dict, pdf_dir: Path, output_dir: Path, selected: list[str],
                     template: str, model: str, ask: Callable[[str], str]) -> dict:
    allowed = {item["ruta"]: item for item in manifest["archivos"]}
    state_path = output_dir / "estado.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {"version": 1, "documentos": {}}
    prompt_sha = hashlib.sha256((template + SEGMENTER).encode()).hexdigest()[:12]
    for relative in selected:
        if relative not in allowed:
            raise ValueError(f"PDF no encontrado en el manifiesto: {relative}")
        item = allowed[relative]
        out_path = output_dir / Path(relative).with_suffix(".json")
        previous = state["documentos"].get(relative, {})
        if (previous.get("estado") == "ok" and previous.get("sha256") == item["sha256"]
                and previous.get("modelo") == model and previous.get("prompt") == prompt_sha
                and out_path.exists()):
            continue
        if sha256(pdf_dir / relative) != item["sha256"]:
            raise ValueError(f"El PDF cambió después del inventario: {relative}")
        record = {"sha256": item["sha256"], "modelo": model, "prompt": prompt_sha}
        try:
            candidates, failed = propose(page_texts(pdf_dir / relative), template, ask)
            write_json(out_path, {
                "version": 1, "documento": {"ruta": relative, "sha256": item["sha256"]},
                "extraido_por": f"{model} (candidatos de rag-gdb proponer, sin revisar)",
                "fecha_extraccion": date.today().isoformat(),
                "notas": ("Candidatos de la pasada local: la cita es el bloque literal del PDF; "
                          "autor, número y resumen los propone el modelo; estado y cotejo visual "
                          "no se evalúan. Revisar antes de mover a 03_extraido."
                          + (f" Páginas sin respuesta válida: {failed}." if failed else "")),
                "observaciones": candidates})
            record.update(estado="error" if failed else "ok", candidatos=len(candidates),
                          paginas_error=failed)
        except Exception as exc:  # noqa: BLE001 — se registra por documento y se reintenta al repetir
            record.update(estado="error", detalle=str(exc))
        state["documentos"][relative] = record
        write_json(state_path, state)
    return state
