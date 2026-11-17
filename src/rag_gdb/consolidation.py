"""Consolidación (RF8): agrupa observaciones repetidas y cuenta su frecuencia por radicado IDU."""

from __future__ import annotations

import csv
import hashlib
import json
import urllib.request
from collections.abc import Callable
from pathlib import Path

import numpy as np

from .extraction import _norm
from .inventory import write_json

AUTO = 0.85     # desde aquí dos observaciones se tratan como el mismo requisito
FLOOR = 0.78    # ningún par dentro de un grupo puede quedar por debajo; los pares entre FLOOR y AUTO se revisan


def load_observations(extract_dir: Path) -> list[dict]:
    rows = []
    for path in sorted(extract_dir.rglob("*.json")):
        if path.name == "estado.json":
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        document = data["documento"]
        for obs in data["observaciones"]:
            key = hashlib.sha1(f"{document['sha256']}|{_norm(obs['cita'])}".encode()).hexdigest()[:16]
            rows.append({**obs, "clave": key, "ruta": document["ruta"]})
    return rows


def _text(obs: dict) -> str:
    return f"{obs['resumen']} || {obs['cita']}"


def ollama_embed(model: str, url: str = "http://localhost:11434") -> Callable[[list[str]], list[list[float]]]:
    def embed(texts: list[str]) -> list[list[float]]:
        request = urllib.request.Request(f"{url}/api/embed", json.dumps({"model": model, "input": texts}).encode(),
                                         {"Content-Type": "application/json"})
        with urllib.request.urlopen(request, timeout=600) as response:
            return json.load(response)["embeddings"]
    return embed


def embed_cached(observations: list[dict], embed: Callable, model: str, cache_path: Path) -> np.ndarray:
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    if cache.get("modelo") != model:
        cache = {"modelo": model, "vectores": {}}
    hashes = [hashlib.sha1(_text(o).encode()).hexdigest() for o in observations]
    missing = sorted({h for h in hashes if h not in cache["vectores"]})
    if missing:
        texts = {h: _text(o) for h, o in zip(hashes, observations)}
        for start in range(0, len(missing), 128):
            batch = missing[start:start + 128]
            for h, vector in zip(batch, embed([texts[h] for h in batch])):
                cache["vectores"][h] = [round(x, 6) for x in vector]
        write_json(cache_path, cache)
    matrix = np.array([cache["vectores"][h] for h in hashes], dtype=float)
    return matrix / np.linalg.norm(matrix, axis=1, keepdims=True)


def read_decisions(path: Path) -> dict[frozenset, str]:
    if not path.exists():
        return {}
    decisions = {}
    with path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            value = row.get("decision", "").strip()
            if value not in ("si", "no"):
                raise ValueError(f"Decisión inválida en {path}: {row}")
            decisions[frozenset((row["clave_a"], row["clave_b"]))] = value
    return decisions


def group(vectors: np.ndarray, keys: list[str], decisions: dict[frozenset, str] | None = None,
          auto: float = AUTO, floor: float = FLOOR) -> tuple[list[list[int]], list[tuple[int, int, float]]]:
    """Grupos de índices y pares por revisar: el mejor par desde `floor` entre cada dos grupos que no se unieron
    (incluye pares sobre `auto` que el piso bloqueó)."""
    decisions = decisions or {}
    sims = vectors @ vectors.T
    n = len(keys)
    members = {i: [i] for i in range(n)}
    owner = list(range(n))
    i_idx, j_idx = np.triu_indices(n, 1)
    index = {key: k for k, key in enumerate(keys)}
    candidates = [(float(sims[i, j]), int(i), int(j)) for i, j in zip(i_idx, j_idx) if sims[i, j] >= auto]
    for pair, value in decisions.items():  # «si» une aunque no alcance el umbral ni el piso
        if value == "si" and len(pair) == 2 and all(key in index for key in pair):
            a, b = sorted(pair)
            candidates.append((2.0, index[a], index[b]))
    for sim, i, j in sorted(candidates, reverse=True):
        if decisions.get(frozenset((keys[i], keys[j]))) == "no":
            continue
        a, b = owner[i], owner[j]
        if a == b:
            continue
        if sim <= 1.0 and sims[np.ix_(members[a], members[b])].min() < floor:
            continue
        for k in members[b]:
            owner[k] = a
        members[a] += members.pop(b)
    groups = sorted(members.values(), key=len, reverse=True)
    closed = set()  # un «no» entre dos miembros cierra la revisión entre sus grupos
    for pair, value in decisions.items():
        if value == "no" and len(pair) == 2 and all(key in index for key in pair):
            a, b = (owner[index[key]] for key in pair)
            closed.add((min(a, b), max(a, b)))
    best: dict[tuple[int, int], tuple[int, int, float]] = {}
    for i, j in zip(i_idx, j_idx):
        sim = float(sims[i, j])
        a, b = owner[i], owner[j]
        if a == b or sim < floor or (min(a, b), max(a, b)) in closed:
            continue
        pair = (min(a, b), max(a, b))
        if pair not in best or best[pair][2] < sim:
            best[pair] = (int(i), int(j), sim)
    return groups, sorted(best.values(), key=lambda p: -p[2])


