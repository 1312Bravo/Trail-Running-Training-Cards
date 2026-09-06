from training_cards.philosophy_profiles import SHARMAN_ULTRA
from training_cards.schemas import CardRelationship, CardReference, CardType, MezzoCard, TrainingLevel


def _parent(macro_id: str, tag: str) -> list[CardReference]:
    return [CardReference(card_id=macro_id, relationship=CardRelationship.PARENT, tags=[tag])]


def _card(
    *,
    id: str,
    slug: str,
    title: str,
    parent_macro_id: str,
    parent_tag: str,
    summary: str,
    purpose: str,
    tags: list[str],
    training_profile: list[str],
    expected_adaptations: list[str],
    progression_rules: list[str],
    regression_rules: list[str],
    watchouts: list[str],
    placement_guidance: list[str],
    additional_information: str,
) -> MezzoCard:
    return MezzoCard(
        id=id,
        slug=slug,
        title=title,
        card_type=CardType.MEZZO,
        suitable_levels=[TrainingLevel.ALL],
        philosophy_profile_ids=[SHARMAN_ULTRA],
        summary=summary,
        purpose=purpose,
        tags=["sharman_ultra", "mezzo", *tags],
        goal_race_context=[
            "Use when practical ultra preparation and athlete-context adaptation shape the block.",
            "Most useful when course reality, logistics, substitutions, and learning matter more than a fixed template.",
        ],
        training_profile=training_profile,
        expected_adaptations=expected_adaptations,
        progression_rules=progression_rules,
        regression_rules=regression_rules,
        references=_parent(parent_macro_id, parent_tag),
        recommended_duration_weeks="2-6",
        placement_guidance=placement_guidance,
        watchouts=watchouts,
        additional_information=additional_information,
    )


sharman_course_reality_preparation_block = _card(
    id="mezzo_074",
    slug="sharman-course-reality-preparation-block",
    title="Sharman Course Reality Preparation Block",
    parent_macro_id="macro_037",
    parent_tag="sharman_race_specific",
    summary="An ultra preparation block that fits course demands to the athlete's real life and access.",
    purpose="Prepare the athlete for the most important course realities using practical, available training options.",
    tags=["race_specific", "course_reality", "ultra"],
    training_profile=[
        "The block identifies the demands most likely to matter: vertical, surface, duration, heat, altitude, or technicality.",
        "Training uses accessible substitutions when exact course terrain is unavailable.",
        "The athlete learns how the course will feel, not just what it looks like on paper.",
    ],
    expected_adaptations=[
        "Improved practical course readiness.",
        "Better confidence using available terrain and time.",
        "Clearer understanding of the race's main demands.",
    ],
    progression_rules=[
        "Progress from accessible approximations toward more specific demands.",
        "Prioritize the few course factors most likely to decide the race.",
        "Adjust the block to the athlete's experience and recovery capacity.",
    ],
    regression_rules=[
        "Simplify specificity if the athlete cannot recover from course-like stress.",
        "Use substitutions when exact terrain creates too much logistical or physical cost.",
    ],
    watchouts=[
        "Do not overfit the plan to a course detail the athlete cannot train safely.",
        "Avoid copying elite preparation when the athlete's context is different.",
    ],
    placement_guidance=[
        "Place during Sharman race-specific preparation.",
        "Use when the course profile is known and the athlete needs practical specificity.",
    ],
    additional_information="This card keeps Sharman-style practicality front and center: prepare for the race that exists, with the life and terrain the athlete actually has.",
)


sharman_practical_ultra_execution_block = _card(
    id="mezzo_075",
    slug="sharman-practical-ultra-execution-block",
    title="Sharman Practical Ultra Execution Block",
    parent_macro_id="macro_037",
    parent_tag="sharman_race_specific",
    summary="An execution block for pacing, hiking, logistics, problem-solving, and sustainable ultra decisions.",
    purpose="Practice the decisions and routines that help the athlete move efficiently through a long ultra.",
    tags=["race_specific", "execution", "ultra"],
    training_profile=[
        "Sessions include pacing, hiking transitions, aid-style routines, gear decisions, and late-run problem solving.",
        "The block emphasizes practical reliability over dramatic simulation.",
        "Execution practice is adapted to athlete experience and available terrain.",
    ],
    expected_adaptations=[
        "Improved ultra execution confidence.",
        "Better pacing and hiking decisions.",
        "Reduced race-day friction from unpracticed routines.",
    ],
    progression_rules=[
        "Practice one execution element at a time before combining several.",
        "Use long runs or specific sessions to rehearse the most likely race-day decisions.",
        "Debrief what worked and adjust without overcomplicating the plan.",
    ],
    regression_rules=[
        "Simplify routines if practice becomes distracting.",
        "Return to basic pacing or hiking transitions if combined demands are not reliable.",
    ],
    watchouts=[
        "Do not make every execution practice a race simulation.",
        "Avoid complex gear or pacing systems the athlete cannot execute under fatigue.",
    ],
    placement_guidance=[
        "Place after course realities are understood.",
        "Use before taper when execution routines still need confidence.",
    ],
    additional_information="Practical ultra preparation often wins by reducing avoidable mistakes. This block trains that.",
)


