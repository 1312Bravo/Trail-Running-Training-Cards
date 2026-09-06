from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import CardRelationship, CardReference, CardType, MezzoCard, TrainingLevel


def _parent(macro_id: str, tag: str) -> list[CardReference]:
    return [CardReference(card_id=macro_id, relationship=CardRelationship.PARENT, tags=[tag])]


def _mainstream_mezzo(
    *,
    id: str,
    slug: str,
    title: str,
    parent_macro_id: str,
    parent_tag: str,
    summary: str,
    purpose: str,
    tags: list[str],
    goal_race_context: list[str],
    training_profile: list[str],
    expected_adaptations: list[str],
    progression_rules: list[str],
    regression_rules: list[str],
    watchouts: list[str],
    placement_guidance: list[str],
    additional_information: str,
    suitable_levels: list[TrainingLevel] | None = None,
    recommended_duration_weeks: str = "2-6",
) -> MezzoCard:
    return MezzoCard(
        id=id,
        slug=slug,
        title=title,
        card_type=CardType.MEZZO,
        suitable_levels=suitable_levels or [TrainingLevel.ALL],
        philosophy_profile_ids=[MAINSTREAM_ENDURANCE],
        summary=summary,
        purpose=purpose,
        tags=["mainstream_endurance", "mezzo", *tags],
        goal_race_context=goal_race_context,
        training_profile=training_profile,
        expected_adaptations=expected_adaptations,
        progression_rules=progression_rules,
        regression_rules=regression_rules,
        references=_parent(parent_macro_id, parent_tag),
        recommended_duration_weeks=recommended_duration_weeks,
        placement_guidance=placement_guidance,
        watchouts=watchouts,
        additional_information=additional_information,
    )


mainstream_reentry_rhythm_block = _mainstream_mezzo(
    id="mezzo_001",
    slug="mainstream-reentry-rhythm-block",
    title="Re-Entry Rhythm Block",
    parent_macro_id="macro_001",
    parent_tag="return_to_consistency",
    summary="A low-pressure block that rebuilds dependable running frequency before meaningful load progression.",
    purpose="Restore training rhythm, confidence, and basic repeatability after interruption, inconsistency, or a low-readiness period.",
    tags=["return_to_consistency", "rhythm", "frequency"],
    goal_race_context=[
        "Use when the athlete needs routine before development.",
        "Fits after illness, life disruption, low motivation, or a long training break when full base work is premature.",
        "Useful before any block that would require reliable weekly frequency.",
    ],
    training_profile=[
        "Short, simple running or run-walk exposures repeated often enough to become normal again.",
        "Intensity stays easy and terrain stays low risk unless trail exposure is specifically being reintroduced.",
        "The block values completion, recovery, and emotional ease more than fitness markers.",
    ],
    expected_adaptations=[
        "More dependable training frequency.",
        "Better confidence that running can fit the athlete's current life.",
        "Enough routine to judge whether the next block is realistic.",
    ],
    progression_rules=[
        "Add frequency or small duration before intensity or technical terrain.",
        "Progress only when the athlete finishes most sessions feeling able to train again.",
        "Move toward reconditioning or base work once rhythm is stable for more than one week.",
    ],
    regression_rules=[
        "Use walk breaks, shorter outings, or extra rest days if routine feels forced.",
        "Return to fewer sessions if soreness, fatigue, or dread rises.",
    ],
    watchouts=[
        "Do not use this block to prove former fitness.",
        "Avoid technical descents, long climbs, or intensity while basic rhythm is still fragile.",
    ],
    placement_guidance=[
        "Place at the start of return-to-consistency phases.",
        "Can precede easy aerobic reconditioning or base development.",
    ],
    additional_information="This block is deliberately modest. The coaching win is not a dramatic workout; it is making training feel repeatable enough that later work has a foundation.",
)


mainstream_easy_aerobic_reconditioning_block = _mainstream_mezzo(
    id="mezzo_002",
    slug="mainstream-easy-aerobic-reconditioning-block",
    title="Easy Aerobic Reconditioning Block",
    parent_macro_id="macro_001",
    parent_tag="return_to_consistency",
    summary="A gentle aerobic block that rebuilds basic endurance without rushing toward normal training load.",
    purpose="Rebuild easy aerobic tolerance after interruption while keeping recovery and tissue response visible.",
    tags=["return_to_consistency", "easy_aerobic", "reconditioning"],
    goal_race_context=[
        "Use when routine is returning but the athlete is not ready for a full base phase.",
        "Fits athletes who can train consistently at a small dose but need aerobic tolerance rebuilt.",
        "Useful before aerobic volume or long endurance blocks.",
    ],
    training_profile=[
        "Mostly easy running, run-walk, hiking, or low-impact aerobic alternatives.",
        "Duration progresses conservatively while intensity remains controlled.",
        "Trail terrain may be included only when it does not create hidden mechanical cost.",
    ],
    expected_adaptations=[
        "Improved easy aerobic tolerance.",
        "More reliable recovery from ordinary training.",
        "Clearer readiness for longer or more structured base work.",
    ],
    progression_rules=[
        "Progress total easy time before adding moderate intensity.",
        "Keep the terrain simple until soreness and recovery are predictable.",
        "Move to base development when easy volume is repeatable.",
    ],
    regression_rules=[
        "Reduce duration or choose lower-impact aerobic work if recovery lags.",
        "Return to re-entry rhythm work if consistency breaks down.",
    ],
    watchouts=[
        "Do not let easy running drift into steady effort to feel productive.",
        "Avoid comparing current aerobic pace to pre-break fitness.",
    ],
    placement_guidance=[
        "Place after basic rhythm is re-established.",
        "Can overlap with very light strength reintroduction when recovery is stable.",
    ],
    additional_information="Reconditioning is not a punishment phase. It is the bridge between being back in motion and being ready to build.",
)


mainstream_movement_strength_reintroduction_block = _mainstream_mezzo(
    id="mezzo_003",
    slug="mainstream-movement-strength-reintroduction-block",
    title="Movement Strength Reintroduction Block",
    parent_macro_id="macro_001",
    parent_tag="return_to_consistency",
    summary="A conservative support block that restores basic strength, mobility, and movement tolerance.",
    purpose="Reintroduce supportive strength and movement work without competing with the return to running.",
    tags=["return_to_consistency", "strength_support", "movement_quality"],
    goal_race_context=[
        "Use when the athlete needs basic movement capacity alongside the return to running.",
        "Fits athletes coming back from inconsistency, sedentary periods, or low general strength exposure.",
        "Useful before more demanding strength, hills, or technical terrain.",
    ],
    training_profile=[
        "Low-to-moderate support work focused on control, range, and repeatability.",
        "Strength work stays far enough from failure that running rhythm is protected.",
        "Movement choices should match current capacity and avoid creating delayed soreness.",
    ],
    expected_adaptations=[
        "Improved general movement confidence.",
        "Better tolerance for later running load.",
        "A clearer entry point for strength support in base or capacity phases.",
    ],
    progression_rules=[
        "Progress control and consistency before load or complexity.",
        "Add resistance only when the athlete recovers normally from both running and support work.",
    ],
    regression_rules=[
        "Reduce sets, range, load, or exercise complexity if soreness interferes with running.",
        "Pause strength progression if running rhythm is not yet stable.",
    ],
    watchouts=[
        "Do not turn reintroduction into a hard strength block.",
        "Avoid unfamiliar exercises that create soreness unrelated to the return goal.",
    ],
    placement_guidance=[
        "Place during return-to-consistency when movement support is a limiter.",
        "Keep secondary to restoring running rhythm.",
    ],
    additional_information="This block treats strength as support. It should make the athlete more available for running, not steal the recovery needed to become consistent again.",
)


