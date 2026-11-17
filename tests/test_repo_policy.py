from pathlib import Path

from tools.check_repo import check


def test_version_mismatch_and_duplicate_unreleased_are_reported(tmp_path: Path):
    (tmp_path / "VERSION").write_text("0.2.0\n")
    (tmp_path / "pyproject.toml").write_text('[project]\nversion = "0.1.0"\n')
    (tmp_path / "CHANGELOG.md").write_text("## [Unreleased]\n## [Unreleased]\n")

    errors = check(tmp_path)

    assert any("no coincide" in error for error in errors)
    assert any("exactamente un" in error for error in errors)


def test_repo_policy_accepts_current_state():
    assert check(Path(__file__).resolve().parents[1]) == []