sharman_fueling_gear_logistics_block = _card(
    id="mezzo_076",
    slug="sharman-fueling-gear-logistics-block",
    title="Sharman Fueling Gear Logistics Block",
    parent_macro_id="macro_037",
    parent_tag="sharman_race_specific",
    summary="An ultra block that makes fueling, gear, and logistics reliable before race day.",
    purpose="Turn practical race-day support systems into rehearsed, athlete-specific routines.",
    tags=["race_specific", "fueling", "gear"],
    training_profile=[
        "Fueling, hydration, gear, pack setup, and aid logistics are practiced in relevant sessions.",
        "The athlete tests what is simple and reliable under fatigue.",
        "Strategy is adapted to race duration, aid spacing, conditions, and personal tolerance.",
    ],
    expected_adaptations=[
        "More reliable fueling and gear choices.",
        "Reduced logistical anxiety.",
        "Better ability to execute simple plans late in the race.",
    ],
    progression_rules=[
        "Test one change at a time before combining fueling, gear, and terrain stress.",
        "Practice with the items and timing likely to be used on race day.",
        "Refine the plan from training feedback rather than theory alone.",
    ],
    regression_rules=[
        "Simplify the system if the athlete cannot remember or tolerate it.",
        "Separate fueling practice from very hard terrain when troubleshooting gut issues.",
    ],
    watchouts=[
        "Do not leave practical systems untested until race week.",
        "Avoid overcomplicated gear or nutrition plans that fail under fatigue.",
    ],
    placement_guidance=[
        "Place during Sharman race-specific preparation.",
        "Use before final execution rehearsals and taper.",
    ],
    additional_information="This card is intentionally practical. In ultras, simple systems practiced well can matter as much as another workout.",
)


sharman_context_aware_between_race_recovery_block = _card(
    id="mezzo_077",
    slug="sharman-context-aware-between-race-recovery-block",
    title="Sharman Context-Aware Between-Race Recovery Block",
    parent_macro_id="macro_038",
    parent_tag="sharman_competition",
    summary="A between-race recovery block shaped by event cost, athlete life, and the next race.",
    purpose="Recover from ultra racing with decisions that match the athlete's context rather than a fixed timeline.",
    tags=["competition", "between_races", "recovery"],
    training_profile=[
        "Recovery considers race duration, terrain damage, travel, sleep, work, family stress, and motivation.",
        "The next event is planned around what recovery actually allows.",
        "Training returns through simple movement before demanding specificity.",
    ],
    expected_adaptations=[
        "Better recovery after ultra events.",
        "More realistic between-race planning.",
        "Lower risk of carrying hidden fatigue into the next race.",
    ],
    progression_rules=[
        "Progress when ordinary running feels normal and life stress is manageable.",
        "Use low-risk aerobic movement before race-specific work.",
        "Scale the next block to the athlete's available recovery time.",
    ],
    regression_rules=[
        "Extend recovery if soreness, mood, or sleep remain compromised.",
        "Shift goals if the next race is too close for meaningful rebuilding.",
    ],
    watchouts=[
        "Do not apply a generic recovery timeline to every ultra.",
        "Avoid ignoring non-training stress between events.",
    ],
    placement_guidance=[
        "Place after an ultra or high-cost trail race.",
        "Use before adaptive race feedback or race-season maintenance.",
    ],
    additional_information="The Sharman flavor is context. Recovery is not only what the race did; it is what the race did to this athlete in this life.",
)


sharman_adaptive_race_feedback_block = _card(
    id="mezzo_078",
    slug="sharman-adaptive-race-feedback-block",
    title="Sharman Adaptive Race Feedback Block",
    parent_macro_id="macro_038",
    parent_tag="sharman_competition",
    summary="A competition-learning block that turns race feedback into practical next-step adjustments.",
    purpose="Use what happened in the race to guide training, recovery, logistics, and future race choices.",
    tags=["competition", "feedback", "adaptation"],
    training_profile=[
        "The block reviews pacing, fueling, gear, terrain response, emotional experience, and recovery.",
        "Feedback is translated into a small number of practical changes.",
        "The athlete's goals and context determine which lessons matter most.",
    ],
    expected_adaptations=[
        "Better learning from races.",
        "More practical future preparation.",
        "Improved athlete confidence through clear next steps.",
    ],
    progression_rules=[
        "Separate controllable lessons from one-off race noise.",
        "Choose one or two changes for the next block.",
        "Use the next race context to decide whether a lesson needs training, logistics, or expectation adjustment.",
    ],
    regression_rules=[
        "Avoid major plan changes if feedback is unclear or emotionally raw.",
        "Return to recovery if the athlete needs space before analysis.",
    ],
    watchouts=[
        "Do not turn every disappointing result into a fitness problem.",
        "Avoid vague individualisation that does not change the next decision.",
    ],
    placement_guidance=[
        "Place after initial recovery from a race.",
        "Use before planning the next race-specific or between-event block.",
    ],
    additional_information="This card keeps feedback useful. The goal is not to produce a long debrief; it is to make the next decision better.",
)


SHARMAN_MEZZO_CARDS = [
    sharman_course_reality_preparation_block,
    sharman_practical_ultra_execution_block,
    sharman_fueling_gear_logistics_block,
    sharman_context_aware_between_race_recovery_block,
    sharman_adaptive_race_feedback_block,
]