mainstream_aerobic_volume_block = _mainstream_mezzo(
    id="mezzo_004",
    slug="mainstream-aerobic-volume-block",
    title="Aerobic Volume Block",
    parent_macro_id="macro_002",
    parent_tag="base_development",
    summary="A base block that develops repeatable aerobic workload through controlled volume progression.",
    purpose="Increase sustainable aerobic training load while preserving easy intensity, recovery, and movement quality.",
    tags=["base_development", "aerobic_volume", "progression"],
    goal_race_context=[
        "Use during base development when the athlete is ready to build total aerobic exposure.",
        "Fits runners whose main need is more repeatable easy training rather than intensity.",
        "Useful before higher-cost capacity or race-specific blocks.",
    ],
    training_profile=[
        "Mostly easy aerobic running distributed across the week.",
        "Progression focuses on total time, frequency, or small volume increases rather than harder effort.",
        "Trail volume is counted by total cost, including climbing, surface, and descent exposure.",
    ],
    expected_adaptations=[
        "Greater aerobic durability.",
        "Improved ability to absorb later training stress.",
        "More consistent low-intensity workload.",
    ],
    progression_rules=[
        "Increase one volume variable at a time.",
        "Keep easy days genuinely easy as volume grows.",
        "Use reduced-load weeks when repeatability starts to weaken.",
    ],
    regression_rules=[
        "Reduce total time or frequency if soreness, sleep, or motivation deteriorates.",
        "Hold volume steady when terrain cost has increased.",
    ],
    watchouts=[
        "Do not build volume and intensity at the same time.",
        "Avoid treating vertical gain as free aerobic volume.",
    ],
    placement_guidance=[
        "Place early or mid base phase after basic consistency exists.",
        "Can precede long endurance or capacity development blocks.",
    ],
    additional_information="Aerobic volume is useful only when it can be repeated. The block should create a bigger aerobic platform, not a brittle workload that collapses at the first added stress.",
)


mainstream_long_endurance_development_block = _mainstream_mezzo(
    id="mezzo_005",
    slug="mainstream-long-endurance-development-block",
    title="Long Endurance Development Block",
    parent_macro_id="macro_002",
    parent_tag="base_development",
    summary="A base block that extends long-run tolerance while keeping the effort mostly aerobic.",
    purpose="Develop the athlete's ability to handle longer continuous or accumulated endurance stress.",
    tags=["base_development", "long_endurance", "long_run"],
    goal_race_context=[
        "Use when the athlete needs more long-duration tolerance before specific preparation.",
        "Fits runners who can handle ordinary aerobic volume but need the long run developed.",
        "Useful for trail and ultra goals when time on feet must be introduced gradually.",
    ],
    training_profile=[
        "Long outings progress through duration, time on feet, or route cost.",
        "Effort remains mostly aerobic and controlled.",
        "Fueling, hiking, and descent exposure may be introduced only when they support the block purpose.",
    ],
    expected_adaptations=[
        "Improved tolerance for longer aerobic loading.",
        "Better musculoskeletal durability across sustained outings.",
        "Greater confidence with time on feet.",
    ],
    progression_rules=[
        "Progress long-run duration before adding intensity or technicality.",
        "Use step-back weeks after meaningful long-run increases.",
        "Add fueling practice when duration makes it relevant.",
    ],
    regression_rules=[
        "Shorten the long outing or split the stress if recovery cost becomes disproportionate.",
        "Choose smoother terrain if descent or technicality becomes the limiting stress.",
    ],
    watchouts=[
        "Do not turn every long run into a test.",
        "Avoid adding distance, vertical gain, technical terrain, and fueling experiments all at once.",
    ],
    placement_guidance=[
        "Place after the athlete has enough weekly aerobic rhythm to support longer outings.",
        "Can lead into race-specific or fueling-focused blocks.",
    ],
    additional_information="The long run is a tool, not a weekly exam. This block extends endurance by making long outings purposeful, progressive, and recoverable.",
)


mainstream_strength_and_movement_support_block = _mainstream_mezzo(
    id="mezzo_006",
    slug="mainstream-strength-and-movement-support-block",
    title="Strength And Movement Support Block",
    parent_macro_id="macro_002",
    parent_tag="base_development",
    summary="A base-support block that builds general strength and movement quality around aerobic running.",
    purpose="Support running durability, economy, and later load tolerance without displacing the aerobic base.",
    tags=["base_development", "strength_support", "movement_quality"],
    goal_race_context=[
        "Use when general strength, mobility, or movement control would support later training.",
        "Fits runners preparing for future hills, speed, volume, or technical terrain.",
        "Useful during base because support work can be introduced before race-specific stress rises.",
    ],
    training_profile=[
        "Regular supportive strength, mobility, and movement-quality work.",
        "Running remains the primary adaptation target.",
        "Exercises are selected for transfer, control, and manageable recovery cost.",
    ],
    expected_adaptations=[
        "Improved general durability.",
        "Better movement control and readiness for later stress.",
        "Reduced fragility when running load increases.",
    ],
    progression_rules=[
        "Progress movement quality and consistency before load.",
        "Increase strength load only when it does not compromise key aerobic work.",
    ],
    regression_rules=[
        "Reduce load, volume, or complexity if running quality declines.",
        "Keep only the highest-value support work during busy or fatigue-heavy weeks.",
    ],
    watchouts=[
        "Do not confuse gym fatigue with useful running support.",
        "Avoid adding hard strength near long-run progression before adaptation is known.",
    ],
    placement_guidance=[
        "Place during base when there is recovery room for support work.",
        "Can continue at lower dose through later phases.",
    ],
    additional_information="This block gives strength a clear job: make the runner more durable and prepared for later work while keeping endurance training central.",
)


