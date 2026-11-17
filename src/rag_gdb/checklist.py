"""Borrador de `checklist-gdb.md` a partir de los grupos consolidados (RF8)."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

EXAMPLE_CHARS = 160


def _examples(group: dict, limit: int = 2) -> list[dict]:
    """Ejemplos de radicados distintos; primero los del IDU."""
    chosen, seen = [], set()
    for member in sorted(group["miembros"], key=lambda m: m["autor"] != "idu"):
        origin = member["radicado_origen"] or member["ruta"]
        if origin in seen:
            continue
        seen.add(origin)
        chosen.append(member)
        if len(chosen) == limit:
            break
    return chosen


def _quote(text: str) -> str:
    text = " ".join(text.split())
    return text if len(text) <= EXAMPLE_CHARS else text[:text.rfind(" ", 0, EXAMPLE_CHARS)] + " …"


def render(grupos: dict, today: str | None = None) -> str:
    themes = {t["tema"]: t for t in grupos["temas"]}
    groups = grupos["grupos"]
    total_obs = sum(len(g["miembros"]) for g in groups)
    total_docs = len({m["ruta"] for g in groups for m in g["miembros"]})
    lines = [
        "# Checklist GDB — borrador",
        "",
        f"> Generado por `rag-gdb checklist` el {today or date.today().isoformat()} a partir de "
        f"{total_obs} observaciones de {total_docs} documentos, agrupadas en {len(groups)} requisitos.",
        "> **Pendiente:** la taxonomía de temas (`config/temas.csv`) requiere validación de Aramis; la "
        "normativa vigente (RF7) aún no está enlazada; cada requisito es el enunciado representativo de su "
        "grupo, sin redacción final.",
        "",
        "Cómo leer cada requisito: **IDU ×n** es el número de radicados IDU distintos que lo observaron "
        "(un traslado o una copia no suma); **interventoría ×m** es el número de documentos de la "
        "interventoría que lo plantean.",
        "",
        "## Resumen por tema",
        "",
        "| Tema | Requisitos | Observados por el IDU | Radicados IDU (suma) |",
        "|---|---:|---:|---:|",
    ]
    order = sorted(themes, key=lambda t: -sum(g["frecuencia_idu"] for g in groups if g.get("tema") == t))
    for code in order:
        own = [g for g in groups if g.get("tema") == code]
        lines.append(f"| {code}. {themes[code]['nombre']} | {len(own)} | "
                     f"{sum(g['frecuencia_idu'] > 0 for g in own)} | {sum(g['frecuencia_idu'] for g in own)} |")
    for code in order:
        own = sorted((g for g in groups if g.get("tema") == code),
                     key=lambda g: (-g["frecuencia_idu"], -g["documentos"], g["representante"]))
        lines += ["", f"## {code}. {themes[code]['nombre']}", ""]
        for g in own:
            tags = []
            if g["frecuencia_idu"]:
                tags.append(f"IDU ×{g['frecuencia_idu']}")
            if g["documentos_interventoria"]:
                tags.append(f"interventoría ×{g['documentos_interventoria']}")
            text = g["representante"].rstrip(".")
            lines.append(f"- [ ] {text[:1].upper()}{text[1:]}. — {' · '.join(tags)} `{g['grupo']}`")
            for m in _examples(g):
                origin = m["radicado_origen"] or "sin radicado"
                lines.append(f"  - «{_quote(m['cita'])}» ({origin}, `{m['ruta']}`, p. {m['pagina']})")
    return "\n".join(lines) + "\n"


def write_checklist(grupos_path: Path, output: Path) -> dict:
    grupos = json.loads(grupos_path.read_text(encoding="utf-8"))
    if not grupos.get("temas"):
        raise ValueError("grupos.json no tiene temas: ejecuta `rag-gdb consolidar` con config/temas.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(grupos), encoding="utf-8")
    return {"requisitos": len(grupos["grupos"]),
            "observados_por_idu": sum(g["frecuencia_idu"] > 0 for g in grupos["grupos"])}
