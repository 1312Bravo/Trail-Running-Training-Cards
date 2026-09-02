from __future__ import annotations

import streamlit as st

# ----------------------------------------------------------
# Page Styling
# ----------------------------------------------------------

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
            --card-gold: #b99a3f;
            --card-gold-soft: rgb(185 154 63 / 8%);
            --card-gold-shadow: rgb(94 75 39 / 14%);
            --level-macro: #7197aa;
            --level-macro-soft: #f4fbff;
            --level-mezzo: #6f986b;
            --level-mezzo-soft: #f5fbf2;
            --level-micro: #b36b45;
            --level-micro-soft: #fff5ee;
            --level-session: #cfa63a;
            --level-session-soft: #fff8dc;
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
            background: transparent;
            padding-bottom: 0;
        }
        [class*="st-key-open_"] button,
        [class*="st-key-select_"] button {
            border: 1px solid #6f716b;
            border-radius: 6px;
            background: linear-gradient(180deg, rgb(255 255 255 / 84%), rgb(255 255 255 / 52%));
            color: var(--ink);
            font-weight: 400;
            min-height: 1.58rem;
            padding: 0.08rem 0.5rem;
            font-size: 0.76rem;
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
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.85rem;
            margin: 0.08rem 0 0.44rem;
            padding: 0.42rem 0.62rem;
            border: 1px solid rgb(185 154 63 / 72%);
            border-radius: 7px;
            background:
                linear-gradient(180deg, rgb(255 253 244 / 88%), rgb(248 242 225 / 50%)),
                linear-gradient(90deg, rgb(255 255 255 / 74%), rgb(185 154 63 / 10%));
            color: var(--ink);
            font-family: "Segoe UI", "Trebuchet MS", sans-serif;
            font-size: 1.16rem;
            font-weight: 400;
            letter-spacing: 0;
            line-height: 1.22;
            box-shadow:
                inset 0 1px 0 rgb(255 255 255 / 78%),
                0 1px 2px rgb(110 83 28 / 8%);
        }
        .preview-card-title-text {
            min-width: 0;
        }
        .preview-card-pips {
            display: inline-flex;
            flex: 0 0 auto;
            gap: 0.22rem;
            align-items: center;
            padding-left: 0.35rem;
        }
        .preview-card-pip {
            display: inline-block;
            color: #c2a03d;
            font-size: 0.64rem;
            line-height: 1;
            text-shadow:
                0 1px 0 rgb(255 255 255 / 78%),
                0 1px 1px rgb(75 56 22 / 16%);
        }
        .preview-card-meta {
            margin: 0;
            padding: 0.34rem 0.48rem;
            border-top: 1px solid rgb(111 113 107 / 30%);
            border-bottom: 1px solid rgb(111 113 107 / 22%);
            background: linear-gradient(90deg, rgb(255 255 255 / 70%), rgb(255 255 255 / 18%));
            color: #2f302d;
            font-size: 0.76rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            line-height: 1.2;
            text-transform: uppercase;
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
        .preview-card-type-macro {
            color: #2f302d;
        }
        .preview-card-type-mezzo {
            color: #2f302d;
        }
        .preview-card-type-micro {
            color: #2f302d;
        }
        .preview-card-type-session {
            color: #2f302d;
        }
        .detail-card-header-macro .detail-card-type {
            color: #2f302d;
        }
        .detail-card-header-mezzo .detail-card-type {
            color: #2f302d;
        }
        .detail-card-header-micro .detail-card-type {
            color: #2f302d;
        }
        .detail-card-header-session .detail-card-type {
            color: #2f302d;
        }
        .preview-summary {
            display: flex;
            align-items: center;
            min-height: 4.4rem;
            margin: 1.05rem 0 0.9rem;
            padding: 0.78rem 1rem;
            border: 2px solid rgb(185 154 63 / 42%);
            border-radius: 8px;
            background:
                linear-gradient(180deg, rgb(255 255 255 / 92%), rgb(255 255 255 / 72%));
            color: #2f302d;
            font-family: "Segoe UI", "Trebuchet MS", sans-serif;
            font-size: 0.98rem;
            font-style: normal;
            font-weight: 400;
            letter-spacing: 0;
            line-height: 1.45;
            box-shadow:
                inset 0 1px 0 rgb(255 255 255 / 76%),
                0 4px 10px rgb(110 83 28 / 6%);
        }
        .preview-field {
            display: grid;
            grid-template-columns: minmax(6.7rem, 8.4rem) minmax(0, 1fr);
            align-items: center;
            column-gap: 0.75rem;
            margin: 0;
            padding: 0.48rem 0.45rem;
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
        .preview-card-footer {
            margin: 0.55rem 0 0;
            padding: 0.45rem 0.45rem 0;
            border-top: 1px solid rgb(111 113 107 / 24%);
            color: #73756f;
            font-size: 0.63rem;
            font-weight: 600;
            letter-spacing: 0.065em;
            line-height: 1.2;
            text-align: right;
            text-transform: uppercase;
        }
        [class*="st-key-preview-footer-tags-"] {
            margin-top: 0.42rem !important;
            padding: 0.34rem 0.45rem 0;
            border-top: 1px solid rgb(111 113 107 / 24%);
        }
        [class*="st-key-preview-footer-tags-"] [class*="st-key-tag_preview_footer_"] {
            margin: 0 !important;
        }
        [class*="st-key-preview-footer-tags-"] [class*="st-key-tag_preview_footer_"] button {
            min-height: 0.92rem;
            padding: 0;
            border: 0;
            border-radius: 0;
            background: transparent;
            color: #73756f;
            box-shadow: none;
            font-size: 0.6rem;
            font-weight: 400;
            letter-spacing: 0.045em;
            line-height: 1.2;
            text-decoration: underline;
            text-decoration-thickness: 1px;
            text-underline-offset: 0.18rem;
            text-transform: uppercase;
        }
        [class*="st-key-preview-footer-tags-"] [class*="st-key-tag_preview_footer_"] button p {
            color: #73756f;
            font-size: 0.6rem;
            font-weight: 400;
            letter-spacing: 0.045em;
            line-height: 1.2;
        }
        [class*="st-key-preview-footer-tags-"] [class*="st-key-tag_preview_footer_"] button:hover {
            border: 0;
            background: transparent;
            color: #252525;
        }
        [class*="st-key-card-"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--surface);
            border: 3px solid var(--card-gold) !important;
            border-radius: 12px;
            box-shadow:
                inset 0 0 0 2px rgb(255 255 255 / 38%),
                0 0 0 1px var(--card-gold-shadow),
                0 5px 12px rgb(40 41 35 / 8%);
        }
        [class*="st-key-card-macro"],
        [class*="st-key-card-macro"][data-testid="stVerticalBlockBorderWrapper"],
        [class*="st-key-card-macro"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: linear-gradient(145deg, #ffffff 0%, #fbfaf6 100%) !important;
            border-color: var(--card-gold) !important;
            box-shadow:
                inset 0 0 0 4px var(--card-gold-soft),
                inset 0 0 0 2px rgb(255 255 255 / 38%),
                0 0 0 1px var(--card-gold-shadow),
                0 5px 12px rgb(40 41 35 / 8%);
        }
        [class*="st-key-card-mezzo"],
        [class*="st-key-card-mezzo"][data-testid="stVerticalBlockBorderWrapper"],
        [class*="st-key-card-mezzo"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: linear-gradient(145deg, #ffffff 0%, #fbfaf6 100%) !important;
            border-color: var(--card-gold) !important;
            box-shadow:
                inset 0 0 0 4px var(--card-gold-soft),
                inset 0 0 0 2px rgb(255 255 255 / 38%),
                0 0 0 1px var(--card-gold-shadow),
                0 5px 12px rgb(40 41 35 / 8%);
        }
        [class*="st-key-card-micro"],
        [class*="st-key-card-micro"][data-testid="stVerticalBlockBorderWrapper"],
        [class*="st-key-card-micro"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: linear-gradient(145deg, #ffffff 0%, #fbfaf6 100%) !important;
            border-color: var(--card-gold) !important;
            box-shadow:
                inset 0 0 0 4px var(--card-gold-soft),
                inset 0 0 0 2px rgb(255 255 255 / 38%),
                0 0 0 1px var(--card-gold-shadow),
                0 5px 12px rgb(40 41 35 / 8%);
        }
        [class*="st-key-card-session"],
        [class*="st-key-card-session"][data-testid="stVerticalBlockBorderWrapper"],
        [class*="st-key-card-session"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: linear-gradient(145deg, #ffffff 0%, #fbfaf6 100%) !important;
            border-color: var(--card-gold) !important;
            box-shadow:
                inset 0 0 0 4px var(--card-gold-soft),
                inset 0 0 0 2px rgb(255 255 255 / 38%),
                0 0 0 1px var(--card-gold-shadow),
                0 5px 12px rgb(40 41 35 / 8%);
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
            background: linear-gradient(145deg, #ffffff 0%, #fbfaf6 100%) !important;
            border-color: var(--card-gold) !important;
            box-shadow:
                inset 0 0 0 4px var(--card-gold-soft),
                inset 0 0 0 2px rgb(255 255 255 / 38%),
                0 0 0 1px var(--card-gold-shadow),
                0 5px 12px rgb(40 41 35 / 8%);
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.preview-card-type-mezzo) {
            background: linear-gradient(145deg, #ffffff 0%, #fbfaf6 100%) !important;
            border-color: var(--card-gold) !important;
            box-shadow:
                inset 0 0 0 4px var(--card-gold-soft),
                inset 0 0 0 2px rgb(255 255 255 / 38%),
                0 0 0 1px var(--card-gold-shadow),
                0 5px 12px rgb(40 41 35 / 8%);
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.preview-card-type-micro) {
            background: linear-gradient(145deg, #ffffff 0%, #fbfaf6 100%) !important;
            border-color: var(--card-gold) !important;
            box-shadow:
                inset 0 0 0 4px var(--card-gold-soft),
                inset 0 0 0 2px rgb(255 255 255 / 38%),
                0 0 0 1px var(--card-gold-shadow),
                0 5px 12px rgb(40 41 35 / 8%);
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.preview-card-type-session) {
            background: linear-gradient(145deg, #ffffff 0%, #fbfaf6 100%) !important;
            border-color: var(--card-gold) !important;
            box-shadow:
                inset 0 0 0 4px var(--card-gold-soft),
                inset 0 0 0 2px rgb(255 255 255 / 38%),
                0 0 0 1px var(--card-gold-shadow),
                0 5px 12px rgb(40 41 35 / 8%);
        }
        div[data-testid="stVerticalBlock"][class*="st-key-opened-card-"],
        [class*="st-key-opened-card-"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border: 3px solid var(--card-gold) !important;
            border-radius: 12px;
            background: linear-gradient(145deg, #fffffe 0%, #fbfcfc 100%) !important;
            box-shadow:
                inset 0 0 0 4px var(--card-gold-soft),
                inset 0 0 0 2px rgb(255 255 255 / 38%),
                0 0 0 1px var(--card-gold-shadow),
                0 8px 18px rgb(40 41 35 / 9%);
            position: relative;
            overflow: hidden;
            padding: 0.82rem !important;
        }
        section[role="dialog"]:has([class*="st-key-opened-card-"]) > div {
            padding: 0.75rem 0.75rem 0.9rem !important;
        }
        [data-testid="stDialog"]:has([class*="st-key-opened-card-"]) section[role="dialog"] > div {
            padding: 0.75rem 0.75rem 0.9rem !important;
        }
        [class*="st-key-opened-card-"] div[data-testid="stVerticalBlock"] {
            overflow: visible;
        }
        div[data-testid="stVerticalBlock"][class*="st-key-opened-card-macro"],
        [class*="st-key-opened-card-macro"] div[data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.opened-card-marker-macro) {
            background: linear-gradient(145deg, #fffffe 0%, #fbfcfc 100%) !important;
        }
        div[data-testid="stVerticalBlock"][class*="st-key-opened-card-mezzo"],
        [class*="st-key-opened-card-mezzo"] div[data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.opened-card-marker-mezzo) {
            background: linear-gradient(145deg, #fffffe 0%, #fcfbfd 100%) !important;
        }
        div[data-testid="stVerticalBlock"][class*="st-key-opened-card-micro"],
        [class*="st-key-opened-card-micro"] div[data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.opened-card-marker-micro) {
            background: linear-gradient(145deg, #fffffc 0%, #fffdf8 100%) !important;
        }
        div[data-testid="stVerticalBlock"][class*="st-key-opened-card-session"],
        [class*="st-key-opened-card-session"] div[data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.opened-card-marker-session) {
            background: linear-gradient(145deg, #fffffb 0%, #fffef5 100%) !important;
        }
        [class*="st-key-opened-card-"] div[data-testid="stVerticalBlock"],
        [class*="st-key-opened-card-"] div[data-testid="stElementContainer"] {
            background: transparent !important;
        }
        .opened-card-marker {
            display: none;
        }
        .opened-card-marker::before,
        .opened-card-marker::after {
            display: none;
        }
        .opened-card-marker::before {
            display: none;
        }
        .opened-card-marker::after {
            display: none;
        }
        .opened-card-corners {
            display: none;
        }
        .opened-card-corners::before,
        .opened-card-corners::after {
            display: none;
        }
        .opened-card-corners::before {
            display: none;
        }
        .opened-card-corners::after {
            display: none;
        }
        .opened-card-marker-macro,
        .opened-card-corners-macro {
            --opened-accent: var(--level-macro);
        }
        .opened-card-marker-mezzo,
        .opened-card-corners-mezzo {
            --opened-accent: var(--level-mezzo);
        }
        .opened-card-marker-micro,
        .opened-card-corners-micro {
            --opened-accent: var(--level-micro);
        }
        .opened-card-marker-session,
        .opened-card-corners-session {
            --opened-accent: var(--level-session);
        }
        .detail-card-header {
            position: relative;
            overflow: hidden;
            margin: 0.25rem 0 0.65rem;
            padding: 0.56rem 0.72rem 0.5rem;
            border: 1px solid rgb(185 154 63 / 72%);
            border-radius: 7px;
            background:
                linear-gradient(180deg, rgb(255 253 244 / 88%), rgb(248 242 225 / 50%)),
                linear-gradient(90deg, rgb(255 255 255 / 74%), rgb(185 154 63 / 10%));
            box-shadow:
                inset 0 1px 0 rgb(255 255 255 / 78%),
                0 1px 2px rgb(110 83 28 / 8%);
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
            display: block;
            margin-top: 0.4rem;
            padding: 0 0.2rem;
            border-top: 0;
            color: #2f302d;
            font-size: 0.86rem;
            font-weight: 600;
            letter-spacing: 0.075em;
            line-height: 1.2;
            text-transform: uppercase;
        }
        .detail-card-title-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.9rem;
        }
        .detail-card-title {
            position: relative;
            z-index: 1;
            margin: 0;
            color: var(--ink);
            font-family: "Segoe UI", "Trebuchet MS", sans-serif;
            font-size: clamp(1.32rem, 2.1vw, 1.72rem);
            font-weight: 400;
            letter-spacing: 0;
            line-height: 1.16;
        }
        .detail-card-title-row .preview-card-pips {
            padding-left: 0;
        }
        .detail-card-title-row .preview-card-pip {
            font-size: 0.78rem;
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
            border: 1px solid rgb(185 154 63 / 38%);
            border-top: 2px solid var(--card-gold);
            border-radius: 7px;
            background:
                radial-gradient(circle at 88% 18%, rgb(255 255 255 / 70%) 0, transparent 34%),
                linear-gradient(180deg, rgb(255 255 255 / 88%), rgb(255 255 255 / 48%));
            box-shadow:
                inset 0 1px 0 rgb(255 255 255 / 80%),
                0 3px 8px rgb(40 41 35 / 6%);
        }
        .detail-key-facts-macro .detail-key-fact {
            border-top-color: var(--card-gold);
        }
        .detail-key-facts-mezzo .detail-key-fact {
            border-top-color: var(--card-gold);
        }
        .detail-key-facts-micro .detail-key-fact {
            border-top-color: var(--card-gold);
        }
        .detail-key-facts-session .detail-key-fact {
            border-top-color: var(--card-gold);
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
            font-size: 1.08rem;
            font-style: normal;
            line-height: 1.46;
        }
        .detail-section-summary {
            margin: 0.7rem 0 0.7rem;
            padding: 0.76rem 0.9rem;
            border: 2px solid rgb(185 154 63 / 48%);
            border-radius: 7px;
            background: rgb(255 255 255 / 84%);
            box-shadow:
                inset 0 1px 0 rgb(255 255 255 / 76%),
                0 1px 2px rgb(110 83 28 / 6%);
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
        .detail-section-last {
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
        [class*="st-key-preview-tags-detail-last_"] {
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
        [class*="st-key-detail-references-last"] {
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
            .detail-card-title-row {
                align-items: flex-start;
                flex-wrap: wrap;
            }
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