mainstream_trail_skill_and_terrain_familiarity_block = _mainstream_mezzo(
    id="mezzo_028",
    slug="mainstream-trail-skill-and-terrain-familiarity-block",
    title="Trail Skill And Terrain Familiarity Block",
    parent_macro_id="macro_002",
    parent_tag="base_development",
    summary="A base block that builds low-to-moderate trail skill and terrain confidence before specific preparation.",
    purpose="Develop basic trail movement, hiking transitions, descending control, and terrain familiarity without turning base into race simulation.",
    tags=["base_development", "trail_skill", "terrain_familiarity"],
    goal_race_context=[
        "Use during base when trail or mountain demands will matter later but race-specific work is premature.",
        "Fits runners who need confidence and movement exposure on varied terrain.",
        "Useful before course-demand blocks, technical race preparation, or higher-cost mountain training.",
    ],
    training_profile=[
        "Low-to-moderate trail exposure is added gradually around the aerobic base.",
        "Technicality, descent load, hiking, and surface variety are treated as dose variables.",
        "The block prioritises relaxed skill, rhythm, and confidence over hard effort.",
    ],
    expected_adaptations=[
        "Improved confidence and coordination on varied terrain.",
        "Better tolerance for basic climbing, descending, and hiking transitions.",
        "More readiness for later race-specific trail demands.",
    ],
    progression_rules=[
        "Progress one terrain variable at a time: technicality, vertical gain, descent load, duration, or remoteness.",
        "Keep most work aerobic enough that terrain skill does not become hidden intensity.",
        "Move toward course-demand work when terrain exposure is repeatable and goal specificity matters.",
    ],
    regression_rules=[
        "Choose smoother terrain if technicality changes the intended aerobic stimulus.",
        "Reduce descent exposure when soreness or coordination fatigue persists.",
        "Return to aerobic volume work if terrain familiarity starts displacing the base.",
    ],
    watchouts=[
        "Do not confuse adventurous terrain with useful skill progression.",
        "Avoid adding technical descents, long climbs, and longer duration in the same step.",
        "Do not make every base run trail-specific.",
    ],
    placement_guidance=[
        "Place during base development after basic aerobic rhythm is stable.",
        "Can precede race-specific course-demands or race-execution practice blocks.",
    ],
    additional_information="This block gives trail skill a sensible home before race specificity. The athlete learns to move well on varied ground while the aerobic base remains the main engine of the phase.",
)


mainstream_threshold_control_block = _mainstream_mezzo(
    id="mezzo_007",
    slug="mainstream-threshold-control-block",
    title="Threshold Control Block",
    parent_macro_id="macro_003",
    parent_tag="capacity_development",
    summary="A development block that improves sustainable moderate-hard running without letting intensity sprawl.",
    purpose="Develop threshold-adjacent control, sustained output, and pacing discipline inside a recoverable block.",
    tags=["capacity_development", "threshold", "controlled_quality"],
    goal_race_context=[
        "Use after base consistency is strong enough to support purposeful quality.",
        "Fits runners who need better sustained output or controlled moderate-hard work.",
        "Useful before race-specific preparation when threshold control is a likely limiter.",
    ],
    training_profile=[
        "One or more controlled quality sessions supported by easy aerobic running.",
        "Intensity is anchored by sustainable effort, not ego pace.",
        "Terrain should allow the intended effort to be controlled and reviewed.",
    ],
    expected_adaptations=[
        "Improved sustainable output.",
        "Better pacing control around threshold-like effort.",
        "Greater confidence using moderate-hard work without overreaching.",
    ],
    progression_rules=[
        "Progress total controlled work before increasing intensity.",
        "Keep easy support days easy enough to protect quality.",
        "Move toward race-specific work once sustained effort is stable.",
    ],
    regression_rules=[
        "Shorten intervals, extend recoveries, or use smoother terrain if control fades.",
        "Return to aerobic volume if moderate work disrupts the week.",
    ],
    watchouts=[
        "Do not let this block become repeated racing in training.",
        "Avoid threshold labels when the athlete cannot control the effort.",
    ],
    placement_guidance=[
        "Place in capacity development after adequate base.",
        "Avoid placing immediately after a high-cost race or disrupted return period.",
    ],
    additional_information="Threshold control is useful because it teaches sustainable pressure. The coach should see cleaner control, not just harder running.",
)


mainstream_aerobic_power_block = _mainstream_mezzo(
    id="mezzo_008",
    slug="mainstream-aerobic-power-block",
    title="Aerobic Power Block",
    parent_macro_id="macro_003",
    parent_tag="capacity_development",
    summary="A higher-intensity development block that targets aerobic power with enough recovery to preserve quality.",
    purpose="Improve high-end aerobic capacity and hard-effort tolerance through carefully placed quality work.",
    tags=["capacity_development", "aerobic_power", "high_intensity"],
    goal_race_context=[
        "Use when the athlete has sufficient base and needs high-end aerobic development.",
        "Fits experienced runners who recover well from demanding quality sessions.",
        "Useful before specific race work when aerobic power is a meaningful limiter.",
    ],
    training_profile=[
        "Hard aerobic intervals or hill equivalents placed with deliberate recovery.",
        "Quality is protected by lower-stress running around key sessions.",
        "Trail versions should choose terrain that supports the target effort without unsafe technical demands.",
    ],
    expected_adaptations=[
        "Improved high-end aerobic capacity.",
        "Better ability to tolerate and recover from hard aerobic work.",
        "Sharper distinction between key quality and supporting easy running.",
    ],
    progression_rules=[
        "Progress repetition count, duration, or density one at a time.",
        "Keep the athlete fresh enough that hard work remains technically sound.",
    ],
    regression_rules=[
        "Reduce repetitions or extend recovery when quality falls.",
        "Replace with threshold control or aerobic volume if hard work is not being absorbed.",
    ],
    watchouts=[
        "Do not use this block when base, health, or recovery is unstable.",
        "Avoid stacking hard intervals with high descent load or heavy strength.",
    ],
    placement_guidance=[
        "Place after base and before or early within specific preparation if needed.",
        "Use sparingly for runners whose goal does not require much high-intensity work.",
    ],
    additional_information="Aerobic power blocks can be effective, but they are expensive. The block earns its place only when the athlete can execute hard work well and recover enough to keep training.",
    suitable_levels=[TrainingLevel.INTERMEDIATE, TrainingLevel.ADVANCED, TrainingLevel.ELITE],
)


mainstream_strength_endurance_block = _mainstream_mezzo(
    id="mezzo_009",
    slug="mainstream-strength-endurance-block",
    title="Strength Endurance Block",
    parent_macro_id="macro_003",
    parent_tag="capacity_development",
    summary="A development block that builds force endurance for hills, fatigue, and durable running mechanics.",
    purpose="Improve the ability to sustain running-specific force without replacing aerobic support.",
    tags=["capacity_development", "strength_endurance", "hills"],
    goal_race_context=[
        "Use when hills, fatigue, or force demand are likely limiters.",
        "Fits runners with enough base and basic strength to absorb local muscular work.",
        "Useful before race-specific terrain blocks for trail and mountain goals.",
    ],
    training_profile=[
        "Uphill, resistance, or strength-endurance work supported by aerobic running.",
        "The local muscular demand is progressed deliberately.",
        "Descent and technical cost are managed separately from uphill force work.",
    ],
    expected_adaptations=[
        "Improved force endurance for climbing or sustained running.",
        "Greater durability under muscular fatigue.",
        "Better readiness for terrain-specific preparation.",
    ],
    progression_rules=[
        "Progress grade, duration, repetition count, or load one at a time.",
        "Preserve aerobic support and recovery around specific muscular work.",
    ],
    regression_rules=[
        "Reduce grade, volume, or technicality if local soreness disrupts training.",
        "Return to strength support if the athlete lacks basic control or force reserve.",
    ],
    watchouts=[
        "Do not confuse soreness with adaptation.",
        "Avoid turning every hill run into strength endurance.",
    ],
    placement_guidance=[
        "Place after base and before demanding mountain-specific race preparation.",
        "Can be replaced later by philosophy-specific muscular-endurance blocks when their logic is stronger.",
    ],
    additional_information="This mainstream block keeps strength endurance broad. Named philosophies may later create more specific versions when their progression model changes the block.",
    suitable_levels=[TrainingLevel.INTERMEDIATE, TrainingLevel.ADVANCED, TrainingLevel.ELITE],
)


