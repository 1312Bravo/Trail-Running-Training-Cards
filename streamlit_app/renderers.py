from __future__ import annotations

from base64 import b64encode
from dataclasses import asdict, fields as dataclass_fields, is_dataclass
from functools import lru_cache
from html import escape
from pathlib import Path
from typing import Any

import streamlit as st

from training_cards.philosophy_profiles import philosophy_profile_display_name
from streamlit_app.artwork import artwork_for_card
from streamlit_app.config import DETAIL_FIELD_LABEL_OVERRIDES, DETAIL_SECTION_ORDER
from streamlit_app.data import card_type_label


MAIL_ICON_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path fill="currentColor" d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm-.4 4.25-7.07 4.42a1 1 0 0 1-1.06 0L4.4 8.25 5.46 6.55 12 10.64l6.54-4.09 1.06 1.7Z"/>
</svg>
"""

DETAIL_HIDDEN_FIELDS = {"id", "slug", "title", "card_type"}

GITHUB_ICON_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path fill="currentColor" d="M12 .5A12 12 0 0 0 8.2 23.9c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.5-1.3-1.3-1.7-1.3-1.7-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.6.1-3.2 0 0 1-.3 3.3 1.2a11.3 11.3 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.6.2 2.9.1 3.2.8.9 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.1c0 .3.2.7.8.6A12 12 0 0 0 12 .5Z"/>
</svg>
"""

CARD_TYPE_ICONS = {
    "macro": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="m3 18 6-9 4 6 2-3 6 6" />
            <path d="M3 20h18" />
        </svg>
    """,
    "mezzo": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M3 17c3-5 6-5 9 0 3-4 5-4 9 0" />
            <path d="M3 20h18" />
        </svg>
    """,
    "micro": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M5 19c5 0 1-8 7-8s2-6 7-6" />
            <circle cx="5" cy="19" r="1.4" />
            <circle cx="19" cy="5" r="1.4" />
        </svg>
    """,
    "session": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <circle cx="12" cy="13" r="7" />
            <path d="M12 3v3M9 3h6M12 13l3-2" />
        </svg>
    """,
}

CARD_TYPE_ICON_COLORS = {
    "macro": "#526d80",
    "mezzo": "#765d8c",
    "micro": "#a06a2c",
    "session": "#d7b829",
}

# ----------------------------------------------------------
# Page Styling
# ----------------------------------------------------------
# Keep this function in place for the app shell, but intentionally avoid custom
# styling while we rebuild the UI from a stable native Streamlit baseline.

