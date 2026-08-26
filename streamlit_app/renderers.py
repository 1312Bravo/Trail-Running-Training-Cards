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
DETAIL_KEY_FACT_FIELDS = {
    "suitable_levels",
    "recommended_duration_weeks",
    "recommended_duration_days",
    "typical_duration",
    "philosophy_profile_ids",
}

GITHUB_ICON_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path fill="currentColor" d="M12 .5A12 12 0 0 0 8.2 23.9c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.5-1.3-1.3-1.7-1.3-1.7-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.6.1-3.2 0 0 1-.3 3.3 1.2a11.3 11.3 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.6.2 2.9.1 3.2.8.9 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.1c0 .3.2.7.8.6A12 12 0 0 0 12 .5Z"/>
</svg>
"""

CARD_TYPE_ICONS = {
    "macro": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="m3 18 6-9 4 6 2-3 6 6" />
            <path d="M3 20h18" />
        </svg>
    """,
    "mezzo": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M7 4v16" />
            <path d="M7 5h11l-3 4 3 4H7" />
        </svg>
    """,
    "micro": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="8" />
            <path d="m15.4 8.6-2.2 4.7-4.6 2.1 2.2-4.7 4.6-2.1Z" fill="currentColor" stroke="none" />
            <path d="M12 3v2M12 19v2M3 12h2M19 12h2" />
        </svg>
    """,
    "session": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
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