mainstream_course_demands_block = _mainstream_mezzo(
    id="mezzo_010",
    slug="mainstream-course-demands-block",
    title="Course Demands Block",
    parent_macro_id="macro_004",
    parent_tag="race_specific_preparation",
    summary="A race-specific block that prepares the demands that matter most for the target route or event.",
    purpose="Translate the goal into the key terrain, duration, intensity, technical, and environmental demands to practise.",
    tags=["race_specific_preparation", "course_demands", "specificity"],
    goal_race_context=[
        "Use when a target race or objective has clear consequential demands.",
        "Fits trail and mountain goals where terrain, descent, heat, altitude, or technicality changes preparation.",
        "Useful after general capacity is sufficient for more specific work.",
    ],
    training_profile=[
        "Sessions are selected because they prepare a meaningful event demand.",
        "Specificity increases in proportion to readiness and recovery cost.",
        "Substitutions name what they preserve and what they cannot fully reproduce.",
    ],
    expected_adaptations=[
        "Better preparation for the actual performance problem.",
        "Improved confidence with goal-relevant terrain or conditions.",
        "Clearer distinction between useful specificity and unnecessary simulation.",
    ],
    progression_rules=[
        "Progress from partial demand exposure toward more integrated practice.",
        "Add technicality, duration, or environmental stress only when previous exposure is absorbed.",
    ],
    regression_rules=[
        "Use simpler terrain or shorter exposure when the specific demand is too costly.",
        "Return to capacity development if the athlete is not ready for event-like work.",
    ],
    watchouts=[
        "Do not copy the race just because it looks specific.",
        "Avoid adding every possible demand in the same week.",
    ],
    placement_guidance=[
        "Place after base and capacity blocks when the goal is close enough for transfer.",
        "Can sit alongside fueling or race-execution practice when recovery allows.",
    ],
    additional_information="Specificity is not costume rehearsal. This block asks which event demands actually change the coaching decision and prepares those deliberately.",
)


mainstream_race_execution_practice_block = _mainstream_mezzo(
    id="mezzo_011",
    slug="mainstream-race-execution-practice-block",
    title="Race Execution Practice Block",
    parent_macro_id="macro_004",
    parent_tag="race_specific_preparation",
    summary="A preparation block that rehearses pacing, decisions, gear, and composure under goal-relevant conditions.",
    purpose="Help the athlete practise using fitness through race-day decisions rather than only building more capacity.",
    tags=["race_specific_preparation", "execution", "pacing"],
    goal_race_context=[
        "Use when fitness must be translated into pacing, gear, terrain, or decision practice.",
        "Fits longer trail goals where execution errors can override physical capacity.",
        "Useful after the athlete can absorb specific practice without excessive fatigue.",
    ],
    training_profile=[
        "Practice sessions include pacing, route choices, gear, aid-station habits, hiking transitions, or mental checkpoints.",
        "The block uses enough specificity to teach decisions without making every workout a race simulation.",
        "Feedback after sessions is part of the training stimulus.",
    ],
    expected_adaptations=[
        "Improved pacing and decision quality.",
        "Better confidence with race-day routines.",
        "Reduced surprise from goal-relevant logistics or terrain.",
    ],
    progression_rules=[
        "Progress from isolated execution skills toward integrated rehearsals.",
        "Keep the practice recoverable enough that learning is not buried by fatigue.",
    ],
    regression_rules=[
        "Simplify to one execution skill if integrated rehearsals become messy.",
        "Reduce duration or terrain demand when decision quality collapses.",
    ],
    watchouts=[
        "Do not make every rehearsal maximal.",
        "Avoid practising gear or fueling changes for the first time too close to the race.",
    ],
    placement_guidance=[
        "Place in race-specific preparation after the main physical prerequisites exist.",
        "Coordinate with course demands and fueling blocks.",
    ],
    additional_information="Execution practice is where the athlete learns how to use the fitness they have built. The block should create useful information, not just impressive fatigue.",
)


mainstream_fueling_and_hydration_practice_block = _mainstream_mezzo(
    id="mezzo_012",
    slug="mainstream-fueling-and-hydration-practice-block",
    title="Fueling And Hydration Practice Block",
    parent_macro_id="macro_004",
    parent_tag="race_specific_preparation",
    summary="A race-preparation block that practises intake, tolerance, and hydration decisions during relevant training.",
    purpose="Make fueling and hydration trainable execution skills for longer or higher-cost events.",
    tags=["race_specific_preparation", "fueling", "hydration"],
    goal_race_context=[
        "Use when event duration, heat, altitude, or stomach tolerance makes intake important.",
        "Fits long trail, ultra, or demanding mountain goals.",
        "Useful before race day so problems can be discovered while there is time to adjust.",
    ],
    training_profile=[
        "Longer or specific sessions include planned intake and post-session review.",
        "Practice focuses on timing, amount, tolerance, logistics, and recovery support.",
        "Guidance stays within coaching scope and avoids clinical nutrition prescription.",
    ],
    expected_adaptations=[
        "Better confidence with intake during running.",
        "More useful information about what the athlete tolerates.",
        "Improved ability to support long or demanding sessions.",
    ],
    progression_rules=[
        "Practise intake first in controlled sessions before difficult terrain or race-like stress.",
        "Change one variable at a time: product, timing, amount, or conditions.",
    ],
    regression_rules=[
        "Simplify the session or intake plan if tolerance problems dominate the workout.",
        "Move practice to easier terrain or lower intensity when learning is the main goal.",
    ],
    watchouts=[
        "Do not wait until race day to test important fueling decisions.",
        "Do not treat this block as medical nutrition care.",
    ],
    placement_guidance=[
        "Place inside race-specific preparation once long or event-relevant sessions are present.",
        "Can support long endurance development when duration already warrants practice.",
    ],
    additional_information="Fueling and hydration practice belongs where it changes performance and recovery. The block should help the athlete learn, not overwhelm them with rigid rules.",
)