def css() -> None:
    st.html(
        """
        <style>
        :root {
            --paper: #ffffff;
            --surface: #ffffff;
            --ink: #252525;
            --muted-ink: #737373;
            --line: #d6d6d6;
            --strong-line: #4d4d4d;
            --soft-surface: #f7f7f7;
        }
        [data-testid="stAppViewContainer"],
        .stApp {
            background: var(--paper);
            color: var(--ink);
        }
        [data-testid="stHeader"] {
            background: transparent;
        }
        [data-testid="stMainBlockContainer"],
        .block-container {
            max-width: 92rem;
            padding-top: 2.75rem;
            padding-bottom: 4rem;
        }
        h1 {
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: clamp(2.25rem, 4vw, 3.35rem);
            font-weight: 600;
            letter-spacing: -0.045em;
            line-height: 1.02;
        }
        [data-testid="stCaptionContainer"] {
            color: var(--muted-ink);
        }
        [data-testid="stButton"] > button {
            min-height: 2rem;
            border: 1px solid #bfc0b8;
            background: var(--surface);
            color: var(--ink);
            box-shadow: none;
            transition: background 160ms ease, border-color 160ms ease;
        }
        [data-testid="stButton"] > button:hover {
            border-color: var(--strong-line);
            background: var(--soft-surface);
            color: var(--ink);
        }
        [data-testid="stTextInput"] input,
        [data-testid="stMultiSelect"] div[data-baseweb="select"] > div {
            background: var(--surface);
        }
        [data-testid="stSegmentedControl"] {
            background: var(--surface);
        }
        [class*="st-key-browse-toolbar"] [data-testid="stTextInput"] input,
        [class*="st-key-browse-toolbar"] [data-testid="stMultiSelect"] div[data-baseweb="select"] > div,
        [class*="st-key-mode-toolbar-"] [data-testid="stTextInput"] input,
        [class*="st-key-mode-toolbar-"] [data-testid="stMultiSelect"] div[data-baseweb="select"] > div {
            background: var(--soft-surface);
        }
        [data-testid="stDivider"] {
            border-color: var(--line);
        }
        .contact-links {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-end;
            gap: 0.4rem;
            margin-top: 0;
        }
        .contact-links a {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            color: var(--ink);
            text-decoration: none;
            font-size: 0.98rem;
        }
        .contact-icon {
            width: 1.12rem;
            height: 1.12rem;
            display: inline-block;
        }
        .contact-links a:hover {
            text-decoration: underline;
            text-underline-offset: 0.18rem;
        }
        [class*="st-key-philosophy-"] h1 {
            margin: 0 0 0.8rem;
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.35rem;
            font-weight: 600;
            letter-spacing: -0.02em;
        }
        [class*="st-key-philosophy-"] h2 {
            margin: 1rem 0 0.45rem;
            font-size: 1rem;
        }
        [class*="st-key-philosophy-"] p,
        [class*="st-key-philosophy-"] li {
            color: #555555;
        }
        [class*="st-key-tag_"],
        [class*="st-key-selected_tag_"],
        [class*="st-key-pathway_search_terms_"],
        [class*="st-key-today_search_terms_"] {
            margin: 0 !important;
        }
        [class*="st-key-tag_"] button,
        [class*="st-key-selected_tag_"] button,
        [class*="st-key-pathway_search_terms_"] button,
        [class*="st-key-today_search_terms_"] button {
            min-height: 1.65rem;
            padding: 0.12rem 0.52rem;
            background: linear-gradient(180deg, rgb(255 255 255 / 78%), rgb(255 255 255 / 44%));
            border: 1px solid rgb(37 37 37 / 42%);
            border-radius: 6px;
            color: var(--ink);
            box-shadow: inset 0 1px 0 rgb(255 255 255 / 78%), 0 1px 1px rgb(40 41 35 / 8%);
            font-size: 0.86rem;
            font-weight: 400;
        }
        [class*="st-key-selected_tag_"] button {
            background: linear-gradient(180deg, rgb(255 255 255 / 92%), rgb(255 255 255 / 58%));
            border-color: #6f716b;
            font-weight: 600;
        }
        [class*="st-key-tag_"] button:hover,
        [class*="st-key-selected_tag_"] button:hover,
        [class*="st-key-pathway_search_terms_"] button:hover,
        [class*="st-key-today_search_terms_"] button:hover,
        [class*="st-key-open_"] button:hover,
        [class*="st-key-select_"] button:hover {
            background: linear-gradient(180deg, rgb(255 255 255 / 96%), rgb(255 255 255 / 64%));
            border-color: #6f716b;
            color: var(--ink);
        }
        [class*="st-key-open-action"] {
            position: sticky;
            top: 0;
            z-index: 2;
            background: transparent;
            padding-bottom: 0.25rem;
        }
        [class*="st-key-open_"] button,
        [class*="st-key-select_"] button {
            border: 1px solid #6f716b;
            border-radius: 6px;
            background: linear-gradient(180deg, rgb(255 255 255 / 84%), rgb(255 255 255 / 52%));
            color: var(--ink);
            font-weight: 400;
            min-height: 1.8rem;
            padding: 0.12rem 0.55rem;
            font-size: 0.8rem;
            box-shadow: inset 0 1px 0 rgb(255 255 255 / 82%), 0 1px 1px rgb(40 41 35 / 10%);
        }
        [class*="st-key-pathway_open_"] button,
        [class*="st-key-pathway_change_"] button {
            border: 1px solid var(--line);
            background: var(--surface);
            color: var(--ink);
            font-weight: 400;
            min-height: 1.55rem;
            padding: 0.05rem 0.4rem;
            font-size: 0.78rem;
            box-shadow: none;
        }
        [class*="st-key-pathway-selection"] {
            position: sticky;
            top: 0;
            z-index: 4;
            background: var(--paper);
            padding-bottom: 0.4rem;
        }
        .preview-card-title {
            margin: 0.25rem 0 0.4rem;
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.45rem;
            font-weight: 500;
            letter-spacing: 0;
            line-height: 1.12;
        }
        [class*="st-key-prototype-art-"] img {
            border: 1px solid #526d80;
            border-radius: 8px;
            object-fit: cover;
        }
        .preview-card-identity {
            display: flex;
            align-items: center;
            gap: 0.28rem;
            min-height: 1.9rem;
        }
        .preview-card-type {
            display: inline-flex;
            align-items: center;
            padding: 0;
            border: 0;
            border-radius: 0;
            background: transparent !important;
            color: var(--muted-ink);
            font-size: 0.78rem;
            font-weight: 400;
            letter-spacing: 0.045em;
            line-height: 1.1;
            text-transform: uppercase;
        }
        [class*="st-key-preview-art-"] {
            position: relative;
            overflow: hidden;
            margin: 0.35rem 0 0.95rem;
            padding: 1.05rem;
            border: 2px solid rgb(37 37 37 / 34%);
            border-radius: 8px;
            box-shadow:
                inset 0 0 26px rgb(255 255 255 / 66%),
                inset 0 0 68px rgb(255 255 255 / 42%),
                0 1px 0 rgb(255 255 255 / 42%);
        }
        [class*="st-key-preview-art-"] img {
            position: relative;
            z-index: 1;
            object-fit: contain;
        }
        [class*="st-key-preview-art-macro"] {
            background:
                radial-gradient(circle at 50% 42%, rgb(255 255 255 / 72%) 0, rgb(255 255 255 / 38%) 28%, transparent 56%),
                linear-gradient(135deg, #e6f3fa 0, #d4e7f0 48%, #bdd3e1 100%) !important;
        }
        [class*="st-key-preview-art-mezzo"] {
            background:
                radial-gradient(circle at 50% 42%, rgb(255 255 255 / 72%) 0, rgb(255 255 255 / 38%) 28%, transparent 56%),
                linear-gradient(135deg, #f2e7f8 0, #e2d2ee 48%, #cdb8df 100%) !important;
        }
        [class*="st-key-preview-art-micro"] {
            background:
                radial-gradient(circle at 50% 42%, rgb(255 255 255 / 72%) 0, rgb(255 255 255 / 38%) 28%, transparent 56%),
                linear-gradient(135deg, #f5d8aa 0, #dfa963 48%, #bd7831 100%) !important;
        }
        [class*="st-key-preview-art-session"] {
            background:
                radial-gradient(circle at 50% 42%, rgb(255 255 255 / 72%) 0, rgb(255 255 255 / 38%) 28%, transparent 56%),
                linear-gradient(135deg, #fff9bf 0, #f2dd5d 48%, #d7b829 100%) !important;
        }
        .preview-card-art-image {
            display: block;
            width: 210px;
            max-width: 100%;
            height: auto;
            margin: 0 auto;
        }
        .preview-card-type-macro {
            color: var(--muted-ink);
        }
        .preview-card-type-mezzo {
            color: var(--muted-ink);
        }
        .preview-card-type-micro {
            color: var(--muted-ink);
        }
        .preview-card-type-session {
            color: var(--muted-ink);
        }
        .preview-summary {
            margin: 0.95rem 0 0.75rem;
            padding: 0.75rem 0.85rem;
            border: 1px solid rgb(111 113 107 / 56%);
            border-radius: 6px;
            background: rgb(255 255 255 / 42%);
            color: var(--ink);
            font-size: 1.04rem;
            line-height: 1.42;
        }
        .preview-field {
            display: grid;
            grid-template-columns: minmax(6.7rem, 8.4rem) minmax(0, 1fr);
            align-items: center;
            column-gap: 0.75rem;
            margin: 0;
            padding: 0.58rem 0.45rem;
            border-top: 1px solid rgb(111 113 107 / 24%);
            background: transparent;
            color: var(--ink);
            font-size: 0.88rem;
            line-height: 1.38;
        }
        .preview-field + .preview-field {
            margin-top: 0;
        }
        .preview-field-label {
            color: #666964;
            font-weight: 600;
            font-size: 0.76rem;
            letter-spacing: 0.015em;
            text-transform: none;
        }
        .preview-field-value {
            color: #2f302d;
            font-weight: 400;
        }
        .preview-tag-labels {
            display: flex;
            flex-wrap: wrap;
            gap: 0.55rem 0.9rem;
            margin-top: 0.7rem;
            padding: 0.15rem 0.45rem 0;
        }
        .preview-tag-label {
            color: #373936;
            font-size: 0.86rem;
            line-height: 1.3;
            text-decoration: underline;
            text-decoration-thickness: 1px;
            text-underline-offset: 0.18rem;
        }
        @media (max-width: 640px) {
            .preview-field {
                display: block;
            }
            .preview-field-label {
                display: block;
                margin-bottom: 0.1rem;
            }
        }
        .preview-tags-title {
            margin: 1rem 0 0.25rem;
            color: #222222;
            font-weight: 400;
        }
        [class*="st-key-card-"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--surface);
            border: 2px solid #6f716b !important;
            border-radius: 12px;
            box-shadow: 0 5px 12px rgb(40 41 35 / 8%);
        }
        [class*="st-key-card-macro"],
        [class*="st-key-card-macro"][data-testid="stVerticalBlockBorderWrapper"],
        [class*="st-key-card-macro"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: #f3f9fc !important;
            border-color: #6f716b !important;
            box-shadow: 0 0 0 1px #6f716b, 0 5px 12px rgb(40 41 35 / 10%);
        }
        [class*="st-key-card-mezzo"],
        [class*="st-key-card-mezzo"][data-testid="stVerticalBlockBorderWrapper"],
        [class*="st-key-card-mezzo"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: #faf5fd !important;
            border-color: #6f716b !important;
            box-shadow: 0 0 0 1px #6f716b, 0 5px 12px rgb(40 41 35 / 10%);
        }
        [class*="st-key-card-micro"],
        [class*="st-key-card-micro"][data-testid="stVerticalBlockBorderWrapper"],
        [class*="st-key-card-micro"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: #fff2df !important;
            border-color: #6f716b !important;
            box-shadow: 0 0 0 1px #6f716b, 0 5px 12px rgb(40 41 35 / 10%);
        }
        [class*="st-key-card-session"],
        [class*="st-key-card-session"][data-testid="stVerticalBlockBorderWrapper"],
        [class*="st-key-card-session"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: #fffbe3 !important;
            border-color: #6f716b !important;
            box-shadow: 0 0 0 1px #6f716b, 0 5px 12px rgb(40 41 35 / 10%);
        }
        [class*="st-key-card-macro"] div[data-testid="stVerticalBlock"],
        [class*="st-key-card-mezzo"] div[data-testid="stVerticalBlock"],
        [class*="st-key-card-micro"] div[data-testid="stVerticalBlock"],
        [class*="st-key-card-session"] div[data-testid="stVerticalBlock"],
        [class*="st-key-card-macro"] div[data-testid="stElementContainer"],
        [class*="st-key-card-mezzo"] div[data-testid="stElementContainer"],
        [class*="st-key-card-micro"] div[data-testid="stElementContainer"],
        [class*="st-key-card-session"] div[data-testid="stElementContainer"] {
            background: transparent !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.preview-card-type-macro) {
            background: #f3f9fc !important;
            border-color: #6f716b !important;
            box-shadow: 0 0 0 1px #6f716b, 0 5px 12px rgb(40 41 35 / 10%);
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.preview-card-type-mezzo) {
            background: #faf5fd !important;
            border-color: #6f716b !important;
            box-shadow: 0 0 0 1px #6f716b, 0 5px 12px rgb(40 41 35 / 10%);
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.preview-card-type-micro) {
            background: #fff2df !important;
            border-color: #6f716b !important;
            box-shadow: 0 0 0 1px #6f716b, 0 5px 12px rgb(40 41 35 / 10%);
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.preview-card-type-session) {
            background: #fffbe3 !important;
            border-color: #6f716b !important;
            box-shadow: 0 0 0 1px #6f716b, 0 5px 12px rgb(40 41 35 / 10%);
        }
        .detail-card-header {
            position: relative;
            overflow: hidden;
            margin: 0.25rem 0 1rem;
            padding: 1rem 1.1rem 1.05rem;
            border-top: 6px solid var(--strong-line);
            border-bottom: 1px solid var(--line);
        }
        .detail-card-header-macro { border-top-color: #526d80; }
        .detail-card-header-mezzo { border-top-color: #765d8c; }
        .detail-card-header-micro { border-top-color: #a06a2c; }
        .detail-card-header-session { border-top-color: #d7b829; }
        .detail-card-type {
            display: inline-block;
            margin-bottom: 0.45rem;
            color: var(--muted-ink);
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.055em;
            text-transform: uppercase;
        }
        .detail-card-title {
            position: relative;
            z-index: 1;
            max-width: 82%;
            margin: 0;
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.8rem;
            font-weight: 600;
            letter-spacing: -0.03em;
            line-height: 1.08;
        }
        .detail-card-emblem {
            position: absolute;
            right: 1.1rem;
            bottom: 0.65rem;
            width: 4rem;
            height: 4rem;
            opacity: 0.18;
            transform: rotate(-7deg);
        }
        .detail-section {
            margin: 0;
            padding: 0.1rem 0 0.8rem;
            border-bottom: 1px solid var(--line);
        }
        .detail-section-label {
            margin-bottom: 0.25rem;
            color: var(--muted-ink);
            font-size: 0.78rem;
            font-weight: 600;
            letter-spacing: 0.045em;
            text-transform: uppercase;
        }
        .detail-section-value {
            color: var(--ink);
            font-size: 1rem;
            line-height: 1.45;
        }
        .detail-section-summary .detail-section-value {
            font-size: 1.13rem;
            line-height: 1.5;
        }
        .detail-section-coaching-note {
            padding: 0.9rem 1rem;
            border: 1px solid var(--line);
            border-left: 3px solid var(--strong-line);
            border-radius: 8px;
            background: var(--soft-surface);
        }
        .detail-section-coaching-note .detail-section-label {
            margin-bottom: 0.45rem;
        }
        .detail-section-list {
            margin: 0.2rem 0 0;
            padding-left: 1.2rem;
        }
        .detail-section-list li + li {
            margin-top: 0.25rem;
        }
        .detail-section-tags {
            border-bottom: 0;
            padding-bottom: 0.2rem;
        }
        [class*="st-key-detail-"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border: 0 !important;
            border-top: 1px solid var(--line) !important;
            border-radius: 0 !important;
            background: transparent;
            box-shadow: none;
        }
        [class*="st-key-pathway-card-"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--surface);
            border: 1px solid var(--strong-line) !important;
            border-radius: 8px;
        }
        [class*="st-key-pathway-card-macro"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #526d80 !important;
        }
        [class*="st-key-pathway-card-mezzo"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #765d8c !important;
        }
        [class*="st-key-pathway-card-micro"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #a06a2c !important;
        }
        [class*="st-key-pathway-card-session"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #d7b829 !important;
        }
        </style>
        """
    )


