from __future__ import annotations
from dataclasses import asdict
from typing import Any

from training_cards.schemas import (
    BaseTrainingCard,
    CardReference,
    CardRelationship,
    CardType,
    MacroCard,
    MezzoCard,
    MicroCard,
    SessionCard,
    SessionFamily,
    SessionPart,
    TrainingLevel,
    WorkoutBlock,
    WorkoutBlockExecutionMode,
    WorkoutBlockType,
    WorkoutOption,
)
from training_cards.session_families import get_session_family

CARD_CLASS_BY_TYPE = {
    CardType.MACRO: MacroCard,
    CardType.MEZZO: MezzoCard,
    CardType.MICRO: MicroCard,
    CardType.SESSION: SessionCard,
}

# Convert a validated card object into plain JSON-safe data.
def card_to_dict(card: BaseTrainingCard) -> dict[str, Any]:
    data = asdict(card)

    data["card_type"] = str(card.card_type)
    data["suitable_levels"] = [str(level) for level in card.suitable_levels]
    data["references"] = [
        {
            "card_id": reference.card_id,
            "relationship": str(reference.relationship),
            "tags": reference.tags,
        }
        for reference in card.references
    ]
    if isinstance(card, SessionCard):
        data["workout_blocks"] = [
            {
                "block_type": str(block.block_type),
                "execution_mode": str(block.execution_mode),
                "options": [
                    {
                        "title": option.title,
                        "repeat": option.repeat,
                        "selection_notes": option.selection_notes,
                        "load_notes": option.load_notes,
                        "parts": [
                            {
                                "title": part.title,
                                "prescription": part.prescription,
                                "duration": part.duration,
                                "rpe": part.rpe,
                                "selection_notes": part.selection_notes,
                                "coaching_notes": part.coaching_notes,
                                "terrain_notes": part.terrain_notes,
                                "adjustment_notes": part.adjustment_notes,
                            }
                            for part in option.parts
                        ],
                    }
                    for option in block.options
                ],
            }
            for block in card.workout_blocks
        ]
    return data

# Convert JSON data back into the correct card dataclass.
def card_from_dict(data: dict[str, Any]) -> BaseTrainingCard:
    card_data = dict(data)
    card_type = CardType(card_data["card_type"])

    card_data.setdefault("slug", card_data["id"].replace("_", "-"))
    card_data["card_type"] = card_type
    card_data["suitable_levels"] = [TrainingLevel(level) for level in card_data["suitable_levels"]]

    legacy_goal_context = card_data.pop("when_to_choose", [])
    legacy_training_profile = card_data.pop("training_characteristics", [])
    legacy_terrain_demands = card_data.pop("terrain_demands", [])
    legacy_watchouts = card_data.pop("when_not_to_choose", [])
    legacy_common_mistakes = card_data.pop("common_mistakes", [])
    legacy_warning_signs = card_data.pop("warning_signs", [])
    legacy_description = card_data.pop("detailed_description", "")

    if not card_data.get("additional_information"):
        card_data["additional_information"] = legacy_description
    elif legacy_description:
        card_data["additional_information"] = (
            card_data["additional_information"].rstrip()
            + "\n\n"
            + legacy_description.lstrip()
        )

    card_data["goal_race_context"] = list(card_data.get("goal_race_context", [])) + list(legacy_goal_context)
    card_data["training_profile"] = list(card_data.get("training_profile", [])) + list(legacy_training_profile) + list(legacy_terrain_demands)
    card_data["watchouts"] = (
        list(card_data.get("watchouts", []))
        + list(legacy_watchouts)
        + list(legacy_common_mistakes)
        + list(legacy_warning_signs)
    )
    card_data["references"] = [
        CardReference(
            card_id = reference["card_id"],
            relationship = CardRelationship(reference["relationship"]),
            tags = reference.get("tags", []),
        )
        for reference in card_data.get("references", [])
    ]
    if card_type == CardType.SESSION:
        legacy_intensity_guidance = card_data.pop("intensity_guidance", [])
        legacy_execution_notes = card_data.pop("execution_notes", [])
        legacy_recovery_requirements = card_data.pop("recovery_requirements", [])
        session_family = card_data.get("session_family")
        if isinstance(session_family, str):
            card_data["session_family"] = get_session_family(session_family)
        elif isinstance(session_family, dict):
            card_data["session_family"] = SessionFamily(**session_family)
        card_data["workout_blocks"] = _workout_blocks_from_data(
            card_data.get("workout_blocks", []),
        )
        session_notes = []
        if legacy_intensity_guidance:
            session_notes.append("Intensity guidance: " + "; ".join(legacy_intensity_guidance))
        if legacy_execution_notes:
            session_notes.append("Execution notes: " + "; ".join(legacy_execution_notes))
        if legacy_recovery_requirements:
            session_notes.append("Recovery requirements: " + "; ".join(legacy_recovery_requirements))
        if session_notes:
            card_data["additional_information"] = (
                (card_data.get("additional_information", "").rstrip() + "\n\n" if card_data.get("additional_information") else "")
                + "\n".join(session_notes)
            )
    else:
        card_data.pop("workout_blocks", None)

    card_class = CARD_CLASS_BY_TYPE[card_type]

    return card_class(**card_data)


def _workout_blocks_from_data(workout_blocks: list[dict[str, Any]]) -> list[WorkoutBlock]:
    return [
        WorkoutBlock(
            block_type=WorkoutBlockType(block["block_type"]),
            execution_mode=WorkoutBlockExecutionMode(
                block.get("execution_mode", WorkoutBlockExecutionMode.DO_ALL)
            ),
            options=[
                WorkoutOption(
                    title=option["title"],
                    repeat=option.get("repeat", ""),
                    selection_notes=option.get("selection_notes", ""),
                    load_notes=option.get("load_notes", ""),
                    parts=[
                        SessionPart(
                            title=part["title"],
                            prescription=part.get("prescription", ""),
                            duration=part.get("duration", ""),
                            rpe=part.get("rpe", ""),
                            selection_notes=part.get("selection_notes", ""),
                            coaching_notes=part.get("coaching_notes", ""),
                            terrain_notes=part.get("terrain_notes", ""),
                            adjustment_notes=part.get("adjustment_notes", ""),
                        )
                        for part in option.get("parts", [])
                    ],
                )
                for option in block.get("options", [])
            ],
        )
        for block in workout_blocks
    ]