mainstream_taper_freshness_block = _mainstream_mezzo(
    id="mezzo_013",
    slug="mainstream-taper-freshness-block",
    title="Taper Freshness Block",
    parent_macro_id="macro_005",
    parent_tag="peak_and_taper",
    summary="A taper block that reduces accumulated fatigue while preserving rhythm and confidence.",
    purpose="Help the athlete arrive fresher without losing the familiar feel of running.",
    tags=["peak_and_taper", "taper", "freshness"],
    goal_race_context=[
        "Use before an important race or objective after meaningful preparation has been completed.",
        "Fits athletes who need fatigue reduced more than fitness increased.",
        "Useful when the final weeks must protect confidence and readiness.",
    ],
    training_profile=[
        "Total volume and cost decrease while some rhythm remains.",
        "Training avoids unfamiliar demands and late fitness chasing.",
        "Trail-specific reminders are small enough to avoid soreness or anxiety.",
    ],
    expected_adaptations=[
        "Reduced fatigue.",
        "Preserved running rhythm.",
        "Better readiness to express existing fitness.",
    ],
    progression_rules=[
        "Progress by reducing cost while keeping the athlete connected to familiar movement.",
        "Use only small reminders when sharpness is needed.",
    ],
    regression_rules=[
        "Reduce more aggressively if fatigue is still visible.",
        "Remove unfamiliar or high-soreness work immediately.",
    ],
    watchouts=[
        "Do not use taper to create missing fitness.",
        "Avoid panic workouts when freshness feels unfamiliar.",
    ],
    placement_guidance=[
        "Place in the final part of peak and taper.",
        "Follow race-specific preparation or competition management.",
    ],
    additional_information="A good taper can feel almost too easy. That is part of the point: the block protects the work already done so it can show up on race day.",
)


mainstream_sharpening_touchpoint_block = _mainstream_mezzo(
    id="mezzo_014",
    slug="mainstream-sharpening-touchpoint-block",
    title="Sharpening Touchpoint Block",
    parent_macro_id="macro_005",
    parent_tag="peak_and_taper",
    summary="A low-volume block that preserves useful sharpness without adding meaningful fatigue.",
    purpose="Keep the athlete connected to race rhythm, coordination, or controlled intensity while tapering.",
    tags=["peak_and_taper", "sharpening", "touchpoint"],
    goal_race_context=[
        "Use near the target race when small reminders are useful.",
        "Fits athletes who benefit from retaining rhythm but no longer need development work.",
        "Useful when previous preparation is complete enough to avoid cramming.",
    ],
    training_profile=[
        "Brief controlled quality, strides, hill reminders, or race-rhythm touches.",
        "Volume is low and recovery is generous.",
        "Terrain reminders stay familiar and low risk.",
    ],
    expected_adaptations=[
        "Preserved coordination and confidence.",
        "Maintained feel for controlled race-relevant effort.",
        "Minimal added fatigue.",
    ],
    progression_rules=[
        "Keep touchpoints short and familiar.",
        "Progress only by improving ease or control, not by adding load.",
    ],
    regression_rules=[
        "Remove the touchpoint if fatigue, soreness, or anxiety rises.",
        "Use easy running instead when sharpness work feels forced.",
    ],
    watchouts=[
        "Do not turn sharpening into a final test.",
        "Avoid unfamiliar shoes, terrain, intensity, or strength work.",
    ],
    placement_guidance=[
        "Place before or within taper freshness work.",
        "Use sparingly and only when it supports confidence.",
    ],
    additional_information="Sharpening is a reminder, not a build. The athlete should leave the block feeling more ready, not more impressed by how much they squeezed into the final days.",
)


mainstream_race_readiness_check_block = _mainstream_mezzo(
    id="mezzo_015",
    slug="mainstream-race-readiness-check-block",
    title="Race Readiness Check Block",
    parent_macro_id="macro_005",
    parent_tag="peak_and_taper",
    summary="A short taper block that turns final readiness checks into calm, low-cost race-week practice.",
    purpose="Organise the final one-to-two week readiness process so movement, logistics, pacing, and support routines stay familiar and low stress.",
    tags=["peak_and_taper", "readiness", "logistics"],
    goal_race_context=[
        "Use near an important race after the main training has been completed.",
        "Fits trail and ultra goals where gear, fueling, travel, and route decisions matter.",
        "Useful when practical uncertainty could disturb the final taper if left unmanaged.",
    ],
    training_profile=[
        "Short, familiar sessions carry simple readiness checks for gear, fueling, pacing, and route requirements.",
        "The block avoids new workouts and new decisions that create soreness or doubt.",
        "Readiness is judged by calm repeatability across the final taper window, not by proving fitness.",
    ],
    expected_adaptations=[
        "Clearer race-day plan.",
        "Reduced avoidable uncertainty.",
        "More confidence in familiar routines.",
    ],
    progression_rules=[
        "Finalize decisions early enough that the last days remain calm.",
        "Use only familiar movement and gear for confirmation.",
    ],
    regression_rules=[
        "Simplify choices if the athlete becomes overloaded by details.",
        "Remove nonessential checks if they create anxiety or fatigue.",
    ],
    watchouts=[
        "Do not introduce new shoes, fueling, routes, or strength work late.",
        "Avoid mistaking nervous energy for a need to train more.",
    ],
    placement_guidance=[
        "Place in the final one-to-two weeks of peak and taper.",
        "Use alongside taper freshness rather than as a separate fitness-development block.",
    ],
    additional_information="This block stays mezzo-level only because it organises the final taper window, not because checklists deserve their own training phase. Readiness is broader than fitness, but the work must remain low cost.",
    recommended_duration_weeks="1-2",
)


mainstream_between_race_recovery_block = _mainstream_mezzo(
    id="mezzo_016",
    slug="mainstream-between-race-recovery-block",
    title="Between-Race Recovery Block",
    parent_macro_id="macro_006",
    parent_tag="competition_management",
    summary="A competition-season block that restores function after one race before preparing for the next.",
    purpose="Absorb race stress and decide how much training can responsibly fit before another event.",
    tags=["competition_management", "between_races", "recovery"],
    goal_race_context=[
        "Use when races or meaningful events are close enough to affect each other.",
        "Fits race series, tune-up races, and multi-event trail seasons.",
        "Important when race stress includes descents, travel, heat, or long duration.",
    ],
    training_profile=[
        "Recovery, easy running, and small readiness checks after the race.",
        "Training resumes according to actual response rather than calendar ambition.",
        "The next race determines whether the block can include maintenance or only recovery.",
    ],
    expected_adaptations=[
        "Better recovery between competitions.",
        "Reduced chance of compounding race stress.",
        "Clearer readiness for the next event.",
    ],
    progression_rules=[
        "Progress from rest or easy movement to short aerobic running before adding quality.",
        "Add small touchpoints only when soreness and fatigue have resolved enough.",
    ],
    regression_rules=[
        "Extend recovery if muscle damage, sleep disruption, or motivation remains poor.",
        "Skip planned touchpoints if the next race is close and freshness is more valuable.",
    ],
    watchouts=[
        "Do not treat race fitness as proof that recovery is complete.",
        "Avoid squeezing a full build between close races.",
    ],
    placement_guidance=[
        "Place immediately after a race inside competition management.",
        "Can precede race-season maintenance or another taper freshness block.",
    ],
    additional_information="Between-race recovery is an active coaching decision. The question is not what training fits on paper, but what the athlete can absorb before the next start.",
)