def read_themes(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def read_overrides(path: Path, themes: list[dict]) -> dict[str, str]:
    """Tema fijado a mano para el grupo que contenga la observación `clave`."""
    if not path.exists():
        return {}
    valid = {t["tema"] for t in themes}
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    for row in rows:
        if row["tema"] not in valid:
            raise ValueError(f"Tema inexistente en {path}: {row}")
    return {row["clave"]: row["tema"] for row in rows}


def summarize(observations: list[dict], vectors: np.ndarray, groups: list[list[int]],
              themes: list[dict] | None = None, theme_vectors: np.ndarray | None = None,
              overrides: dict[str, str] | None = None) -> list[dict]:
    result = []
    for members in groups:
        obs = [observations[k] for k in members]
        sub = vectors[members] @ vectors[members].T
        central = sorted(range(len(members)), key=lambda k: (obs[k]["autor"] != "idu", -sub[k].mean()))
        idu = {o["radicado_origen"] or o["ruta"] for o in obs if o["autor"] == "idu"}
        theme = {}
        if themes and theme_vectors is not None:
            centroid = vectors[members].mean(axis=0)
            scores = theme_vectors @ (centroid / np.linalg.norm(centroid))
            ranked = np.argsort(-scores)
            fixed = next((overrides[o["clave"]] for o in obs if o["clave"] in (overrides or {})), None)
            theme = {"tema": fixed or themes[ranked[0]]["tema"], "tema_manual": fixed is not None,
                     "tema_similitud": round(float(scores[ranked[0]]), 3),
                     "tema_alternativo": themes[ranked[1]]["tema"]}
        result.append({
            **theme,
            "representante": obs[central[0]]["resumen"],
            "frecuencia_idu": len(idu),
            "radicados_idu": sorted(idu),
            "documentos": len({o["ruta"] for o in obs}),
            "documentos_interventoria": len({o["ruta"] for o in obs if o["autor"] == "interventoria"}),
            "miembros": [{k: o[k] for k in ("clave", "ruta", "id", "autor", "radicado_origen", "pagina",
                                           "cita", "resumen", "estado_en_documento")}
                         for o in (obs[k] for k in central)],
        })
    result.sort(key=lambda g: (-g["frecuencia_idu"], -g["documentos"], g["representante"]))
    for number, entry in enumerate(result, 1):
        entry["grupo"] = f"G{number:03d}"
    return result


def consolidate(extract_dir: Path, output_dir: Path, decisions_path: Path, embed: Callable, model: str,
                auto: float = AUTO, floor: float = FLOOR, themes_path: Path | None = None,
                overrides_path: Path | None = None) -> dict:
    observations = load_observations(extract_dir)
    vectors = embed_cached(observations, embed, model, output_dir / "embeddings.json")
    keys = [o["clave"] for o in observations]
    groups, review = group(vectors, keys, read_decisions(decisions_path), auto, floor)
    themes = read_themes(themes_path) if themes_path else []
    theme_vectors = None
    if themes:
        raw = np.array(embed([f"{t['nombre']}: {t['descripcion']}" for t in themes]), dtype=float)
        theme_vectors = raw / np.linalg.norm(raw, axis=1, keepdims=True)
    overrides = read_overrides(overrides_path, themes) if overrides_path and themes else {}
    summary = summarize(observations, vectors, groups, themes, theme_vectors, overrides)
    write_json(output_dir / "grupos.json", {"version": 1, "modelo": model, "umbral": auto, "piso": floor,
                                             "temas": themes, "grupos": summary})
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "pares-revisar.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["clave_a", "clave_b", "similitud", "resumen_a", "resumen_b", "decision"])
        for i, j, sim in review:
            writer.writerow([keys[i], keys[j], f"{sim:.3f}", observations[i]["resumen"],
                             observations[j]["resumen"], ""])
    return {"observaciones": len(observations), "grupos": len(summary),
            "grupos_repetidos": sum(len(g["miembros"]) > 1 for g in summary), "pares_por_revisar": len(review)}
