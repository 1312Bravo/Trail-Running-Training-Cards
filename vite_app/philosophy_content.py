from __future__ import annotations

from pathlib import Path


APP_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = APP_ROOT.parent
APP_PHILOSOPHIES_DIR = APP_ROOT / "content" / "philosophies"
COACHING_DIR = PROJECT_ROOT / "coaching"

REVIEWED_SOURCE_SECTIONS = {
    "80_20_endurance": {"## Reviewed Official 80/20 Material"},
    "cts": {"## Official CTS Material"},
    "evoke_endurance": {"## Reviewed Official Evoke Material"},
    "lydiard": {"## Reviewed Official Lydiard Foundation Material"},
    "mainstream_endurance": {
        "## Primary Textbooks And Academic Material",
        "## Coaching Education And Consensus Material",
        "## Research Reviews And Position Stands",
    },
    "sharman_ultra": {"## Reviewed Official Sharman Ultra Material"},
    "swap": {"## Reviewed Official SWAP Material"},
}
EXCLUDED_SOURCE_SECTIONS = {
    "80_20_endurance": {
        "## Scope",
        "## Primary Books To Review",
        "## Interpretation Boundaries",
    },
    "cts": {"## Scope", "## Primary Book", "## Interpretation Notes"},
    "evoke_endurance": {
        "## Scope",
        "## Primary Books To Review",
        "## Interpretation Boundaries",
    },
    "lydiard": {
        "## Scope",
        "## Primary Sources To Review",
        "## Interpretation Boundaries",
    },
    "mainstream_endurance": {
        "## Scope",
        "## Sources To Add",
        "## Interpretation Notes",
    },
    "sharman_ultra": {
        "## Scope",
        "## Direct Sources To Review",
        "## Interpretation Boundaries",
    },
    "swap": {
        "## Scope",
        "## Direct Sources To Review",
        "## Interpretation Boundaries",
    },
}


def app_summary_path(profile_id: str) -> Path:
    return APP_PHILOSOPHIES_DIR / f"{profile_id}.md"


def detailed_note_path(profile_id: str) -> Path:
    return COACHING_DIR / "philosophies" / profile_id / "philosophy.md"


def sources_note_path(profile_id: str) -> Path | None:
    path = COACHING_DIR / "philosophies" / profile_id / "sources.md"
    return path if path.exists() else None


def load_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_app_summary(profile_id: str) -> str:
    path = app_summary_path(profile_id)
    if not path.exists():
        return (
            f"No app summary has been written yet for `{profile_id}`. "
            "Use the detailed coaching philosophy note until a short app-facing summary is added."
        )
    return load_markdown(path)


def load_detailed_note(profile_id: str) -> str:
    return load_markdown(detailed_note_path(profile_id))


def validate_source_sections(profile_id: str, source_note: str) -> None:
    """Ensure each top-level source section has an explicit app role."""
    reviewed = REVIEWED_SOURCE_SECTIONS.get(profile_id)
    excluded = EXCLUDED_SOURCE_SECTIONS.get(profile_id)
    if reviewed is None or excluded is None:
        raise ValueError(f"No source-section classification is configured for {profile_id}.")

    actual = {line for line in source_note.splitlines() if line.startswith("## ")}
    configured = reviewed | excluded
    unclassified = actual - configured
    missing = configured - actual
    if unclassified or missing:
        details = []
        if unclassified:
            details.append(f"unclassified: {sorted(unclassified)}")
        if missing:
            details.append(f"missing: {sorted(missing)}")
        raise ValueError(
            f"Source-section classification is out of date for {profile_id}: "
            + "; ".join(details)
        )


def extract_reviewed_source_bullets(profile_id: str, source_note: str) -> str:
    """Return the selected source bullets shown by the card app."""
    reviewed = REVIEWED_SOURCE_SECTIONS[profile_id]
    bullets: list[str] = []
    in_section = False
    for line in source_note.splitlines():
        if line.startswith("## "):
            in_section = line in reviewed
        elif in_section and line.startswith("- "):
            bullets.append(line)
    return "\n".join(bullets)


def load_reviewed_source_bullets(profile_id: str) -> str:
    path = sources_note_path(profile_id)
    if path is None:
        return ""
    source_note = load_markdown(path)
    validate_source_sections(profile_id, source_note)
    return extract_reviewed_source_bullets(profile_id, source_note)
