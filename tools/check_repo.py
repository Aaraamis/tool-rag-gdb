"""Comprueba la política mínima de versión del repositorio."""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\Z")


def check(root: Path = ROOT) -> list[str]:
    errors = []
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(version):
        errors.append(f"VERSION debe ser SemVer MAJOR.MINOR.PATCH: {version!r}")
    project = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
    if project["project"]["version"] != version:
        errors.append("pyproject.toml [project].version no coincide con VERSION")
    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    if len(re.findall(r"^## \[Unreleased\]$", changelog, re.MULTILINE)) != 1:
        errors.append("CHANGELOG.md debe tener exactamente un encabezado ## [Unreleased]")
    headings = re.findall(r"^## \[([^]]+)\]", changelog, re.MULTILINE)
    if len(headings) != len(set(headings)):
        errors.append("CHANGELOG.md tiene secciones de versión duplicadas")
    return errors


def main() -> int:
    errors = check()
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("OK: versión y changelog coherentes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