# ----------------------------------------------------------
# Shared Formatting
# ----------------------------------------------------------
# These helpers keep schema values readable without adding visual complexity.

def as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if hasattr(value, "value"):
        return str(value.value)
    return str(value)


def as_list_text(values: list[Any]) -> str:
    return ", ".join(as_text(value) for value in values)


def display_text(value: Any) -> str:
    return as_text(value).replace("_", " ")


def format_field_value(field_name: str, value: Any) -> str:
    text = as_text(value)
    if field_name == "recommended_duration_weeks" and text:
        return f"{text} weeks"
    if field_name == "recommended_duration_days" and text:
        return f"{text} days"
    return text


def field_label(field_name: str, display_config: dict[str, Any]) -> str:
    labels = display_config.get("field_labels", {})
    return labels.get(field_name, field_name.replace("_", " ").title())


def svg_data_uri(svg: str) -> str:
    encoded_svg = b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded_svg}"


@lru_cache(maxsize=128)
def image_file_data_uri(path: Path) -> str:
    suffix = path.suffix.lower()
    mime_type = {
        ".svg": "image/svg+xml",
        ".webp": "image/webp",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
    }.get(suffix)
    if not mime_type:
        return ""

    try:
        encoded_image = b64encode(path.read_bytes()).decode("ascii")
    except OSError:
        return ""
    return f"data:{mime_type};base64,{encoded_image}"


