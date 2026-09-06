from training_cards.philosophy_profiles import CTS
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
        philosophy_profile_ids=[CTS],
        summary=summary,
        purpose=purpose,
        tags=["cts", "mezzo", *tags],
        goal_race_context=[
            "Use when event demands, athlete limiters, and practical execution choices shape the block.",
            "Most useful for trail and ultra contexts where durability, time, terrain, and recovery trade-offs must be explicit.",
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


cts_repeatable_workload_foundation_block = _card(
    id="mezzo_046",
    slug="cts-repeatable-workload-foundation-block",
    title="CTS Repeatable Workload Foundation Block",
    parent_macro_id="macro_020",
    parent_tag="cts_base",
    summary="A foundation block that builds workload the athlete can repeat before adding sharper demands.",
    purpose="Establish a dependable training workload that supports later limiter-focused and event-specific work.",
    tags=["base", "workload", "repeatability"],
    training_profile=[
        "Weekly training is organized around what the athlete can repeat, absorb, and sustain.",
        "Volume, frequency, and terrain are selected by current durability rather than idealized target mileage.",
        "Support work is included only when it helps the athlete tolerate the running workload.",
    ],
    expected_adaptations=[
        "More dependable baseline workload.",
        "Clearer understanding of the athlete's current training durability.",
        "Better readiness for targeted limiter work.",
    ],
    progression_rules=[
        "Progress when the athlete can repeat the workload without accumulating fatigue.",
        "Add terrain or duration only when recovery remains predictable.",
        "Use recovery weeks as part of workload development, not as failure.",
    ],
    regression_rules=[
        "Reduce workload if consistency breaks or soreness rises.",
        "Simplify the week when the athlete cannot recover from ordinary training.",
    ],
    watchouts=[
        "Do not build the block around theoretical volume the athlete cannot currently absorb.",
        "Avoid adding intensity before the workload foundation is repeatable.",
    ],
    placement_guidance=[
        "Place early in CTS base development.",
        "Use before long-run durability or limiter-focused quality blocks.",
    ],
    additional_information="CTS logic here is practical: before solving sophisticated race problems, the athlete needs a workload that can actually be repeated.",
)


cts_long_run_durability_block = _card(
    id="mezzo_047",
    slug="cts-long-run-durability-block",
    title="CTS Long-Run Durability Block",
    parent_macro_id="macro_020",
    parent_tag="cts_base",
    summary="A durability block that develops long-run tolerance for real trail and ultra demands.",
    purpose="Build long-duration resilience while tracking the terrain and recovery costs that matter for the athlete's event.",
    tags=["base", "long_run", "durability"],
    training_profile=[
        "Long runs are selected by event relevance and recovery cost.",
        "Duration, vertical, technicality, fueling practice, and downhill load are progressed deliberately.",
        "The rest of the week supports the durability target rather than competing with it.",
    ],
    expected_adaptations=[
        "Improved tolerance for long trail outings.",
        "Better recovery from race-relevant duration and terrain.",
        "Clearer identification of durability limiters.",
    ],
    progression_rules=[
        "Progress long-run stress only when the athlete recovers well enough to resume normal training.",
        "Add vertical, technicality, or duration one at a time.",
        "Use event demands to decide which long-run variable matters most.",
    ],
    regression_rules=[
        "Reduce long-run complexity if it compromises the next training week.",
        "Use hiking or flatter terrain when durability is needed without excessive damage.",
    ],
    watchouts=[
        "Do not confuse longer with more specific if the course limiter is different.",
        "Avoid long-run escalation that forces repeated recovery debt.",
    ],
    placement_guidance=[
        "Place after workload foundation is stable.",
        "Use before CTS race-specific preparation when long-duration tolerance is a limiter.",
    ],
    additional_information="Durability is not just surviving a long run. It is being able to train again after race-relevant stress.",
)


cts_limiter_focused_quality_block = _card(
    id="mezzo_048",
    slug="cts-limiter-focused-quality-block",
    title="CTS Limiter-Focused Quality Block",
    parent_macro_id="macro_021",
    parent_tag="cts_capacity",
    summary="A quality block chosen because it solves a meaningful limiter, not because intensity is missing.",
    purpose="Target the athlete's current performance limiter with the smallest effective quality emphasis.",
    tags=["capacity", "quality", "limiter"],
    training_profile=[
        "Quality sessions are chosen from the athlete's event demands and current limiter profile.",
        "The block may emphasize threshold, aerobic power, climbing, or sustained effort depending on the problem.",
        "Recovery and total workload are adjusted so the limiter work can be absorbed.",
    ],
    expected_adaptations=[
        "Improved capacity in the targeted limiter.",
        "Better alignment between workouts and event demands.",
        "Less wasted intensity from generic hard training.",
    ],
    progression_rules=[
        "Progress only the limiter-specific variable that matters most.",
        "Keep supporting runs easy enough to protect quality execution.",
        "Reassess the limiter after several weeks instead of extending the block automatically.",
    ],
    regression_rules=[
        "Reduce intensity or volume if the athlete cannot hit the intended stimulus.",
        "Return to workload foundation if quality exposes poor durability.",
    ],
    watchouts=[
        "Do not label all hard work as limiter-focused.",
        "Avoid chasing multiple limiters in the same short block.",
    ],
    placement_guidance=[
        "Place after base workload can support targeted quality.",
        "Use before event-demands preparation when a specific limiter needs attention.",
    ],
    additional_information="The CTS flavor is diagnostic. The block starts with 'what limits this athlete for this event?' and builds from there.",
)


cts_ultra_strength_endurance_limiter_block = _card(
    id="mezzo_049",
    slug="cts-ultra-strength-endurance-limiter-block",
    title="CTS Ultra Strength-Endurance Limiter Block",
    parent_macro_id="macro_021",
    parent_tag="cts_capacity",
    summary="A strength-endurance block for athletes limited by climbing, fatigue resistance, or terrain cost.",
    purpose="Improve the athlete's ability to sustain force and movement quality under ultra-relevant terrain demands.",
    tags=["capacity", "strength_endurance", "ultra_limiter"],
    training_profile=[
        "Hill, hike, climb, or resistance work is selected because it matches a real event limiter.",
        "The block balances force development with enough easy running to maintain endurance continuity.",
        "Downhill and technical costs are monitored so strength-endurance work does not create unmanaged soreness.",
    ],
    expected_adaptations=[
        "Improved climbing or hiking durability.",
        "Better fatigue resistance on terrain that previously exposed weakness.",
        "More practical confidence for ultra-specific demands.",
    ],
    progression_rules=[
        "Progress the limiter variable gradually: grade, duration, load, or repetition count.",
        "Keep session purpose clear when combining running and hiking.",
        "Use event specificity only after general strength-endurance tolerance improves.",
    ],
    regression_rules=[
        "Reduce force demand if soreness interferes with normal running.",
        "Use lower-grade terrain if mechanics become sloppy.",
    ],
    watchouts=[
        "Do not turn every hill workout into a maximal grind.",
        "Avoid ignoring eccentric cost from descents paired with climbing work.",
    ],
    placement_guidance=[
        "Place in CTS capacity development when terrain force is a limiter.",
        "Use before race-specific course-demands work.",
    ],
    additional_information="This card is CTS-specific because the strength-endurance work is not generic hill training; it is a targeted answer to a limiter.",
)


cts_event_demands_block = _card(
    id="mezzo_050",
    slug="cts-event-demands-block",
    title="CTS Event Demands Block",
    parent_macro_id="macro_022",
    parent_tag="cts_race_specific",
    summary="A race-specific block that starts with what the event will actually require.",
    purpose="Translate course, duration, terrain, climate, and logistics into a focused preparation block.",
    tags=["race_specific", "event_demands", "course"],
    training_profile=[
        "The event profile determines which demands are practiced now.",
        "Training choices are filtered through what is realistically available to the athlete.",
        "The block prioritizes the most consequential demands instead of simulating everything.",
    ],
    expected_adaptations=[
        "Better event-specific readiness.",
        "Clearer confidence around the race's main demands.",
        "More realistic substitutions when exact terrain is unavailable.",
    ],
    progression_rules=[
        "Progress from isolated demands toward combined demands.",
        "Use the athlete's limiter profile to decide which event variable deserves the most attention.",
        "Add specificity only while recovery remains good enough to preserve training quality.",
    ],
    regression_rules=[
        "Simplify demands if combined specificity creates too much fatigue.",
        "Return to limiter-focused or durability work if the event block exposes a gap.",
    ],
    watchouts=[
        "Do not attempt full race simulation too often.",
        "Avoid copying another athlete's event block without matching course and context.",
    ],
    placement_guidance=[
        "Place after CTS base and capacity work.",
        "Use when the target race is close enough that specificity matters.",
    ],
    additional_information="The block is anchored by a practical question: what will this race ask of this athlete, and what can we prepare safely now?",
)


cts_race_execution_rehearsal_block = _card(
    id="mezzo_051",
    slug="cts-race-execution-rehearsal-block",
    title="CTS Race Execution Rehearsal Block",
    parent_macro_id="macro_022",
    parent_tag="cts_race_specific",
    summary="A rehearsal block for pacing, terrain decisions, gear, aid, and race-day problem solving.",
    purpose="Practice execution decisions that could materially affect race performance or completion.",
    tags=["race_specific", "execution", "rehearsal"],
    training_profile=[
        "Runs include intentional practice of pacing, hiking, aid-style transitions, gear use, and decision points.",
        "The athlete rehearses trade-offs rather than just completing hard workouts.",
        "Practice scenarios are selected from likely race-day failure points.",
    ],
    expected_adaptations=[
        "Better race-day decision confidence.",
        "Reduced surprise around logistics and pacing.",
        "Improved ability to adapt when conditions change.",
    ],
    progression_rules=[
        "Start with one execution skill per workout before combining several.",
        "Use lower-pressure rehearsals before key simulation runs.",
        "Debrief each rehearsal and adjust the next one based on what failed or felt uncertain.",
    ],
    regression_rules=[
        "Simplify rehearsals if logistics distract from the training stimulus.",
        "Return to basic pacing or gear practice when combined demands become messy.",
    ],
    watchouts=[
        "Do not treat rehearsal as a race effort by default.",
        "Avoid practicing new gear or fueling only on the hardest days.",
    ],
    placement_guidance=[
        "Place during CTS race-specific preparation.",
        "Use before taper once key execution skills still need practice.",
    ],
    additional_information="For CTS-style ultra preparation, execution is trainable. The block makes decisions part of training, not an afterthought.",
)


cts_fueling_and_hydration_strategy_block = _card(
    id="mezzo_052",
    slug="cts-fueling-and-hydration-strategy-block",
    title="CTS Fueling And Hydration Strategy Block",
    parent_macro_id="macro_022",
    parent_tag="cts_race_specific",
    summary="A race-specific block that turns fueling and hydration from advice into practiced strategy.",
    purpose="Develop a practical fueling, hydration, and electrolyte approach for the athlete's event demands.",
    tags=["race_specific", "fueling", "hydration"],
    training_profile=[
        "Fueling and hydration are practiced in long or specific sessions before race day.",
        "Strategy is adjusted for duration, heat, altitude, aid access, stomach tolerance, and intensity.",
        "The athlete learns what is reliable under fatigue, not just what sounds good on paper.",
    ],
    expected_adaptations=[
        "Improved fueling confidence.",
        "Better tolerance of race-relevant intake.",
        "Fewer preventable execution errors in long events.",
    ],
    progression_rules=[
        "Progress from simple intake targets to race-like timing and logistics.",
        "Test changes one variable at a time.",
        "Use rehearsal feedback to refine the strategy before taper.",
    ],
    regression_rules=[
        "Simplify intake if the athlete cannot execute it during training.",
        "Separate stomach-tolerance practice from maximal workouts if distress becomes the main limiter.",
    ],
    watchouts=[
        "Do not leave fueling practice for race week.",
        "Avoid assuming the same strategy works across heat, altitude, and aid-station spacing.",
    ],
    placement_guidance=[
        "Place during CTS race-specific preparation.",
        "Use when fueling or hydration is likely to decide the race outcome.",
    ],
    additional_information="This is a block because ultra fueling is not a note at the bottom of the plan. It needs repetition, feedback, and adjustment.",
)


cts_race_stress_recovery_block = _card(
    id="mezzo_053",
    slug="cts-race-stress-recovery-block",
    title="CTS Race Stress Recovery Block",
    parent_macro_id="macro_023",
    parent_tag="cts_competition",
    summary="A competition block that treats each race as a specific stress to recover from before rebuilding.",
    purpose="Match post-race training decisions to the actual physiological and logistical cost of the event.",
    tags=["competition", "recovery", "race_stress"],
    training_profile=[
        "Recovery is based on race duration, vertical, surface, weather, travel, sleep, and emotional load.",
        "Easy movement returns before structured development.",
        "The next event matters, but it does not erase the cost of the previous race.",
    ],
    expected_adaptations=[
        "Better recovery between demanding events.",
        "More accurate planning after races with different stress profiles.",
        "Reduced risk of stacking hidden fatigue.",
    ],
    progression_rules=[
        "Resume normal training only when easy movement, sleep, mood, and soreness are stable.",
        "Use short low-risk runs before workouts.",
        "Adjust recovery length by event cost, not by calendar habit.",
    ],
    regression_rules=[
        "Extend recovery when the athlete remains flat or unusually sore.",
        "Use non-running movement if impact feels costly.",
    ],
    watchouts=[
        "Do not assume a shorter race was low stress if terrain or travel was severe.",
        "Avoid making the next event plan before honestly accounting for recovery.",
    ],
    placement_guidance=[
        "Place immediately after important or costly races.",
        "Use before between-event adjustment when another race is upcoming.",
    ],
    additional_information="The CTS decision is practical: what did this event cost, and what does that allow next?",
)


cts_between_event_adjustment_block = _card(
    id="mezzo_054",
    slug="cts-between-event-adjustment-block",
    title="CTS Between-Event Adjustment Block",
    parent_macro_id="macro_023",
    parent_tag="cts_competition",
    summary="A between-race block that uses readiness and race feedback to choose the next adjustment.",
    purpose="Maintain or redirect training between events based on what the last race revealed and what the next race requires.",
    tags=["competition", "between_events", "feedback"],
    training_profile=[
        "The block reviews race feedback, current readiness, and upcoming event demands together.",
        "Training may maintain, sharpen, recover, or target a small limiter depending on timing.",
        "The plan avoids adding new fitness goals when there is only room to preserve readiness.",
    ],
    expected_adaptations=[
        "Better between-race decision-making.",
        "More useful translation of race feedback into training.",
        "Improved readiness for the next event without unnecessary overload.",
    ],
    progression_rules=[
        "Choose one adjustment priority for the block.",
        "Use the next event's timing to decide whether development is realistic.",
        "Keep feedback specific: what changed the race, and what can still be changed now?",
    ],
    regression_rules=[
        "Shift to recovery if readiness is worse than expected.",
        "Drop limiter work if the next race is too close for adaptation.",
    ],
    watchouts=[
        "Do not overreact to one race by rewriting the whole season.",
        "Avoid adding workouts just because the athlete feels anxious between events.",
    ],
    placement_guidance=[
        "Place after race-stress recovery when another event is planned.",
        "Use between closely spaced races or during a multi-race season.",
    ],
    additional_information="This card merges readiness and feedback because they are one coaching decision: what, if anything, should change before the next start line?",
)


CTS_MEZZO_CARDS = [
    cts_repeatable_workload_foundation_block,
    cts_long_run_durability_block,
    cts_limiter_focused_quality_block,
    cts_ultra_strength_endurance_limiter_block,
    cts_event_demands_block,
    cts_race_execution_rehearsal_block,
    cts_fueling_and_hydration_strategy_block,
    cts_race_stress_recovery_block,
    cts_between_event_adjustment_block,
]
