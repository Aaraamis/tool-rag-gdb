"""Propuesta auditable de enlaces entre grupos de observaciones y normativa RF7."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import defaultdict
from collections.abc import Callable
from pathlib import Path

import numpy as np

from .inventory import write_json


def group_key(group: dict) -> str:
    members = "|".join(sorted(member["clave"] for member in group["miembros"]))
    return hashlib.sha1(members.encode()).hexdigest()[:16]


def _embed_cached(texts: list[str], embed: Callable, model: str, cache_path: Path) -> np.ndarray:
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    if cache.get("modelo") != model:
        cache = {"modelo": model, "vectores": {}}
    hashes = [hashlib.sha1(text.encode()).hexdigest() for text in texts]
    missing = sorted({key for key in hashes if key not in cache["vectores"]})
    if missing:
        by_hash = {key: text for key, text in zip(hashes, texts)}
        for start in range(0, len(missing), 128):
            batch = missing[start:start + 128]
            for key, vector in zip(batch, embed([by_hash[key] for key in batch])):
                cache["vectores"][key] = [round(value, 6) for value in vector]
        write_json(cache_path, cache)
    matrix = np.array([cache["vectores"][key] for key in hashes], dtype=float)
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    if np.any(norms == 0):
        raise ValueError("El modelo produjo un embedding vacío")
    return matrix / norms


def rank_links(group_vectors: np.ndarray, requirement_vectors: np.ndarray,
               top_k: int = 5) -> list[list[tuple[int, float]]]:
    """Índice y similitud de los requisitos más próximos a cada grupo."""
    if top_k < 1:
        raise ValueError("top_k debe ser positivo")
    similarities = group_vectors @ requirement_vectors.T
    limit = min(top_k, requirement_vectors.shape[0])
    return [[(int(index), float(row[index])) for index in np.argsort(-row)[:limit]]
            for row in similarities]


def propose_links(groups_path: Path, catalog_path: Path, output_path: Path, cache_path: Path,
                  embed: Callable, model: str, top_k: int = 5) -> dict:
    group_data = json.loads(groups_path.read_text(encoding="utf-8"))
    groups = group_data["grupos"]
    themes = {theme["tema"]: theme for theme in group_data.get("temas", [])}
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    group_texts = []
    for group in groups:
        theme = themes.get(group.get("tema"), {})
        context = f"{theme.get('nombre', '')}: {theme.get('descripcion', '')}".strip(": ")
        group_texts.append(f"{context} || {group['representante']}" if context else group["representante"])
    requirement_texts = [f"{item['fuente']} || {item['seccion']} || {item['texto']}" for item in catalog]
    vectors = _embed_cached(group_texts + requirement_texts, embed, model, cache_path)
    ranked = rank_links(vectors[:len(groups)], vectors[len(groups):], top_k)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["clave_grupo", "grupo", "tema", "resumen_grupo", "rango", "fuente",
                         "requisito_id", "seccion", "texto_normativo", "similitud", "decision"])
        for group, candidates in zip(groups, ranked):
            for rank, (index, similarity) in enumerate(candidates, 1):
                item = catalog[index]
                writer.writerow([group_key(group), group["grupo"], group.get("tema", ""),
                                 group["representante"], rank, item["fuente"], item["id"],
                                 item["seccion"], item["texto"], f"{similarity:.3f}", ""])
    best = [candidates[0][1] for candidates in ranked]
    return {"grupos": len(groups), "requisitos": len(catalog), "candidatos": len(groups) * min(top_k, len(catalog)),
            "mejor_similitud_min": round(min(best), 3), "mejor_similitud_media": round(float(np.mean(best)), 3),
            "mejor_similitud_max": round(max(best), 3), "salida": str(output_path)}


def _case_text(key: str, rows: list[dict]) -> str:
    first = rows[0]
    lines = [f"GRUPO {key} ({first['grupo']}, tema {first['tema']}): {first['resumen_grupo']}",
             "CANDIDATOS:"]
    for row in rows:
        lines.append(f"- [{row['requisito_id']}] {row['fuente']} | {row['seccion']} | "
                     f"{row['texto_normativo'][:500]}")
    return "\n".join(lines)


def review_links(candidates_path: Path, output_path: Path, state_path: Path, template: str,
                 ask: Callable[[str], str], model: str, batch_size: int = 5) -> dict:
    """Segunda opinión local reanudable; sus selecciones siguen sin ser decisiones finales."""
    if batch_size < 1:
        raise ValueError("batch_size debe ser positivo")
    with candidates_path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[row["clave_grupo"]].append(row)
    prompt_hash = hashlib.sha256(template.encode()).hexdigest()[:12]
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    if state.get("modelo") != model or state.get("prompt") != prompt_hash:
        state = {"version": 1, "modelo": model, "prompt": prompt_hash, "grupos": {}}
    pending = [key for key in grouped if state["grupos"].get(key, {}).get("estado") != "ok"]
    for start in range(0, len(pending), batch_size):
        batch = pending[start:start + batch_size]
        cases = "\n\n".join(_case_text(key, grouped[key]) for key in batch)
        try:
            answer = json.loads(ask(template.replace("{casos}", cases)))["grupos"]
            by_key = {item["clave_grupo"]: item for item in answer if isinstance(item, dict)}
            for key in batch:
                allowed = {row["requisito_id"] for row in grouped[key]}
                selected = []
                for item in by_key.get(key, {}).get("enlaces", []):
                    requirement = str(item.get("requisito_id", ""))
                    kind = item.get("tipo")
                    if requirement in allowed and kind in ("directo", "parcial"):
                        selected.append({"requisito_id": requirement, "tipo": kind,
                                         "motivo": str(item.get("motivo", "")).strip()})
                state["grupos"][key] = {"estado": "ok", "enlaces": selected[:2]}
        except Exception as exc:  # noqa: BLE001 — el servicio local puede fallar por lote; reintentable
            for key in batch:
                state["grupos"][key] = {"estado": "error", "detalle": str(exc)}
        write_json(state_path, state)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["clave_grupo", "grupo", "requisito_id", "tipo_modelo", "motivo_modelo", "modelo"])
        for key, group_rows in grouped.items():
            for link in state["grupos"].get(key, {}).get("enlaces", []):
                writer.writerow([key, group_rows[0]["grupo"], link["requisito_id"], link["tipo"],
                                 link["motivo"], model])
    ok = sum(item.get("estado") == "ok" for item in state["grupos"].values())
    errors = sum(item.get("estado") == "error" for item in state["grupos"].values())
    selected = sum(len(item.get("enlaces", [])) for item in state["grupos"].values())
    return {"grupos": len(grouped), "revisados": ok, "errores": errors,
            "enlaces_sugeridos": selected, "salida": str(output_path)}


def read_link_decisions(path: Path, catalog: list[dict]) -> tuple[dict[str, list[dict]], set[str]]:
    """Enlaces confirmados por clave estable de grupo y conjunto de grupos ya revisados."""
    by_id = {item["id"]: item for item in catalog}
    confirmed: dict[str, list[dict]] = defaultdict(list)
    reviewed = set()
    seen = set()
    with path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            decision = row.get("decision", "").strip()
            kind = row.get("tipo", "").strip()
            key = row["clave_grupo"]
            pair = (key, row["requisito_id"])
            if decision not in ("si", "no"):
                raise ValueError(f"Decisión normativa inválida: {row}")
            if pair in seen:
                raise ValueError(f"Enlace normativo repetido: {pair}")
            if row["requisito_id"] not in by_id:
                raise ValueError(f"Requisito normativo inexistente: {row['requisito_id']}")
            if decision == "si" and kind not in ("directo", "parcial"):
                raise ValueError(f"Tipo de enlace normativo inválido: {row}")
            seen.add(pair)
            reviewed.add(key)
            if decision == "si":
                confirmed[key].append({**by_id[row["requisito_id"]], "tipo": kind, "nota": row["nota"]})
    return dict(confirmed), reviewed


def read_group_registry(path: Path) -> dict[str, set[str]]:
    """Miembros de cada clave de grupo revisada (`config/grupos-registro.csv`)."""
    registry: dict[str, set[str]] = defaultdict(set)
    if path.exists():
        with path.open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream):
                registry[row["clave_grupo"]].add(row["clave_miembro"])
    return dict(registry)


def register_groups(grupos_path: Path, registry_path: Path) -> dict:
    """Añade al registro las claves de los grupos actuales que aún no figuran; nunca borra."""
    registry = read_group_registry(registry_path)
    groups = json.loads(grupos_path.read_text(encoding="utf-8"))["grupos"]
    new = [g for g in groups if group_key(g) not in registry]
    write_header = not registry_path.exists()
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    with registry_path.open("a", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        if write_header:
            writer.writerow(["clave_grupo", "clave_miembro"])
        for g in new:
            key = group_key(g)
            writer.writerows([key, member] for member in sorted(m["clave"] for m in g["miembros"]))
    return {"grupos": len(groups), "registrados": len(new)}


def current_keys(groups: list[dict], registry: dict[str, set[str]]) -> dict[str, str]:
    """Traslada cada clave registrada al grupo actual que contiene la mayoría de sus miembros.

    Tras reconsolidar con más documentos, un grupo revisado suele ganar miembros y cambiar de
    clave; sus decisiones siguen aplicando. Si ningún grupo actual reúne más de la mitad de los
    miembros (el grupo se dividió), la clave no se traslada y el grupo vuelve a quedar pendiente.
    """
    owner = {m["clave"]: group_key(g) for g in groups for m in g["miembros"]}
    mapping = {group_key(g): group_key(g) for g in groups}
    for old, members in registry.items():
        if old in mapping:
            continue
        counts: dict[str, int] = defaultdict(int)
        for member in members:
            if member in owner:
                counts[owner[member]] += 1
        if counts:
            best = max(counts, key=lambda k: (counts[k], k))
            if counts[best] * 2 > len(members):
                mapping[old] = best
    return mapping


def remap_decisions(links: dict[str, list[dict]], reviewed: set[str],
                    mapping: dict[str, str]) -> tuple[dict[str, list[dict]], set[str]]:
    """Expresa enlaces y revisiones con las claves de los grupos actuales."""
    moved: dict[str, list[dict]] = defaultdict(list)
    for key, items in links.items():
        if key in mapping:
            target = moved[mapping[key]]
            target += [item for item in items if item["id"] not in {t["id"] for t in target}]
    return dict(moved), {mapping[key] for key in reviewed if key in mapping}