# ----------------------------------------------------------
# Contact Links
# ----------------------------------------------------------

def render_contact_links() -> None:
    mail_icon = svg_data_uri(MAIL_ICON_SVG)
    github_icon = svg_data_uri(GITHUB_ICON_SVG)
    st.html(
        f"""
        <div class="contact-links">
            <a href="mailto:pecek.urh@gmail.com">
                <img class="contact-icon" src="{mail_icon}" alt="">
                <span>pecek.urh@gmail.com</span>
            </a>
            <a href="https://github.com/1312Bravo/Trail-Running-Training-Cards" target="_blank">
                <img class="contact-icon" src="{github_icon}" alt="">
                <span>GitHub</span>
            </a>
        </div>
        """
    )


def set_tag_filter(tag: str) -> None:
    current_tags = list(st.session_state.get("tag_filters", []))
    if tag not in current_tags:
        current_tags.append(tag)
    st.session_state.tag_filters = current_tags


def render_tag_buttons(tags: list[Any], key_prefix: str) -> None:
    if not tags:
        return

    with st.container(horizontal=True):
        for tag in tags:
            tag_text = as_text(tag)
            st.button(
                display_text(tag_text),
                key=f"tag_{key_prefix}_{tag_text}",
                type="secondary",
                width="content",
                on_click=set_tag_filter,
                args=(tag_text,),
            )