LABEL_TEXT_OVERRIDES = {
    "cts": "CTS",
    "rpe": "RPE",
    "utmb": "UTMB",
    "vo2max": "VO2max",
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
        .preview-card-art-shell {
            position: relative;
            display: flex;
            justify-content: center;
            width: 100%;
        }
        .preview-card-level-emblem {
            position: absolute;
            top: -0.58rem;
            right: -0.5rem;
            z-index: 2;
            width: 4.4rem;
            height: 4.4rem;
            opacity: 0.34;
            pointer-events: none;
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
            color: #526d80;
        }
        .preview-card-type-mezzo {
            color: #765d8c;
        }
        .preview-card-type-micro {
            color: #a06a2c;
        }
        .preview-card-type-session {
            color: #b69718;
        }
        .detail-card-header-macro .detail-card-type {
            color: #526d80;
        }
        .detail-card-header-mezzo .detail-card-type {
            color: #765d8c;
        }
        .detail-card-header-micro .detail-card-type {
            color: #a06a2c;
        }
        .detail-card-header-session .detail-card-type {
            color: #b69718;
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
        [class*="st-key-preview-tags-"] {
            margin-top: 0.7rem !important;
        }
        [class*="st-key-preview-tags-"] [class*="st-key-tag_preview_"] {
            margin: 0 !important;
        }
        [class*="st-key-preview-tags-"] [class*="st-key-tag_preview_"] button {
            min-height: 1.3rem;
            padding: 0;
            border: 0;
            border-radius: 0;
            background: transparent;
            color: #373936;
            box-shadow: none;
            font-size: 0.86rem;
            font-weight: 400;
            line-height: 1.3;
            text-decoration: underline;
            text-decoration-thickness: 1px;
            text-underline-offset: 0.18rem;
        }
        [class*="st-key-preview-tags-"] [class*="st-key-tag_preview_"] button:hover {
            border: 0;
            background: transparent;
            color: #111111;
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
        [class*="st-key-opened-card-"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border: 0 !important;
            border-radius: 12px;
            box-shadow: none;
            position: relative;
            overflow: hidden;
        }
        [class*="st-key-opened-card-"] div[data-testid="stVerticalBlock"] {
            overflow: visible;
        }
        [class*="st-key-opened-card-macro"] div[data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.opened-card-marker-macro) {
            background: #f3f9fc !important;
        }
        [class*="st-key-opened-card-mezzo"] div[data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.opened-card-marker-mezzo) {
            background: #faf5fd !important;
        }
        [class*="st-key-opened-card-micro"] div[data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.opened-card-marker-micro) {
            background: #fff2df !important;
        }
        [class*="st-key-opened-card-session"] div[data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.opened-card-marker-session) {
            background: #fffbe3 !important;
        }
        [class*="st-key-opened-card-"] div[data-testid="stVerticalBlock"],
        [class*="st-key-opened-card-"] div[data-testid="stElementContainer"] {
            background: transparent !important;
        }
        .opened-card-marker {
            position: absolute;
            inset: 0;
            pointer-events: none;
            z-index: 0;
        }
        .opened-card-marker::before,
        .opened-card-marker::after {
            content: "";
            position: absolute;
            width: 13.5rem;
            height: 2.35rem;
            border-radius: 999px;
            background: var(--opened-accent, var(--strong-line));
            opacity: 0.78;
            box-shadow: 0 5px 12px rgb(40 41 35 / 10%);
        }
        .opened-card-marker::before {
            left: -3.8rem;
            top: 1.1rem;
            transform: rotate(-24deg);
        }
        .opened-card-marker::after {
            right: -3.8rem;
            top: 1.1rem;
            transform: rotate(24deg);
        }
        .opened-card-corners {
            position: absolute;
            inset: 0;
            pointer-events: none;
            z-index: 0;
        }
        .opened-card-corners::before,
        .opened-card-corners::after {
            content: "";
            position: absolute;
            width: 10.25rem;
            height: 1.35rem;
            border-radius: 999px;
            background: var(--opened-accent, var(--strong-line));
            opacity: 0.46;
            box-shadow: 0 -4px 10px rgb(40 41 35 / 8%);
        }
        .opened-card-corners::before {
            left: -3.1rem;
            bottom: 0.8rem;
            transform: rotate(22deg);
        }
        .opened-card-corners::after {
            right: -3.1rem;
            bottom: 0.8rem;
            transform: rotate(-22deg);
        }
        .opened-card-marker-macro,
        .opened-card-corners-macro {
            --opened-accent: #526d80;
        }
        .opened-card-marker-mezzo,
        .opened-card-corners-mezzo {
            --opened-accent: #765d8c;
        }
        .opened-card-marker-micro,
        .opened-card-corners-micro {
            --opened-accent: #a06a2c;
        }
        .opened-card-marker-session,
        .opened-card-corners-session {
            --opened-accent: #d7b829;
        }
        .detail-card-header {
            position: relative;
            overflow: hidden;
            margin: 0.15rem 0 0.45rem;
            padding: 0.92rem 0.4rem 0.7rem;
            border: 0;
            border-bottom: 1px solid var(--line);
            border-radius: 0;
            background: transparent;
            z-index: 1;
        }
        .detail-card-header::before {
            display: none;
        }
        .detail-card-header-macro {
            --detail-accent: #526d80;
        }
        .detail-card-header-mezzo {
            --detail-accent: #765d8c;
        }
        .detail-card-header-micro {
            --detail-accent: #a06a2c;
        }
        .detail-card-header-session {
            --detail-accent: #d7b829;
        }
        .detail-card-type {
            display: inline-block;
            margin-top: 0.7rem;
            color: #4d4f4c;
            font-size: 0.92rem;
            font-weight: 600;
            letter-spacing: 0.075em;
            text-transform: uppercase;
        }
        .detail-card-title {
            position: relative;
            z-index: 1;
            margin: 0;
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.85rem;
            font-weight: 600;
            letter-spacing: -0.03em;
            line-height: 1.08;
        }
        .detail-card-emblem {
            display: none;
        }
        .detail-key-facts {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.7rem;
            margin: 0.75rem 0 0.85rem;
        }
        .detail-key-fact {
            min-height: 3.35rem;
            padding: 0.62rem 0.72rem;
            border: 1px solid rgb(111 113 107 / 22%);
            border-top: 3px solid var(--strong-line);
            border-radius: 8px;
            background:
                radial-gradient(circle at 88% 18%, rgb(255 255 255 / 82%) 0, transparent 34%),
                linear-gradient(180deg, rgb(255 255 255 / 82%), rgb(255 255 255 / 36%));
            box-shadow:
                inset 0 1px 0 rgb(255 255 255 / 80%),
                0 7px 15px rgb(40 41 35 / 10%);
        }
        .detail-key-facts-macro .detail-key-fact {
            border-top-color: #526d80;
        }
        .detail-key-facts-mezzo .detail-key-fact {
            border-top-color: #765d8c;
        }
        .detail-key-facts-micro .detail-key-fact {
            border-top-color: #a06a2c;
        }
        .detail-key-facts-session .detail-key-fact {
            border-top-color: #d7b829;
        }
        .detail-key-fact-label {
            display: block;
            margin-bottom: 0.28rem;
            color: #666964;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.055em;
            text-transform: uppercase;
        }
        .detail-key-fact-value {
            color: #2f302d;
            font-size: 0.95rem;
            line-height: 1.34;
        }
        .detail-section {
            margin: 0;
            padding: 0.15rem 0.75rem 0.85rem;
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
            font-size: 1.06rem;
            font-style: normal;
            line-height: 1.46;
        }
        .detail-section-summary {
            margin: 0 0 0.35rem;
            padding: 0.72rem 0.92rem;
            border: 0;
            border-left: 4px solid rgb(111 113 107 / 42%);
            border-radius: 0 10px 10px 0;
            background:
                linear-gradient(90deg, rgb(255 255 255 / 72%), rgb(255 255 255 / 22%));
            box-shadow:
                inset 0 1px 0 rgb(255 255 255 / 55%),
                0 4px 12px rgb(40 41 35 / 5%);
        }
        .detail-section-coaching-note {
            margin-top: 0.25rem;
            padding: 0.45rem 0.75rem 0.25rem;
            border: 0;
            border-bottom: 1px solid var(--line);
            border-radius: 0;
            background: transparent;
        }
        .detail-section-coaching-note .detail-section-label {
            margin-bottom: 0.35rem;
            font-size: 0.72rem;
        }
        .detail-section-coaching-note .detail-section-value {
            color: #3f413d;
            font-size: 0.92rem;
            line-height: 1.42;
        }
        .detail-section-final {
            border-bottom: 0 !important;
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
            padding-bottom: 0.1rem;
        }
        .detail-section-tags .detail-section-label {
            margin-bottom: 0;
        }
        [class*="st-key-preview-tags-detail_"] {
            margin-top: -0.65rem !important;
            padding: 0 0.75rem 0.42rem;
            border-bottom: 1px solid var(--line);
        }
        [class*="st-key-preview-tags-detail-final_"] {
            border-bottom: 0;
        }
        .detail-section-references {
            border-bottom: 0;
            padding-bottom: 0.1rem;
        }
        [class*="st-key-detail-references"] {
            margin-top: -0.55rem !important;
            padding: 0 0.75rem 0.55rem;
            border-bottom: 1px solid var(--line);
        }
        [class*="st-key-detail-references-final"] {
            border-bottom: 0;
        }
        [class*="st-key-detail-history-back"] {
            margin: 0 0 0.35rem !important;
            position: relative;
            z-index: 1;
        }
        [class*="st-key-detail-history-back"] button {
            min-height: 1.35rem;
            padding: 0;
            border: 0;
            border-radius: 0;
            background: transparent;
            color: #373936;
            box-shadow: none;
            font-size: 0.9rem;
            font-weight: 400;
            line-height: 1.35;
            text-align: left;
            text-decoration: underline;
            text-decoration-thickness: 1px;
            text-underline-offset: 0.18rem;
        }
        [class*="st-key-detail-history-back"] button:hover {
            border: 0;
            background: transparent;
            color: #111111;
        }
        .detail-session-family-title {
            margin: 0 0 0.28rem;
            color: var(--ink);
            font-size: 1rem;
            font-weight: 600;
        }
        .detail-session-family-summary,
        .detail-session-family-description {
            margin: 0;
            color: #3f413d;
            font-size: 0.95rem;
            line-height: 1.4;
        }
        .detail-session-family-summary {
            color: #2f302d;
        }
        .detail-session-family-description {
            color: #6f716b;
            margin-top: 0.38rem;
        }
        .detail-workout-part {
            padding: 0.62rem 0;
            border-top: 1px solid rgb(111 113 107 / 18%);
        }
        .detail-workout-part:first-child {
            border-top: 0;
            padding-top: 0;
        }
        .detail-workout-part-title {
            margin: 0 0 0.25rem;
            color: var(--ink);
            font-weight: 600;
        }
        .detail-workout-part-meta {
            margin: 0 0 0.34rem;
            color: #2f302d;
            font-size: 0.98rem;
            font-weight: 400;
        }
        .detail-workout-part-line {
            margin: 0.16rem 0 0;
            color: #4a4c48;
            font-size: 0.95rem;
            line-height: 1.4;
        }
        .detail-workout-part-terrain {
            color: #666964;
            font-size: 0.92rem;
        }
        [class*="st-key-detail-reference_"] {
            margin: 0 !important;
        }
        [class*="st-key-detail-reference_"] button {
            min-height: 1.25rem;
            padding: 0;
            border: 0;
            border-radius: 0;
            background: transparent;
            color: #373936;
            box-shadow: none;
            font-size: 0.95rem;
            font-weight: 400;
            line-height: 1.35;
            text-align: left;
            text-decoration: underline;
            text-decoration-thickness: 1px;
            text-underline-offset: 0.18rem;
        }
        [class*="st-key-detail-reference_"] button:hover {
            border: 0;
            background: transparent;
            color: #111111;
        }
        .detail-reference-list {
            display: grid;
            gap: 0.32rem;
            margin-top: 0.1rem;
        }
        .detail-reference-item {
            color: #2f302d;
            font-size: 0.95rem;
            line-height: 1.38;
        }
        @media (max-width: 760px) {
            .detail-key-facts {
                grid-template-columns: 1fr;
            }
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


def display_label_text(value: Any) -> str:
    text = display_text(value).replace("-", " ").strip()
    words = []
    for word in text.split():
        words.append(LABEL_TEXT_OVERRIDES.get(word.lower(), word[:1].upper() + word[1:]))
    return " ".join(words)


def format_field_value(field_name: str, value: Any) -> str:
    text = as_text(value)
    if field_name == "recommended_duration_weeks" and text:
        if "week" in text.lower():
            return text
        return f"{text} weeks"
    if field_name == "recommended_duration_days" and text:
        if "day" in text.lower():
            return text
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


def card_type_icon_html(card_type_key: str) -> str:
    icon_svg = CARD_TYPE_ICONS.get(card_type_key, "").strip()
    if not icon_svg:
        return ""
    icon_svg = icon_svg.replace("currentColor", "#2F302D")
    icon_uri = svg_data_uri(icon_svg)
    return f'<img class="preview-card-level-emblem" src="{icon_uri}" alt="">'


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


def open_card(card_id: str) -> None:
    st.session_state.active_card_id = card_id
    st.session_state.active_card_history = []


def render_card_history_back(card_by_id: dict[str, Any]) -> None:
    history = list(st.session_state.get("active_card_history", []))
    if not history:
        return

    previous_card_id = history[-1]
    previous_card = card_by_id.get(previous_card_id)
    previous_title = previous_card.title if previous_card else previous_card_id

    if st.button(
        f"Back to {previous_title}",
        key=f"detail-history-back-{previous_card_id}",
        type="secondary",
        width="content",
    ):
        st.session_state.active_card_history = history[:-1]
        st.session_state.active_card_id = previous_card_id
        st.rerun(scope="app")


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


def render_preview_tag_labels(tags: list[Any], key_prefix: str) -> None:
    if not tags:
        return

    with st.container(horizontal=True, key=f"preview-tags-{key_prefix}"):
        for tag in tags:
            tag_text = as_text(tag)
            st.button(
                display_label_text(tag_text),
                key=f"tag_preview_{key_prefix}_{tag_text}",
                type="secondary",
                width="content",
                on_click=set_tag_filter,
                args=(tag_text,),
            )


# ----------------------------------------------------------
# Preview Cards
# ----------------------------------------------------------

def render_preview_field(
    card: Any,
    field_name: str,
    display_config: dict[str, Any],
    key_prefix: str,
) -> None:
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
        render_preview_tag_labels(value, f"{key_prefix}_{card.id}")
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
        formatter = display_label_text if field_name == "suitable_levels" else display_text
        rendered_value = ", ".join(formatter(item) for item in value)
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
        artwork = artwork_for_card(card.id, fallback_level=card_type_key)

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
                    on_click=open_card,
                    args=(card.id,),
                )

        if artwork:
            art_uri = image_file_data_uri(artwork.asset_path)
            with st.container(
                key=f"preview-art-{card_type_key}-{key_prefix}-{card.id}",
                horizontal=True,
                horizontal_alignment="center",
            ):
                if art_uri:
                    level_icon_html = card_type_icon_html(card_type_key)
                    st.html(
                        '<div class="preview-card-art-shell">'
                        f'{level_icon_html}'
                        '<img class="preview-card-art-image" '
                        f'src="{art_uri}" '
                        f'alt="{escape(artwork.alt_text, quote=True)}">'
                        '</div>'
                    )

        for field_name in ordered_preview_fields:
            if field_name == "tags":
                continue
            render_preview_field(card, field_name, display_config, key_prefix)

        if "tags" in ordered_preview_fields and card.tags:
            render_preview_field(card, "tags", display_config, key_prefix)


# ----------------------------------------------------------
# Detail View
# ----------------------------------------------------------

def render_reference_list(card: Any, card_by_id: dict[str, Any], is_final: bool = False) -> None:
    if not card.references:
        return

    final_class = " detail-section-final" if is_final else ""
    st.html(
        f'<section class="detail-section detail-section-references{final_class}">'
        '<div class="detail-section-label">References</div>'
        '</section>'
    )
    with st.container(
        horizontal=True,
        key=f"detail-references{'-final' if is_final else ''}-{card.id}",
    ):
        for index, reference in enumerate(card.references):
            linked = card_by_id.get(reference.card_id)
            linked_title = linked.title if linked else reference.card_id
            relationship = display_label_text(reference.relationship)
            label = f"{relationship}: {linked_title}"
            if st.button(
                label,
                key=f"detail-reference_{card.id}_{index}_{reference.card_id}",
                type="secondary",
                width="content",
            ):
                history = list(st.session_state.get("active_card_history", []))
                if not history or history[-1] != card.id:
                    history.append(card.id)
                st.session_state.active_card_history = history
                st.session_state.active_card_id = reference.card_id
                st.rerun(scope="app")


def render_workout_parts(parts: list[Any], is_final: bool = False) -> None:
    if not parts:
        return

    rendered_parts = []
    for part in parts:
        rpe = as_text(part.rpe)
        rpe_text = rpe if rpe.upper().startswith("RPE") else f"RPE {rpe}"
        lines = []
        lines.append(f'<p class="detail-workout-part-meta">{escape(part.duration)} | {escape(rpe_text)}</p>')
        if part.instructions:
            lines.append(f'<p class="detail-workout-part-line">{escape(part.instructions)}</p>')
        if part.terrain_notes:
            lines.append(
                '<p class="detail-workout-part-line detail-workout-part-terrain">'
                f'Terrain: {escape(part.terrain_notes)}'
                '</p>'
            )
        rendered_parts.append(
            '<div class="detail-workout-part">'
            f'<p class="detail-workout-part-title">{escape(part.name)}</p>'
            f'{"".join(lines)}'
            '</div>'
        )

    final_class = " detail-section-final" if is_final else ""
    st.html(
        f'<section class="detail-section detail-section-workout-parts{final_class}">'
        '<div class="detail-section-label">Workout Parts</div>'
        f'<div class="detail-workout-parts">{"".join(rendered_parts)}</div>'
        '</section>'
    )


def render_dataclass_value(
    field_name: str,
    value: Any,
    display_config: dict[str, Any],
    is_final: bool = False,
) -> bool:
    if field_name != "session_family" or not is_dataclass(value):
        return False

    family = asdict(value)
    title = family.get("title", "")
    summary = family.get("summary", "")
    description = family.get("description", "")
    summary_html = (
        f'<p class="detail-session-family-summary">{escape(summary)}</p>'
        if summary
        else ""
    )
    description_html = (
        f'<p class="detail-session-family-description">{escape(description)}</p>'
        if description
        else ""
    )
    final_class = " detail-section-final" if is_final else ""
    st.html(
        f'<section class="detail-section detail-section-session-family{final_class}">'
        f'<div class="detail-section-label">{escape(field_label(field_name, display_config))}</div>'
        f'<p class="detail-session-family-title">{escape(title)}</p>'
        f'{summary_html}'
        f'{description_html}'
        '</section>'
    )
    return True


def render_field(
    field_name: str,
    value: Any,
    display_config: dict[str, Any],
    key_prefix: str = "detail",
    is_final: bool = False,
) -> None:
    if value is None:
        return
    if isinstance(value, str) and not value.strip():
        return
    if isinstance(value, list) and not value:
        return
    if render_dataclass_value(field_name, value, display_config, is_final=is_final):
        return

    label = field_label(field_name, display_config)
    section_class = "detail-section"
    if field_name == "summary":
        section_class += " detail-section-summary"
    elif field_name == "additional_information":
        section_class += " detail-section-coaching-note"
    elif field_name == "tags":
        section_class += " detail-section-tags"
    if is_final:
        section_class += " detail-section-final"

    if field_name == "tags" and isinstance(value, list):
        st.html(
            f'<section class="{section_class}">'
            f'<div class="detail-section-label">{escape(label)}</div>'
            '</section>'
        )
        tag_key_prefix = f"detail-final_{key_prefix}" if is_final else key_prefix
        render_preview_tag_labels(value, tag_key_prefix)
        return

    if field_name == "philosophy_profile_ids" and isinstance(value, list):
        rendered_value = ", ".join(
            philosophy_profile_display_name(profile_id)
            for profile_id in value
        )
        value_html = escape(rendered_value)
    elif isinstance(value, list):
        formatter = display_label_text if field_name == "suitable_levels" else as_text
        if len(value) == 1:
            value_html = escape(formatter(value[0]))
        else:
            value_html = (
                '<ul class="detail-section-list">'
                + "".join(f'<li>{escape(formatter(item))}</li>' for item in value)
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
    if str(card.card_type).replace("_", "-") == "session":
        promoted = [field for field in ["session_family", "workout_parts"] if field in ordered]
        ordered = [field for field in ordered if field not in promoted]
        insert_at = ordered.index("purpose") + 1 if "purpose" in ordered else 0
        ordered[insert_at:insert_at] = promoted
    return ordered


def render_detail_header(card: Any, display_config: dict[str, Any]) -> None:
    card_type_key = str(card.card_type).replace("_", "-")
    card_type = card_type_label(card.card_type, display_config)

    st.html(
        f'<section class="detail-card-header detail-card-header-{card_type_key}">'
        f'<h2 class="detail-card-title">{escape(card.title)}</h2>'
        f'<div class="detail-card-type">{escape(card_type)}</div>'
        '</section>'
    )


def detail_key_fact_value(card: Any, field_name: str) -> str:
    value = getattr(card, field_name, None)
    if value is None:
        return ""
    if isinstance(value, str) and not value.strip():
        return ""
    if isinstance(value, list):
        if not value:
            return ""
        if field_name == "suitable_levels":
            return ", ".join(display_label_text(item) for item in value)
        if field_name == "philosophy_profile_ids":
            return ", ".join(philosophy_profile_display_name(profile_id) for profile_id in value)
        return ", ".join(display_text(item) for item in value)
    return format_field_value(field_name, value)


def render_detail_key_facts(card: Any) -> None:
    card_type_key = str(card.card_type).replace("_", "-")
    duration = (
        detail_key_fact_value(card, "recommended_duration_weeks")
        or detail_key_fact_value(card, "recommended_duration_days")
        or detail_key_fact_value(card, "typical_duration")
    )
    facts = [
        ("Suitable For", detail_key_fact_value(card, "suitable_levels")),
        ("Duration", duration),
        ("Philosophy", detail_key_fact_value(card, "philosophy_profile_ids")),
    ]
    rendered_facts = "".join(
        '<div class="detail-key-fact">'
        f'<span class="detail-key-fact-label">{escape(label)}</span>'
        f'<span class="detail-key-fact-value">{escape(value)}</span>'
        '</div>'
        for label, value in facts
        if value
    )
    if rendered_facts:
        st.html(f'<section class="detail-key-facts detail-key-facts-{card_type_key}">{rendered_facts}</section>')


def render_detail(
    card: Any,
    display_config: dict[str, Any],
    card_by_id: dict[str, Any],
    show_header: bool = True,
) -> None:
    card_type_key = str(card.card_type).replace("_", "-")
    with st.container(border=False, key=f"opened-card-{card_type_key}-{card.id}"):
        st.html(f'<div class="opened-card-marker opened-card-marker-{card_type_key}"></div>')
        st.html(f'<div class="opened-card-corners opened-card-corners-{card_type_key}"></div>')
        render_card_history_back(card_by_id)
        if show_header:
            render_detail_header(card, display_config)
            render_field("summary", card.summary, display_config, f"detail_{card.id}")
            render_detail_key_facts(card)

        fields_to_render = []
        for field_name in ordered_detail_fields(card):
            if field_name == "summary" or field_name in DETAIL_KEY_FACT_FIELDS:
                continue
            value = getattr(card, field_name, None)
            if value is None or (isinstance(value, str) and not value.strip()):
                continue
            if isinstance(value, list) and not value:
                continue
            fields_to_render.append(field_name)

        for index, field_name in enumerate(fields_to_render):
            is_final = index == len(fields_to_render) - 1
            value = getattr(card, field_name)
            if field_name == "workout_parts":
                render_workout_parts(value, is_final=is_final)
            elif field_name == "references":
                render_reference_list(card, card_by_id, is_final=is_final)
            else:
                render_field(
                    field_name,
                    value,
                    display_config,
                    f"detail_{card.id}",
                    is_final=is_final,
                )


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
