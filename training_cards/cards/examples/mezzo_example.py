from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import CardReference, CardRelationship, CardType, MezzoCard, TrainingLevel


example_mezzo_card = MezzoCard(
    id="example_mezzo_001",
    slug="example-mezzo-block",
    title="Example Mezzo Block",
    card_type=CardType.MEZZO,
    philosophy_profile_ids=[MAINSTREAM_ENDURANCE],
    suitable_levels=[TrainingLevel.ALL],
    summary="Example mezzo card showing a focused block inside one macro phase.",
    purpose="Use this as an authoring reference, not as a publishable card.",
    recommended_duration_weeks="2-6 weeks",
    placement_guidance=[
        "Place this block inside the parent macro phase only when it serves the phase purpose.",
        "Do not use mezzo cards for single-week or single-session details.",
    ],
    expected_adaptations=["Example block-level adaptation."],
    watchouts=["Example block-level risk."],
    progression_rules=["Progress when the block's main sessions are controlled and repeatable."],
    regression_rules=["Reduce intensity, volume, or block length when recovery quality drops."],
    additional_information=(
        "Mezzo cards describe multi-week blocks. They should be specific enough to guide block "
        "selection but broad enough that several micro weeks can sit underneath them."
    ),
    references=[
        CardReference(
            card_id="example_macro_001",
            relationship=CardRelationship.PARENT,
            tags=["example_parent"],
        )
    ],
)