mainstream_race_season_maintenance_block = _mainstream_mezzo(
    id="mezzo_017",
    slug="mainstream-race-season-maintenance-block",
    title="Race Season Maintenance Block",
    parent_macro_id="macro_006",
    parent_tag="competition_management",
    summary="A competition-season block that preserves useful fitness without burying the next event in fatigue.",
    purpose="Maintain aerobic rhythm, small quality touchpoints, and event readiness between competitions.",
    tags=["competition_management", "maintenance", "race_season"],
    goal_race_context=[
        "Use when the athlete has another race soon but needs more than passive recovery.",
        "Fits periods where fitness should be preserved rather than substantially developed.",
        "Useful when race load itself is already a major stressor.",
    ],
    training_profile=[
        "Controlled aerobic work plus small reminders of quality or terrain.",
        "Training cost stays lower than in a development block.",
        "Race-specific work is selected only when it solves a practical readiness issue.",
    ],
    expected_adaptations=[
        "Preserved useful fitness.",
        "Better rhythm between competitions.",
        "Reduced risk of overtraining through race-season excitement.",
    ],
    progression_rules=[
        "Keep touchpoints small and stop adding load once readiness is preserved.",
        "Use the next race date to limit the block's ambition.",
    ],
    regression_rules=[
        "Shift to between-race recovery if fatigue remains high.",
        "Remove quality before removing easy rhythm when recovery is tight.",
    ],
    watchouts=[
        "Do not try to rebuild fitness between closely spaced races.",
        "Avoid moderate training creep when the athlete feels recovered but is not fully restored.",
    ],
    placement_guidance=[
        "Place between races after initial recovery.",
        "Can lead into taper freshness when the next race becomes the priority.",
    ],
    additional_information="Race-season maintenance is deliberately restrained. It keeps the athlete connected to training while respecting that competition is already a large input.",
)


mainstream_competition_learning_block = _mainstream_mezzo(
    id="mezzo_018",
    slug="mainstream-competition-learning-block",
    title="Competition Learning Block",
    parent_macro_id="macro_006",
    parent_tag="competition_management",
    summary="A race-season block that converts repeated competition feedback into targeted training decisions.",
    purpose="Use race outcomes, execution notes, recovery response, and targeted practice to improve the next event without overreacting to one result.",
    tags=["competition_management", "learning", "race_review"],
    goal_race_context=[
        "Use during a race season when events are meant to teach as well as test.",
        "Fits athletes learning pacing, fueling, terrain management, or competition routines.",
        "Useful after tune-up races when there is time to practise one or two clear lessons.",
    ],
    training_profile=[
        "Short review loops connect race execution, recovery response, and next-block choices.",
        "Training changes are proportionate to patterns, not one emotional result.",
        "The block includes targeted low-to-moderate practice for one clear lesson when recovery allows.",
    ],
    expected_adaptations=[
        "Better race decision-making.",
        "More accurate understanding of current readiness and limiters.",
        "Improved ability to adjust training between events.",
    ],
    progression_rules=[
        "Choose one or two lessons to apply before the next race.",
        "Adjust training only when the race evidence is relevant enough and there is room to practise before the next event.",
    ],
    regression_rules=[
        "Return to simple recovery if race review becomes emotionally or physically costly.",
        "Avoid adding training to fix a problem that was actually pacing, fueling, or conditions.",
    ],
    watchouts=[
        "Do not rewrite the whole plan after one race.",
        "Avoid confusing a successful race with permission to ignore recovery.",
    ],
    placement_guidance=[
        "Place after tune-up or learning races.",
        "Can support race-specific preparation or race-season maintenance.",
    ],
    additional_information="Competition learning remains a training block only when the review changes the next several weeks of practice. If it is only a debrief, it belongs in notes or app guidance rather than as a card.",
)


mainstream_post_race_recovery_block = _mainstream_mezzo(
    id="mezzo_019",
    slug="mainstream-post-race-recovery-block",
    title="Post-Race Recovery Block",
    parent_macro_id="macro_007",
    parent_tag="recovery_and_transition",
    summary="A recovery block that restores physical and mental readiness after a race or major objective.",
    purpose="Let the athlete absorb the event, reduce fatigue, and restore normal movement before training resumes.",
    tags=["recovery_and_transition", "post_race", "recovery"],
    goal_race_context=[
        "Use after an important race, ultra, mountain objective, or very demanding simulation.",
        "Fits events with high descent, duration, travel, heat, or emotional load.",
        "Useful before deciding whether the next phase should build, maintain, or rest more.",
    ],
    training_profile=[
        "Rest, walking, easy movement, and gradual return to low-cost running.",
        "Readiness is judged by soreness, mood, sleep, appetite, and ordinary movement.",
        "No training stress is added to prove toughness.",
    ],
    expected_adaptations=[
        "Reduced event fatigue.",
        "Restored basic movement quality.",
        "Clearer next-cycle readiness.",
    ],
    progression_rules=[
        "Progress from rest to easy movement to short easy running.",
        "Resume structure only when basic recovery markers are stable.",
    ],
    regression_rules=[
        "Return to rest or walking if running feels mechanically poor or emotionally forced.",
        "Extend recovery after unusually damaging descents, heat, or long duration.",
    ],
    watchouts=[
        "Do not judge readiness only by cardiovascular fitness.",
        "Avoid returning to hard training because the race went well.",
    ],
    placement_guidance=[
        "Place immediately after a major event.",
        "Can lead into reduced-load adaptation, transition bridge, off-season, or maintenance.",
    ],
    additional_information="Post-race recovery respects the full event cost. The block protects the athlete from turning one good performance into the start of a fatigue spiral.",
)


mainstream_reduced_load_adaptation_block = _mainstream_mezzo(
    id="mezzo_020",
    slug="mainstream-reduced-load-adaptation-block",
    title="Reduced-Load Adaptation Block",
    parent_macro_id="macro_007",
    parent_tag="recovery_and_transition",
    summary="A recovery block that lowers load so previous training can be absorbed and reviewed.",
    purpose="Consolidate adaptation after demanding training, accumulated fatigue, or a block that needs a lower-cost follow-up.",
    tags=["recovery_and_transition", "reduced_load", "adaptation"],
    goal_race_context=[
        "Use after a demanding block when the athlete needs recovery before the next progression.",
        "Fits non-race fatigue, training plateaus, or warning signs from accumulated load.",
        "Useful inside longer plans that need planned relief.",
    ],
    training_profile=[
        "Lower volume, lower density, and mostly easy running.",
        "Small familiar movement may remain if it supports rhythm.",
        "The block reviews response to the previous work before choosing the next step.",
    ],
    expected_adaptations=[
        "Better absorption of previous training.",
        "Reduced accumulated fatigue.",
        "Improved clarity about what the next block should be.",
    ],
    progression_rules=[
        "Return to normal load only after recovery markers improve.",
        "Use the block to decide whether to progress, repeat, or redirect.",
    ],
    regression_rules=[
        "Reduce further if easy running does not feel easy.",
        "Shift to post-race-style recovery if fatigue is deeper than expected.",
    ],
    watchouts=[
        "Do not fill recovery weeks with hidden intensity.",
        "Avoid interpreting freshness late in the block as a reason to cram.",
    ],
    placement_guidance=[
        "Place after high-load or high-intensity blocks.",
        "Can precede capacity, race-specific, or maintenance work depending on response.",
    ],
    additional_information="Reduced load is not wasted time. It is where the coach checks whether the previous work became adaptation or merely fatigue.",
)


