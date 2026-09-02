from __future__ import annotations

from pathlib import Path

import streamlit as st


# App summaries are deliberately separate from the detailed coaching notes. The
# app can present both without making the source documentation its default view.
APP_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = APP_ROOT.parent
APP_PHILOSOPHIES_DIR = APP_ROOT / "content" / "philosophies"
COACHING_DIR = PROJECT_ROOT / "coaching"


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
    return load_markdown(str(app_summary_path(profile_id)))


def load_detailed_note(profile_id: str) -> str:
    return load_markdown(str(detailed_note_path(profile_id)))


def extract_reviewed_source_bullets(source_note: str) -> str:
    """Return only the reviewed-official-material bullets from a source note."""
    reviewed_bullets: list[str] = []
    in_reviewed_section = False

    for line in source_note.splitlines():
        if line.startswith("## "):
            in_reviewed_section = (
                "Reviewed Official" in line or line == "## Official CTS Material"
            )
            continue
        if in_reviewed_section and line.startswith("- "):
            reviewed_bullets.append(line)

    return "\n".join(reviewed_bullets)


def load_reviewed_source_bullets(profile_id: str) -> str:
    source_path = sources_note_path(profile_id)
    if source_path is None:
        return ""
    return extract_reviewed_source_bullets(load_markdown(str(source_path)))