# ----------------------------------------------------------
# Preview Cards
# ----------------------------------------------------------

def render_preview_field(card: Any, field_name: str, display_config: dict[str, Any]) -> None:
    value = getattr(card, field_name, None)
    if value is None:
        return
    if isinstance(value, str) and not value.strip():
        return
    if isinstance(value, list) and not value:
        return

    label = DETAIL_FIELD_LABEL_OVERRIDES.get(
        field_name,
        field_label(field_name, display_config),
    )
    if field_name == "summary":
        st.html(f'<p class="preview-summary">{escape(as_text(value))}</p>')
    elif field_name == "tags" and isinstance(value, list):
        render_tag_buttons(value, f"preview_{card.id}")
    elif field_name == "philosophy_profile_ids" and isinstance(value, list):
        rendered_value = ", ".join(
            philosophy_profile_display_name(profile_id)
            for profile_id in value
        )
        st.html(
            '<div class="preview-field">'
            f'<span class="preview-field-label">{escape(label)}:</span> '
            f'<span class="preview-field-value">{escape(rendered_value)}</span>'
            '</div>'
        )
    elif isinstance(value, list):
        rendered_value = ", ".join(display_text(item) for item in value)
        st.html(
            '<div class="preview-field">'
            f'<span class="preview-field-label">{escape(label)}:</span> '
            f'<span class="preview-field-value">{escape(rendered_value)}</span>'
            '</div>'
        )
    else:
        st.html(
            '<div class="preview-field">'
            f'<span class="preview-field-label">{escape(label)}:</span> '
            f'<span class="preview-field-value">{escape(as_text(value))}</span>'
            '</div>'
        )


