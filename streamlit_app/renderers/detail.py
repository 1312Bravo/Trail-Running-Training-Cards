from __future__ import annotations

from dataclasses import asdict, fields as dataclass_fields, is_dataclass
from html import escape
from typing import Any

import streamlit as st

from training_cards.philosophy_profiles import philosophy_profile_display_name
from streamlit_app.config import DETAIL_SECTION_ORDER

from .shared import (
    as_text,
    display_label_text,
    display_text,
    field_label,
    format_field_value,
    preview_card_meta_text,
    preview_card_pips_html,
    render_card_history_back,
    render_preview_tag_labels,
)


DETAIL_HIDDEN_FIELDS = {"id", "slug", "title", "card_type"}
DETAIL_KEY_FACT_FIELDS = {
    "suitable_levels",
    "recommended_duration_weeks",
    "recommended_duration_days",
    "typical_duration",
    "philosophy_profile_ids",
}


# ----------------------------------------------------------
# Detail View
# ----------------------------------------------------------

def render_reference_list(card: Any, card_by_id: dict[str, Any], is_last_section: bool = False) -> None:
    if not card.references:
        return

    last_section_class = " detail-section-last" if is_last_section else ""
    st.html(
        f'<section class="detail-section detail-section-references{last_section_class}">'
        '<div class="detail-section-label">References</div>'
        '</section>'
    )
    with st.container(
        horizontal=True,
        key=f"detail-references{'-last' if is_last_section else ''}-{card.id}",
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


def render_workout_blocks(blocks: list[Any], is_last_section: bool = False) -> None:
    if not blocks:
        return

    rendered_blocks = []
    for block in blocks:
        rendered_options = []
        for option in block.options:
            option_notes = []
            if option.repeat:
                option_notes.append(f"Repeat: {option.repeat}")
            if option.selection_notes:
                option_notes.append(f"Best for: {option.selection_notes}")
            if option.load_notes:
                option_notes.append(f"Load: {option.load_notes}")

            rendered_parts = []
            for part in option.parts:
                meta_items = []
                if part.duration:
                    meta_items.append(part.duration)
                if part.rpe:
                    rpe = as_text(part.rpe)
                    meta_items.append(rpe if rpe.upper().startswith("RPE") else f"RPE {rpe}")

                lines = []
                if meta_items:
                    lines.append(
                        f'<p class="detail-workout-part-meta">{escape(" | ".join(meta_items))}</p>'
                    )
                if part.prescription:
                    lines.append(f'<p class="detail-workout-part-line">{escape(part.prescription)}</p>')
                if part.selection_notes:
                    lines.append(
                        '<p class="detail-workout-part-line">'
                        f'Best for: {escape(part.selection_notes)}'
                        '</p>'
                    )
                if part.coaching_notes:
                    lines.append(
                        '<p class="detail-workout-part-line">'
                        f'Coach: {escape(part.coaching_notes)}'
                        '</p>'
                    )
                if part.terrain_notes:
                    lines.append(
                        '<p class="detail-workout-part-line detail-workout-part-terrain">'
                        f'Terrain: {escape(part.terrain_notes)}'
                        '</p>'
                    )
                if part.adjustment_notes:
                    lines.append(
                        '<p class="detail-workout-part-line">'
                        f'Adjust: {escape(part.adjustment_notes)}'
                        '</p>'
                    )
                rendered_parts.append(
                    '<div class="detail-workout-part">'
                    f'<p class="detail-workout-part-title">{escape(part.title)}</p>'
                    f'{"".join(lines)}'
                    '</div>'
                )

            rendered_option_notes = (
                '<ul class="detail-workout-option-notes">'
                + "".join(f'<li>{escape(note)}</li>' for note in option_notes)
                + "</ul>"
                if option_notes
                else ""
            )
            rendered_options.append(
                '<div class="detail-workout-option">'
                f'<p class="detail-workout-option-title">{escape(option.title)}</p>'
                f'{rendered_option_notes}'
                f'<div class="detail-workout-parts">{"".join(rendered_parts)}</div>'
                '</div>'
            )

        rendered_blocks.append(
            '<div class="detail-workout-block">'
            f'<p class="detail-workout-block-title">{escape(display_label_text(block.block_type))}</p>'
            f'<p class="detail-workout-block-mode">{escape(display_label_text(block.execution_mode))}</p>'
            f'{"".join(rendered_options)}'
            '</div>'
        )

    last_section_class = " detail-section-last" if is_last_section else ""
    st.html(
        f'<section class="detail-section detail-section-workout-parts{last_section_class}">'
        '<div class="detail-section-label">Workout Guide</div>'
        f'<div class="detail-workout-blocks">{"".join(rendered_blocks)}</div>'
        '</section>'
    )


def render_dataclass_value(
    field_name: str,
    value: Any,
    display_config: dict[str, Any],
    is_last_section: bool = False,
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
    last_section_class = " detail-section-last" if is_last_section else ""
    st.html(
        f'<section class="detail-section detail-section-session-family{last_section_class}">'
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
    is_last_section: bool = False,
) -> None:
    if value is None:
        return
    if isinstance(value, str) and not value.strip():
        return
    if isinstance(value, list) and not value:
        return
    if render_dataclass_value(field_name, value, display_config, is_last_section=is_last_section):
        return

    label = field_label(field_name, display_config)
    section_class = "detail-section"
    if field_name == "summary":
        section_class += " detail-section-summary"
    elif field_name == "additional_information":
        section_class += " detail-section-coaching-note"
    elif field_name == "tags":
        section_class += " detail-section-tags"
    if is_last_section:
        section_class += " detail-section-last"

    if field_name == "tags" and isinstance(value, list):
        st.html(
            f'<section class="{section_class}">'
            f'<div class="detail-section-label">{escape(label)}</div>'
            '</section>'
        )
        tag_key_prefix = f"detail-last_{key_prefix}" if is_last_section else key_prefix
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
        promoted = [field for field in ["session_family", "workout_blocks"] if field in ordered]
        ordered = [field for field in ordered if field not in promoted]
        insert_at = ordered.index("purpose") + 1 if "purpose" in ordered else 0
        ordered[insert_at:insert_at] = promoted
    return ordered


def render_detail_header(card: Any, display_config: dict[str, Any]) -> None:
    card_type_key = str(card.card_type).replace("_", "-")

    st.html(
        f'<section class="detail-card-header detail-card-header-{card_type_key}">'
        '<div class="detail-card-title-row">'
        f'<h2 class="detail-card-title">{escape(card.title)}</h2>'
        f'{preview_card_pips_html(card_type_key)}'
        '</div>'
        f'<div class="detail-card-type">{escape(preview_card_meta_text(card, display_config))}</div>'
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
            is_last_section = index == len(fields_to_render) - 1
            value = getattr(card, field_name)
            if field_name == "workout_blocks":
                render_workout_blocks(value, is_last_section=is_last_section)
            elif field_name == "references":
                render_reference_list(card, card_by_id, is_last_section=is_last_section)
            else:
                render_field(
                    field_name,
                    value,
                    display_config,
                    f"detail_{card.id}",
                    is_last_section=is_last_section,
                )
