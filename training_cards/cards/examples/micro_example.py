from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import CardReference, CardRelationship, CardType, MicroCard, TrainingLevel


example_micro_card = MicroCard(
    id="example_micro_001",
    slug="example-micro-week",
    title="Example Micro Week",
    card_type=CardType.MICRO,
    philosophy_profile_ids=[MAINSTREAM_ENDURANCE],
    suitable_levels=[TrainingLevel.ALL],
    summary="Example micro card showing one reusable week structure inside a mezzo block.",
    purpose="Use this as an authoring reference, not as a publishable card.",
    recommended_duration_days="7 days",
    week_structure=[
        "One primary session that serves the block purpose.",
        "Easy aerobic support around the primary session.",
        "Enough recovery spacing to keep the week repeatable.",
    ],
    key_sessions=["Example primary session.", "Example support session."],
    load_pattern="Example loading pattern: moderate build with clear recovery space.",
    placement_guidance=[
        "Use this week when the athlete is ready for the block's main stimulus.",
        "Avoid placing it immediately after a race or unusually demanding week.",
    ],
    recovery_requirements=["At least one easy or recovery day after the primary stimulus."],
    expected_adaptations=["Example week-level adaptation."],
    watchouts=["Example week-level risk."],
    progression_rules=["Progress by repeating the week cleanly before adding load."],
    regression_rules=["Reduce the primary session or replace it with aerobic support if readiness is low."],
    additional_information=(
        "Micro cards describe week-level organization. They should decide session mix, spacing, "
        "load pattern, and recovery requirements without prescribing every workout detail."
    ),
    references=[
        CardReference(
            card_id="example_mezzo_001",
            relationship=CardRelationship.PARENT,
            tags=["example_parent"],
        )
    ],
)
