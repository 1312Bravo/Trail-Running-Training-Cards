from __future__ import annotations

import re
from dataclasses import dataclass

from training_cards.schemas import CardRelationship, CardReference, CardType, MicroCard, TrainingLevel


@dataclass(frozen=True, slots=True)
class PhilosophyMicroSpec:
    id: str
    title: str
    parent_mezzo_id: str
    parent_title: str
    parent_tag: str
    philosophy_profile_id: str
    profile_label: str
    distinction: str
    weekly_job: str
    key_sessions: list[str]
    load_pattern: str
    trail_context: str


def _slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def build_philosophy_micro_cards(specs: tuple[PhilosophyMicroSpec, ...]) -> list[MicroCard]:
    return [_build_card(spec) for spec in specs]


def _build_card(spec: PhilosophyMicroSpec) -> MicroCard:
    slug = _slugify(spec.title)
    tag_parts = slug.split("-")
    return MicroCard(
        id=spec.id,
        slug=slug,
        title=spec.title,
        card_type=CardType.MICRO,
        suitable_levels=[TrainingLevel.ALL],
        philosophy_profile_ids=[spec.philosophy_profile_id],
        summary=f"A {spec.profile_label} week structure for {spec.weekly_job}.",
        purpose=(
            f"Organize one week inside the {spec.parent_title} so the athlete can {spec.weekly_job} "
            f"while preserving the {spec.profile_label} coaching logic."
        ),
        tags=[spec.philosophy_profile_id, "micro", spec.parent_tag, *tag_parts],
        goal_race_context=[
            f"Use inside the {spec.parent_title}.",
            "Fits when the philosophy changes the week-level coaching decision enough to justify a specific card.",
            "Use a reused mainstream micro card instead when only wording, reminders, or exact workout execution would change.",
        ],
        training_profile=[
            spec.distinction,
            f"Weekly job: {spec.weekly_job}.",
            f"Load pattern: {spec.load_pattern}",
            spec.trail_context,
        ],
        expected_adaptations=[
            "A clearer week-level expression of the selected coaching philosophy.",
            "Better alignment between the parent block and the athlete's actual weekly stress.",
            "More reliable sequencing because the week's progression, restraint, and recovery demands are explicit.",
        ],
        watchouts=[
            "Do not create extra sessions merely to make the philosophy visible.",
            "Avoid using this card when a mainstream week structure would make the same coaching decision.",
            "Do not let philosophy-specific language hide poor recovery, excessive density, or mismatched terrain cost.",
        ],
        progression_rules=[
            "Progress only when the athlete absorbs the week without worsening soreness, mood, sleep, or easy-effort feel.",
            "Change one main stress variable at a time: frequency, duration, intensity, vertical load, technicality, density, or execution complexity.",
            "Repeat the week when the same stimulus is still useful and better than adding novelty.",
        ],
        regression_rules=[
            "Reduce the primary stressor if recovery signals worsen or the week stops matching the parent block.",
            "Use a lower-cost or reused mainstream week when the philosophy-specific distinction is not currently needed.",
            "Move back to a simpler week if execution complexity becomes the limiting factor.",
        ],
        additional_information=(
            "This is a philosophy-specific weekly structure, not a fixed seven-day calendar. "
            "The coach should preserve the week job while adapting exact sessions, rest days, terrain, and loading to the athlete."
        ),
        references=[
            CardReference(
                card_id=spec.parent_mezzo_id,
                relationship=CardRelationship.PARENT,
                tags=[spec.parent_tag, spec.philosophy_profile_id],
            )
        ],
        recommended_duration_days="7",
        week_structure=[
            "Anchor the week around the philosophy-specific decision named in the card.",
            "Place the key session or execution emphasis where the athlete can absorb it.",
            "Use the rest of the week to protect recovery, easy support, and the parent block purpose.",
        ],
        key_sessions=spec.key_sessions,
        load_pattern=spec.load_pattern,
        placement_guidance=[
            f"Place within the {spec.parent_title} when this specific weekly role is needed.",
            "Alternate with lower-cost, absorption, or reused mainstream weeks according to athlete response.",
        ],
        recovery_requirements=[
            "Protect at least one clear recovery opportunity around the highest-cost stress.",
            "Keep support days easy enough that the specific weekly purpose remains clear.",
            "Adjust promptly when trail cost, life stress, or lingering fatigue changes the true load.",
        ],
    )