def render_preview_card(
    card: Any,
    display_config: dict[str, Any],
    key_prefix: str,
    select_label: str | None = None,
    open_label: str = "Open card",
    on_select: Any | None = None,
    select_args: tuple[Any, ...] = (),
) -> None:
    preview_fields = display_config.get("preview_fields", [])
    ordered_preview_fields = [
        field_name
        for field_name in ["summary", "purpose", "suitable_levels", "goal_race_context", "training_profile", "philosophy_profile_ids", "tags"]
        if field_name in preview_fields
    ]
    card_type_key = str(card.card_type).replace("_", "-")

    with st.container(border=True, key=f"card-{card_type_key}-{key_prefix}-{card.id}", height=660):
        artwork = artwork_for_card(card.id)

        st.html(f'<div class="preview-card-title">{escape(card.title)}</div>')

        header_cols = st.columns([1, 0.38], vertical_alignment="top")

        with header_cols[0]:
            card_type = card_type_label(card.card_type, display_config)
            st.html(
                '<div class="preview-card-identity">'
                f'<span class="preview-card-type preview-card-type-{card_type_key}">'
                f'{escape(card_type)}</span>'
                '</div>'
            )
        with header_cols[1]:
            with st.container(
                key=f"open-action-{key_prefix}-{card.id}",
                horizontal=True,
                horizontal_alignment="right",
            ):
                if select_label and on_select:
                    st.button(
                        select_label,
                        key=f"select_{key_prefix}_{card.id}",
                        type="secondary",
                        width="content",
                        on_click=on_select,
                        args=select_args,
                    )
                st.button(
                    open_label,
                    key=f"open_{key_prefix}_{card.id}",
                    type="secondary",
                    width="content",
                    on_click=lambda card_id=card.id: st.session_state.__setitem__("active_card_id", card_id),
                )

        if artwork:
            art_uri = image_file_data_uri(artwork.asset_path)
            with st.container(
                key=f"preview-art-{card_type_key}-{key_prefix}-{card.id}",
                horizontal=True,
                horizontal_alignment="center",
            ):
                if art_uri:
                    st.html(
                        '<img class="preview-card-art-image" '
                        f'src="{art_uri}" '
                        f'alt="{escape(artwork.alt_text, quote=True)}">'
                    )

        for field_name in ordered_preview_fields:
            if field_name == "tags":
                continue
            render_preview_field(card, field_name, display_config)

        if "tags" in ordered_preview_fields and card.tags:
            render_preview_field(card, "tags", display_config)