mainstream_transition_bridge_block = _mainstream_mezzo(
    id="mezzo_021",
    slug="mainstream-transition-bridge-block",
    title="Transition Bridge Block",
    parent_macro_id="macro_007",
    parent_tag="recovery_and_transition",
    summary="A bridge block that moves the athlete from recovery toward the next appropriate training direction.",
    purpose="Reintroduce structure after recovery while deciding whether the next phase should build, maintain, or decompress.",
    tags=["recovery_and_transition", "transition", "bridge"],
    goal_race_context=[
        "Use when the athlete is no longer in acute recovery but not ready for full development.",
        "Fits the space between seasons, goals, or demanding blocks.",
        "Useful when the next objective is still uncertain.",
    ],
    training_profile=[
        "Simple aerobic rhythm with optional light strides, mobility, or terrain familiarity.",
        "The block keeps cost moderate and decisions flexible.",
        "Training reveals readiness rather than forcing a predetermined next phase.",
    ],
    expected_adaptations=[
        "Restored training structure.",
        "Clearer next-phase readiness.",
        "Smoother transition from recovery to purposeful work.",
    ],
    progression_rules=[
        "Add structure only when recovery remains stable.",
        "Choose the next macro phase from response, goals, and timing.",
    ],
    regression_rules=[
        "Return to reduced-load adaptation if fatigue reappears.",
        "Move to off-season if motivation or life context needs decompression.",
    ],
    watchouts=[
        "Do not drift into an unplanned build.",
        "Avoid using transition as a place to hide missed training.",
    ],
    placement_guidance=[
        "Place after post-race recovery or reduced-load adaptation.",
        "Can lead into base, maintenance, off-season, or return-to-consistency.",
    ],
    additional_information="Transition is a decision bridge. It lets the athlete resume useful structure without pretending the next big training direction is already obvious.",
)


mainstream_low_pressure_aerobic_rhythm_block = _mainstream_mezzo(
    id="mezzo_022",
    slug="mainstream-low-pressure-aerobic-rhythm-block",
    title="Low-Pressure Aerobic Rhythm Block",
    parent_macro_id="macro_008",
    parent_tag="off_season",
    summary="An off-season block that keeps easy aerobic rhythm without performance pressure.",
    purpose="Preserve enough running continuity while giving the athlete a break from race preparation.",
    tags=["off_season", "aerobic_rhythm", "low_pressure"],
    goal_race_context=[
        "Use when the athlete is between goal cycles and needs decompression.",
        "Fits runners who benefit from movement continuity but not structured development.",
        "Useful when complete inactivity would make returning harder.",
    ],
    training_profile=[
        "Easy, flexible aerobic running or hiking with low performance pressure.",
        "Volume is enough to maintain rhythm but not enough to feel like a build.",
        "Trail movement can be playful and low consequence.",
    ],
    expected_adaptations=[
        "Preserved basic aerobic rhythm.",
        "Reduced pressure from structured preparation.",
        "Easier re-entry into future base work.",
    ],
    progression_rules=[
        "Progress only if the athlete wants more movement and recovery remains easy.",
        "Keep effort and structure relaxed.",
    ],
    regression_rules=[
        "Reduce frequency if the block starts feeling like another training cycle.",
        "Use walking, hiking, or cross-training when running feels stale.",
    ],
    watchouts=[
        "Do not turn off-season rhythm into secret base building.",
        "Avoid judging the block by fitness gain.",
    ],
    placement_guidance=[
        "Place after recovery or at the start of off-season.",
        "Can run alongside strength, mobility, or movement-variety blocks.",
    ],
    additional_information="This block keeps the thread of running alive without pulling the athlete back into race-prep pressure too soon.",
)


mainstream_general_strength_and_mobility_block = _mainstream_mezzo(
    id="mezzo_023",
    slug="mainstream-general-strength-and-mobility-block",
    title="General Strength And Mobility Block",
    parent_macro_id="macro_008",
    parent_tag="off_season",
    summary="An off-season support block for rebuilding general strength, mobility, and movement options.",
    purpose="Use lower race pressure to address supportive qualities that are harder to develop during specific preparation.",
    tags=["off_season", "strength", "mobility"],
    goal_race_context=[
        "Use away from key races when support work can receive more attention.",
        "Fits athletes who need better general capacity before the next build.",
        "Useful when running load is intentionally lower.",
    ],
    training_profile=[
        "General strength, mobility, balance, and control work selected for the athlete's needs.",
        "Running load stays moderate enough to absorb support work.",
        "The block can include non-running movement that improves general robustness.",
    ],
    expected_adaptations=[
        "Improved general strength and mobility.",
        "More options for future training progressions.",
        "Better readiness for later running-specific support work.",
    ],
    progression_rules=[
        "Progress load or complexity gradually while movement quality remains high.",
        "Keep enough aerobic rhythm to avoid a hard restart later.",
    ],
    regression_rules=[
        "Reduce strength dose if soreness interferes with basic running rhythm.",
        "Simplify exercises when control or consistency is poor.",
    ],
    watchouts=[
        "Do not create a gym peak that compromises future running.",
        "Avoid novelty overload just because the season is less specific.",
    ],
    placement_guidance=[
        "Place in off-season after acute recovery.",
        "Can precede base strength support in the next cycle.",
    ],
    additional_information="Off-season is often the best time to widen the athlete's physical toolkit. The block should build options, not distract from future running.",
)


mainstream_movement_variety_block = _mainstream_mezzo(
    id="mezzo_024",
    slug="mainstream-movement-variety-block",
    title="Movement Variety Block",
    parent_macro_id="macro_008",
    parent_tag="off_season",
    summary="An off-season block that restores freshness through varied, low-stakes movement.",
    purpose="Reduce monotony, preserve general fitness, and refresh motivation through purposeful variety.",
    tags=["off_season", "movement_variety", "cross_training"],
    goal_race_context=[
        "Use when the athlete needs a mental or physical break from normal running structure.",
        "Fits off-season periods without immediate race-specific demands.",
        "Useful when alternative movement can preserve fitness with lower impact or pressure.",
    ],
    training_profile=[
        "Hiking, cycling, skiing, strength circuits, mobility, easy running, or other suitable movement.",
        "The block keeps intensity and volume controlled enough to support freshness.",
        "Trail exploration is welcome when route risk and recovery cost stay proportionate.",
    ],
    expected_adaptations=[
        "Improved mental freshness.",
        "Maintained general aerobic and movement capacity.",
        "Reduced repetitive stress from one narrow pattern.",
    ],
    progression_rules=[
        "Increase variety only when it remains recoverable and enjoyable.",
        "Keep at least a small running thread if future running restart matters.",
    ],
    regression_rules=[
        "Simplify if variety becomes chaotic or fatiguing.",
        "Return to low-pressure aerobic rhythm if the athlete needs more consistency.",
    ],
    watchouts=[
        "Do not let fun novelty become hidden high load.",
        "Avoid risky technical adventures when the athlete is supposed to be decompressing.",
    ],
    placement_guidance=[
        "Place during off-season after acute race recovery.",
        "Can support motivation before the next base phase.",
    ],
    additional_information="Variety has a job here: refresh the runner and maintain general capacity. It is not random training in costume.",
)


