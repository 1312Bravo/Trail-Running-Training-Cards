from __future__ import annotations

from pathlib import Path

import streamlit as st


# App summaries are deliberately separate from the detailed coaching notes. The
# app can present both without making the source documentation its default view.
APP_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = APP_ROOT.parent
APP_PHILOSOPHIES_DIR = APP_ROOT / "content" / "philosophies"
COACHING_DIR = PROJECT_ROOT / "coaching"

# Source records remain human-authored Markdown. This classification makes the
# compact app dialog show only reviewed source sections and flags future
# heading changes instead of silently omitting them.
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
    "cts": {
        "## Scope",
        "## Primary Book",
        "## Interpretation Notes",
    },
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
    return COACHING_DIR / "philosophies" / profile_id / "sources.md"


@st.cache_data(show_spinner=False)
def load_markdown(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def load_app_summary(profile_id: str) -> str:
    summary_path = app_summary_path(profile_id)
    if not summary_path.exists():
        return (
            f"No app summary has been written yet for `{profile_id}`. "
            "Use the detailed coaching philosophy note until a short app-facing summary is added."
        )
    return load_markdown(str(summary_path))


def load_detailed_note(profile_id: str) -> str:
    return load_markdown(str(detailed_note_path(profile_id)))


def validate_source_sections(profile_id: str, source_note: str) -> None:
    """Ensure every top-level source-record section has an explicit app role."""
    reviewed_sections = REVIEWED_SOURCE_SECTIONS.get(profile_id)
    excluded_sections = EXCLUDED_SOURCE_SECTIONS.get(profile_id)
    if reviewed_sections is None or excluded_sections is None:
        raise ValueError(f"No source-section classification is configured for {profile_id}.")

    actual_sections = {
        line
        for line in source_note.splitlines()
        if line.startswith("## ")
    }
    configured_sections = reviewed_sections | excluded_sections
    unclassified_sections = actual_sections - configured_sections
    missing_sections = configured_sections - actual_sections
    if unclassified_sections or missing_sections:
        details = []
        if unclassified_sections:
            details.append(f"unclassified: {sorted(unclassified_sections)}")
        if missing_sections:
            details.append(f"missing: {sorted(missing_sections)}")
        raise ValueError(
            f"Source-section classification is out of date for {profile_id}: "
            + "; ".join(details)
        )


def extract_reviewed_source_bullets(profile_id: str, source_note: str) -> str:
    """Return source bullets from the reviewed sections for one philosophy."""
    reviewed_bullets: list[str] = []
    in_reviewed_section = False
    reviewed_sections = REVIEWED_SOURCE_SECTIONS[profile_id]

    for line in source_note.splitlines():
        if line.startswith("## "):
            in_reviewed_section = line in reviewed_sections
            continue
        if in_reviewed_section and line.startswith("- "):
            reviewed_bullets.append(line)

    return "\n".join(reviewed_bullets)


def load_reviewed_source_bullets(profile_id: str) -> str:
    source_path = sources_note_path(profile_id)
    if source_path is None:
        return ""
    source_note = load_markdown(str(source_path))
    validate_source_sections(profile_id, source_note)
    return extract_reviewed_source_bullets(profile_id, source_note)
