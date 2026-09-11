from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import CardType, MacroCard, TrainingLevel


example_macro_card = MacroCard(
    id="example_macro_001",
    slug="example-macro-phase",
    title="Example Macro Phase",
    card_type=CardType.MACRO,
    philosophy_profile_ids=[MAINSTREAM_ENDURANCE],
    suitable_levels=[TrainingLevel.ALL],
    summary="Example macro card showing the minimum shape of a larger training phase.",
    purpose="Use this as an authoring reference, not as a publishable card.",
    recommended_duration_weeks="4-12 weeks",
    timing_guidance=[
        "Place the phase where its main adaptation has enough time to develop.",
        "Keep the phase purpose clear before choosing mezzo blocks.",
    ],
    goal_race_context=["Example race context."],
    training_profile=["Example athlete profile."],
    expected_adaptations=["Example phase-level adaptation."],
    watchouts=["Example phase-level risk."],
    progression_rules=["Progress when the athlete absorbs the phase load consistently."],
    regression_rules=["Reduce scope when fatigue, soreness, or life stress changes readiness."],
    additional_information=(
        "Macro cards describe broad training phases. They should explain why the phase exists, "
        "what it emphasizes, what it avoids, and which mezzo blocks usually belong inside it."
    ),
)
