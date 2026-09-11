from __future__ import annotations

import re
from dataclasses import dataclass

from training_cards.schemas import (
    CardReference,
    CardRelationship,
    CardType,
    SessionCard,
    SessionPart,
    TrainingLevel,
    WorkoutBlock,
    WorkoutBlockExecutionMode,
    WorkoutBlockType,
    WorkoutOption,
)
from training_cards.schemas.session_family import SessionFamily


@dataclass(frozen=True, slots=True)
class PhilosophySessionSpec:
    id: str
    title: str
    philosophy_profile_id: str
    session_family: SessionFamily
    parent_micro_ids: tuple[str, ...]
    typical_duration: str
    summary: str
    purpose: str
    tags: tuple[str, ...]
    training_profile: tuple[str, ...]
    expected_adaptations: tuple[str, ...]
    watchouts: tuple[str, ...]
    workout_blocks: tuple[WorkoutBlock, ...]
    progression_rules: tuple[str, ...] = ()
    regression_rules: tuple[str, ...] = ()
    additional_information: str = ""


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def part(
    title: str,
    prescription: str,
    duration: str = "",
    rpe: str = "",
    *,
    selection_notes: str = "",
    coaching_notes: str = "",
    terrain_notes: str = "",
    adjustment_notes: str = "",
) -> SessionPart:
    return SessionPart(
        title=title,
        prescription=prescription,
        duration=duration,
        rpe=rpe,
        selection_notes=selection_notes,
        coaching_notes=coaching_notes,
        terrain_notes=terrain_notes,
        adjustment_notes=adjustment_notes,
    )


def option(
    title: str,
    parts: list[SessionPart],
    *,
    repeat: str = "",
    selection_notes: str = "",
    load_notes: str = "",
) -> WorkoutOption:
    return WorkoutOption(
        title=title,
        repeat=repeat,
        selection_notes=selection_notes,
        load_notes=load_notes,
        parts=parts,
    )


def block(
    block_type: WorkoutBlockType,
    options: list[WorkoutOption],
    execution_mode: WorkoutBlockExecutionMode = WorkoutBlockExecutionMode.DO_ALL,
) -> WorkoutBlock:
    return WorkoutBlock(
        block_type=block_type,
        execution_mode=execution_mode,
        options=options,
    )


def choose_main(options: list[WorkoutOption]) -> WorkoutBlock:
    mode = (
        WorkoutBlockExecutionMode.CHOOSE_ONE
        if len(options) > 1
        else WorkoutBlockExecutionMode.DO_ALL
    )
    return block(WorkoutBlockType.MAIN, options, mode)


def running_warmup() -> WorkoutBlock:
    return block(
        WorkoutBlockType.WARMUP,
        [
            option(
                "Standard Running Warm-Up",
                [
                    part(
                        "Easy Running",
                        "Run easily until breathing, legs, and coordination feel settled.",
                        "10-20 minutes",
                        "2-4",
                    ),
                    part(
                        "Preparatory Pickups",
                        "Add 3-5 relaxed 15-20 second pickups only if the main set is faster than easy running.",
                        "3-6 minutes",
                        "5-7",
                        coaching_notes="These should prepare rhythm, not create fatigue.",
                    ),
                ],
            )
        ],
    )


def easy_cooldown() -> WorkoutBlock:
    return block(
        WorkoutBlockType.COOLDOWN,
        [
            option(
                "Easy Cooldown",
                [
                    part(
                        "Easy Running Or Walking",
                        "Move very easily until breathing and legs settle.",
                        "5-20 minutes",
                        "1-3",
                    )
                ],
            )
        ],
    )


def support_notes(*notes: str) -> WorkoutBlock:
    return block(
        WorkoutBlockType.NOTES,
        [option("Coaching Notes", [part("Decision Notes", " ".join(notes))])],
    )


def build_philosophy_session_card(spec: PhilosophySessionSpec) -> SessionCard:
    progression_rules = spec.progression_rules or (
        "Progress only when the athlete executes the current option with the intended philosophy-specific control.",
        "Increase one variable at a time: duration, repetitions, vertical load, intensity, terrain complexity, or decision complexity.",
    )
    regression_rules = spec.regression_rules or (
        "Choose a lower-cost option when readiness, recovery, confidence, or terrain access does not support the intended session.",
        "Use the corresponding mainstream easy, recovery, or support session when the philosophy-specific reason for this card is not present.",
    )
    additional_information = spec.additional_information or (
        "This is a philosophy-specific session card. It should be selected only when its distinctive workout structure, gates, "
        "or decision rules matter more than the shared mainstream session equivalent."
    )

    return SessionCard(
        id=spec.id,
        slug=slugify(spec.title),
        title=spec.title,
        card_type=CardType.SESSION,
        suitable_levels=[TrainingLevel.ALL],
        philosophy_profile_ids=[spec.philosophy_profile_id],
        summary=spec.summary,
        purpose=spec.purpose,
        tags=[spec.philosophy_profile_id, "session", *spec.tags],
        goal_race_context=[
            "Use when this workout concept matches the selected philosophy-specific micro week's key session role.",
            "Do not select this card when the same work can be represented accurately by a mainstream session card.",
        ],
        training_profile=list(spec.training_profile),
        expected_adaptations=list(spec.expected_adaptations),
        watchouts=list(spec.watchouts),
        progression_rules=list(progression_rules),
        regression_rules=list(regression_rules),
        additional_information=additional_information,
        references=[
            CardReference(
                card_id=micro_id,
                relationship=CardRelationship.PARENT,
                tags=["philosophy_specific_session_fit"],
            )
            for micro_id in spec.parent_micro_ids
        ],
        session_family=spec.session_family,
        typical_duration=spec.typical_duration,
        workout_blocks=list(spec.workout_blocks),
    )


def build_philosophy_session_cards(
    specs: tuple[PhilosophySessionSpec, ...],
) -> list[SessionCard]:
    return [build_philosophy_session_card(spec) for spec in specs]