# ----------------------------------------------------------
# Detail View
# ----------------------------------------------------------

def render_reference_list(card: Any, card_by_id: dict[str, Any]) -> None:
    if not card.references:
        return

    with st.container(border=False, key="detail-references"):
        st.markdown("**References**")
        items = []
        for reference in card.references:
            linked = card_by_id.get(reference.card_id)
            linked_title = linked.title if linked else reference.card_id
            tags = f" ({as_list_text(reference.tags)})" if reference.tags else ""
            items.append(f"- {as_text(reference.relationship)}: {linked_title}{tags}")
        st.markdown("\n".join(items))


def render_workout_parts(parts: list[Any]) -> None:
    if not parts:
        return

    with st.container(border=False, key="detail-workout-parts"):
        st.markdown("**Workout parts**")
        lines = []
        for part in parts:
            lines.append(f"- **{part.name}**")
            lines.append(f"  - Duration: {part.duration}")
            lines.append(f"  - RPE: {part.rpe}")
            if part.instructions:
                lines.append(f"  - {part.instructions}")
            if part.terrain_notes:
                lines.append(f"  - Terrain notes: {part.terrain_notes}")
        st.markdown("\n".join(lines))


def render_dataclass_value(field_name: str, value: Any, display_config: dict[str, Any]) -> bool:
    if field_name != "session_family" or not is_dataclass(value):
        return False

    family = asdict(value)
    with st.container(border=False, key="detail-session-family"):
        st.markdown(f"**{field_label(field_name, display_config)}**")
        st.write(family.get("title", ""))
        if family.get("summary"):
            st.caption(family["summary"])
        if family.get("description"):
            st.write(family["description"])
        if family.get("tags"):
            st.caption(f"Tags: {', '.join(display_text(tag) for tag in family['tags'])}")
    return True


