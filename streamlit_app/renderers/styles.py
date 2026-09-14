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
            --muted-ink: #4f514c;
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
            text-align: center;
        }
        .app-card-count {
            margin-top: -0.4rem;
            color: var(--muted-ink);
            font-size: 0.9rem;
            text-align: center;
        }
        [data-testid="stCaptionContainer"] {
            color: var(--muted-ink);
        }
        [data-testid="stCaptionContainer"] p {
            color: #30322e !important;
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
        [class*="st-key-app_mode"] {
            margin: 0.7rem 0 1.05rem;
        }
        [class*="st-key-app_mode"] [data-testid="stButtonGroup"] {
            border-bottom: 1px solid #d6d7d2;
            background: transparent;
        }
        [class*="st-key-app_mode"] [role="radiogroup"] {
            display: flex;
            justify-content: center;
            gap: 1.35rem;
        }
        [class*="st-key-app_mode"] [role="radiogroup"] button[data-variant="segmented_control"] {
            flex: 0 0 auto;
            min-height: 2.25rem;
            padding: 0.38rem 0.12rem 0.48rem;
            border: 0;
            border-bottom: 2px solid transparent;
            border-radius: 0;
            background: transparent;
            color: #62645f;
            font-size: 0.88rem;
            font-weight: 400;
            line-height: 1.25;
            transition: background 160ms ease, color 160ms ease;
        }
        [class*="st-key-app_mode"] [role="radiogroup"] button[data-variant="segmented_control"]:hover {
            background: transparent;
            border-bottom-color: #b8bab3;
            color: #20221f;
        }
        [class*="st-key-app_mode"] [role="radiogroup"] button[data-variant="segmented_control"][data-selected="true"] {
            background: transparent;
            border-bottom-color: #30322e;
            color: #20221f;
            font-weight: 600;
        }
        [class*="st-key-app_mode"] [role="radiogroup"] button[data-variant="segmented_control"][data-selected="true"]:hover {
            background: transparent;
            border-bottom-color: #20221f;
            color: #20221f;
        }
        [class*="st-key-app_mode"] [role="radiogroup"] button[data-variant="segmented_control"] [data-testid="stMarkdownContainer"] p {
            color: inherit;
        }
        @media (max-width: 760px) {
            [data-testid="stMainBlockContainer"],
            .block-container {
                padding-top: 1.65rem;
                padding-right: 0.85rem;
                padding-left: 0.85rem;
            }
            h1 {
                font-size: 2rem;
                line-height: 1.05;
            }
            [data-testid="stAppViewContainer"] {
                overflow-x: hidden;
            }
            [class*="st-key-app_mode"] {
                overflow-x: auto;
                margin-right: -0.5rem;
                margin-left: -0.5rem;
                padding: 0 0.5rem;
            }
            [class*="st-key-app_mode"] [data-testid="stButtonGroup"] {
                min-width: max-content;
            }
            [class*="st-key-app_mode"] [role="radiogroup"] {
                justify-content: flex-start;
                gap: 0.95rem;
            }
            [class*="st-key-app_mode"] [role="radiogroup"] button[data-variant="segmented_control"] {
                flex: 0 0 auto;
                padding-right: 0.62rem;
                padding-left: 0.62rem;
                font-size: 0.82rem;
                min-height: 2.65rem;
            }
        }
        [class*="st-key-browse-toolbar"],
        [class*="st-key-mode-toolbar-"] {
            max-width: 1220px;
            margin: 0 auto 0.8rem;
            padding: 0.12rem 0.35rem 0.2rem;
        }
        [class*="st-key-browse-scope-links"],
        [class*="st-key-library-level-links"] {
            overflow-x: auto;
            padding: 0.12rem 0.2rem 0;
            border: 0 !important;
            background: transparent !important;
        }
        [class*="st-key-browse-scope-links"],
        [class*="st-key-library-level-links"] {
            justify-content: center;
        }
        [class*="st-key-browse-scope-row"] {
            margin-bottom: 0.18rem;
        }
        [class*="st-key-browse-filter-row"],
        [class*="st-key-today-filter-row"],
        [class*="st-key-pathway-filter-row"] {
            max-width: 980px;
            margin: 0 auto;
        }
        [class*="st-key-browse-scope-links"] [class*="st-key-browse-scope-"] button,
        [class*="st-key-library-level-links"] [class*="st-key-library-level-"] button {
            min-height: 1.85rem !important;
            padding: 0.28rem 0.05rem 0.38rem !important;
            border: 0 !important;
            border-bottom: 1px solid transparent !important;
            border-radius: 0 !important;
            background: transparent !important;
            color: #5f615c !important;
            box-shadow: none !important;
            font-size: 0.86rem !important;
            font-weight: 400 !important;
            line-height: 1.25;
            white-space: nowrap;
            transition: color 160ms ease, border-color 160ms ease;
        }
        [class*="st-key-browse-scope-links"] [class*="st-key-browse-scope-"] button:hover,
        [class*="st-key-library-level-links"] [class*="st-key-library-level-"] button:hover {
            border-bottom-color: #b8bab3 !important;
            background: transparent !important;
            color: #242622 !important;
        }
        [class*="st-key-browse-scope-links"] [class*="st-key-browse-scope-selected-"] button,
        [class*="st-key-library-level-links"] [class*="st-key-library-level-selected-"] button {
            border-bottom-color: #30322e !important;
            color: #20221f !important;
            font-weight: 600 !important;
        }
        [class*="st-key-browse-scope-links"] [class*="st-key-browse-scope-selected-"] button:hover,
        [class*="st-key-library-level-links"] [class*="st-key-library-level-selected-"] button:hover {
            border-bottom-color: #30322e !important;
            background: transparent !important;
            color: #20221f !important;
        }
        [class*="st-key-browse-scope-links"] [class*="st-key-browse-scope-"] button p,
        [class*="st-key-library-level-links"] [class*="st-key-library-level-"] button p {
            color: inherit !important;
        }
        [class*="st-key-browse-toolbar"] [data-testid="stTextInputRootElement"],
        [class*="st-key-browse-toolbar"] [data-testid="stMultiSelect"] .react-aria-ComboBox > div[role="group"],
        [class*="st-key-library_search_query"] [data-testid="stTextInputRootElement"],
        [class*="st-key-mode-toolbar-"] [data-testid="stTextInputRootElement"],
        [class*="st-key-mode-toolbar-"] [data-testid="stMultiSelect"] .react-aria-ComboBox > div[role="group"] {
            min-height: 2.1rem;
            border: 0 !important;
            border-bottom: 1px solid #c9cac4 !important;
            border-radius: 0 !important;
            background: transparent !important;
            box-shadow: none !important;
        }
        [class*="st-key-browse-toolbar"] [data-testid="stTextInput"] input,
        [class*="st-key-browse-toolbar"] [data-testid="stMultiSelect"] input,
        [class*="st-key-library_search_query"] [data-testid="stTextInput"] input,
        [class*="st-key-mode-toolbar-"] [data-testid="stTextInput"] input,
        [class*="st-key-mode-toolbar-"] [data-testid="stMultiSelect"] input {
            background: transparent !important;
            color: #3e403b;
        }
        [class*="st-key-browse-toolbar"] input::placeholder,
        [class*="st-key-library_search_query"] input::placeholder,
        [class*="st-key-mode-toolbar-"] input::placeholder {
            color: #656761 !important;
            opacity: 1;
        }
        [class*="st-key-browse-toolbar"] [data-testid="stMultiSelect"] button,
        [class*="st-key-mode-toolbar-"] [data-testid="stMultiSelect"] button {
            border: 0 !important;
            background: transparent !important;
            box-shadow: none !important;
        }
        [class*="st-key-mode-toolbar-"] [data-testid="stMultiSelect"] [data-tag] {
            display: inline-flex;
            align-items: center;
            gap: 0.28rem;
            margin: 0 0.3rem 0 0;
            padding: 0 !important;
            border: 0 !important;
            border-radius: 0 !important;
            background: transparent !important;
            color: #555752 !important;
            box-shadow: none !important;
        }
        [class*="st-key-philosophy_profile_filters"] [data-testid="stMultiSelect"] [data-tag] {
            display: inline-flex;
            align-items: center;
            gap: 0.28rem;
            margin: 0 0.3rem 0 0;
            padding: 0 !important;
            border: 0 !important;
            border-radius: 0 !important;
            background: transparent !important;
            color: #555752 !important;
            box-shadow: none !important;
        }
        [class*="st-key-mode-toolbar-"] [data-testid="stMultiSelect"] [data-tag] > span[title] {
            color: #555752 !important;
            font-size: 0.86rem;
            line-height: 1.35;
            text-decoration: underline;
            text-decoration-color: #777a72;
            text-underline-offset: 0.18rem;
        }
        [class*="st-key-philosophy_profile_filters"] [data-testid="stMultiSelect"] [data-tag] > span[title] {
            color: #555752 !important;
            font-size: 0.86rem;
            line-height: 1.35;
            text-decoration: underline;
            text-decoration-color: #777a72;
            text-underline-offset: 0.18rem;
        }
        [class*="st-key-mode-toolbar-"] [data-testid="stMultiSelect"] [data-tag] button {
            min-width: 0;
            min-height: 1rem;
            margin: 0;
            padding: 0 !important;
            border: 0 !important;
            background: transparent !important;
            color: #777a72 !important;
            box-shadow: none !important;
        }
        [class*="st-key-philosophy_profile_filters"] [data-testid="stMultiSelect"] [data-tag] button {
            min-width: 0;
            min-height: 1rem;
            margin: 0;
            padding: 0 !important;
            border: 0 !important;
            background: transparent !important;
            color: #777a72 !important;
            box-shadow: none !important;
        }
        [class*="st-key-browse-toolbar"] [data-testid="stTextInputRootElement"]:has(input:focus),
        [class*="st-key-browse-toolbar"] [data-testid="stMultiSelect"] .react-aria-ComboBox > div[role="group"]:has(input:focus),
        [class*="st-key-library_search_query"] [data-testid="stTextInputRootElement"]:has(input:focus),
        [class*="st-key-mode-toolbar-"] [data-testid="stTextInputRootElement"]:has(input:focus),
        [class*="st-key-mode-toolbar-"] [data-testid="stMultiSelect"] .react-aria-ComboBox > div[role="group"]:has(input:focus) {
            border-bottom-color: #777a72 !important;
        }
        .library-intro {
            margin: 0.28rem 0 0.7rem;
            color: var(--muted-ink);
            font-size: 0.9rem;
            line-height: 1.35;
            text-align: center;
        }
        [class*="st-key-library-profile-grid"] {
            max-width: 980px;
            margin: 0 auto;
        }
        [class*="st-key-library-group-"]:not([class*="st-key-library-group-toggle-"]) {
            width: 100%;
            margin: 0 0 0.7rem;
            padding: 0 0 0.3rem;
            border: 0 !important;
            border-bottom: 1px solid #dedfd9 !important;
            border-radius: 0;
            background: #ffffff;
        }
        [class*="st-key-library-group-toggle-"] button {
            display: flex !important;
            justify-content: flex-start !important;
            width: 100% !important;
            min-height: 2.15rem !important;
            padding: 0.38rem 0.7rem !important;
            border: 0 !important;
            background: transparent !important;
            color: #30322e !important;
            box-shadow: none !important;
            font-size: 0.94rem !important;
            font-weight: 500 !important;
            text-align: left !important;
        }
        [class*="st-key-library-group-toggle-"] button p {
            width: 100% !important;
            color: inherit !important;
            text-align: left !important;
        }
        [class*="st-key-library-group-toggle-"] button:hover {
            background: transparent !important;
            color: #111310 !important;
        }
        .page-intro {
            margin: 0.35rem 0 0.8rem;
            color: #30322e;
            font-size: 0.9rem;
            line-height: 1.4;
        }
        .page-intro-centered {
            text-align: center;
        }
        [class*="st-key-library-expanded-"] {
            max-width: 1120px;
            margin: 0.85rem auto 0;
            padding: 0.75rem 0.15rem 0;
            border-top: 1px solid #cfd1ca;
        }
        .library-expanded-title {
            color: #252725;
            font-size: 1.02rem;
            font-weight: 600;
            line-height: 1.3;
        }
        .library-table-heading {
            padding: 0.35rem 0 0.28rem;
            border-bottom: 1px solid #cfd1ca;
            color: #686a64;
            font-size: 0.7rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            line-height: 1.2;
            text-transform: uppercase;
        }
        [class*="st-key-card-"][class*="library_preview_dialog"] {
            width: 100%;
            max-width: 484px;
            min-height: 470px;
            margin-right: auto;
            margin-left: auto;
        }
        section[role="dialog"]:has([class*="library_preview_dialog"]) {
            width: min(540px, calc(100vw - 2rem)) !important;
            max-width: calc(100vw - 2rem) !important;
            border: 1px solid #d5d6d1 !important;
            border-radius: 16px !important;
            background: #ffffff !important;
            box-shadow: 0 10px 26px rgb(40 41 35 / 12%) !important;
        }
        section[role="dialog"]:has([class*="library_preview_dialog"]) > div,
        [data-testid="stDialog"]:has([class*="library_preview_dialog"]) > div {
            width: min(540px, calc(100vw - 2rem)) !important;
            max-width: calc(100vw - 2rem) !important;
            padding: 0.35rem 0.65rem 2rem !important;
            border: 0 !important;
            background: transparent !important;
            box-shadow: none !important;
            overflow: visible !important;
        }
        [data-testid="stDialog"]:has([class*="library_preview_dialog"]) section[role="dialog"] {
            border: 1px solid #d5d6d1 !important;
            border-radius: 16px !important;
            background: #ffffff !important;
            box-shadow: 0 10px 26px rgb(40 41 35 / 12%) !important;
        }
        [class*="st-key-mode-toolbar-"] [data-testid="stCaptionContainer"] {
            display: flex;
            align-items: center;
            min-height: 2.1rem;
            margin: 0;
        }
        [class*="st-key-mode-toolbar-"] [data-testid="stCaptionContainer"] p {
            margin: 0;
            color: #30322e !important;
        }
        [data-testid="stDivider"] {
            border-color: var(--line);
        }
        .author-footer {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin-top: 3rem;
            padding-top: 1rem;
            border-top: 1px solid rgb(111 113 107 / 20%);
            color: var(--muted-ink);
            font-size: 0.82rem;
        }
        .author-footer-label {
            color: #555752;
            font-weight: 600;
        }
        .author-footer a {
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            color: #555752;
            text-decoration: underline;
            text-decoration-color: rgb(185 154 63 / 65%);
            text-underline-offset: 0.18rem;
        }
        .contact-icon {
            width: 0.9rem;
            height: 0.9rem;
            display: inline-block;
        }
        .author-footer a:hover {
            color: var(--ink);
            text-decoration-color: var(--card-gold);
        }
        [class*="st-key-philosophy-"] h1 {
            margin: 0 0 0.8rem;
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.35rem;
            font-weight: 600;
            letter-spacing: -0.02em;
        }
        div[class*="st-key-philosophy-"]:not([class*="st-key-philosophy-summary-"]):not([class*="st-key-philosophy-actions-"]):not([class*="st-key-philosophy-summary-content-"]) {
            background: var(--surface) !important;
            border: 0 !important;
            border-top: 1px solid #d5d6d1 !important;
            border-bottom: 1px solid #d5d6d1 !important;
            border-radius: 0 !important;
            box-shadow: none;
            margin-bottom: 1.15rem;
        }
        .philosophy-card-title {
            margin: 0.35rem 0 0.65rem;
            padding: 0 0.35rem;
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.35rem;
            font-weight: 600;
            letter-spacing: -0.02em;
            line-height: 1.15;
            text-align: center;
        }
        [class*="st-key-philosophy-actions-"] {
            margin-bottom: 0.08rem;
            padding: 0.34rem 0.35rem 0.56rem;
            border-top: 1px solid #e1e2dd;
            border-bottom: 1px solid #e1e2dd;
            background: var(--surface);
        }
        [class*="st-key-philosophy-actions-"] [data-testid="stButton"] {
            display: flex;
            justify-content: center;
        }
        .philosophy-card-count {
            margin-bottom: 0.4rem;
            color: #666862;
            font-size: 0.8rem;
            text-align: center;
        }
        [class*="st-key-philosophy-actions-"] [data-testid="stButton"] > button {
            min-height: 1.72rem;
            padding: 0.12rem 0.35rem;
            border: 0 !important;
            background: transparent !important;
            box-shadow: none;
            color: #454740;
            font-size: 0.8rem;
            font-weight: 500;
            white-space: nowrap;
        }
        [class*="st-key-philosophy-actions-"] [data-testid="stButton"] > button:hover {
            border: 0 !important;
            background: transparent !important;
            color: #20221f;
            text-decoration: underline;
            text-decoration-color: #b6b8b1;
            text-underline-offset: 0.18rem;
        }
        [class*="st-key-philosophy-summary-content-"] {
            padding: 0.05rem 0.15rem 0.2rem !important;
            background: var(--surface) !important;
            scrollbar-color: #c4c6be transparent;
            scrollbar-width: thin;
        }
        [class*="st-key-philosophy-summary-content-"]::-webkit-scrollbar {
            width: 6px;
        }
        [class*="st-key-philosophy-summary-content-"]::-webkit-scrollbar-thumb {
            border-radius: 999px;
            background: #c4c6be;
        }
        [class*="st-key-philosophy-summary-content-"] [data-testid="stMarkdownContainer"] > h2:first-child {
            margin-top: 0.2rem !important;
        }
        section[role="dialog"]:has([class*="st-key-full-philosophy-"]) {
            width: min(760px, calc(100vw - 2rem)) !important;
            max-width: calc(100vw - 2rem) !important;
            margin-right: auto !important;
            margin-left: auto !important;
        }
        section[role="dialog"]:has([class*="st-key-full-philosophy-"]) > div {
            padding: 0.75rem 1rem 1.1rem !important;
        }
        [class*="st-key-full-philosophy-"] {
            min-width: 0;
            max-width: 660px;
            margin: 0 auto;
        }
        [class*="st-key-full-philosophy-"] [data-testid="stMarkdownContainer"] {
            min-width: 0;
            max-width: 660px;
            margin: 0 auto;
        }
        [class*="st-key-full-philosophy-"] [data-testid="stMarkdownContainer"] h1 {
            margin: 0.15rem 0 1.1rem;
            color: #20221f;
            font-size: clamp(1.35rem, 2.6vw, 1.85rem);
            line-height: 1.12;
            text-align: center;
            white-space: normal !important;
            overflow-wrap: anywhere;
            text-wrap: balance;
        }
        [class*="st-key-full-philosophy-"] [data-testid="stMarkdownContainer"] h2 {
            margin: 1.35rem 0 0.48rem;
            color: #30322e;
            font-size: 1.08rem;
            line-height: 1.25;
            text-align: center;
        }
        [class*="st-key-full-philosophy-"] [data-testid="stMarkdownContainer"] h3 {
            margin: 1rem 0 0.35rem;
            color: #30322e;
            font-size: 0.98rem;
            line-height: 1.3;
        }
        [class*="st-key-full-philosophy-"] [data-testid="stMarkdownContainer"] p,
        [class*="st-key-full-philosophy-"] [data-testid="stMarkdownContainer"] li {
            color: #41433e;
            font-size: 0.94rem;
            line-height: 1.52;
        }
        [class*="st-key-full-philosophy-"] [data-testid="stMarkdownContainer"] p {
            margin: 0.55rem 0;
        }
        section[role="dialog"]:has([class*="st-key-philosophy-sources-"]) {
            width: min(760px, calc(100vw - 2rem)) !important;
            max-width: calc(100vw - 2rem) !important;
            margin-right: auto !important;
            margin-left: auto !important;
        }
        section[role="dialog"]:has([class*="st-key-philosophy-sources-"]) > div {
            padding: 0.75rem 1rem 1.1rem !important;
        }
        [class*="st-key-philosophy-sources-"] {
            min-width: 0;
            max-width: 660px;
            margin: 0 auto;
        }
        [class*="st-key-philosophy-sources-"] [data-testid="stCaptionContainer"] {
            margin: 0 0 1rem;
            color: #41433e;
            font-size: 0.88rem;
            text-align: center;
        }
        [class*="st-key-philosophy-sources-"] [data-testid="stMarkdownContainer"] {
            min-width: 0;
            max-width: 660px;
            margin: 0 auto;
        }
        [class*="st-key-philosophy-sources-"] [data-testid="stMarkdownContainer"] ul {
            margin: 0;
            padding-left: 1.1rem;
        }
        [class*="st-key-philosophy-sources-"] [data-testid="stMarkdownContainer"] li {
            margin: 0;
            padding: 0 0 0.9rem;
            color: #41433e;
            font-size: 0.88rem;
            line-height: 1.5;
            overflow-wrap: anywhere;
        }
        [class*="st-key-philosophy-sources-"] [data-testid="stMarkdownContainer"] li + li {
            padding-top: 0.9rem;
            border-top: 1px solid #e0e1dc;
        }
        [class*="st-key-philosophy-sources-"] [data-testid="stMarkdownContainer"] a {
            overflow-wrap: anywhere;
        }
        [class*="st-key-philosophy-"] h2 {
            margin: 1rem 0 0.45rem;
            font-size: 1rem;
        }
        [class*="st-key-philosophy-"] p,
        [class*="st-key-philosophy-"] li {
            color: #41433e;
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
        [class*="st-key-select_"] button:hover {
            background: linear-gradient(180deg, rgb(255 255 255 / 96%), rgb(255 255 255 / 64%));
            border-color: #6f716b;
            color: var(--ink);
        }
        [class*="st-key-open-action"] {
            background: transparent;
            padding-bottom: 0;
        }
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
        [class*="st-key-open_"] button,
        [class*="st-key-pathway_open_"] button,
        [class*="st-key-pathway_change_"] button {
            min-height: 1.55rem;
            padding: 0.05rem 0.2rem;
            border: 0 !important;
            border-radius: 0;
            background: transparent !important;
            color: #111111;
            box-shadow: none !important;
            font-size: 0.78rem;
            font-weight: 500;
            text-decoration: underline;
            text-decoration-color: #4f514c;
            text-underline-offset: 0.18rem;
            white-space: nowrap;
        }
        [class*="st-key-open_"] button:hover,
        [class*="st-key-pathway_open_"] button:hover,
        [class*="st-key-pathway_change_"] button:hover {
            border: 0 !important;
            background: transparent !important;
            color: #000000;
            text-decoration-color: #20221f;
        }
        [class*="st-key-pathway-selection"] {
            position: sticky;
            top: 0;
            z-index: 4;
            max-width: 88%;
            margin: 0.1rem auto 0.35rem;
            padding: 0.28rem 0.5rem 0.3rem;
            border: 0 !important;
            border-radius: 0;
            background: #ffffff;
            box-shadow: none;
        }
        [class*="st-key-clear_pathway"] {
            display: flex;
            justify-content: center;
            width: 100%;
        }
        [class*="st-key-clear_pathway"] button {
            min-height: 1.55rem;
            padding: 0.05rem 0.1rem;
            border: 0 !important;
            background: transparent !important;
            color: #111111;
            box-shadow: none !important;
            font-size: 0.78rem;
            font-weight: 500;
            text-decoration: underline;
            text-decoration-color: #4f514c;
            text-underline-offset: 0.18rem;
        }
        [class*="st-key-clear_pathway"] button:hover {
            border: 0 !important;
            background: transparent !important;
            color: #000000;
            text-decoration-color: #20221f;
        }
        .pathway-summary-footer-rule {
            margin: 0.18rem 0.2rem 0.08rem;
            border-top: 1px solid #e1e2dd;
        }
        [class*="st-key-pathway-selection"] [data-testid="stCaptionContainer"] {
            margin: 0;
        }
        [class*="st-key-pathway-selection"] [data-testid="stCaptionContainer"] p {
            color: #30322e !important;
        }
        .section-label,
        .toolbar-label,
        .pathway-level-label,
        .pathway-empty {
            color: #30322e;
            font-size: 0.86rem;
            line-height: 1.35;
        }
        .section-label,
        .toolbar-label,
        .pathway-level-label {
            font-weight: 600;
        }
        .toolbar-label {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 2.1rem;
            text-align: center;
        }
        .pathway-level-label {
            margin-bottom: 0.25rem;
            text-align: center;
        }
        .pathway-empty {
            color: #555752;
            text-align: center;
        }
        .pathway-selected-title {
            color: #555752;
            font-size: 0.84rem;
            font-weight: 400;
            line-height: 1.25;
            text-align: center;
        }
        .pathway-level-rule {
            margin: 0.12rem 0.15rem 0.28rem;
            border-top: 1px solid #e1e2dd;
        }
        [class*="st-key-pathway-card-"] {
            min-height: 7.5rem;
            padding: 0.26rem 0.5rem;
            border-bottom: 0;
            background: transparent;
        }
        [class*="st-key-pathway-card-mezzo"],
        [class*="st-key-pathway-card-micro"],
        [class*="st-key-pathway-card-session"] {
            border-left: 1px solid #dedfd9;
            padding-left: 0.85rem;
        }
        [class*="st-key-pathway-card-"]:last-child {
            border-bottom: 0;
        }
        .preview-card-title {
            position: relative;
            display: block;
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
            text-align: center;
        }
        .preview-card-title-text {
            display: block;
            min-width: 0;
            padding: 0 2.35rem;
        }
        .preview-card-title > .preview-card-pips {
            position: absolute;
            top: 50%;
            right: 0.72rem;
            transform: translateY(-50%);
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
        .detail-card-type-line {
            display: flex;
            align-items: baseline;
            justify-content: flex-start;
            margin: 0.05rem 0 0.15rem;
            padding: 0 0.85rem;
            color: #30322e;
            font-size: 0.82rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            line-height: 1.2;
            text-transform: uppercase;
        }
        .detail-card-title-row {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.9rem;
            text-align: center;
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
            padding: 0 2.2rem;
        }
        .detail-card-title-row .preview-card-pips {
            position: absolute;
            top: 50%;
            right: 0;
            padding-left: 0;
            transform: translateY(-50%);
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
        .detail-workout-block {
            padding: 0.72rem 0;
            border-top: 1px solid rgb(111 113 107 / 22%);
        }
        .detail-workout-block:first-child {
            border-top: 0;
            padding-top: 0;
        }
        .detail-workout-block-title {
            margin: 0;
            color: var(--ink);
            font-size: 1rem;
            font-weight: 700;
        }
        .detail-workout-block-mode {
            margin: 0.12rem 0 0.48rem;
            color: #6f716b;
            font-size: 0.78rem;
            font-weight: 600;
            letter-spacing: 0.045em;
            text-transform: uppercase;
        }
        .detail-workout-option {
            margin-top: 0.5rem;
            padding: 0.58rem 0.65rem;
            border: 1px solid rgb(185 154 63 / 28%);
            border-radius: 7px;
            background: rgb(255 255 255 / 48%);
        }
        .detail-workout-option-title {
            margin: 0 0 0.28rem;
            color: var(--ink);
            font-weight: 600;
        }
        .detail-workout-option-notes {
            margin: 0.12rem 0 0.4rem;
            padding-left: 1.05rem;
            color: #555752;
            font-size: 0.9rem;
            line-height: 1.35;
        }
        .detail-workout-option-notes li + li {
            margin-top: 0.14rem;
        }
        .detail-workout-part {
            padding: 0.5rem 0;
            border-top: 1px solid rgb(111 113 107 / 16%);
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
            background: transparent;
            border: 0 !important;
            border-radius: 0;
            box-shadow: none;
        }
        [class*="st-key-pagination-"] {
            margin-top: 1.25rem !important;
            padding: 0.95rem 0 0.15rem;
            border-top: 1px solid rgb(111 113 107 / 20%);
        }
        .pagination-status {
            display: flex;
            align-items: baseline;
            gap: 0.42rem;
            color: #4f514d;
            font-size: 0.9rem;
            line-height: 1.2;
        }
        .pagination-status strong {
            color: #252725;
            font-size: 0.9rem;
            font-weight: 600;
        }
        .pagination-page {
            color: #444641;
            font-size: 0.9rem;
            line-height: 2.05rem;
            text-align: center;
            white-space: nowrap;
        }
        [class*="st-key-pagination_"] button {
            min-height: 1.55rem;
            padding: 0.05rem 0.15rem;
            border: 0 !important;
            border-radius: 0;
            background: transparent !important;
            color: #111111;
            box-shadow: none !important;
            font-size: 0.82rem;
            font-weight: 500;
            text-decoration: underline;
            text-decoration-color: #4f514c;
            text-underline-offset: 0.18rem;
        }
        [class*="st-key-pagination_"] button:hover {
            border: 0 !important;
            background: transparent !important;
            color: #000000;
            text-decoration-color: #20221f;
        }
        [class*="st-key-pagination_"] button:disabled {
            border: 0 !important;
            background: transparent !important;
            color: #a5a6a1;
            opacity: 1;
            text-decoration-color: #cfd0cb;
        }
        [class*="st-key-pagination-"] [data-testid="stSegmentedControl"] {
            margin: 0;
        }
        [class*="st-key-pagination-"] [data-testid="stSegmentedControl"] label {
            font-size: 0.85rem;
        }
        .library-bullet {
            color: #7b7d77;
            font-size: 1.05rem;
            line-height: 1.45;
            text-align: center;
        }
        [class*="st-key-library-entry-"] {
            padding: 0.48rem 0;
            border-bottom: 1px solid rgb(111 113 107 / 14%);
        }
        [class*="st-key-library-entry-"]:last-child {
            border-bottom: 0;
        }
        .library-description {
            color: #3f403c;
            font-size: 0.94rem;
            line-height: 1.35;
        }
        .library-meta {
            margin-top: 0.16rem;
            color: #73746e;
            font-size: 0.78rem;
            letter-spacing: 0.05em;
            line-height: 1.25;
            text-transform: uppercase;
        }
        [class*="st-key-library_open_"] button {
            justify-content: flex-start;
            min-height: 1.35rem;
            padding: 0;
            border: 0;
            background: transparent;
            color: #22231f;
            box-shadow: none;
            font-size: 0.9rem;
            font-weight: 600;
            text-align: left;
            text-decoration: underline;
            text-decoration-color: #a9aba5;
            text-underline-offset: 0.18rem;
        }
        [class*="st-key-library_open_"] button:hover {
            border: 0;
            background: transparent;
            color: #111111;
            text-decoration-color: #4f514c;
        }
        @media (max-width: 760px) {
            [class*="st-key-browse-toolbar"],
            [class*="st-key-mode-toolbar-"] {
                max-width: 100%;
                margin-bottom: 0.5rem;
                padding-right: 0;
                padding-left: 0;
            }
            [class*="st-key-browse-filter-row"],
            [class*="st-key-today-filter-row"],
            [class*="st-key-pathway-filter-row"] {
                max-width: 100%;
            }
            [class*="st-key-browse-filter-row"] > [data-testid="stHorizontalBlock"],
            [class*="st-key-today-filter-row"] > [data-testid="stHorizontalBlock"],
            [class*="st-key-pathway-filter-row"] > [data-testid="stHorizontalBlock"],
            [data-testid="stHorizontalBlock"]:has([class*="st-key-library-level-links"]) {
                flex-direction: column !important;
                gap: 0.55rem !important;
            }
            [class*="st-key-browse-filter-row"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"],
            [class*="st-key-today-filter-row"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"],
            [class*="st-key-pathway-filter-row"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"],
            [data-testid="stHorizontalBlock"]:has([class*="st-key-library-level-links"]) > [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 0 !important;
                flex: 1 1 auto !important;
            }
            [class*="st-key-browse-filter-row"] [data-testid="stTextInputRootElement"],
            [class*="st-key-today-filter-row"] [data-testid="stTextInputRootElement"],
            [class*="st-key-pathway-filter-row"] [data-testid="stTextInputRootElement"],
            [class*="st-key-philosophy_profile_filters"] [data-testid="stMultiSelect"] .react-aria-ComboBox > div[role="group"] {
                min-height: 2.5rem;
            }
            [class*="st-key-library-level-links"] {
                justify-content: flex-start;
                overflow-x: auto;
            }
            [class*="st-key-card-grid-row-"] > [data-testid="stHorizontalBlock"],
            [class*="st-key-philosophy-grid-row-"] > [data-testid="stHorizontalBlock"] {
                display: grid !important;
                grid-template-columns: minmax(0, 1fr);
                gap: 0.95rem !important;
            }
            [class*="st-key-card-grid-row-"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(1),
            [class*="st-key-card-grid-row-"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(3),
            [class*="st-key-card-grid-row-"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(5),
            [class*="st-key-philosophy-grid-row-"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(1),
            [class*="st-key-philosophy-grid-row-"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(3),
            [class*="st-key-philosophy-grid-row-"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(5) {
                display: none !important;
            }
            [class*="st-key-card-grid-row-"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(2),
            [class*="st-key-card-grid-row-"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(4),
            [class*="st-key-philosophy-grid-row-"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(2),
            [class*="st-key-philosophy-grid-row-"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(4) {
                width: 100% !important;
                min-width: 0 !important;
                grid-column: 1;
            }
            [class*="st-key-library-profile-grid"] > [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
                gap: 0.85rem !important;
            }
            [class*="st-key-library-profile-grid"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 0 !important;
                flex: 1 1 auto !important;
            }
            [class*="st-key-pathway-selection"] > [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
                gap: 0 !important;
            }
            [class*="st-key-pathway-selection"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 0 !important;
                flex: 1 1 auto !important;
            }
            [class*="st-key-pathway-selection"] [class*="st-key-pathway-card-mezzo"],
            [class*="st-key-pathway-selection"] [class*="st-key-pathway-card-micro"],
            [class*="st-key-pathway-selection"] [class*="st-key-pathway-card-session"] {
                border-top: 1px solid #dedfd9;
                border-left: 0;
                padding-top: 0.7rem;
                padding-left: 0.5rem;
            }
            [class*="st-key-pathway-selection"] [class*="st-key-pathway-card-"] {
                min-height: 6.5rem;
            }
            [class*="st-key-browse-scope-links"] [class*="st-key-browse-scope-"] button,
            [class*="st-key-library-level-links"] [class*="st-key-library-level-"] button,
            [class*="st-key-library-group-toggle-"] button,
            [class*="st-key-open_"] button,
            [class*="st-key-select_"] button,
            [class*="st-key-pathway_open_"] button,
            [class*="st-key-pathway_change_"] button,
            [class*="st-key-clear_pathway"] button,
            [class*="st-key-pagination_"] button,
            [class*="st-key-philosophy_show_cards_"] button,
            [class*="st-key-philosophy_read_"] button,
            [class*="st-key-philosophy_sources_"] button,
            [class*="st-key-library_open_"] button {
                min-height: 2.5rem !important;
                padding-top: 0.5rem !important;
                padding-bottom: 0.5rem !important;
            }
            section[role="dialog"] {
                width: calc(100vw - 1rem) !important;
                max-width: calc(100vw - 1rem) !important;
            }
            section[role="dialog"] > div,
            [data-testid="stDialog"] section[role="dialog"] > div {
                max-height: calc(100dvh - 1rem);
                overflow-y: auto;
                padding-right: 0.55rem !important;
                padding-left: 0.55rem !important;
            }
            [class*="st-key-card-"][class*="library_preview_dialog"] {
                max-width: 100%;
                min-height: 0;
            }
            [class*="st-key-library-profile-grid"] {
                max-width: 100%;
            }
            [class*="st-key-browse-filter-row"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"],
            [class*="st-key-today-filter-row"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"],
            [class*="st-key-pathway-filter-row"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"],
            [data-testid="stHorizontalBlock"]:has([class*="st-key-library-level-links"]) {
                flex-direction: column !important;
                gap: 0.55rem !important;
            }
            [class*="st-key-browse-filter-row"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"],
            [class*="st-key-today-filter-row"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"],
            [class*="st-key-pathway-filter-row"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 0 !important;
                flex: 1 1 auto !important;
            }
            [class*="st-key-card-grid-row-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"],
            [class*="st-key-philosophy-grid-row-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
                display: grid !important;
                grid-template-columns: minmax(0, 1fr) !important;
                gap: 0.95rem !important;
            }
            [class*="st-key-card-grid-row-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(1),
            [class*="st-key-card-grid-row-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(3),
            [class*="st-key-card-grid-row-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(5),
            [class*="st-key-philosophy-grid-row-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(1),
            [class*="st-key-philosophy-grid-row-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(3),
            [class*="st-key-philosophy-grid-row-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(5) {
                display: none !important;
            }
            [class*="st-key-card-grid-row-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(2),
            [class*="st-key-card-grid-row-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(4),
            [class*="st-key-philosophy-grid-row-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(2),
            [class*="st-key-philosophy-grid-row-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(4) {
                width: 100% !important;
                min-width: 0 !important;
                grid-column: 1;
            }
            [class*="st-key-library-profile-grid"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
                gap: 0.85rem !important;
            }
            [class*="st-key-library-profile-grid"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 0 !important;
                flex: 1 1 auto !important;
            }
            [class*="st-key-pathway-selection"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
                gap: 0 !important;
            }
            [class*="st-key-pathway-selection"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 0 !important;
                flex: 1 1 auto !important;
            }
            [class*="st-key-library-expanded-"] [data-testid="stHorizontalBlock"]:has(.library-table-heading) {
                display: none !important;
            }
            [class*="st-key-library-entry-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
                gap: 0.2rem !important;
            }
            [class*="st-key-library-entry-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 0 !important;
                flex: 1 1 auto !important;
            }
            [class*="st-key-philosophy-actions-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
                display: grid !important;
                grid-template-columns: minmax(0, 1fr) !important;
                gap: 0.15rem !important;
            }
            [class*="st-key-philosophy-actions-"] > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 0 !important;
                grid-column: 1;
            }
            [class*="st-key-card-"] {
                height: auto !important;
                max-height: none !important;
                overflow: visible !important;
            }
            [class*="st-key-card-"] > [data-testid="stLayoutWrapper"] {
                height: auto !important;
                max-height: none !important;
                overflow: visible !important;
            }
            [data-testid="stLayoutWrapper"]:has(> [class*="st-key-card-"]) {
                height: auto !important;
                max-height: none !important;
                overflow: visible !important;
            }
            [class*="st-key-library-group-"]:not([class*="st-key-library-group-toggle-"]) {
                width: 100%;
            }
            .pagination-status {
                justify-content: center;
                margin-bottom: 0.15rem;
                text-align: center;
            }
            .pagination-page {
                line-height: 1.4;
            }
            .author-footer {
                align-items: flex-start;
                flex-wrap: wrap;
                gap: 0.5rem 0.8rem;
            }
        }
        </style>
        """
    )
