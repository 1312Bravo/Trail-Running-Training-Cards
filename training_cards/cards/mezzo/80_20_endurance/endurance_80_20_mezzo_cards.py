from training_cards.philosophy_profiles import ENDURANCE_80_20
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
        philosophy_profile_ids=[ENDURANCE_80_20],
        summary=summary,
        purpose=purpose,
        tags=["80_20_endurance", "mezzo", *tags],
        goal_race_context=[
            "Use when the athlete wants an 80/20-informed block rather than a generic endurance block.",
            "Most useful when intensity distribution, trail cost, or quality spacing changes the planning decision.",
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


endurance_80_20_low_intensity_volume_block = _card(
    id="mezzo_029",
    slug="endurance-80-20-low-intensity-volume-block",
    title="80/20 Low-Intensity Volume Block",
    parent_macro_id="macro_010",
    parent_tag="80_20_base",
    summary="A base block that grows aerobic volume while protecting the low-intensity majority.",
    purpose="Build durable aerobic volume without letting ordinary runs drift into moderate grey-zone stress.",
    tags=["base", "low_intensity", "volume"],
    training_profile=[
        "Most running stays clearly easy by effort, heart rate, talk test, or terrain-adjusted perception.",
        "Volume increases are conservative enough that easy days still feel easy by the end of the week.",
        "Short strides or light neuromuscular touches can appear only if they do not change the block's low-intensity character.",
    ],
    expected_adaptations=[
        "Greater aerobic durability at low physiological cost.",
        "Improved discipline around easy running and terrain-adjusted effort.",
        "More weekly training capacity without needing frequent hard sessions.",
    ],
    progression_rules=[
        "Add easy time before adding intensity.",
        "Use terrain substitutions when climbing would turn an easy run into hidden moderate work.",
        "Progress only when the athlete can repeat the week without accumulating background fatigue.",
    ],
    regression_rules=[
        "Reduce total duration if easy runs require concentration to stay controlled.",
        "Flatten routes, add hiking, or split runs if trail cost pushes too much time above easy.",
    ],
    watchouts=[
        "Do not chase pace on easy days.",
        "Do not count steep hiking, technical descents, or heat-stressed running as automatically easy.",
    ],
    placement_guidance=[
        "Place early in an 80/20 base macro phase.",
        "Use before high-intensity quality when the athlete needs more low-cost volume.",
    ],
    additional_information="This block is the practical heart of 80/20 base work: the athlete earns more training by keeping most training truly easy.",
)


endurance_80_20_long_endurance_distribution_block = _card(
    id="mezzo_030",
    slug="endurance-80-20-long-endurance-distribution-block",
    title="80/20 Long Endurance Distribution Block",
    parent_macro_id="macro_010",
    parent_tag="80_20_base",
    summary="A long-endurance block that accounts for duration, climbing, descents, and hidden hard cost.",
    purpose="Develop long-run durability while keeping the total block consistent with 80/20 stress balance.",
    tags=["base", "long_run", "distribution"],
    training_profile=[
        "Long outings are mostly easy but may include planned terrain exposure if the cost is understood.",
        "Climb, descent, altitude, heat, and technicality are counted as stress even when pace looks slow.",
        "The rest of the week supports the long run instead of quietly adding more moderate load.",
    ],
    expected_adaptations=[
        "Improved long-duration aerobic tolerance.",
        "Better terrain-cost awareness during long outings.",
        "Stronger recovery rhythm after long aerobic stress.",
    ],
    progression_rules=[
        "Progress one major stress at a time: duration, vertical, technicality, heat, or intensity.",
        "Keep the following day low cost unless recovery is clearly robust.",
        "Use back-off weeks when long-run cost rises even if mileage does not.",
    ],
    regression_rules=[
        "Shorten or simplify the long run if it forces multiple compromised days afterward.",
        "Replace steep running with hiking when effort control is more important than pace.",
    ],
    watchouts=[
        "Do not let every long run become a race-specific simulation.",
        "Watch for athletes who call a run easy because it was slow, while the muscular cost was high.",
    ],
    placement_guidance=[
        "Place after low-intensity volume is stable.",
        "Use before race-specific preparation when the athlete needs durable long-run support.",
    ],
    additional_information="In trail running, the long run can be the easiest-looking hard workout in the plan. This card makes that cost visible.",
)


endurance_80_20_planned_moderate_work_block = _card(
    id="mezzo_031",
    slug="endurance-80-20-planned-moderate-work-block",
    title="80/20 Planned Moderate Work Block",
    parent_macro_id="macro_011",
    parent_tag="80_20_capacity",
    summary="A capacity block where moderate work is deliberate, dosed, and protected from spillover.",
    purpose="Use threshold-adjacent work only when it has a clear job inside the broader intensity distribution.",
    tags=["capacity", "moderate_intensity", "threshold_control"],
    training_profile=[
        "Moderate work is scheduled, named, and separated from accidental steady running.",
        "Easy days around the workout are kept easy enough to preserve the intended contrast.",
        "Terrain and fatigue are monitored so moderate work does not become too frequent by stealth.",
    ],
    expected_adaptations=[
        "Improved controlled moderate-effort tolerance.",
        "Better ability to distinguish productive moderate work from habitual grey-zone running.",
        "More reliable recovery between quality sessions.",
    ],
    progression_rules=[
        "Increase moderate volume only when easy-running quality remains intact.",
        "Keep the workout purpose stable before changing duration, grade, or intensity.",
        "Use subjective effort alongside metrics when trails distort pace or heart rate.",
    ],
    regression_rules=[
        "Reduce moderate duration if easy days begin to feel steady.",
        "Return to low-intensity volume if the athlete cannot recover from planned moderate work.",
    ],
    watchouts=[
        "Do not use moderate work as the default solution for every fitness goal.",
        "Avoid stacking moderate terrain, moderate pace, and fatigue in the same week.",
    ],
    placement_guidance=[
        "Place after a stable base block.",
        "Use when threshold control is useful but high-intensity work is not the primary limiter.",
    ],
    additional_information="80/20 does not ban moderate training; it asks the coach to be honest about when moderate work is purposeful and when it is just drift.",
)


endurance_80_20_high_intensity_quality_block = _card(
    id="mezzo_032",
    slug="endurance-80-20-high-intensity-quality-block",
    title="80/20 High-Intensity Quality Block",
    parent_macro_id="macro_011",
    parent_tag="80_20_capacity",
    summary="A quality block that adds hard work without sacrificing the low-intensity support system.",
    purpose="Develop high-intensity capacity while preserving enough easy training and recovery to make the hard work absorbable.",
    tags=["capacity", "high_intensity", "quality_spacing"],
    training_profile=[
        "Hard sessions are few, clear, and surrounded by genuinely low-cost running.",
        "Session difficulty is controlled by purpose, not by turning every quality day into a maximal test.",
        "Weekly load is judged by the total stress mix, including terrain and life fatigue.",
    ],
    expected_adaptations=[
        "Improved ability to produce high-quality hard work.",
        "Better hard-easy contrast across the week.",
        "Lower risk of turning a capacity block into chronic moderate stress.",
    ],
    progression_rules=[
        "Progress hard-session volume only when easy volume and recovery remain stable.",
        "Add intensity before adding extra hard days.",
        "Use simpler terrain when physiological intensity is the target.",
    ],
    regression_rules=[
        "Reduce repetitions, duration, or frequency if quality fades across sessions.",
        "Replace a hard day with easy running if soreness or fatigue changes movement quality.",
    ],
    watchouts=[
        "Do not add hard work on top of a week already made hard by vertical, heat, or racing.",
        "Avoid counting every uphill push as harmless because speed is low.",
    ],
    placement_guidance=[
        "Place after base development when the athlete has stable easy volume.",
        "Use before race-specific preparation if the athlete needs a sharper capacity stimulus.",
    ],
    additional_information="The block should make hard work better, not just more frequent. The easy side of the ratio is what allows that.",
)


endurance_80_20_hill_strength_quality_block = _card(
    id="mezzo_033",
    slug="endurance-80-20-hill-strength-quality-block",
    title="80/20 Hill Strength Quality Block",
    parent_macro_id="macro_011",
    parent_tag="80_20_capacity",
    summary="A hill-strength block that counts muscular and climbing stress as real hard work.",
    purpose="Develop hill-related strength endurance while preserving 80/20 recovery accounting.",
    tags=["capacity", "hill_strength", "trail_cost"],
    training_profile=[
        "Hill efforts are treated as quality stress even when pace or heart rate underreports the load.",
        "The block uses enough easy terrain to absorb local muscular stress from climbs and descents.",
        "Technical or steep routes are chosen only when they serve the intended strength-quality goal.",
    ],
    expected_adaptations=[
        "Improved uphill strength endurance.",
        "Better recognition of local muscular cost.",
        "More realistic recovery planning after hill-focused work.",
    ],
    progression_rules=[
        "Progress grade, duration, or repetition count one at a time.",
        "Keep downhill exposure conservative when uphill force is the main target.",
        "Allow extra recovery when soreness outlasts cardiovascular fatigue.",
    ],
    regression_rules=[
        "Reduce steepness or repetition count if form deteriorates.",
        "Move hill work to smoother terrain if technical demand obscures the training purpose.",
    ],
    watchouts=[
        "Do not hide extra hard work inside scenic climbing days.",
        "Watch for delayed soreness from descents after uphill-focused sessions.",
    ],
    placement_guidance=[
        "Place in capacity development after low-intensity volume is stable.",
        "Use before race-specific climbing work when hill strength is a limiter.",
    ],
    additional_information="This card keeps 80/20 honest on trails: hard is not only a pace or heart-rate number.",
)


endurance_80_20_distribution_safe_course_demands_block = _card(
    id="mezzo_034",
    slug="endurance-80-20-distribution-safe-course-demands-block",
    title="80/20 Distribution-Safe Course Demands Block",
    parent_macro_id="macro_012",
    parent_tag="80_20_race_specific",
    summary="A race-specific block that adds course demands without dissolving into constant moderate stress.",
    purpose="Prepare for terrain, grade, surface, and duration demands while preserving purposeful intensity distribution.",
    tags=["race_specific", "course_demands", "distribution"],
    training_profile=[
        "Course-specific work is selected by the race limiter, not by trying to simulate everything at once.",
        "Specific terrain exposure is balanced with enough easy running to absorb the added cost.",
        "Race-pace or race-effort work is planned explicitly rather than appearing in every terrain session.",
    ],
    expected_adaptations=[
        "Improved readiness for race-specific terrain.",
        "Better ability to keep specificity from becoming chronic grey-zone running.",
        "Clearer trade-offs between specificity and recovery.",
    ],
    progression_rules=[
        "Add one specificity variable at a time: vertical, surface, duration, weather, or effort.",
        "Use easier routes when the week's distribution is already strained.",
        "Move toward simulation only after the athlete handles smaller specific exposures.",
    ],
    regression_rules=[
        "Return to controlled capacity or base work if specific terrain causes persistent fatigue.",
        "Reduce race-effort segments when climbing or technicality already supplies enough stress.",
    ],
    watchouts=[
        "Do not turn race specificity into weekly racing.",
        "Do not ignore muscular cost just because the athlete remained mostly below threshold by heart rate.",
    ],
    placement_guidance=[
        "Place after capacity development when the event demands are known.",
        "Use before taper when course-specific confidence is still needed.",
    ],
    additional_information="The block answers a very 80/20 trail question: how do we become specific without making every week medium-hard?",
)


endurance_80_20_race_counted_recovery_block = _card(
    id="mezzo_035",
    slug="endurance-80-20-race-counted-recovery-block",
    title="80/20 Race-Counted Recovery Block",
    parent_macro_id="macro_014",
    parent_tag="80_20_competition",
    summary="A competition block that treats races as hard inputs before adding more training stress.",
    purpose="Protect recovery and future readiness by counting race effort inside the intensity-distribution picture.",
    tags=["competition", "race_recovery", "distribution"],
    training_profile=[
        "Races, tune-ups, and hard group efforts are counted as quality stress.",
        "The post-race week prioritizes low-cost aerobic work unless readiness clearly supports more.",
        "Training resumes based on recovery response, not on the desire to keep the calendar full.",
    ],
    expected_adaptations=[
        "Better recovery after racing.",
        "Fewer accidental overload weeks during competition periods.",
        "Clearer decision-making about the next hard stimulus.",
    ],
    progression_rules=[
        "Add quality only after race soreness, mood, sleep, and easy-run feel have normalized.",
        "Use easy frequency before returning to longer or harder sessions.",
        "Treat technical downhill races as mechanically costly even if duration was short.",
    ],
    regression_rules=[
        "Extend easy recovery if the athlete feels flat or unusually sore.",
        "Skip planned quality if the race already supplied the week's hard stress.",
    ],
    watchouts=[
        "Do not treat a race as separate from training load.",
        "Avoid using a good race result as permission to rush the next block.",
    ],
    placement_guidance=[
        "Place immediately after a race inside an 80/20 competition macro.",
        "Use between closely spaced events when recovery quality determines the next decision.",
    ],
    additional_information="This block prevents the classic race-season mistake: racing hard, then training as if nothing happened.",
)


endurance_80_20_race_season_distribution_maintenance_block = _card(
    id="mezzo_036",
    slug="endurance-80-20-race-season-distribution-maintenance-block",
    title="80/20 Race-Season Distribution Maintenance Block",
    parent_macro_id="macro_014",
    parent_tag="80_20_competition",
    summary="A between-race block that maintains fitness with low-cost volume and sparse quality touchpoints.",
    purpose="Maintain readiness between races without letting frequent competition turn the whole season hard.",
    tags=["competition", "maintenance", "race_season"],
    training_profile=[
        "Most training between races stays low intensity and confidence-building.",
        "Quality touchpoints are small and justified by timing, not habit.",
        "The next race date determines whether the block maintains, sharpens, or simply recovers.",
    ],
    expected_adaptations=[
        "Preserved aerobic rhythm during racing periods.",
        "Better freshness for repeated competitions.",
        "Less background fatigue from unnecessary between-race workouts.",
    ],
    progression_rules=[
        "Use short controlled intensity only when the athlete has recovered from the previous race.",
        "Keep easy volume steady rather than chasing new fitness between close events.",
        "Adjust by race importance: key races need more freshness, low-priority races may support continuity.",
    ],
    regression_rules=[
        "Remove quality if races are frequent or recovery is uncertain.",
        "Reduce long-run cost when competition already provides specific stress.",
    ],
    watchouts=[
        "Do not stack tune-up races, hard workouts, and long technical runs in the same distribution window.",
        "Avoid maintaining fitness by making every run moderately purposeful.",
    ],
    placement_guidance=[
        "Place between races after immediate recovery is complete.",
        "Use when the athlete needs continuity more than another development block.",
    ],
    additional_information="Race season often rewards restraint. This card keeps enough work in the system without pretending there is room for everything.",
)


endurance_80_20_easy_discipline_maintenance_block = _card(
    id="mezzo_037",
    slug="endurance-80-20-easy-discipline-maintenance-block",
    title="80/20 Easy Discipline Maintenance Block",
    parent_macro_id="macro_015",
    parent_tag="80_20_maintenance",
    summary="A maintenance block that protects easy running when time, stress, or motivation is constrained.",
    purpose="Hold endurance continuity without letting every short run become moderately hard.",
    tags=["maintenance", "easy_discipline", "constraints"],
    training_profile=[
        "Runs are short enough and easy enough to fit the athlete's current life.",
        "The block values repeatability more than squeezing intensity into limited time.",
        "Low-cost cross-training or hiking can support consistency when running stress is too high.",
    ],
    expected_adaptations=[
        "Maintained aerobic habit.",
        "Better restraint during constrained periods.",
        "Reduced risk of turning maintenance into chronic stress.",
    ],
    progression_rules=[
        "Add frequency or easy duration before quality.",
        "Keep the week obviously recoverable while outside-life load is high.",
        "Move to base development once constraints ease and easy rhythm is stable.",
    ],
    regression_rules=[
        "Reduce duration if the athlete starts turning every run into a stress release workout.",
        "Use run-walk or hiking if easy running is not staying easy.",
    ],
    watchouts=[
        "Do not use time pressure as a reason to make every session intense.",
        "Watch for athletes who feel guilty unless easy runs are faster than useful.",
    ],
    placement_guidance=[
        "Place during maintenance periods with limited bandwidth.",
        "Use after a race season, during travel, or between larger build phases.",
    ],
    additional_information="This is the quiet 80/20 maintenance skill: keep enough easy work alive without asking a constrained athlete to prove fitness every day.",
)


endurance_80_20_quality_touchpoint_maintenance_block = _card(
    id="mezzo_038",
    slug="endurance-80-20-quality-touchpoint-maintenance-block",
    title="80/20 Quality Touchpoint Maintenance Block",
    parent_macro_id="macro_015",
    parent_tag="80_20_maintenance",
    summary="A maintenance block with small quality touches surrounded by clearly easy support.",
    purpose="Preserve neuromuscular sharpness or aerobic power without turning maintenance into a development phase.",
    tags=["maintenance", "quality_touchpoint", "hard_easy_contrast"],
    training_profile=[
        "Quality is brief, familiar, and placed only when recovery is stable.",
        "Easy work remains the majority and does not creep upward to compensate for lower volume.",
        "The athlete finishes the block feeling ready to build, not relieved to survive.",
    ],
    expected_adaptations=[
        "Preserved touch with faster or stronger running.",
        "Better confidence returning to structured training.",
        "Maintenance of hard-easy contrast during lower-volume periods.",
    ],
    progression_rules=[
        "Use one small touchpoint before adding a second.",
        "Keep intensity familiar rather than introducing new demanding workouts.",
        "Progress back to capacity only after life load and easy volume support it.",
    ],
    regression_rules=[
        "Remove the touchpoint if it compromises consistency or mood.",
        "Return to easy-discipline maintenance if recovery becomes uncertain.",
    ],
    watchouts=[
        "Do not let a touchpoint become a hidden test.",
        "Avoid hard work when the athlete is using maintenance because stress is already high.",
    ],
    placement_guidance=[
        "Place late in maintenance if the athlete is preparing to resume build work.",
        "Use sparingly between races or during constrained training windows.",
    ],
    additional_information="The key word is touchpoint. The block keeps the door open to quality without walking through it every week.",
)


ENDURANCE_80_20_MEZZO_CARDS = [
    endurance_80_20_low_intensity_volume_block,
    endurance_80_20_long_endurance_distribution_block,
    endurance_80_20_planned_moderate_work_block,
    endurance_80_20_high_intensity_quality_block,
    endurance_80_20_hill_strength_quality_block,
    endurance_80_20_distribution_safe_course_demands_block,
    endurance_80_20_race_counted_recovery_block,
    endurance_80_20_race_season_distribution_maintenance_block,
    endurance_80_20_easy_discipline_maintenance_block,
    endurance_80_20_quality_touchpoint_maintenance_block,
]
