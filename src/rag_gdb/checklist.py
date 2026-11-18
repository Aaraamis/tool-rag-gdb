"""Borrador de `checklist-gdb.md` a partir de los grupos consolidados (RF8)."""

from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

from .normative_links import current_keys, group_key, read_group_registry, read_link_decisions, remap_decisions

EXAMPLE_CHARS = 160


def read_editorial(path: Path) -> dict[str, dict]:
    """Redacción por clave de grupo (`config/requisitos-redaccion.csv`): requisito, tema y texto."""
    if not path.exists():
        return {}
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    texts: dict[str, tuple[str, str]] = {}
    result = {}
    for row in rows:
        rid, entry = row["requisito_id"], (row["tema"], row["requisito"])
        if texts.setdefault(rid, entry) != entry:
            raise ValueError(f"El requisito {rid} tiene temas o textos distintos entre filas")
        if row["clave_grupo"] in result:
            raise ValueError(f"Grupo asignado a dos requisitos: {row['grupo']}")
        result[row["clave_grupo"]] = {"requisito_id": rid, "tema": entry[0], "requisito": entry[1]}
    return result


def _examples(members: list[dict], limit: int = 2) -> list[dict]:
    """Ejemplos de radicados distintos; primero los del IDU."""
    chosen, seen = [], set()
    for member in sorted(members, key=lambda m: m["autor"] != "idu"):
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


def _units(groups: list[dict], editorial: dict[str, dict], normative_links: dict | None,
           reviewed: set[str]) -> list[dict]:
    """Une los grupos que comparten requisito redactado; los demás quedan como su propio requisito."""
    units: dict[str, dict] = {}
    for g in groups:
        key = group_key(g)
        edit = editorial.get(key)
        uid = edit["requisito_id"] if edit else g["grupo"]
        unit = units.setdefault(uid, {
            "id": uid, "tema": edit["tema"] if edit else g.get("tema"), "redactado": bool(edit),
            "texto": edit["requisito"] if edit else g["representante"], "grupos": [], "miembros": [],
            "links": [], "revisados": 0})
        unit["grupos"].append(g["grupo"])
        unit["miembros"] += g["miembros"]
        for link in (normative_links or {}).get(key, []):
            if link["id"] not in {x["id"] for x in unit["links"]}:
                unit["links"].append(link)
        unit["revisados"] += key in reviewed
    for unit in units.values():
        members = unit["miembros"]
        unit["frecuencia_idu"] = len({m["radicado_origen"] or m["ruta"] for m in members if m["autor"] == "idu"})
        unit["documentos"] = len({m["ruta"] for m in members})
        unit["documentos_interventoria"] = len({m["ruta"] for m in members if m["autor"] == "interventoria"})
    return list(units.values())