mainstream_aerobic_maintenance_block = _mainstream_mezzo(
    id="mezzo_025",
    slug="mainstream-aerobic-maintenance-block",
    title="Aerobic Maintenance Block",
    parent_macro_id="macro_009",
    parent_tag="maintenance",
    summary="A maintenance block that preserves aerobic fitness with controlled cost.",
    purpose="Hold useful endurance when full development is not the right objective.",
    tags=["maintenance", "aerobic", "controlled_cost"],
    goal_race_context=[
        "Use between goals, during busy life periods, or when the athlete needs stability.",
        "Fits runners who want to preserve fitness without building aggressively.",
        "Useful before a later return to base or capacity development.",
    ],
    training_profile=[
        "Regular easy aerobic running at a sustainable dose.",
        "Longer outings may remain, but without full development pressure.",
        "Terrain cost is kept familiar and manageable.",
    ],
    expected_adaptations=[
        "Preserved aerobic fitness.",
        "Maintained training rhythm.",
        "Reduced cost compared with development blocks.",
    ],
    progression_rules=[
        "Hold a repeatable dose rather than escalating.",
        "Use small changes only to maintain engagement or terrain familiarity.",
    ],
    regression_rules=[
        "Reduce volume when life stress or fatigue rises.",
        "Shift to return-to-consistency if maintenance rhythm breaks down.",
    ],
    watchouts=[
        "Do not let maintenance become an unplanned build.",
        "Avoid judging the block by rapid improvement.",
    ],
    placement_guidance=[
        "Place between major goals or during constraints.",
        "Can precede base development once a new goal is chosen.",
    ],
    additional_information="Maintenance is successful when the athlete remains available, capable, and ready for the next real training direction.",
)


mainstream_quality_touchpoint_block = _mainstream_mezzo(
    id="mezzo_026",
    slug="mainstream-quality-touchpoint-block",
    title="Quality Touchpoint Block",
    parent_macro_id="macro_009",
    parent_tag="maintenance",
    summary="A maintenance block that keeps a small amount of quality without starting a full build.",
    purpose="Preserve coordination, controlled intensity, or confidence while keeping total training cost low.",
    tags=["maintenance", "quality", "touchpoint"],
    goal_race_context=[
        "Use when the athlete benefits from small quality reminders between development phases.",
        "Fits experienced runners who lose sharpness or confidence with only easy running.",
        "Useful when full capacity development would be too costly.",
    ],
    training_profile=[
        "Small doses of strides, controlled intervals, hills, or steady work.",
        "Easy aerobic running remains the main weekly content.",
        "Touchpoints are familiar and recoverable.",
    ],
    expected_adaptations=[
        "Preserved neuromuscular or controlled-intensity feel.",
        "Better readiness to resume future quality work.",
        "Maintained confidence without high training cost.",
    ],
    progression_rules=[
        "Keep quality small and repeatable.",
        "Progress only by improving control, not by turning the block into development.",
    ],
    regression_rules=[
        "Remove quality first if recovery or life stress worsens.",
        "Use strides or short hills instead of longer intensity if fatigue is uncertain.",
    ],
    watchouts=[
        "Do not sneak a capacity block into maintenance.",
        "Avoid adding quality when basic aerobic rhythm is already strained.",
    ],
    placement_guidance=[
        "Place inside maintenance when some quality should be preserved.",
        "Can precede capacity development if the athlete later chooses a goal.",
    ],
    additional_information="A touchpoint is deliberately small. The block should keep a quality alive without asking the athlete to develop it fully.",
    suitable_levels=[TrainingLevel.INTERMEDIATE, TrainingLevel.ADVANCED, TrainingLevel.ELITE],
)


mainstream_constraint_friendly_consistency_block = _mainstream_mezzo(
    id="mezzo_027",
    slug="mainstream-constraint-friendly-consistency-block",
    title="Constraint-Friendly Consistency Block",
    parent_macro_id="macro_009",
    parent_tag="maintenance",
    summary="A maintenance block that preserves training through busy, uncertain, or limited life periods.",
    purpose="Keep the athlete connected to running when time, travel, work, family, or stress limits training ambition.",
    tags=["maintenance", "constraints", "consistency"],
    goal_race_context=[
        "Use when life constraints make a normal build unrealistic.",
        "Fits athletes who want to preserve a floor of fitness and confidence.",
        "Useful during travel, heavy work periods, caregiving load, or uncertain schedules.",
    ],
    training_profile=[
        "Short, flexible, high-value sessions that preserve rhythm.",
        "Intensity and terrain are chosen for reliability rather than ambition.",
        "The block protects the athlete from all-or-nothing thinking.",
    ],
    expected_adaptations=[
        "Maintained consistency under constraint.",
        "Reduced loss of fitness and confidence.",
        "A smoother return to fuller training later.",
    ],
    progression_rules=[
        "Add training only when the constraint actually eases.",
        "Prioritise the smallest repeatable dose before optional extras.",
    ],
    regression_rules=[
        "Use shorter sessions, fewer days, or cross-training when constraints tighten.",
        "Shift to return-to-consistency if the routine fully breaks.",
    ],
    watchouts=[
        "Do not pretend a constrained period is a hidden build.",
        "Avoid guilt-driven sessions that compromise recovery or life stability.",
    ],
    placement_guidance=[
        "Place when maintenance is needed because context, not ambition, is the limiter.",
        "Can lead back to base, return-to-consistency, or continued maintenance.",
    ],
    additional_information="This block is a pressure valve. It keeps the athlete in the sport while respecting the reality that not every season can be a build.",
)


MAINSTREAM_MEZZO_CARDS = [
    mainstream_reentry_rhythm_block,
    mainstream_easy_aerobic_reconditioning_block,
    mainstream_movement_strength_reintroduction_block,
    mainstream_aerobic_volume_block,
    mainstream_long_endurance_development_block,
    mainstream_strength_and_movement_support_block,
    mainstream_trail_skill_and_terrain_familiarity_block,
    mainstream_threshold_control_block,
    mainstream_aerobic_power_block,
    mainstream_strength_endurance_block,
    mainstream_course_demands_block,
    mainstream_race_execution_practice_block,
    mainstream_fueling_and_hydration_practice_block,
    mainstream_taper_freshness_block,
    mainstream_sharpening_touchpoint_block,
    mainstream_race_readiness_check_block,
    mainstream_between_race_recovery_block,
    mainstream_race_season_maintenance_block,
    mainstream_competition_learning_block,
    mainstream_post_race_recovery_block,
    mainstream_reduced_load_adaptation_block,
    mainstream_transition_bridge_block,
    mainstream_low_pressure_aerobic_rhythm_block,
    mainstream_general_strength_and_mobility_block,
    mainstream_movement_variety_block,
    mainstream_aerobic_maintenance_block,
    mainstream_quality_touchpoint_block,
    mainstream_constraint_friendly_consistency_block,
]
