from __future__ import annotations

from dataclasses import asdict, is_dataclass
from html import escape
from typing import Any

import streamlit as st

from streamlit_app.config import DETAIL_SKIP_FIELDS
from streamlit_app.data import card_type_label


# ----------------------------------------------------------
# Page Styling
# ----------------------------------------------------------
# The CSS is intentionally local to the Streamlit app package so the training
# card library itself stays presentation-agnostic.

def css() -> None:
    st.markdown(
        """
        <style>
        header[data-testid="stHeader"],
        div[data-testid="stToolbar"],
        div[data-testid="stDecoration"] {
            background: #ffffff !important;
        }
        .stApp {
            background: #f6f6f6;
            color: #5a5a5a;
        }
        .block-container {
            padding-top: 2.4rem;
            padding-bottom: 1.2rem;
            max-width: 1180px;
        }
        .app-heading {
            margin-bottom: 1.1rem;
        }
        .contact-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.95rem;
            margin: 2rem 0 0.4rem 0;
            padding-top: 1rem;
            border-top: 1px solid #dedede;
            color: #686868;
            font-size: 0.86rem;
        }
        .contact-link {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            color: #5f5f5f !important;
            text-decoration: none !important;
        }
        .contact-link:hover {
            color: #333333 !important;
            text-decoration: underline !important;
            text-underline-offset: 0.2em;
        }
        .contact-icon {
            width: 15px;
            height: 15px;
            color: #666666;
        }
        .page-title {
            margin: 0 0 0.2rem 0;
            font-size: 1.65rem;
            line-height: 1.1;
            font-weight: 500;
            color: #5a5a5a;
        }
        .count-line {
            margin: 0 0 0.85rem 0;
            color: #777777;
            font-size: 0.84rem;
            line-height: 1.4;
        }
        .card-title {
            margin: 0 0 0.15rem 0;
            font-size: 1rem;
            color: #444444;
            font-weight: 600;
        }
        .card-type-line {
            margin: 0 0 0.55rem 0;
            font-size: 0.75rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #777777;
            font-weight: 600;
        }
        .summary {
            font-size: 0.92rem;
            line-height: 1.45;
            color: #4b4b4b;
            margin-bottom: 0.8rem;
        }
        .preview-meta {
            margin: 0.2rem 0 0.6rem 0;
            color: #555555;
            font-size: 0.83rem;
            line-height: 1.35;
        }
        .preview-meta-row {
            margin-bottom: 0.25rem;
        }
        .preview-meta-label {
            color: #777777;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            font-size: 0.7rem;
            font-weight: 600;
            margin-right: 0.35rem;
        }
        .preview-tags {
            margin-top: 0.4rem;
        }
        .preview-tags-title {
            font-size: 0.7rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #777777;
            font-weight: 600;
            margin-bottom: 0.35rem;
        }
        .pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.35rem;
            margin: 0.25rem 0 0.9rem 0;
        }
        .pill {
            display: inline-block;
            border-radius: 999px;
            padding: 0.24rem 0.7rem;
            font-size: 0.72rem;
            font-weight: 600;
            line-height: 1.2;
            border: 1px solid #cfcfcf;
            white-space: nowrap;
            background: #f7f7f7;
            color: #555555;
        }
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: #ffffff;
            border: 1px solid #c9c9c9 !important;
            border-radius: 8px !important;
            box-shadow: 0 1px 0 rgba(0, 0, 0, 0.03);
        }
        .field-label {
            font-size: 0.72rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #777777;
            font-weight: 600;
            margin-bottom: 0.3rem;
        }
        .field-box {
            background: #ffffff;
            border: 1px solid #dddddd;
            border-radius: 12px;
            padding: 0.9rem 1rem;
            margin-bottom: 0.9rem;
        }
        .field-box ul {
            margin-top: 0.3rem;
            margin-bottom: 0;
        }
        .field-box li {
            margin-bottom: 0.28rem;
        }
        .small-note {
            color: #666666;
            font-size: 0.9rem;
        }
        .stButton > button {
            border-radius: 0;
            border: none;
            background: transparent;
            color: #666666;
            font-weight: 500;
            padding: 0;
            font-size: 0.85rem;
            text-decoration: underline;
            text-underline-offset: 0.18em;
            width: auto;
        }
        .stButton > button:hover {
            border: none;
            background: transparent;
            color: #444444;
        }
        .stButton[data-testid="stButton"] {
            margin-bottom: 0.1rem;
        }
        .stTextInput input,
        div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            border: 1px solid #2f2f2f !important;
            border-radius: 8px !important;
            box-shadow: none !important;
            min-height: 3rem;
        }
        div[data-testid="stSelectbox"] div[data-baseweb="select"],
        div[data-testid="stSelectbox"] div[data-baseweb="select"] * {
            background-color: #ffffff !important;
            color: #666666 !important;
        }
        div[data-testid="stSelectbox"] svg {
            fill: #666666 !important;
            color: #666666 !important;
        }
        .stTextInput input {
            color: #666666 !important;
            border: 1px solid #2f2f2f !important;
            border-radius: 8px !important;
        }
        .stTextInput input::placeholder {
            color: #9a9a9a !important;
        }
        label,
        .stTextInput label,
        .stSelectbox label,
        div[data-testid="stWidgetLabel"] {
            color: #777777 !important;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border-bottom: 1px solid #e5e5e5;
            padding: 0.55rem 0.45rem;
            vertical-align: top;
        }
        th {
            text-align: left;
            color: #666666;
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }
        div[data-testid="stDialog"] div[role="dialog"] {
            width: min(94vw, 1120px) !important;
            max-width: min(94vw, 1120px) !important;
        }
        div[data-testid="stDialog"] div[role="dialog"] > div {
            max-height: 88vh;
            overflow-y: auto;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ----------------------------------------------------------
# Shared Formatting
# ----------------------------------------------------------
# These helpers convert schema values into safe text and small visual chips.

def as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return str(value)


def chip_html(values: list[Any], class_name: str) -> str:
    if not values:
        return ""
    chips = "".join(
        f'<span class="pill {class_name}">{escape(as_text(value))}</span>'
        for value in values
    )
    return f'<div class="pill-row">{chips}</div>'


def render_contact_footer() -> None:
    st.markdown(
        """
        <div class="contact-row">
            <a class="contact-link" href="mailto:pecek.urh@gmail.com">
                <svg class="contact-icon" viewBox="0 0 24 24" aria-hidden="true">
                    <path fill="currentColor" d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm-.4 4.25-7.07 4.42a1 1 0 0 1-1.06 0L4.4 8.25 5.46 6.55 12 10.64l6.54-4.09 1.06 1.7Z"/>
                </svg>
                <span>pecek.urh@gmail.com</span>
            </a>
            <a class="contact-link" href="https://github.com/1312Bravo/Trail-Running-Training-Cards" target="_blank">
                <svg class="contact-icon" viewBox="0 0 24 24" aria-hidden="true">
                    <path fill="currentColor" d="M12 .5A12 12 0 0 0 8.2 23.9c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.5-1.3-1.3-1.7-1.3-1.7-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.6.1-3.2 0 0 1-.3 3.3 1.2a11.3 11.3 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.6.2 2.9.1 3.2.8.9 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.1c0 .3.2.7.8.6A12 12 0 0 0 12 .5Z"/>
                </svg>
                <span>GitHub</span>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def format_scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if hasattr(value, "value"):
        return as_text(getattr(value, "value"))
    return as_text(value)


# ----------------------------------------------------------
# Preview Cards
# ----------------------------------------------------------
# The preview card is intentionally compact so the browser can scan quickly.

def render_preview_card(card: Any, display_config: dict[str, Any], key_prefix: str) -> None:
    field_labels = display_config.get("field_labels", {})
    preview_fields = display_config.get("preview_fields", [])

    with st.container(border=True):
        st.markdown(f'<div class="card-title">{escape(card.title)}</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="card-type-line">{escape(card_type_label(card.card_type, display_config))}</div>',
            unsafe_allow_html=True,
        )
        for field in preview_fields:
            if field in {"title", "card_type"}:
                continue
            value = getattr(card, field, None)
            if field == "summary" and value:
                st.markdown(f'<div class="summary">{escape(value)}</div>', unsafe_allow_html=True)
                continue
            if field == "purpose" and value:
                st.markdown(
                    f"""
                    <div class="preview-meta">
                        <div class="preview-meta-row"><span class="preview-meta-label">Purpose</span>{escape(value)}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                continue
            if field == "suitable_levels" and value:
                st.markdown(
                    f"""
                    <div class="preview-meta">
                        <div class="preview-meta-row"><span class="preview-meta-label">{escape(field_labels.get(field, "Suitable for"))}</span>{escape(", ".join(str(level) for level in value))}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                continue
            if field == "tags" and value:
                st.markdown(
                    f"""
                    <div class="preview-tags">
                        <div class="preview-tags-title">{escape(field_labels.get(field, "Tags"))}</div>
                        {chip_html(value, "pill-tag")}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                continue

        open_cols = st.columns([10, 2])
        with open_cols[1]:
            st.button(
                "Open card",
                key=f"open_{key_prefix}_{card.id}",
                use_container_width=False,
                on_click=lambda card_id=card.id: st.session_state.__setitem__("active_card_id", card_id),
            )


# ----------------------------------------------------------
# Detail View
# ----------------------------------------------------------
# The detail renderer exposes the full coaching context behind the preview.

def render_list(values: list[Any]) -> str:
    items = "".join(f"<li>{escape(format_scalar(item))}</li>" for item in values)
    return f"<ul>{items}</ul>"


def render_reference_list(card: Any, card_by_id: dict[str, Any]) -> str:
    if not card.references:
        return ""

    rows = []
    for reference in card.references:
        linked = card_by_id.get(reference.card_id)
        linked_title = escape(linked.title) if linked else escape(reference.card_id)
        relationship = escape(format_scalar(reference.relationship))
        tags = ", ".join(reference.tags) if reference.tags else ""
        tag_text = f" <span class='small-note'>({escape(tags)})</span>" if tags else ""
        rows.append(f"<li><strong>{relationship}</strong>: {linked_title}{tag_text}</li>")
    return f"<ul>{''.join(rows)}</ul>"


def render_workout_parts(parts: list[Any]) -> str:
    header = """
        <thead>
            <tr>
                <th>Part</th>
                <th>Duration</th>
                <th>RPE</th>
                <th>Instructions</th>
                <th>Terrain notes</th>
            </tr>
        </thead>
        <tbody>
    """
    body = ""
    for part in parts:
        body += f"""
            <tr>
                <td>{escape(part.name)}</td>
                <td>{escape(part.duration)}</td>
                <td>{escape(part.rpe)}</td>
                <td>{escape(part.instructions or "")}</td>
                <td>{escape(part.terrain_notes or "")}</td>
            </tr>
        """
    return f"""
    <div class="field-box">
        <div class="field-label">Workout guide</div>
        <table>
            {header}
            {body}
            </tbody>
        </table>
    </div>
    """


def render_dataclass_value(field_name: str, value: Any) -> bool:
    if field_name == "session_family" and is_dataclass(value):
        family = asdict(value)
        st.markdown(
            f"""
            <div class="field-box">
                <div class="field-label">Session family</div>
                <strong>{escape(family["title"])}</strong><br>
                <span class="small-note">{escape(family["summary"])}</span>
                {f"<p class='small-note'>{escape(family.get('description', ''))}</p>" if family.get("description") else ""}
                {chip_html(family.get("tags", []), "pill-tag")}
            </div>
            """,
            unsafe_allow_html=True,
        )
        return True
    return False


def render_field(field_name: str, label: str, value: Any) -> None:
    if value is None:
        return
    if isinstance(value, str) and not value.strip():
        return
    if isinstance(value, list) and not value:
        return
    if render_dataclass_value(field_name, value):
        return

    if isinstance(value, list):
        st.markdown(
            f"""
            <div class="field-box">
                <div class="field-label">{escape(label.replace("_", " ").title())}</div>
                {render_list(value)}
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    st.markdown(
        f"""
        <div class="field-box">
            <div class="field-label">{escape(label.replace("_", " ").title())}</div>
            <div>{escape(format_scalar(value))}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ----------------------------------------------------------
# Card Detail Composition
# ----------------------------------------------------------
# The full card view follows the display config's field order so the app stays
# aligned with the schema rather than hard-coding card layouts.

def render_detail(card: Any, display_config: dict[str, Any], card_by_id: dict[str, Any]) -> None:
    field_labels = display_config.get("field_labels", {})
    detail_order = display_config.get("detail_field_order", [])
    preview_fields = display_config.get("preview_fields", [])

    with st.container(border=True):
        header_cols = st.columns([5, 1])
        with header_cols[0]:
            st.markdown(f"### {card.title}")
            st.caption(f"{card.slug}")
        with header_cols[1]:
            if st.button("Close", use_container_width=True):
                st.session_state.active_card_id = None
                st.rerun()

        if card.purpose:
            st.markdown(
                f"""
                <div class="field-box">
                    <div class="field-label">Purpose</div>
                    <div>{escape(card.purpose)}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        for field in preview_fields:
            if field in DETAIL_SKIP_FIELDS:
                continue
            value = getattr(card, field, None)
            if field == "references":
                rendered = render_reference_list(card, card_by_id)
                if rendered:
                    st.markdown(
                        f"""
                        <div class="field-box">
                            <div class="field-label">{escape(field_labels.get(field, "Linked cards"))}</div>
                            {rendered}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                continue
            render_field(field, field_labels.get(field, field), value)

        for field in detail_order:
            if field in preview_fields or field in DETAIL_SKIP_FIELDS:
                continue
            value = getattr(card, field, None)
            if field == "workout_parts" and value:
                st.markdown(render_workout_parts(value), unsafe_allow_html=True)
                continue
            if field == "references":
                rendered = render_reference_list(card, card_by_id)
                if rendered:
                    st.markdown(
                        f"""
                        <div class="field-box">
                            <div class="field-label">{escape(field_labels.get(field, "Linked cards"))}</div>
                            {rendered}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                continue
            render_field(field, field_labels.get(field, field), value)


# ----------------------------------------------------------
# Grid Layout
# ----------------------------------------------------------
# Card grids stay two-up for readable scanning on desktop while still working
# comfortably on narrower screens.

def render_grid(cards: list[Any], display_config: dict[str, Any], key_prefix: str) -> None:
    cols = st.columns(2)
    for index, card in enumerate(cards):
        with cols[index % 2]:
            render_preview_card(card, display_config, f"{key_prefix}_{index}")