def render(grupos: dict, today: str | None = None, normative_links: dict[str, list[dict]] | None = None,
           reviewed_links: set[str] | None = None, editorial: dict[str, dict] | None = None) -> str:
    themes = {t["tema"]: t for t in grupos["temas"]}
    groups = grupos["grupos"]
    reviewed = reviewed_links or set()
    units = _units(groups, editorial or {}, normative_links, reviewed)
    total_obs = sum(len(g["miembros"]) for g in groups)
    total_docs = len({m["ruta"] for g in groups for m in g["miembros"]})
    drafted = sum(u["redactado"] for u in units)
    if drafted:
        wording = (f"{drafted} requisitos tienen redacción propuesta en `config/requisitos-redaccion.csv`, "
                   "pendiente de validación de Aramis")
        undrafted = len(units) - drafted
        wording += f"; {undrafted} conservan el enunciado representativo de su grupo." if undrafted else "."
    else:
        wording = "Cada requisito conserva todavía la redacción representativa de su grupo."
    if normative_links is None:
        normative_status = "la normativa vigente (RF7) aún no está enlazada. " + wording
    else:
        practices = sum(not u["links"] and u["revisados"] == len(u["grupos"]) for u in units)
        if len(reviewed) == len(groups):
            normative_status = (f"la revisión normativa está confirmada para los {len(groups)} grupos; "
                                f"{practices} requisitos quedan identificados como prácticas observadas sin "
                                "respaldo escrito localizado. " + wording)
        else:
            normative_status = (f"la revisión normativa está confirmada para {len(reviewed)} de "
                                f"{len(groups)} grupos; los demás quedan marcados como pendientes. " + wording)
    lines = [
        "# Checklist GDB — borrador",
        "",
        f"> Generado por `rag-gdb checklist` el {today or date.today().isoformat()} a partir de "
        f"{total_obs} observaciones de {total_docs} documentos, agrupadas en {len(groups)} grupos"
        + (f" y {len(units)} requisitos." if len(units) != len(groups) else " y requisitos."),
        "> **Pendiente:** la taxonomía de temas (`config/temas.csv`) requiere validación de Aramis; "
        + normative_status,
        "",
        "Cómo leer cada requisito: **IDU ×n** es el número de radicados IDU distintos que lo observaron "
        "(un traslado o una copia no suma); **interventoría ×m** es el número de documentos de la "
        "interventoría que lo plantean. Entre comillas invertidas van los grupos de observaciones que lo "
        "respaldan.",
        "",
        "## Resumen por tema",
        "",
        "| Tema | Requisitos | Observados por el IDU | Radicados IDU (suma) |",
        "|---|---:|---:|---:|",
    ]
    order = sorted(themes, key=lambda t: -sum(u["frecuencia_idu"] for u in units if u["tema"] == t))
    for code in order:
        own = [u for u in units if u["tema"] == code]
        lines.append(f"| {code}. {themes[code]['nombre']} | {len(own)} | "
                     f"{sum(u['frecuencia_idu'] > 0 for u in own)} | {sum(u['frecuencia_idu'] for u in own)} |")
    for code in order:
        own = sorted((u for u in units if u["tema"] == code),
                     key=lambda u: (-u["frecuencia_idu"], -u["documentos"], u["id"]))
        lines += ["", f"## {code}. {themes[code]['nombre']}", ""]
        for u in own:
            tags = []
            if u["frecuencia_idu"]:
                tags.append(f"IDU ×{u['frecuencia_idu']}")
            if u["documentos_interventoria"]:
                tags.append(f"interventoría ×{u['documentos_interventoria']}")
            text = u["texto"].rstrip(".")
            label = f"**{u['id']}** " if u["redactado"] else ""
            refs = " ".join(f"`{code}`" for code in u["grupos"])
            lines.append(f"- [ ] {label}{text[:1].upper()}{text[1:]}. — {' · '.join(tags)} {refs}")
            if normative_links is not None:
                for link in u["links"]:
                    lines.append(f"  - Normativa {link['tipo']}: **{link['id']}** — {_quote(link['texto'])}")
                if not u["links"] and u["revisados"] == len(u["grupos"]):
                    lines.append("  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.")
                elif u["revisados"] < len(u["grupos"]):
                    lines.append("  - Normativa: pendiente de revisión"
                                 + (" para parte de sus grupos." if u["links"] or u["revisados"] else "."))
            for m in _examples(u["miembros"]):
                origin = m["radicado_origen"] or "sin radicado"
                lines.append(f"  - «{_quote(m['cita'])}» ({origin}, `{m['ruta']}`, p. {m['pagina']})")
    return "\n".join(lines) + "\n"


def write_checklist(grupos_path: Path, output: Path, links_path: Path | None = None,
                    catalog_path: Path | None = None, registry_path: Path | None = None,
                    editorial_path: Path | None = None) -> dict:
    grupos = json.loads(grupos_path.read_text(encoding="utf-8"))
    if not grupos.get("temas"):
        raise ValueError("grupos.json no tiene temas: ejecuta `rag-gdb consolidar` con config/temas.csv")
    mapping = None
    if registry_path:
        mapping = current_keys(grupos["grupos"], read_group_registry(registry_path))
    links = reviewed = None
    if links_path and catalog_path and links_path.exists() and catalog_path.exists():
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        links, reviewed = read_link_decisions(links_path, catalog)
        if mapping is not None:
            links, reviewed = remap_decisions(links, reviewed, mapping)
    editorial = read_editorial(editorial_path) if editorial_path else {}
    if mapping is not None:
        editorial = remap_editorial(editorial, mapping)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(grupos, normative_links=links, reviewed_links=reviewed, editorial=editorial),
                      encoding="utf-8")
    units = _units(grupos["grupos"], editorial, links, reviewed or set())
    return {"grupos": len(grupos["grupos"]), "requisitos": len(units),
            "requisitos_redactados": sum(u["redactado"] for u in units),
            "observados_por_idu": sum(u["frecuencia_idu"] > 0 for u in units),
            "grupos_normativa_revisados": len(reviewed or set()),
            "grupos_con_enlace": len(links or {})}


def remap_editorial(editorial: dict[str, dict], mapping: dict[str, str]) -> dict[str, dict]:
    """Expresa la redacción con las claves actuales; si dos claves caen en un grupo, gana la primera."""
    moved: dict[str, dict] = {}
    for key, entry in editorial.items():
        if key in mapping:
            moved.setdefault(mapping[key], entry)
    return moved


def editorial_themes(grupos_path: Path, editorial_path: Path, registry_path: Path) -> dict[str, str]:
    """Tema editorial por código de grupo actual, para reutilizarlo en la matriz."""
    grupos = json.loads(grupos_path.read_text(encoding="utf-8"))["grupos"]
    editorial = remap_editorial(read_editorial(editorial_path),
                                current_keys(grupos, read_group_registry(registry_path)))
    return {g["grupo"]: editorial[group_key(g)]["tema"] for g in grupos if group_key(g) in editorial}