def render_field(field_name: str, value: Any, display_config: dict[str, Any]) -> None:
    if value is None:
        return
    if isinstance(value, str) and not value.strip():
        return
    if isinstance(value, list) and not value:
        return
    if render_dataclass_value(field_name, value, display_config):
        return

    label = field_label(field_name, display_config)
    section_class = "detail-section"
    if field_name == "summary":
        section_class += " detail-section-summary"
    elif field_name == "additional_information":
        section_class += " detail-section-coaching-note"
    elif field_name == "tags":
        section_class += " detail-section-tags"

    if field_name == "tags" and isinstance(value, list):
        st.html(
            f'<section class="{section_class}">'
            f'<div class="detail-section-label">{escape(label)}</div>'
            '</section>'
        )
        render_tag_buttons(value, "detail")
        return

    if field_name == "philosophy_profile_ids" and isinstance(value, list):
        rendered_value = ", ".join(
            philosophy_profile_display_name(profile_id)
            for profile_id in value
        )
        value_html = escape(rendered_value)
    elif isinstance(value, list):
        value_html = (
            '<ul class="detail-section-list">'
            + "".join(f'<li>{escape(as_text(item))}</li>' for item in value)
            + "</ul>"
        )
    else:
        value_html = escape(format_field_value(field_name, value))

    st.html(
        f'<section class="{section_class}">'
        f'<div class="detail-section-label">{escape(label)}</div>'
        f'<div class="detail-section-value">{value_html}</div>'
        '</section>'
    )


def ordered_detail_fields(card: Any) -> list[str]:
    dataclass_field_names = [field.name for field in dataclass_fields(card)]
    ordered = []
    for field_name in DETAIL_SECTION_ORDER + dataclass_field_names:
        if field_name in DETAIL_HIDDEN_FIELDS:
            continue
        if field_name not in ordered and hasattr(card, field_name):
            ordered.append(field_name)
    return ordered


def render_detail_header(card: Any, display_config: dict[str, Any]) -> None:
    card_type_key = str(card.card_type).replace("_", "-")
    card_type = card_type_label(card.card_type, display_config)
    icon_svg = CARD_TYPE_ICONS.get(card_type_key, "")
    icon_color = CARD_TYPE_ICON_COLORS.get(card_type_key, "#4d4d4d")
    emblem = ""
    if icon_svg:
        icon_uri = svg_data_uri(icon_svg.replace("currentColor", icon_color))
        emblem = f'<img class="detail-card-emblem" src="{icon_uri}" alt="">'

    st.html(
        f'<section class="detail-card-header detail-card-header-{card_type_key}">'
        f'<div class="detail-card-type">{escape(card_type)}</div>'
        f'<h2 class="detail-card-title">{escape(card.title)}</h2>'
        f'{emblem}'
        '</section>'
    )


def render_detail(
    card: Any,
    display_config: dict[str, Any],
    card_by_id: dict[str, Any],
    show_header: bool = True,
) -> None:
    if show_header:
        render_detail_header(card, display_config)

    for field_name in ordered_detail_fields(card):
        value = getattr(card, field_name, None)
        if value is None or (isinstance(value, str) and not value.strip()):
            continue
        if isinstance(value, list) and not value:
            continue
        if field_name == "workout_parts":
            render_workout_parts(value)
        elif field_name == "references":
            render_reference_list(card, card_by_id)
        else:
            render_field(field_name, value, display_config)


# ----------------------------------------------------------
# Grid Layout
# ----------------------------------------------------------

def render_grid(
    cards: list[Any],
    display_config: dict[str, Any],
    key_prefix: str,
    select_label: str | None = None,
    open_label: str = "Open card",
    on_select: Any | None = None,
    select_level: str | None = None,
) -> None:
    cards_per_row = 2
    for row_start in range(0, len(cards), cards_per_row):
        cols = st.columns([0.18, 1, 0.28, 1, 0.18], gap="small")
        row_cards = cards[row_start: row_start + cards_per_row]
        for offset, card in enumerate(row_cards):
            index = row_start + offset
            with cols[1 + offset * 2]:
                select_args = (select_level, card.id) if select_level else ()
                render_preview_card(
                    card,
                    display_config,
                    f"{key_prefix}_{index}",
                    select_label=select_label,
                    open_label=open_label,
                    on_select=on_select,
                    select_args=select_args,
                )
