from __future__ import annotations

from pathlib import Path

import streamlit as st

from streamlit_app.philosophy_content import (
    app_summary_path,
    detailed_note_path,
    extract_reviewed_source_bullets,
    load_app_summary as read_app_summary,
    load_markdown as read_markdown,
    sources_note_path,
    validate_source_sections,
)


@st.cache_data(show_spinner=False)
def load_markdown(path: str) -> str:
    return read_markdown(Path(path))


def load_app_summary(profile_id: str) -> str:
    summary_path = app_summary_path(profile_id)
    if not summary_path.exists():
        return read_app_summary(profile_id)
    return load_markdown(str(summary_path))


def load_detailed_note(profile_id: str) -> str:
    return load_markdown(str(detailed_note_path(profile_id)))


def load_reviewed_source_bullets(profile_id: str) -> str:
    source_path = sources_note_path(profile_id)
    if source_path is None:
        return ""
    source_note = load_markdown(str(source_path))
    validate_source_sections(profile_id, source_note)
    return extract_reviewed_source_bullets(profile_id, source_note)
