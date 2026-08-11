from __future__ import annotations

from dataclasses import asdict, is_dataclass
from html import escape
from typing import Any

import streamlit as st

from streamlit_app.config import DETAIL_SKIP_FIELDS, PREVIEW_FIELDS
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
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(182, 194, 167, 0.22), transparent 28%),
                radial-gradient(circle at top right, rgba(210, 158, 108, 0.16), transparent 24%),
                linear-gradient(180deg, #f6f3ec 0%, #f2ede4 46%, #ece5d8 100%);
            color: #1f2a24;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1300px;
        }
        .hero {
            background: linear-gradient(135deg, rgba(28, 46, 37, 0.96), rgba(49, 71, 59, 0.92));
            color: #f7f2e8;
            border-radius: 28px;
            padding: 2rem 2rem 1.5rem 2rem;
            box-shadow: 0 18px 45px rgba(30, 40, 34, 0.18);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        .hero h1 {
            margin: 0;
            font-size: 2.5rem;
            line-height: 1.05;
        }
        .hero p {
            margin-bottom: 0;
            color: rgba(247, 242, 232, 0.88);
            font-size: 1.02rem;
        }
        .section-label {
            font-size: 0.75rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: rgba(31, 42, 36, 0.65);
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        .card-shell {
            background: rgba(255, 255, 255, 0.78);
            border: 1px solid rgba(65, 82, 70, 0.14);
            border-radius: 22px;
            padding: 1rem 1rem 0.85rem 1rem;
            box-shadow: 0 10px 25px rgba(50, 57, 49, 0.08);
            height: 100%;
        }
        .card-title {
            margin: 0 0 0.15rem 0;
            font-size: 1.05rem;
            color: #16221d;
            font-weight: 700;
        }
        .card-subtitle {
            margin: 0 0 0.5rem 0;
            color: rgba(22, 34, 29, 0.72);
            font-size: 0.88rem;
        }
        .summary {
            font-size: 0.95rem;
            line-height: 1.5;
            color: #24332c;
            margin-bottom: 0.8rem;
        }
        .pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.35rem;
            margin: 0.45rem 0 0.7rem 0;
        }
        .pill {
            display: inline-block;
            border-radius: 999px;
            padding: 0.24rem 0.7rem;
            font-size: 0.76rem;
            font-weight: 700;
            line-height: 1.2;
            border: 1px solid transparent;
            white-space: nowrap;
        }
        .pill-type {
            background: rgba(42, 65, 52, 0.1);
            color: #264435;
            border-color: rgba(42, 65, 52, 0.16);
        }
        .pill-level {
            background: rgba(211, 161, 102, 0.16);
            color: #7b4f20;
            border-color: rgba(211, 161, 102, 0.2);
        }
        .pill-tag {
            background: rgba(78, 108, 89, 0.12);
            color: #355545;
            border-color: rgba(78, 108, 89, 0.16);
        }
        .detail-hero {
            background: rgba(255, 255, 255, 0.82);
            border-radius: 26px;
            border: 1px solid rgba(65, 82, 70, 0.14);
            padding: 1.25rem 1.3rem;
            box-shadow: 0 10px 25px rgba(50, 57, 49, 0.07);
        }
        .detail-callout {
            background: linear-gradient(135deg, rgba(36, 58, 47, 0.95), rgba(53, 82, 65, 0.92));
            color: #f7f2e8;
            border-radius: 20px;
            padding: 1rem 1.05rem;
            margin: 0.75rem 0 1rem 0;
        }
        .detail-callout .label {
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            opacity: 0.72;
            margin-bottom: 0.25rem;
            font-weight: 700;
        }
        .detail-callout .value {
            font-size: 1rem;
            line-height: 1.55;
        }
        .field-label {
            font-size: 0.76rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: rgba(31, 42, 36, 0.65);
            font-weight: 700;
            margin-bottom: 0.3rem;
        }
        .field-box {
            background: rgba(255, 255, 255, 0.72);
            border: 1px solid rgba(65, 82, 70, 0.11);
            border-radius: 18px;
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
            color: rgba(31, 42, 36, 0.68);
            font-size: 0.9rem;
        }
        .stButton > button {
            border-radius: 999px;
            border: 1px solid rgba(36, 58, 47, 0.22);
            background: linear-gradient(135deg, #274233, #355845);
            color: white;
            font-weight: 700;
            padding: 0.45rem 1rem;
        }
        .stButton > button:hover {
            border-color: rgba(36, 58, 47, 0.34);
            background: linear-gradient(135deg, #1f3529, #2d4a3a);
            color: white;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border-bottom: 1px solid rgba(65, 82, 70, 0.12);
            padding: 0.55rem 0.45rem;
            vertical-align: top;
        }
        th {
            text-align: left;
            color: rgba(31, 42, 36, 0.72);
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
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
        f'<span class="pill {class_name}">{escape(as_text(value).replace("_", " ").title())}</span>'
        for value in values
    )
    return f'<div class="pill-row">{chips}</div>'


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
    with st.container():
        st.markdown(
            f"""
            <div class="card-shell">
                <div class="card-title">{escape(card.title)}</div>
                <div class="card-subtitle">{escape(card.slug)}</div>
                {chip_html([card_type_label(card.card_type, display_config)], "pill-type")}
                <div class="summary">{escape(card.summary)}</div>
                {chip_html(card.suitable_levels, "pill-level")}
                {chip_html(card.tags, "pill-tag")}
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button(
            "Open card",
            key=f"open_{key_prefix}_{card.id}",
            use_container_width=True,
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
    preview_fields = set(PREVIEW_FIELDS)

    st.markdown('<div class="detail-hero">', unsafe_allow_html=True)
    header_cols = st.columns([3, 1])
    with header_cols[0]:
        st.markdown(f"## {card.title}")
        st.caption(f"{card.card_type} card | {card.slug}")
    with header_cols[1]:
        if st.button("Clear selection", use_container_width=True):
            st.session_state.active_card_id = None

    st.markdown(
        f"""
        <div class="detail-callout">
            <div class="label">Preview sentence</div>
            <div class="value">{escape(card.summary)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    quick_cols = st.columns(3)
    with quick_cols[0]:
        st.metric("Planning level", card_type_label(card.card_type, display_config))
    with quick_cols[1]:
        st.metric("Suitable for", ", ".join(str(level) for level in card.suitable_levels))
    with quick_cols[2]:
        st.metric("Tags", str(len(card.tags)))

    st.markdown(chip_html(card.suitable_levels, "pill-level"), unsafe_allow_html=True)
    st.markdown(chip_html(card.tags, "pill-tag"), unsafe_allow_html=True)

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

    st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------------------------------------
# Grid Layout
# ----------------------------------------------------------
# Card grids stay two-up for readable scanning on desktop while still working
# comfortably on narrower screens.

def render_grid(cards: list[Any], display_config: dict[str, Any], key_prefix: str) -> None:
    cols = st.columns(2)
    for index, card in enumerate(cards):
        with cols[index % 2]:
            render_preview_card(card, display_config, key_prefix)
