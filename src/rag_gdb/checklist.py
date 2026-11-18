"""Borrador de `checklist-gdb.md` a partir de los grupos consolidados (RF8)."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from .normative_links import current_keys, group_key, read_group_registry, read_link_decisions, remap_decisions

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


def render(grupos: dict, today: str | None = None, normative_links: dict[str, list[dict]] | None = None,
           reviewed_links: set[str] | None = None) -> str:
    themes = {t["tema"]: t for t in grupos["temas"]}
    groups = grupos["grupos"]
    total_obs = sum(len(g["miembros"]) for g in groups)
    total_docs = len({m["ruta"] for g in groups for m in g["miembros"]})
    if normative_links is None:
        normative_status = ("la normativa vigente (RF7) aún no está enlazada; cada requisito es el enunciado "
                            "representativo de su grupo, sin redacción final.")
    else:
        reviewed_count = len(reviewed_links or set())
        if reviewed_count == len(groups):
            practices = len(groups) - len(normative_links)
            normative_status = (f"la revisión normativa está confirmada para los {len(groups)} grupos; "
                                f"{practices} quedan identificados como prácticas observadas sin respaldo "
                                "escrito localizado. Cada requisito conserva todavía la redacción "
                                "representativa de su grupo.")
        else:
            normative_status = (f"la revisión normativa está confirmada para {reviewed_count} de "
                                f"{len(groups)} grupos; los demás quedan marcados como pendientes. Cada "
                                "requisito conserva todavía la redacción representativa de su grupo.")
    lines = [
        "# Checklist GDB — borrador",
        "",
        f"> Generado por `rag-gdb checklist` el {today or date.today().isoformat()} a partir de "
        f"{total_obs} observaciones de {total_docs} documentos, agrupadas en {len(groups)} requisitos.",
        "> **Pendiente:** la taxonomía de temas (`config/temas.csv`) requiere validación de Aramis; "
        + normative_status,
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
            if normative_links is not None:
                key = group_key(g)
                links = normative_links.get(key, [])
                for link in links:
                    lines.append(f"  - Normativa {link['tipo']}: **{link['id']}** — "
                                 f"{_quote(link['texto'])}")
                if not links and key in (reviewed_links or set()):
                    lines.append("  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.")
                elif not links:
                    lines.append("  - Normativa: pendiente de revisión.")
            for m in _examples(g):
                origin = m["radicado_origen"] or "sin radicado"
                lines.append(f"  - «{_quote(m['cita'])}» ({origin}, `{m['ruta']}`, p. {m['pagina']})")
    return "\n".join(lines) + "\n"


def write_checklist(grupos_path: Path, output: Path, links_path: Path | None = None,
                    catalog_path: Path | None = None, registry_path: Path | None = None) -> dict:
    grupos = json.loads(grupos_path.read_text(encoding="utf-8"))
    if not grupos.get("temas"):
        raise ValueError("grupos.json no tiene temas: ejecuta `rag-gdb consolidar` con config/temas.csv")
    links = reviewed = None
    if links_path and catalog_path and links_path.exists() and catalog_path.exists():
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        links, reviewed = read_link_decisions(links_path, catalog)
        if registry_path:
            mapping = current_keys(grupos["grupos"], read_group_registry(registry_path))
            links, reviewed = remap_decisions(links, reviewed, mapping)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(grupos, normative_links=links, reviewed_links=reviewed), encoding="utf-8")
    return {"requisitos": len(grupos["grupos"]),
            "observados_por_idu": sum(g["frecuencia_idu"] > 0 for g in grupos["grupos"]),
            "grupos_normativa_revisados": len(reviewed or set()),
            "grupos_con_enlace": len(links or {})}
