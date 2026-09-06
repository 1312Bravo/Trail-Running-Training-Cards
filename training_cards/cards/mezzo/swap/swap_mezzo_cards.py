from training_cards.philosophy_profiles import SWAP
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
        philosophy_profile_ids=[SWAP],
        summary=summary,
        purpose=purpose,
        tags=["swap", "mezzo", *tags],
        goal_race_context=[
            "Use when SWAP's health, agency, joy, and long-term development lens changes the block decision.",
            "Most useful when the athlete needs performance development without sacrificing confidence, sustainability, or whole-life fit.",
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


swap_supported_recovery_reset_block = _card(
    id="mezzo_062",
    slug="swap-supported-recovery-reset-block",
    title="SWAP Supported Recovery Reset Block",
    parent_macro_id="macro_007",
    parent_tag="recovery_transition",
    summary="A recovery block that restores health, agency, and emotional readiness after stress.",
    purpose="Help the athlete recover physically and psychologically before training becomes ambitious again.",
    tags=["recovery", "reset", "whole_athlete"],
    training_profile=[
        "Training is reduced, low pressure, and chosen to restore rather than prove fitness.",
        "The block makes space for mood, identity, confidence, and life stress alongside physical readiness.",
        "Running, hiking, strength, or rest are selected by what helps the athlete return healthier.",
    ],
    expected_adaptations=[
        "Improved readiness after stressful training or racing.",
        "Rebuilt trust in the body and the process.",
        "Better transition into the next sustainable training phase.",
    ],
    progression_rules=[
        "Progress when the athlete feels curiosity and energy returning.",
        "Add structure gradually and with athlete buy-in.",
        "Use low-pressure movement before demanding performance work.",
    ],
    regression_rules=[
        "Return to more rest or easier movement if pressure rises again.",
        "Remove goals that turn recovery into another test.",
    ],
    watchouts=[
        "Do not rush recovery because the athlete is emotionally eager to make up for lost time.",
        "Avoid framing reduced load as failure.",
    ],
    placement_guidance=[
        "Place after hard races, setbacks, burnout signs, or stressful life periods.",
        "Use before SWAP return, base, or race-season work when confidence needs repair.",
    ],
    additional_information="The SWAP distinction is that recovery includes the athlete's relationship with training. The goal is not only fresh legs; it is a healthier restart.",
)


swap_confidence_reentry_block = _card(
    id="mezzo_063",
    slug="swap-confidence-reentry-block",
    title="SWAP Confidence Re-Entry Block",
    parent_macro_id="macro_027",
    parent_tag="swap_return",
    summary="A return block that rebuilds running rhythm without shame, pressure, or fitness comparison.",
    purpose="Restore consistency while protecting the athlete's confidence, agency, and sense of belonging in training.",
    tags=["return_to_consistency", "confidence", "agency"],
    training_profile=[
        "The block uses small wins, flexible structure, and easy aerobic work.",
        "Training language avoids punishment, guilt, and comparisons with former fitness.",
        "Movement support is included only when it helps the athlete feel capable and durable.",
    ],
    expected_adaptations=[
        "More confident training rhythm.",
        "Improved willingness to show up consistently.",
        "A safer bridge toward aerobic development.",
    ],
    progression_rules=[
        "Progress through repeatable success before adding challenge.",
        "Let the athlete help choose sustainable training options.",
        "Add duration or frequency only when confidence and recovery are both improving.",
    ],
    regression_rules=[
        "Shrink the plan if the athlete starts dreading sessions.",
        "Use more flexibility if rigid structure creates shame or avoidance.",
    ],
    watchouts=[
        "Do not turn re-entry into a proving phase.",
        "Avoid motivational language that implies the athlete failed by needing a return block.",
    ],
    placement_guidance=[
        "Place at the start of SWAP return-to-consistency.",
        "Use after breaks, setbacks, low confidence, or disrupted life periods.",
    ],
    additional_information="This merged card carries the no-shame rhythm and aerobic reconditioning ideas together because, in SWAP logic, confidence is part of consistency.",
)


swap_sustainable_aerobic_rhythm_block = _card(
    id="mezzo_064",
    slug="swap-sustainable-aerobic-rhythm-block",
    title="SWAP Sustainable Aerobic Rhythm Block",
    parent_macro_id="macro_028",
    parent_tag="swap_base",
    summary="A base block that builds aerobic durability while protecting health and long-term consistency.",
    purpose="Develop aerobic rhythm in a way the athlete can sustain, enjoy, and recover from.",
    tags=["base", "aerobic_rhythm", "sustainability"],
    training_profile=[
        "Most training is relaxed, repeatable, and compatible with the athlete's life.",
        "Volume grows only when health, mood, and recovery stay supportive.",
        "The block avoids making base work emotionally or physically brittle.",
    ],
    expected_adaptations=[
        "Improved aerobic consistency.",
        "Stronger confidence in sustainable training.",
        "Better readiness for speed, economy, or race-specific development.",
    ],
    progression_rules=[
        "Progress when the athlete is recovering well and enjoying the rhythm.",
        "Use flexible options to preserve consistency through real life.",
        "Add load conservatively if injury history or stress load is relevant.",
    ],
    regression_rules=[
        "Reduce volume if health markers, motivation, or recovery decline.",
        "Shift to easier movement if the athlete starts forcing the plan.",
    ],
    watchouts=[
        "Do not mistake enthusiasm for unlimited capacity.",
        "Avoid building identity around mileage if it threatens health.",
    ],
    placement_guidance=[
        "Place early in SWAP base development.",
        "Use before adventure endurance or speed-economy support blocks.",
    ],
    additional_information="This is not soft base work. It is base work with a long-term athlete lens: durable, repeatable, and emotionally sustainable.",
)


swap_adventure_endurance_block = _card(
    id="mezzo_065",
    slug="swap-adventure-endurance-block",
    title="SWAP Adventure Endurance Block",
    parent_macro_id="macro_028",
    parent_tag="swap_base",
    summary="A long-endurance block that uses adventure as purposeful aerobic and confidence development.",
    purpose="Build endurance through meaningful outings while keeping health, recovery, and training purpose intact.",
    tags=["base", "long_run", "adventure"],
    training_profile=[
        "Long outings may include trails, exploration, hiking, and varied terrain when they support the athlete.",
        "The block treats joy and confidence as useful, but not as permission to ignore stress.",
        "Adventure is scaled to current capacity and future goals.",
    ],
    expected_adaptations=[
        "Greater long-duration confidence.",
        "Improved aerobic and terrain tolerance.",
        "A stronger positive relationship with endurance work.",
    ],
    progression_rules=[
        "Progress adventure complexity gradually: duration, vertical, technicality, remoteness, or weather.",
        "Keep the next days easy enough to absorb the outing.",
        "Use debriefs to learn what created energy versus depletion.",
    ],
    regression_rules=[
        "Simplify outings if recovery becomes unpredictable.",
        "Return to sustainable aerobic rhythm if adventure starts replacing consistency.",
    ],
    watchouts=[
        "Do not use adventure language to hide overreaching.",
        "Avoid technical or remote routes before the athlete has enough durability and skill.",
    ],
    placement_guidance=[
        "Place after aerobic rhythm is stable.",
        "Use before race-specific preparation when long confidence and terrain comfort matter.",
    ],
    additional_information="In SWAP logic, joy can be performance-relevant. This block keeps that joy purposeful and recoverable.",
)


swap_economy_speed_skill_support_block = _card(
    id="mezzo_066",
    slug="swap-economy-speed-skill-support-block",
    title="SWAP Economy Speed Skill Support Block",
    parent_macro_id="macro_028",
    parent_tag="swap_base",
    summary="A base-support block that keeps speed, economy, and coordination alive without hijacking aerobic work.",
    purpose="Maintain transferable speed and movement skill during base development with low-risk touches.",
    tags=["base", "speed_skill", "economy"],
    training_profile=[
        "Short relaxed strides, hill sprints, drills, or neuromuscular touches support economy.",
        "Fast work is small enough that it improves movement rather than creating workout fatigue.",
        "The block uses fun and skill to make the athlete feel capable.",
    ],
    expected_adaptations=[
        "Improved running economy and coordination.",
        "Better confidence changing gears.",
        "Preserved speed qualities during aerobic development.",
    ],
    progression_rules=[
        "Progress by quality and ease before adding volume.",
        "Keep touches short and separated from fatigue.",
        "Use forgiving surfaces and grades when injury risk is a concern.",
    ],
    regression_rules=[
        "Remove speed touches if they create soreness or anxiety.",
        "Return to relaxed strides if structured speed feels too demanding.",
    ],
    watchouts=[
        "Do not turn skill support into a hidden interval block.",
        "Avoid fast work when the athlete is not recovering from base volume.",
    ],
    placement_guidance=[
        "Place inside SWAP base when economy support is useful.",
        "Use before capacity development or race-specific work.",
    ],
    additional_information="The point is to keep the athlete springy and confident, not to win the workout.",
)


swap_speed_economy_development_block = _card(
    id="mezzo_067",
    slug="swap-speed-economy-development-block",
    title="SWAP Speed Economy Development Block",
    parent_macro_id="macro_029",
    parent_tag="swap_capacity",
    summary="A capacity block that develops speed and economy as sustainable performance skills.",
    purpose="Improve faster running capacity without making intensity detached from health, confidence, and long-term growth.",
    tags=["capacity", "speed", "economy"],
    training_profile=[
        "Quality work is purposeful, confidence-building, and scaled to the athlete's durability.",
        "The block may use strides, hill power, intervals, or controlled faster running depending on context.",
        "Easy support and recovery are protected so speed develops without emotional or physical strain.",
    ],
    expected_adaptations=[
        "Improved speed economy.",
        "Better ability to run faster while staying composed.",
        "Greater confidence with performance-oriented work.",
    ],
    progression_rules=[
        "Progress from relaxed speed to more demanding quality only when confidence remains high.",
        "Keep workouts repeatable rather than spectacular.",
        "Use athlete feedback to adjust challenge before it becomes pressure.",
    ],
    regression_rules=[
        "Reduce intensity if mechanics tighten or confidence drops.",
        "Return to short speed skill touches if workouts feel threatening.",
    ],
    watchouts=[
        "Do not use intensity to validate the athlete's worth.",
        "Avoid pushing speed when injury risk or stress load is elevated.",
    ],
    placement_guidance=[
        "Place after sustainable base rhythm.",
        "Use before race-specific preparation when speed or economy is a useful limiter.",
    ],
    additional_information="This card keeps SWAP's performance optimism, but with guardrails: speed should build the athlete up, not grind them down.",
)


swap_fatigue_resistance_development_block = _card(
    id="mezzo_068",
    slug="swap-fatigue-resistance-development-block",
    title="SWAP Fatigue Resistance Development Block",
    parent_macro_id="macro_029",
    parent_tag="swap_capacity",
    summary="A capacity block that explores fatigue resistance without chasing exhaustion.",
    purpose="Develop the athlete's ability to hold useful output under fatigue while preserving health and curiosity.",
    tags=["capacity", "fatigue_resistance", "durability"],
    training_profile=[
        "Workouts target late-session strength, climbing resilience, or sustained effort depending on the race context.",
        "The athlete learns how fatigue changes mechanics, decisions, and confidence.",
        "The block stops short of making exhaustion the training identity.",
    ],
    expected_adaptations=[
        "Improved performance durability.",
        "Better confidence when effort accumulates.",
        "Sharper awareness of fatigue signs that require adjustment.",
    ],
    progression_rules=[
        "Progress fatigue exposure gradually and with clear recovery.",
        "Keep the purpose specific: late-race strength, climbing durability, or sustained aerobic pressure.",
        "Use debriefs to learn from fatigue rather than glorify it.",
    ],
    regression_rules=[
        "Reduce load if fatigue changes mechanics or mood for multiple days.",
        "Return to aerobic rhythm if durability work becomes draining rather than developmental.",
    ],
    watchouts=[
        "Do not frame suffering as proof that the block is working.",
        "Avoid high fatigue when the athlete is already under life stress.",
    ],
    placement_guidance=[
        "Place during SWAP capacity development.",
        "Use before race-specific preparation when durability is a limiter.",
    ],
    additional_information="The SWAP nuance is curiosity: fatigue is information to train with, not a contest to win.",
)


swap_confidence_building_course_demands_block = _card(
    id="mezzo_069",
    slug="swap-confidence-building-course-demands-block",
    title="SWAP Confidence-Building Course Demands Block",
    parent_macro_id="macro_030",
    parent_tag="swap_race_specific",
    summary="A race-specific block that prepares course demands while protecting confidence and agency.",
    purpose="Build readiness for terrain, duration, and conditions in a way that makes the athlete feel more capable.",
    tags=["race_specific", "course_demands", "confidence"],
    training_profile=[
        "Course demands are practiced at a scale that develops belief instead of dread.",
        "Specific terrain, vertical, weather, or duration is chosen by what matters most for the race.",
        "The athlete participates in interpreting what each specific session taught.",
    ],
    expected_adaptations=[
        "Improved course-specific confidence.",
        "Better readiness for the race's most important demands.",
        "Reduced fear around unfamiliar or challenging terrain.",
    ],
    progression_rules=[
        "Progress specificity through successful exposures before bigger simulations.",
        "Use substitutions when exact course terrain is unavailable.",
        "Debrief confidence and decision quality, not only pace or distance.",
    ],
    regression_rules=[
        "Reduce specificity if it starts lowering confidence or health.",
        "Return to capacity or adventure endurance when the athlete needs more foundation.",
    ],
    watchouts=[
        "Do not scare the athlete into preparedness.",
        "Avoid all-or-nothing course simulations that leave no room to adapt.",
    ],
    placement_guidance=[
        "Place during SWAP race-specific preparation.",
        "Use before taper when the course still feels intimidating or unfamiliar.",
    ],
    additional_information="Specificity should make the athlete braver and better prepared, not smaller.",
)


swap_agency_race_execution_practice_block = _card(
    id="mezzo_070",
    slug="swap-agency-race-execution-practice-block",
    title="SWAP Agency Race Execution Practice Block",
    parent_macro_id="macro_030",
    parent_tag="swap_race_specific",
    summary="A race-execution block that helps the athlete practice decisions, not just logistics.",
    purpose="Prepare pacing, fueling, terrain choices, and self-talk in a way that supports athlete agency.",
    tags=["race_specific", "execution", "agency"],
    training_profile=[
        "Race practice includes decision points, pacing choices, fueling routines, and problem-solving.",
        "The athlete rehearses adapting rather than obeying a script.",
        "Practice sessions are debriefed through confidence, learning, and self-trust.",
    ],
    expected_adaptations=[
        "Better race-day decision confidence.",
        "More resilient execution when conditions change.",
        "Improved athlete ownership of the plan.",
    ],
    progression_rules=[
        "Start with simple decisions before combining pacing, fueling, and terrain complexity.",
        "Let the athlete describe what they would do when plans go sideways.",
        "Use rehearsals to refine the plan collaboratively.",
    ],
    regression_rules=[
        "Simplify practice if the athlete feels overwhelmed.",
        "Return to basic pacing or fueling routines if decision complexity causes stress.",
    ],
    watchouts=[
        "Do not make the athlete dependent on perfect instructions.",
        "Avoid rehearsals that punish mistakes instead of teaching from them.",
    ],
    placement_guidance=[
        "Place in race-specific preparation after course demands are understood.",
        "Use before key races when execution confidence is a limiter.",
    ],
    additional_information="SWAP race execution is not only what to do. It is helping the athlete trust themselves when reality gets messy.",
)


swap_whole_athlete_between_race_recovery_block = _card(
    id="mezzo_071",
    slug="swap-whole-athlete-between-race-recovery-block",
    title="SWAP Whole-Athlete Between-Race Recovery Block",
    parent_macro_id="macro_032",
    parent_tag="swap_competition",
    summary="A between-race recovery block that weighs excitement, health, identity, and long-term consistency.",
    purpose="Recover from racing while protecting the athlete from pressure-driven decisions between events.",
    tags=["competition", "between_races", "whole_athlete"],
    training_profile=[
        "Recovery decisions include physical cost, emotional load, travel, sleep, and motivation.",
        "The next race is considered without letting urgency override health.",
        "Training may be easy, playful, or minimal depending on what restores the athlete.",
    ],
    expected_adaptations=[
        "Better recovery between events.",
        "More sustainable race-season rhythm.",
        "Reduced pressure to prove fitness immediately after racing.",
    ],
    progression_rules=[
        "Progress when the athlete feels physically and emotionally ready.",
        "Use gentle structure before returning to performance work.",
        "Let the importance of the next race guide how much freshness to protect.",
    ],
    regression_rules=[
        "Extend recovery if motivation feels pressured rather than genuine.",
        "Remove workouts when health or life stress is the limiter.",
    ],
    watchouts=[
        "Do not let race excitement hide fatigue.",
        "Avoid framing recovery as lost opportunity.",
    ],
    placement_guidance=[
        "Place after races in a SWAP competition macro.",
        "Use before race-season maintenance or health-and-joy blocks.",
    ],
    additional_information="This block asks a very SWAP question: what helps the athlete keep loving this while still preparing well?",
)


swap_race_season_health_and_joy_block = _card(
    id="mezzo_072",
    slug="swap-race-season-health-and-joy-block",
    title="SWAP Race-Season Health And Joy Block",
    parent_macro_id="macro_032",
    parent_tag="swap_competition",
    summary="A race-season block that preserves health, learning, and joy across repeated competitions.",
    purpose="Maintain performance readiness without turning every race into pressure or every week into proof.",
    tags=["competition", "race_season", "health_joy"],
    training_profile=[
        "Training between races protects freshness, confidence, and long-term health.",
        "Race feedback is used to learn without overreacting.",
        "The block keeps small performance touches only when they help rather than strain.",
    ],
    expected_adaptations=[
        "More sustainable race-season consistency.",
        "Better learning from races.",
        "Preserved confidence and health through competition periods.",
    ],
    progression_rules=[
        "Use the athlete's response to each race before planning the next stress.",
        "Keep quality small and familiar unless there is a clear reason.",
        "Celebrate learning and process markers, not only outcomes.",
    ],
    regression_rules=[
        "Shift to recovery if the season starts feeling heavy.",
        "Remove performance pressure when the athlete needs reconnection more than sharpening.",
    ],
    watchouts=[
        "Do not let race season become identity pressure.",
        "Avoid chasing missed fitness between events.",
    ],
    placement_guidance=[
        "Place between races after initial recovery.",
        "Use during multi-race seasons or when joy and health need active protection.",
    ],
    additional_information="This card merges maintenance and learning because SWAP race-season work should keep the athlete whole while still moving forward.",
)


swap_off_season_identity_and_play_block = _card(
    id="mezzo_073",
    slug="swap-off-season-identity-and-play-block",
    title="SWAP Off-Season Identity And Play Block",
    parent_macro_id="macro_034",
    parent_tag="swap_off_season",
    summary="An off-season block that reconnects the athlete with movement, identity, and playful variety.",
    purpose="Restore the athlete's relationship with training while preserving enough aerobic rhythm to restart well.",
    tags=["off_season", "identity", "play"],
    training_profile=[
        "Movement choices can include easy running, hiking, cross-training, strength, play, or unstructured exploration.",
        "The block lowers performance pressure while keeping the athlete connected to their body.",
        "Aerobic rhythm remains present but does not dominate the reset.",
    ],
    expected_adaptations=[
        "Renewed motivation and identity outside strict race preparation.",
        "Maintained basic movement rhythm.",
        "Better emotional readiness for the next build.",
    ],
    progression_rules=[
        "Progress only when the athlete wants more structure.",
        "Use variety to restore energy, not to sneak in hidden load.",
        "Transition toward base once curiosity and consistency return.",
    ],
    regression_rules=[
        "Remove structure if off-season starts feeling like another training block.",
        "Choose lower-impact movement if the body needs more restoration.",
    ],
    watchouts=[
        "Do not make off-season a disguised fitness test.",
        "Avoid losing all rhythm if the athlete benefits from gentle continuity.",
    ],
    placement_guidance=[
        "Place after a race season or demanding build.",
        "Use before returning to SWAP base or confidence re-entry work.",
    ],
    additional_information="The merged off-season card keeps identity reset and play together because both serve the same recovery of relationship with movement.",
)


SWAP_MEZZO_CARDS = [
    swap_supported_recovery_reset_block,
    swap_confidence_reentry_block,
    swap_sustainable_aerobic_rhythm_block,
    swap_adventure_endurance_block,
    swap_economy_speed_skill_support_block,
    swap_speed_economy_development_block,
    swap_fatigue_resistance_development_block,
    swap_confidence_building_course_demands_block,
    swap_agency_race_execution_practice_block,
    swap_whole_athlete_between_race_recovery_block,
    swap_race_season_health_and_joy_block,
    swap_off_season_identity_and_play_block,
]
