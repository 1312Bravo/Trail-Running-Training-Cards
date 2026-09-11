from __future__ import annotations

import re
from dataclasses import dataclass

from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
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
from training_cards.session_families import (
    AEROBIC_POWER_SESSION_FAMILY,
    CONTROLLED_QUALITY_SESSION_FAMILY,
    EASY_SESSION_FAMILY,
    ENDURANCE_SESSION_FAMILY,
    HILL_POWER_SESSION_FAMILY,
    LOW_IMPACT_AEROBIC_SUPPORT_SESSION_FAMILY,
    NEUROMUSCULAR_SESSION_FAMILY,
    RACE_PRACTICE_SESSION_FAMILY,
    RECOVERY_SESSION_FAMILY,
    STEADY_SESSION_FAMILY,
    STRENGTH_ENDURANCE_SESSION_FAMILY,
    STRENGTH_MOBILITY_SUPPORT_SESSION_FAMILY,
    THRESHOLD_SESSION_FAMILY,
    TRAIL_SPECIFIC_SESSION_FAMILY,
)
from training_cards.schemas.session_family import SessionFamily


@dataclass(frozen=True, slots=True)
class _SessionSpec:
    id: str
    title: str
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


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return f"mainstream-{slug}"


def _parents(micro_ids: tuple[str, ...]) -> list[CardReference]:
    return [
        CardReference(
            card_id=micro_id,
            relationship=CardRelationship.PARENT,
            tags=["mainstream_session_fit"],
        )
        for micro_id in micro_ids
    ]


def _part(
    title: str,
    prescription: str,
    duration: str = "",
    rpe: str = "",
    *,
    coaching_notes: str = "",
    terrain_notes: str = "",
    adjustment_notes: str = "",
    selection_notes: str = "",
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


def _option(
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


def _block(
    block_type: WorkoutBlockType,
    options: list[WorkoutOption],
    execution_mode: WorkoutBlockExecutionMode = WorkoutBlockExecutionMode.DO_ALL,
) -> WorkoutBlock:
    return WorkoutBlock(
        block_type=block_type,
        execution_mode=execution_mode,
        options=options,
    )


def _choose_main(options: list[WorkoutOption]) -> WorkoutBlock:
    mode = (
        WorkoutBlockExecutionMode.CHOOSE_ONE
        if len(options) > 1
        else WorkoutBlockExecutionMode.DO_ALL
    )
    return _block(WorkoutBlockType.MAIN, options, mode)


def _running_warmup() -> WorkoutBlock:
    return _block(
        WorkoutBlockType.WARMUP,
        [
            _option(
                "Standard Running Warm-Up",
                [
                    _part(
                        "Easy Running",
                        "Run easily until breathing, legs, and coordination feel settled.",
                        "10-20 minutes",
                        "2-4",
                    ),
                    _part(
                        "Preparatory Pickups",
                        "Add 3-5 relaxed 15-20 second pickups only if the main set is faster than easy running.",
                        "3-6 minutes",
                        "5-7",
                        coaching_notes="The pickups should prepare rhythm, not create fatigue.",
                    ),
                ],
            )
        ],
    )


def _easy_cooldown() -> WorkoutBlock:
    return _block(
        WorkoutBlockType.COOLDOWN,
        [
            _option(
                "Easy Cooldown",
                [
                    _part(
                        "Easy Running Or Walking",
                        "Move very easily until breathing and legs settle.",
                        "5-20 minutes",
                        "1-3",
                    )
                ],
            )
        ],
    )


def _mainstream_session(spec: _SessionSpec) -> SessionCard:
    return SessionCard(
        id=spec.id,
        slug=_slugify(spec.title),
        title=spec.title,
        card_type=CardType.SESSION,
        suitable_levels=[TrainingLevel.ALL],
        philosophy_profile_ids=[MAINSTREAM_ENDURANCE],
        summary=spec.summary,
        purpose=spec.purpose,
        tags=["mainstream_endurance", "session", *spec.tags],
        goal_race_context=[
            "Use when this workout concept matches the selected micro week's key session role.",
            "Place only when athlete readiness, recovery, terrain access, and current training phase support the intended stimulus.",
        ],
        training_profile=list(spec.training_profile),
        expected_adaptations=list(spec.expected_adaptations),
        watchouts=list(spec.watchouts),
        progression_rules=[
            "Progress by choosing a slightly larger option only when the athlete executes the current option calmly and recovers predictably.",
            "Change one main variable at a time: duration, repetition count, recovery, intensity, terrain, vertical load, or complexity.",
        ],
        regression_rules=[
            "Choose a shorter, easier, flatter, or lower-complexity option when readiness is uncertain.",
            "Replace the session with an easy, recovery, or rest option when the intended stimulus no longer fits the athlete's current state.",
        ],
        additional_information=(
            "This session card defines a reusable workout concept. Exact daily prescription should be selected from the "
            "workout options while preserving the session purpose and the parent micro week's role."
        ),
        references=_parents(spec.parent_micro_ids),
        session_family=spec.session_family,
        typical_duration=spec.typical_duration,
        workout_blocks=list(spec.workout_blocks),
    )


_SPECS: tuple[_SessionSpec, ...] = (
    _SessionSpec(
        "session_001",
        "Rest Day",
        RECOVERY_SESSION_FAMILY,
        ("micro_001", "micro_002", "micro_004", "micro_009", "micro_012", "micro_028", "micro_035", "micro_036", "micro_040", "micro_041", "micro_042", "micro_045", "micro_047", "micro_048", "micro_049", "micro_050", "micro_052", "micro_053", "micro_054", "micro_057", "micro_058", "micro_062", "micro_064"),
        "Full day",
        "A deliberate no-training day used to protect recovery, adaptation, and readiness.",
        "Make rest an intentional training decision rather than an absence of useful work.",
        ("recovery", "rest"),
        ("No structured training load.", "Useful when recovery is the highest-value input."),
        ("Improved freshness and adaptation opportunity.", "Reduced accumulated fatigue."),
        ("Do not fill the day with hidden strenuous activity.", "Avoid treating rest as failure when it is the right prescription."),
        (
            _choose_main(
                [
                    _option("Full Rest", [_part("Rest", "No structured exercise.", coaching_notes="Prioritize sleep, food, hydration, and normal life recovery.")]),
                    _option("Travel Or Logistics Rest", [_part("Rest With Logistics Focus", "Skip training and use the day to reduce travel, gear, or schedule stress.")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_002",
        "Walk Or Gentle Movement",
        RECOVERY_SESSION_FAMILY,
        ("micro_001", "micro_025", "micro_047", "micro_048", "micro_054", "micro_056", "micro_060", "micro_064"),
        "10-60 minutes",
        "Very gentle movement that supports recovery or re-entry without becoming training stress.",
        "Preserve circulation, confidence, and routine when running would add too much cost.",
        ("recovery", "walking", "gentle_movement"),
        ("Very low intensity movement.", "Flexible duration according to soreness and energy."),
        ("Improved recovery rhythm.", "Better confidence during return-to-movement periods."),
        ("Do not turn gentle movement into a hike workout.", "Stop if pain, soreness, or fatigue worsens."),
        (
            _choose_main(
                [
                    _option("Easy Walk", [_part("Gentle Walk", "Walk easily on low-risk terrain.", "10-40 minutes", "1-2")]),
                    _option("Gentle Hike", [_part("Gentle Hike", "Hike easily on familiar terrain with minimal descent cost.", "20-60 minutes", "1-3")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_003",
        "Mobility Reset",
        STRENGTH_MOBILITY_SUPPORT_SESSION_FAMILY,
        ("micro_005", "micro_006", "micro_012", "micro_013", "micro_014", "micro_016", "micro_035", "micro_038", "micro_041", "micro_045", "micro_047", "micro_049", "micro_050", "micro_052", "micro_055", "micro_056", "micro_058", "micro_060", "micro_062", "micro_064"),
        "10-30 minutes",
        "A low-load mobility session that restores movement quality without adding training strain.",
        "Support recovery, range of motion, and basic coordination when the day should stay low cost.",
        ("mobility", "support", "recovery"),
        ("Low-load mobility and tissue-care work.", "No meaningful endurance or strength stress."),
        ("Improved movement comfort.", "Better readiness for later easy training."),
        ("Avoid aggressive stretching or novelty that creates soreness.", "Do not use mobility to hide another workout."),
        (
            _choose_main(
                [
                    _option("Mobility Flow", [_part("Mobility Flow", "Move through easy hips, ankles, thoracic spine, and calf mobility.", "10-20 minutes", "1-2")]),
                    _option("Recovery Reset", [_part("Gentle Reset", "Use relaxed mobility plus breathing or easy tissue care.", "15-30 minutes", "1-2")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_004",
        "Light Activation Strength",
        STRENGTH_MOBILITY_SUPPORT_SESSION_FAMILY,
        ("micro_005", "micro_006", "micro_014", "micro_023", "micro_056", "micro_063"),
        "10-30 minutes",
        "A low-dose strength or activation session that supports movement without creating soreness.",
        "Prepare or preserve movement quality while keeping the training day low cost.",
        ("activation", "strength", "support"),
        ("Low-load activation, coordination, and simple strength.", "Placed so running quality is not compromised."),
        ("Better movement readiness.", "Low-risk return to strength habits."),
        ("Avoid exercises that create next-day soreness.", "Do not add plyometrics or heavy strength when the week calls for support."),
        (
            _choose_main(
                [
                    _option("Activation Circuit", [_part("Activation Circuit", "Complete easy glute, calf, core, and balance activation.", "10-20 minutes", "2-4")]),
                    _option("Pre-Run Movement Prep", [_part("Movement Prep", "Use light drills and activation before easy running.", "8-15 minutes", "2-4")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_005",
        "General Strength Session",
        STRENGTH_MOBILITY_SUPPORT_SESSION_FAMILY,
        ("micro_055",),
        "25-50 minutes",
        "A general strength session that builds durable movement capacity without needing race specificity.",
        "Develop broad strength, control, and tissue capacity that can support future running work.",
        ("strength", "general_strength"),
        ("General strength is the primary stress.", "Running stays secondary or easy around the session."),
        ("Improved general durability.", "Better movement control and strength reserve."),
        ("Avoid excessive soreness that disrupts running.", "Do not chase gym load when the plan needs freshness."),
        (
            _choose_main(
                [
                    _option("Intro General Strength", [_part("General Strength Circuit", "Use controlled bodyweight or light resistance movements.", "20-35 minutes", "3-5")], selection_notes="Best when returning to strength or learning exercises."),
                    _option("Standard General Strength", [_part("General Strength Session", "Use moderate lower-body, core, and posterior-chain strength work.", "30-50 minutes", "4-6")], selection_notes="Best when strength is already tolerated."),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_006",
        "Strength Support Session",
        STRENGTH_MOBILITY_SUPPORT_SESSION_FAMILY,
        ("micro_013",),
        "20-45 minutes",
        "A running-support strength session placed to improve durability without stealing from key runs.",
        "Support the parent running week through appropriately dosed strength and movement control.",
        ("strength_support", "durability"),
        ("Supportive strength load with careful soreness management.", "Exercises should match the runner's current tolerance."),
        ("Improved running durability.", "Better control under normal training load."),
        ("Avoid heavy eccentric work near key runs.", "Reduce load if easy running feels worse afterward."),
        (
            _choose_main(
                [
                    _option("Durability Circuit", [_part("Support Circuit", "Use controlled single-leg, calf, hip, and trunk work.", "20-35 minutes", "3-5")]),
                    _option("Low-Eccentric Support", [_part("Low-Eccentric Strength", "Use lighter support work when downhill or hard running load is already high.", "15-30 minutes", "2-4")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_007",
        "Run-Walk Re-Entry",
        EASY_SESSION_FAMILY,
        ("micro_001", "micro_002", "micro_048"),
        "15-45 minutes",
        "A conservative run-walk session that rebuilds running tolerance and confidence.",
        "Reintroduce running exposure without asking the athlete to run continuously before they are ready.",
        ("run_walk", "reentry", "easy"),
        ("Alternating easy running and walking.", "Very low to low musculoskeletal and aerobic cost."),
        ("Improved running confidence.", "Gradual tolerance for continuous easy running."),
        ("Avoid racing the run portions.", "Stop or walk more if symptoms or anxiety rise."),
        (
            _choose_main(
                [
                    _option("Intro Run-Walk", [_part("Run-Walk Pattern", "Alternate 1 min easy run with 2 min walk.", "15-30 minutes", "2-4")], selection_notes="Best for early return or very low confidence."),
                    _option("Progressed Run-Walk", [_part("Run-Walk Pattern", "Alternate 3 min easy run with 1-2 min walk.", "20-45 minutes", "2-4")], selection_notes="Best once short run exposures feel calm."),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_008",
        "Short Easy Run",
        EASY_SESSION_FAMILY,
        ("micro_002", "micro_009", "micro_012", "micro_035", "micro_039", "micro_063", "micro_064"),
        "15-40 minutes",
        "A short low-intensity run used when the week needs rhythm without much load.",
        "Provide a small aerobic and routine anchor while keeping recovery cost very low.",
        ("easy", "short_run"),
        ("Continuous easy running at conversational effort.", "Low duration and low complexity."),
        ("Maintained routine.", "Small aerobic support with minimal fatigue."),
        ("Avoid letting a short run become fast because it feels easy.", "Choose simple terrain when recovery matters."),
        (
            _choose_main(
                [
                    _option("Very Short Easy", [_part("Easy Running", "Run continuously at easy conversational effort.", "15-20 minutes", "2-4")]),
                    _option("Short Easy", [_part("Easy Running", "Run continuously at easy conversational effort.", "25-40 minutes", "2-4")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_009",
        "Easy Aerobic Run",
        EASY_SESSION_FAMILY,
        ("micro_003", "micro_004", "micro_007", "micro_008", "micro_009", "micro_013", "micro_014", "micro_015", "micro_016", "micro_017", "micro_019", "micro_020", "micro_022", "micro_023", "micro_024", "micro_026", "micro_030", "micro_034", "micro_037", "micro_038", "micro_042", "micro_043", "micro_044", "micro_046", "micro_049", "micro_051", "micro_052", "micro_053", "micro_054", "micro_055", "micro_057", "micro_058", "micro_059", "micro_060", "micro_061"),
        "30-75 minutes",
        "A low-intensity aerobic run that builds consistency, durability, and recoverable volume.",
        "Build aerobic volume while keeping the session easy enough to support repeatable training.",
        ("easy", "aerobic", "volume"),
        ("Continuous low-intensity running.", "Effort should remain conversational and recoverable."),
        ("Improved aerobic consistency.", "Greater durability through repeatable low-stress volume."),
        ("Do not let the run drift into steady effort.", "Technical climbs or descents can make an easy run harder than intended."),
        (
            _choose_main(
                [
                    _option("Standard Easy Run", [_part("Easy Aerobic Running", "Run continuously at conversational effort.", "30-60 minutes", "2-4", terrain_notes="Use terrain where effort can stay easy.")]),
                    _option("Extended Easy Run", [_part("Easy Aerobic Running", "Run continuously at conversational effort for a slightly longer easy dose.", "60-75 minutes", "2-4", selection_notes="Use only when the week can absorb the duration.")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_010",
        "Recovery Run",
        RECOVERY_SESSION_FAMILY,
        ("micro_003", "micro_007", "micro_008", "micro_010", "micro_011", "micro_017", "micro_019", "micro_022", "micro_024", "micro_026", "micro_028", "micro_030", "micro_031", "micro_033", "micro_034", "micro_037", "micro_041", "micro_042", "micro_043", "micro_044", "micro_046", "micro_048"),
        "15-45 minutes",
        "A very easy run used to support recovery without adding meaningful training stress.",
        "Maintain gentle rhythm while protecting freshness and adaptation from harder work.",
        ("recovery_run", "easy"),
        ("Very easy continuous running or run-walk.", "Lower intensity and usually shorter than a normal easy run."),
        ("Improved recovery rhythm.", "Reduced stiffness without significant fatigue."),
        ("Do not turn recovery into aerobic development.", "Walk instead if running does not feel restorative."),
        (
            _choose_main(
                [
                    _option("Very Easy Jog", [_part("Recovery Jog", "Run very easily, slower than normal easy effort.", "15-30 minutes", "1-3")]),
                    _option("Recovery Run-Walk", [_part("Recovery Run-Walk", "Alternate relaxed jogging with walking as needed.", "15-40 minutes", "1-3")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_011",
        "Aerobic Support Run",
        EASY_SESSION_FAMILY,
        ("micro_010", "micro_018", "micro_021", "micro_052"),
        "35-75 minutes",
        "An easy aerobic run placed to support key work rather than become the week's focal stress.",
        "Maintain aerobic rhythm around a key session while protecting the micro week's main purpose.",
        ("easy", "support_run"),
        ("Low-intensity aerobic running.", "Placed before or after key work according to recovery needs."),
        ("Better aerobic continuity.", "Improved support for quality or endurance sessions."),
        ("Do not extend support runs until they compromise key work.", "Keep terrain simple when the key session is demanding."),
        (
            _choose_main(
                [
                    _option("Short Support Run", [_part("Easy Support Running", "Run easily and stop before fatigue builds.", "30-45 minutes", "2-4")]),
                    _option("Normal Support Run", [_part("Easy Support Running", "Run easily at a normal support dose.", "45-75 minutes", "2-4")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_012",
        "Long Easy Run",
        ENDURANCE_SESSION_FAMILY,
        ("micro_007", "micro_008", "micro_010", "micro_012", "micro_018", "micro_021", "micro_029", "micro_043", "micro_059", "micro_060"),
        "60-180 minutes",
        "A longer easy aerobic run that develops endurance while staying controlled enough to repeat.",
        "Extend aerobic duration and durability without making the long run a race-like test.",
        ("long_run", "endurance", "easy"),
        ("Longer low-intensity running.", "Higher single-session cost than a normal easy run."),
        ("Improved endurance durability.", "Better tolerance for longer aerobic outings."),
        ("Avoid adding intensity, terrain novelty, and duration at the same time.", "Fuel when duration makes it relevant."),
        (
            _choose_main(
                [
                    _option("Intro Long Easy Run", [_part("Long Easy Running", "Run longer than normal at easy conversational effort.", "60-90 minutes", "2-4")]),
                    _option("Standard Long Easy Run", [_part("Long Easy Running", "Run at easy conversational effort with fueling if needed.", "90-150 minutes", "2-4")]),
                    _option("Extended Long Easy Run", [_part("Long Easy Running", "Run an extended easy outing only when recovery and phase support it.", "150-180 minutes", "2-4")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_013",
        "Time-On-Feet Outing",
        ENDURANCE_SESSION_FAMILY,
        ("micro_010", "micro_011"),
        "90-300 minutes",
        "A long low-intensity outing where duration, hiking, and terrain time matter more than pace.",
        "Build long-duration tolerance for trail or mountain goals without forcing continuous running.",
        ("time_on_feet", "endurance", "trail"),
        ("Long easy run-hike or hike-run exposure.", "Load is measured by time, vertical cost, and recovery response."),
        ("Improved duration tolerance.", "Better comfort with slow sustainable movement."),
        ("Avoid treating time on feet as permission for uncontrolled adventure fatigue.", "Respect descent and heat cost."),
        (
            _choose_main(
                [
                    _option("Run-Hike Time On Feet", [_part("Easy Run-Hike", "Alternate easy running and hiking by terrain.", "90-180 minutes", "2-4", terrain_notes="Use familiar terrain with manageable descent cost.")]),
                    _option("Long Trail Time On Feet", [_part("Long Easy Trail Outing", "Move continuously at sustainable effort, hiking climbs as needed.", "2-5 hours", "2-4")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_014",
        "Goal-Terrain Endurance Run",
        ENDURANCE_SESSION_FAMILY,
        ("micro_011", "micro_027"),
        "60-240 minutes",
        "An endurance run that uses terrain demands similar to the athlete's goal.",
        "Develop endurance in the terrain context that most changes race or objective preparation.",
        ("goal_terrain", "endurance", "trail"),
        ("Easy to moderate endurance work on relevant terrain.", "Terrain demand is chosen deliberately, not randomly."),
        ("Better terrain-specific endurance.", "Improved pacing and effort interpretation on goal-like routes."),
        ("Do not combine too many new demands at once.", "Avoid route choices that become race simulations too early."),
        (
            _choose_main(
                [
                    _option("Climb-Focused Endurance", [_part("Sustained Climb Exposure", "Run or hike climbs at sustainable effort.", "45-120 minutes of route time", "3-5")]),
                    _option("Rolling Trail Endurance", [_part("Rolling Trail Run", "Run rolling trail terrain at controlled aerobic effort.", "60-150 minutes", "2-5")]),
                    _option("Descent-Light Specificity", [_part("Goal-Like Terrain With Limited Descents", "Practice relevant surface or climbing while limiting downhill damage.", "60-180 minutes", "2-4")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_015",
        "Low-Impact Aerobic Alternative",
        LOW_IMPACT_AEROBIC_SUPPORT_SESSION_FAMILY,
        ("micro_003", "micro_004", "micro_009", "micro_022", "micro_049", "micro_053", "micro_054", "micro_055", "micro_063"),
        "20-90 minutes",
        "A low-impact aerobic session that preserves endurance rhythm while reducing running load.",
        "Support aerobic development or recovery when running impact is not the best choice.",
        ("cross_training", "low_impact", "aerobic"),
        ("Low-impact aerobic movement.", "Intensity should match the intended easy or recovery role."),
        ("Maintained aerobic rhythm.", "Reduced impact stress relative to running."),
        ("Do not make cross-training harder than the run it replaces.", "Choose modes the athlete can do safely and consistently."),
        (
            _choose_main(
                [
                    _option("Easy Bike Or Elliptical", [_part("Low-Impact Aerobic Work", "Bike, elliptical, swim, or ski easily.", "30-75 minutes", "2-4")]),
                    _option("Recovery Cross-Training", [_part("Very Easy Low-Impact Movement", "Move gently with recovery as the goal.", "20-45 minutes", "1-3")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_016",
        "Movement Variety Session",
        LOW_IMPACT_AEROBIC_SUPPORT_SESSION_FAMILY,
        ("micro_057", "micro_058"),
        "20-120 minutes",
        "A low-pressure movement session that restores variety, freshness, and general athleticism.",
        "Use broader movement choices without turning off-season variety into hidden overload.",
        ("movement_variety", "off_season", "low_pressure"),
        ("Flexible easy movement.", "Can include non-running activities if recovery cost stays appropriate."),
        ("Improved mental freshness.", "Broader movement confidence."),
        ("Avoid stacking many fun activities into unexpected fatigue.", "Keep intensity honest and easy."),
        (
            _choose_main(
                [
                    _option("Easy Outdoor Movement", [_part("Easy Hike, Ride, Or Ski", "Choose enjoyable low-pressure aerobic movement.", "30-120 minutes", "1-4")]),
                    _option("Playful Movement", [_part("Playful Athletic Session", "Use light games, drills, or varied movement without chasing fitness.", "20-60 minutes", "1-4")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_017",
        "Trail Familiarity Run",
        TRAIL_SPECIFIC_SESSION_FAMILY,
        ("micro_015", "micro_016"),
        "30-90 minutes",
        "A controlled trail run that builds confidence and coordination on relevant terrain.",
        "Expose the athlete to trail demands while keeping the session aerobic and manageable.",
        ("trail", "skill", "familiarity"),
        ("Easy to moderate running on selected trail terrain.", "Technicality and vertical load are controlled."),
        ("Improved trail confidence.", "Better footing, rhythm, and terrain awareness."),
        ("Avoid technical novelty under fatigue.", "Do not make every trail run race-specific."),
        (
            _choose_main(
                [
                    _option("Forgiving Trail Run", [_part("Easy Trail Running", "Run easy on smooth or familiar trails.", "30-60 minutes", "2-4")]),
                    _option("Controlled Technical Exposure", [_part("Technical Familiarity", "Run or hike short technical sections calmly with full attention.", "30-75 minutes", "2-5")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_018",
        "Trail Skill Drills",
        TRAIL_SPECIFIC_SESSION_FAMILY,
        ("micro_015",),
        "15-45 minutes",
        "A focused trail-skill session that practices coordination without requiring a large fitness load.",
        "Improve specific trail skills such as cadence, foot placement, balance, or relaxed terrain handling.",
        ("trail_skills", "drills"),
        ("Short focused skill practice.", "Low to moderate physiological load."),
        ("Better technical confidence.", "Improved movement fluency on uneven terrain."),
        ("Avoid practicing skill while overly fatigued.", "Stop before sloppy movement becomes the main habit."),
        (
            _choose_main(
                [
                    _option("Foot Placement Practice", [_part("Focused Terrain Practice", "Move over low-risk uneven terrain while practicing quiet, quick foot placement.", "10-25 minutes", "2-4")]),
                    _option("Relaxed Trail Strides", [_part("Trail Strides", "Run 4-8 relaxed short strides on safe trail terrain.", "10-20 seconds each", "5-7")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_019",
        "Power-Hike Practice",
        TRAIL_SPECIFIC_SESSION_FAMILY,
        ("micro_011",),
        "20-75 minutes",
        "A mountain-specific hiking session that develops purposeful uphill rhythm and transitions.",
        "Practice power hiking as a deliberate trail-running skill rather than a fallback when running fails.",
        ("power_hike", "trail", "mountain"),
        ("Uphill hiking or hike-run transitions.", "Intensity ranges from easy skill practice to controlled endurance work."),
        ("Better hiking economy.", "Improved uphill pacing and transition confidence."),
        ("Avoid making hike practice too steep or forceful too soon.", "Limit downhill damage after repeats."),
        (
            _choose_main(
                [
                    _option("Short Steep Hiking Repeats", [_part("Power-Hike Repeat", "Power hike uphill with tall posture and purposeful arm swing.", "1-3 minutes", "4-6"), _part("Easy Recovery", "Walk or jog back down easily.", "1-3 minutes", "1-2")], repeat="4-8 rounds"),
                    _option("Sustained Hike-Run Climb", [_part("Hike-Run Climb", "Alternate hiking steeper sections and easy running gentler sections.", "20-60 minutes", "3-5")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_020",
        "Downhill Skill Conditioning",
        TRAIL_SPECIFIC_SESSION_FAMILY,
        ("micro_011", "micro_026", "micro_027"),
        "25-75 minutes",
        "A controlled downhill session that develops descent skill while respecting mechanical risk.",
        "Improve downhill coordination, confidence, and durability without reckless damage.",
        ("downhill", "trail_skills", "conditioning"),
        ("Downhill technique exposure with careful recovery cost.", "Mechanical load can exceed cardiovascular load."),
        ("Better descent control.", "Improved confidence and eccentric tolerance."),
        ("Avoid when soreness, knee pain, or poor coordination is present.", "Do not chase downhill speed on unsafe terrain."),
        (
            _choose_main(
                [
                    _option("Low-Cost Downhill Exposure", [_part("Controlled Descent", "Descend easy-to-moderate grade focusing on quiet feet and control.", "5-15 minutes total descent", "2-4")]),
                    _option("Controlled Downhill Repeats", [_part("Descent Repeat", "Run a short descent smoothly, not maximally.", "30-90 seconds", "4-6"), _part("Easy Reset", "Walk or jog back up very easily.", "1-3 minutes", "1-2")], repeat="4-8 rounds"),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_021",
        "Steady Aerobic Run",
        STEADY_SESSION_FAMILY,
        ("micro_044", "micro_061"),
        "35-90 minutes",
        "A controlled aerobic run that is stronger than easy but clearly below threshold.",
        "Develop aerobic stamina without the cost or intent of threshold training.",
        ("steady", "aerobic"),
        ("Sustained low-moderate to moderate running.", "Effort is purposeful but controlled."),
        ("Improved aerobic stamina.", "Better control of moderate effort."),
        ("Avoid drifting into threshold because steady feels productive.", "Use effort, not pace, on variable terrain."),
        (
            _choose_main(
                [
                    _option("Steady Finish", [_part("Easy Start", "Run easy first.", "20-45 minutes", "2-4"), _part("Steady Finish", "Finish at controlled steady effort.", "10-25 minutes", "5-6")]),
                    _option("Continuous Steady Run", [_part("Steady Running", "Run continuously at a controlled steady effort.", "25-50 minutes", "5-6")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_022",
        "Controlled Threshold Session",
        THRESHOLD_SESSION_FAMILY,
        ("micro_017", "micro_018"),
        "45-90 minutes",
        "A controlled threshold workout that develops sustainable hard effort and pacing discipline.",
        "Build threshold capacity while preserving restraint and repeatability.",
        ("threshold", "tempo", "controlled_quality"),
        ("Comfortably-hard running near threshold.", "Easy support before, after, and around the work."),
        ("Improved sustainable hard effort.", "Better pacing discipline under pressure."),
        ("Avoid turning threshold into race effort.", "Use smoother terrain if control fades."),
        (
            _running_warmup(),
            _choose_main(
                [
                    _option("Cruise Intervals", [_part("Threshold Repeat", "Run controlled threshold repeats.", "5-8 minutes", "7", adjustment_notes="Extend recoveries or reduce repeats if effort climbs."), _part("Easy Recovery", "Jog easily between repeats.", "1-2 minutes", "1-3")], repeat="3-5 rounds"),
                    _option("Continuous Tempo", [_part("Tempo Run", "Run continuously at controlled comfortably-hard effort.", "15-30 minutes", "7")]),
                    _option("Progression Tempo", [_part("Progression Tempo", "Start steady and finish controlled threshold, never all-out.", "20-35 minutes", "5-7")]),
                ]
            ),
            _easy_cooldown(),
        ),
    ),
    _SessionSpec(
        "session_023",
        "Short Threshold Touch",
        THRESHOLD_SESSION_FAMILY,
        ("micro_019", "micro_044", "micro_061"),
        "35-70 minutes",
        "A small threshold dose used to preserve controlled quality without building a full workout.",
        "Maintain threshold feel or reintroduce quality while keeping total training cost low.",
        ("threshold_touch", "quality_touch"),
        ("Brief controlled threshold work.", "Lower dose than a development threshold session."),
        ("Preserved threshold rhythm.", "Improved confidence without large fatigue."),
        ("Avoid extending the touch into a full workout.", "Skip if the week is truly for absorption."),
        (
            _running_warmup(),
            _choose_main(
                [
                    _option("Short Cruise Touch", [_part("Threshold Touch", "Run short controlled threshold repeats.", "3-5 minutes", "7"), _part("Easy Recovery", "Jog easily.", "1-2 minutes", "1-3")], repeat="2-4 rounds"),
                    _option("Short Tempo Insert", [_part("Tempo Insert", "Run one short controlled tempo segment inside an easy run.", "8-15 minutes", "6-7")]),
                ]
            ),
            _easy_cooldown(),
        ),
    ),
    _SessionSpec(
        "session_024",
        "Aerobic Power Intervals",
        AEROBIC_POWER_SESSION_FAMILY,
        ("micro_021",),
        "50-85 minutes",
        "A hard aerobic interval session that develops upper-aerobic power with controlled recoveries.",
        "Create a clear aerobic-power stimulus without turning the workout into a race.",
        ("aerobic_power", "vo2max", "intervals"),
        ("Repeated hard intervals with easy recoveries.", "High training cost requiring deliberate spacing."),
        ("Improved aerobic power.", "Better control of repeated hard efforts."),
        ("Avoid sprinting early repetitions.", "Do not use technical terrain that disrupts mechanics."),
        (
            _running_warmup(),
            _choose_main(
                [
                    _option("6 x 2 Min Hard / 2 Min Easy", [_part("Hard Repetition", "Run hard at controlled aerobic-power effort.", "2 minutes", "8-9"), _part("Easy Recovery", "Jog easily.", "2 minutes", "1-3")], repeat="6 rounds", selection_notes="Best introductory structured aerobic-power option."),
                    _option("5 x 3 Min Hard / 2-3 Min Easy", [_part("Hard Repetition", "Run hard at controlled aerobic-power effort.", "3 minutes", "8-9"), _part("Easy Recovery", "Jog easily.", "2-3 minutes", "1-3")], repeat="5 rounds", selection_notes="Standard option for prepared athletes."),
                    _option("4 x 4 Min Hard / 3 Min Easy", [_part("Hard Repetition", "Run hard at controlled aerobic-power effort.", "4 minutes", "8-9"), _part("Easy Recovery", "Jog easily.", "3 minutes", "1-3")], repeat="4 rounds", selection_notes="More sustained option for experienced athletes."),
                ]
            ),
            _easy_cooldown(),
        ),
    ),
    _SessionSpec(
        "session_025",
        "Aerobic Power Touch",
        AEROBIC_POWER_SESSION_FAMILY,
        ("micro_020", "micro_022", "micro_061"),
        "35-65 minutes",
        "A brief aerobic-power touch used to introduce or maintain hard-effort coordination at low dose.",
        "Provide a small high-intensity signal without creating a full aerobic-power stimulus week.",
        ("aerobic_power_touch", "quality_touch"),
        ("Short hard repetitions or hill equivalents.", "Low total hard volume with generous recovery."),
        ("Maintained hard-effort coordination.", "Lower-risk introduction to aerobic-power work."),
        ("Avoid adding extra repetitions when the goal is only a touch.", "Skip if recovery is uncertain."),
        (
            _running_warmup(),
            _choose_main(
                [
                    _option("Short Hard Touch", [_part("Hard Touch", "Run short hard but controlled repetitions.", "45-75 seconds", "8"), _part("Easy Recovery", "Jog easily until fully reset.", "90-180 seconds", "1-3")], repeat="4-6 rounds"),
                    _option("Brief Hill Touch", [_part("Uphill Touch", "Run uphill hard but smooth.", "30-60 seconds", "8"), _part("Walk Down", "Walk down and reset.", "90-180 seconds", "1-2")], repeat="4-6 rounds"),
                ]
            ),
            _easy_cooldown(),
        ),
    ),
    _SessionSpec(
        "session_026",
        "Aerobic Power Fartlek",
        AEROBIC_POWER_SESSION_FAMILY,
        ("micro_021", "micro_061"),
        "45-80 minutes",
        "A variable hard-easy aerobic-power session that uses fartlek rhythm instead of fixed intervals.",
        "Develop high-end aerobic effort while keeping execution adaptable and less pace-bound.",
        ("aerobic_power", "fartlek"),
        ("Variable hard segments inside continuous running.", "Hard work is guided by effort and rhythm."),
        ("Improved hard-effort adaptability.", "Better effort control without strict split chasing."),
        ("Avoid making every hard segment a sprint.", "Use safe terrain where effort can stay purposeful."),
        (
            _running_warmup(),
            _choose_main(
                [
                    _option("10 x 1 Min Fartlek", [_part("Hard Segment", "Run hard and smooth by effort.", "1 minute", "8"), _part("Easy Float", "Run easy between hard segments.", "1-2 minutes", "2-3")], repeat="10 rounds"),
                    _option("8 x 90 Sec Fartlek", [_part("Hard Segment", "Run hard and smooth by effort.", "90 seconds", "8"), _part("Easy Float", "Run easy between hard segments.", "2 minutes", "2-3")], repeat="8 rounds"),
                ]
            ),
            _easy_cooldown(),
        ),
    ),
    _SessionSpec(
        "session_027",
        "Intro Uphill Endurance Repeats",
        STRENGTH_ENDURANCE_SESSION_FAMILY,
        ("micro_023",),
        "40-75 minutes",
        "A controlled uphill repeat session that introduces climbing force without full strength-endurance load.",
        "Introduce uphill muscular demand gradually while preserving movement control and recovery.",
        ("uphill", "strength_endurance_intro"),
        ("Short to moderate uphill repeats.", "Low-to-moderate muscular load with easy recoveries."),
        ("Improved climbing familiarity.", "Initial tolerance for uphill force work."),
        ("Avoid steep grades that force poor mechanics.", "Control downhill recovery cost."),
        (
            _running_warmup(),
            _choose_main(
                [
                    _option("Short Uphill Repeats", [_part("Uphill Repeat", "Run uphill at strong controlled effort.", "45-75 seconds", "6-7"), _part("Easy Downhill Recovery", "Walk or jog down easily.", "1-3 minutes", "1-2")], repeat="4-8 rounds"),
                    _option("Intro Hike-Run Repeats", [_part("Uphill Hike-Run", "Alternate short power-hike and easy run sections on a climb.", "2-4 minutes", "5-6"), _part("Easy Recovery", "Recover easily.", "2-4 minutes", "1-2")], repeat="3-5 rounds"),
                ]
            ),
            _easy_cooldown(),
        ),
    ),
    _SessionSpec(
        "session_028",
        "Strength-Endurance Climb Session",
        STRENGTH_ENDURANCE_SESSION_FAMILY,
        ("micro_024",),
        "50-100 minutes",
        "A sustained uphill session that develops climbing-specific muscular endurance.",
        "Build the ability to sustain propulsive force on climbs without turning the session into uncontrolled suffering.",
        ("strength_endurance", "climb", "uphill"),
        ("Sustained uphill running, hiking, or resistance work.", "Meaningful local muscular cost."),
        ("Improved uphill strength endurance.", "Better tolerance for sustained climbing."),
        ("Avoid before the athlete has enough base and hill tolerance.", "Protect recovery after the session."),
        (
            _running_warmup(),
            _choose_main(
                [
                    _option("Sustained Climb Intervals", [_part("Climb Interval", "Run or hike uphill at strong sustainable effort.", "6-10 minutes", "6-8"), _part("Easy Recovery", "Recover very easily.", "3-5 minutes", "1-3")], repeat="3-5 rounds"),
                    _option("Continuous Climb Effort", [_part("Sustained Climb", "Move uphill continuously at controlled muscular-endurance effort.", "25-50 minutes", "5-7")]),
                    _option("Treadmill Or Stair Alternative", [_part("Controlled Uphill Alternative", "Use treadmill incline, stairs, or similar uphill substitute.", "20-45 minutes", "5-7")], selection_notes="Use when outdoor climbs are unavailable."),
                ]
            ),
            _easy_cooldown(),
        ),
    ),
    _SessionSpec(
        "session_029",
        "Hill Strength Circuit",
        STRENGTH_ENDURANCE_SESSION_FAMILY,
        ("micro_024",),
        "50-85 minutes",
        "A structured hill circuit that develops uphill force, coordination, and muscular endurance.",
        "Build trail-relevant strength endurance through repeated hill-force patterns.",
        ("hill_circuit", "strength_endurance"),
        ("Several hill-force parts repeated as rounds.", "Moderate-to-high muscular and coordination load."),
        ("Improved uphill force tolerance.", "Better climbing rhythm under fatigue."),
        ("Avoid sloppy bounding or forceful mechanics.", "Do not combine with heavy downhill load unless prepared."),
        (
            _running_warmup(),
            _choose_main(
                [
                    _option("Intro Hill Circuit", [_part("Steady Uphill Run", "Run uphill at strong but controlled effort.", "45-60 seconds", "7"), _part("Walk Down Recovery", "Walk or jog easily down.", "60-120 seconds", "1-2"), _part("Power Hike", "Power hike uphill with purposeful arm swing.", "45-60 seconds", "6-7"), _part("Walk Down Recovery", "Walk or jog easily down.", "60-120 seconds", "1-2")], repeat="3 rounds", selection_notes="Best when introducing hill circuits."),
                    _option("Advanced Hill Circuit", [_part("Uphill Bound", "Bound uphill with controlled force and posture.", "20-30 seconds", "8"), _part("Walk Down Recovery", "Walk down and reset.", "60-90 seconds", "1"), _part("Strong Uphill Run", "Run uphill at controlled hard effort.", "60 seconds", "7-8"), _part("Jog Down Recovery", "Jog or walk down easily.", "90-120 seconds", "1-2")], repeat="4 rounds", selection_notes="Best for prepared athletes."),
                ]
            ),
            _easy_cooldown(),
        ),
    ),
    _SessionSpec(
        "session_030",
        "Short Hill Power",
        HILL_POWER_SESSION_FAMILY,
        ("micro_025",),
        "30-60 minutes",
        "A short uphill power session that develops snap and mechanics without a long hill grind.",
        "Preserve or develop uphill power, rhythm, and neuromuscular coordination at low total volume.",
        ("hill_power", "neuromuscular"),
        ("Very short uphill efforts with full recovery.", "Low total volume but high local intensity."),
        ("Improved uphill power.", "Better coordination and stride force."),
        ("Avoid when calves, Achilles, or hamstrings feel risky.", "Stop before mechanics deteriorate."),
        (
            _running_warmup(),
            _choose_main(
                [
                    _option("Short Hill Sprints", [_part("Hill Sprint", "Run uphill fast, smooth, and powerful.", "8-12 seconds", "8-9"), _part("Full Recovery", "Walk back and fully reset.", "90-180 seconds", "1")], repeat="4-8 rounds"),
                    _option("Relaxed Uphill Strides", [_part("Uphill Stride", "Run relaxed uphill strides, not all-out.", "15-20 seconds", "6-7"), _part("Easy Recovery", "Walk or jog easy.", "60-120 seconds", "1-2")], repeat="4-8 rounds"),
                ]
            ),
            _easy_cooldown(),
        ),
    ),
    _SessionSpec(
        "session_031",
        "Neuromuscular Strides",
        NEUROMUSCULAR_SESSION_FAMILY,
        ("micro_036", "micro_038", "micro_040"),
        "20-50 minutes",
        "Very short relaxed speed touches that preserve rhythm and coordination at low cost.",
        "Maintain leg speed and relaxed mechanics without creating a hard workout.",
        ("strides", "neuromuscular"),
        ("Short relaxed accelerations with easy recovery.", "Low metabolic cost when controlled."),
        ("Improved rhythm and coordination.", "Maintained leg speed during easy or taper weeks."),
        ("Do not sprint or strain.", "Skip strides if the athlete feels flat in a risky way."),
        (
            _running_warmup(),
            _choose_main(
                [
                    _option("Flat Strides", [_part("Relaxed Stride", "Run smooth relaxed strides on flat safe terrain.", "15-20 seconds", "5-7"), _part("Easy Recovery", "Walk or jog until fully relaxed.", "60-120 seconds", "1-2")], repeat="4-8 rounds"),
                    _option("Gentle Uphill Strides", [_part("Uphill Stride", "Run relaxed strides on a gentle hill.", "10-20 seconds", "5-7"), _part("Easy Recovery", "Walk or jog down easily.", "60-120 seconds", "1-2")], repeat="4-6 rounds"),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_032",
        "Sharpening Touch",
        CONTROLLED_QUALITY_SESSION_FAMILY,
        ("micro_035", "micro_037", "micro_050", "micro_061", "micro_062"),
        "30-65 minutes",
        "A small familiar quality touch that preserves confidence and coordination without fatigue.",
        "Keep the athlete connected to race rhythm or controlled intensity while protecting freshness.",
        ("sharpening", "quality_touch"),
        ("Brief familiar quality inside an otherwise easy session.", "Low total training cost."),
        ("Maintained coordination and confidence.", "Preserved feel for controlled intensity."),
        ("Avoid unfamiliar workouts close to racing.", "Do not extend the touch because it feels good."),
        (
            _running_warmup(),
            _choose_main(
                [
                    _option("Short Controlled Intervals", [_part("Controlled Repeat", "Run short familiar controlled repeats.", "60-90 seconds", "6-8"), _part("Easy Recovery", "Jog easy until fully controlled.", "2-3 minutes", "1-3")], repeat="3-5 rounds"),
                    _option("Race-Feel Touch", [_part("Race-Feel Segment", "Run a short familiar segment at controlled race feel.", "5-12 minutes", "5-7")]),
                ]
            ),
            _easy_cooldown(),
        ),
    ),
    _SessionSpec(
        "session_033",
        "Pre-Race Shakeout",
        EASY_SESSION_FAMILY,
        ("micro_036", "micro_040"),
        "10-35 minutes",
        "A very short familiar run used to settle the athlete before racing.",
        "Support calm, rhythm, and confidence close to race day without adding fatigue.",
        ("shakeout", "pre_race"),
        ("Very short easy running, sometimes with relaxed strides.", "Minimal load and no novelty."),
        ("Improved calm and readiness.", "Maintained movement familiarity."),
        ("Avoid testing fitness or trying new gear.", "Skip or shorten if travel or fatigue makes rest better."),
        (
            _choose_main(
                [
                    _option("Easy Shakeout", [_part("Easy Shakeout Run", "Run very easily on familiar terrain.", "10-25 minutes", "2-3")]),
                    _option("Shakeout With Strides", [_part("Easy Shakeout Run", "Run very easily.", "10-20 minutes", "2-3"), _part("Relaxed Strides", "Add a few relaxed strides if they improve confidence.", "3-4 x 10-15 seconds", "5-6")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_034",
        "Gear And Fueling Check",
        RACE_PRACTICE_SESSION_FAMILY,
        ("micro_029", "micro_032", "micro_036", "micro_039", "micro_040"),
        "10-60 minutes",
        "A low-cost execution session that checks gear, fueling, and race logistics.",
        "Confirm practical race details without turning readiness checks into extra training stress.",
        ("gear", "fueling", "readiness"),
        ("Low-cost movement or rehearsal with equipment/fueling focus.", "Training load stays secondary."),
        ("Improved race-day readiness.", "Reduced uncertainty around gear and intake."),
        ("Do not introduce new gear too close to the race unless necessary.", "Stop if checks create avoidable stress."),
        (
            _choose_main(
                [
                    _option("Gear Check Jog", [_part("Gear Check", "Run or walk easily with planned shoes, vest, bottles, lights, or poles.", "10-40 minutes", "1-3")]),
                    _option("Fueling Timing Check", [_part("Fueling Check", "Practice the planned bottle, gel, or snack timing during easy movement.", "20-60 minutes", "2-4")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_035",
        "Fueling Habit Run",
        RACE_PRACTICE_SESSION_FAMILY,
        ("micro_032",),
        "35-90 minutes",
        "An easy run that builds fueling and hydration habits before higher-stress practice.",
        "Make intake timing and carrying systems familiar during ordinary aerobic work.",
        ("fueling", "hydration", "habit"),
        ("Easy aerobic running with planned intake practice.", "Low-to-moderate training load."),
        ("Improved fueling routine.", "Better comfort carrying and using fluids or calories."),
        ("Avoid turning every easy run into a gut test.", "Stay within coaching scope and avoid clinical nutrition claims."),
        (
            _choose_main(
                [
                    _option("Easy Fueling Habit", [_part("Easy Run With Intake", "Run easy and practice simple planned intake timing.", "35-75 minutes", "2-4")]),
                    _option("Hydration Timing Habit", [_part("Easy Hydration Practice", "Run easy and practice drinking rhythm or bottle handling.", "30-90 minutes", "2-4")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_036",
        "Long-Run Fueling Practice",
        RACE_PRACTICE_SESSION_FAMILY,
        ("micro_011", "micro_028", "micro_032", "micro_033"),
        "75-240 minutes",
        "A longer endurance session that practices fueling under realistic duration and effort.",
        "Improve fueling reliability when duration, terrain, heat, or race context make intake important.",
        ("fueling", "long_run", "race_practice"),
        ("Long easy or specific endurance work with planned intake.", "Gut, logistics, and effort interact."),
        ("Improved fueling confidence.", "Better tolerance for race-relevant intake timing."),
        ("Do not test too many products at once.", "Reduce physical stress if fueling tolerance is the main question."),
        (
            _choose_main(
                [
                    _option("Standard Long-Run Fueling", [_part("Long Run With Planned Intake", "Run easy or specific endurance while practicing planned fueling.", "75-180 minutes", "2-5")]),
                    _option("Heat Or Hydration Emphasis", [_part("Hydration-Focused Long Run", "Practice fluid and electrolyte logistics in controlled conditions.", "60-150 minutes", "2-5")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_037",
        "Controlled Fueling Test",
        RACE_PRACTICE_SESSION_FAMILY,
        ("micro_033", "micro_034"),
        "30-90 minutes",
        "A controlled session that isolates fueling or hydration tolerance more than fitness development.",
        "Test intake timing, product choice, or hydration logistics under interpretable conditions.",
        ("fueling_test", "hydration"),
        ("Simple training load with focused intake observation.", "Terrain and intensity are kept controlled."),
        ("Clearer fueling feedback.", "Reduced race-day uncertainty."),
        ("Avoid hard or technical sessions when the gut question is the priority.", "Do not treat GI distress as a workout success."),
        (
            _choose_main(
                [
                    _option("Simple Product Test", [_part("Easy Test Run", "Run easy while testing one planned product or timing pattern.", "30-75 minutes", "2-4")]),
                    _option("Hydration Check", [_part("Hydration Test", "Use controlled easy running to test drinking rhythm and carrying setup.", "45-90 minutes", "2-4")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_038",
        "Race Execution Cue Run",
        RACE_PRACTICE_SESSION_FAMILY,
        ("micro_029", "micro_031", "micro_039"),
        "30-120 minutes",
        "A low-to-moderate session that practices one or two race execution cues.",
        "Make pacing, gear, hiking, aid-flow, or decision cues more automatic before race day.",
        ("race_execution", "cue_practice"),
        ("Easy or controlled movement with a practical execution focus.", "Fitness stimulus is secondary to skill reliability."),
        ("Improved execution confidence.", "Better translation from plan to race behavior."),
        ("Do not overload the session with every possible race detail.", "Practice one priority cue well."),
        (
            _choose_main(
                [
                    _option("Pacing Cue Run", [_part("Pacing Practice", "Run easy or steady while practicing start-control and effort cues.", "30-90 minutes", "2-5")]),
                    _option("Hiking Transition Practice", [_part("Transition Practice", "Practice smooth run-hike-run transitions on relevant terrain.", "20-60 minutes", "2-5")]),
                    _option("Aid-Flow Rehearsal", [_part("Aid Flow", "Practice opening, eating, drinking, stowing, and moving calmly.", "20-60 minutes", "1-4")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_039",
        "Race Rehearsal Session",
        RACE_PRACTICE_SESSION_FAMILY,
        ("micro_030",),
        "60-240 minutes",
        "A controlled rehearsal that combines selected race demands without becoming a race.",
        "Practice race execution under meaningful but manageable specificity.",
        ("race_rehearsal", "specificity"),
        ("Specific terrain, gear, fueling, or pacing rehearsal.", "Moderate-to-high cost depending on size."),
        ("Improved race execution reliability.", "Better confidence with demand combinations."),
        ("Avoid proving fitness through excessive simulation.", "Do not use unfamiliar risk close to racing."),
        (
            _choose_main(
                [
                    _option("Short Rehearsal", [_part("Specific Rehearsal", "Practice selected race demands at controlled effort.", "60-120 minutes", "2-5")]),
                    _option("Long Rehearsal", [_part("Long Specific Rehearsal", "Combine terrain, gear, fueling, and pacing in a controlled long outing.", "2-4 hours", "2-5")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_040",
        "Course-Demands Exposure Run",
        RACE_PRACTICE_SESSION_FAMILY,
        ("micro_026", "micro_027"),
        "45-180 minutes",
        "A controlled exposure to one important course demand such as climbing, surface, heat, or descent.",
        "Prepare a key race demand without the cost of full simulation.",
        ("course_demands", "exposure"),
        ("One primary course demand is emphasized.", "Training load stays interpretable and controlled."),
        ("Improved familiarity with the selected demand.", "Better confidence and pacing judgement."),
        ("Avoid stacking many new demands in one exposure.", "Use simulation only when demand combinations are the point."),
        (
            _choose_main(
                [
                    _option("Climb Exposure", [_part("Course-Relevant Climb", "Practice a relevant climbing demand at controlled effort.", "20-75 minutes", "3-6")]),
                    _option("Technical Surface Exposure", [_part("Technical Terrain Exposure", "Practice relevant footing at low-to-moderate cost.", "20-60 minutes", "2-5")]),
                    _option("Heat Or Conditions Exposure", [_part("Controlled Conditions Practice", "Practice an environmental demand conservatively and safely.", "30-90 minutes", "2-5")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_041",
        "Course-Demands Simulation Outing",
        RACE_PRACTICE_SESSION_FAMILY,
        ("micro_028",),
        "90-360 minutes",
        "A higher-specificity outing that combines several course demands at meaningful cost.",
        "Simulate the interaction of key race demands when the athlete is ready and timing justifies it.",
        ("course_demands", "simulation", "race_specific"),
        ("Multiple course demands combined in one outing.", "Higher cost and more recovery need than exposure."),
        ("Better understanding of race-demand interactions.", "Improved confidence under specificity."),
        ("Avoid full-race efforts in training.", "Do not simulate when basic exposure is not yet absorbed."),
        (
            _choose_main(
                [
                    _option("Partial Simulation", [_part("Specific Simulation", "Combine selected race-like terrain, fueling, gear, and pacing at controlled effort.", "90-180 minutes", "2-5")]),
                    _option("Large Simulation", [_part("Large Specific Outing", "Use a larger course-like outing only when the athlete is prepared.", "3-6 hours", "2-5")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_042",
        "Easy Run With Response Check",
        EASY_SESSION_FAMILY,
        ("micro_006", "micro_050"),
        "20-60 minutes",
        "An easy run used to observe readiness without adding a hard test.",
        "Check soreness, easy-effort feel, coordination, and confidence through simple familiar movement.",
        ("easy", "readiness_check"),
        ("Easy running with observation focus.", "No intentional fitness test."),
        ("Clearer readiness information.", "Safer decision-making for the next progression."),
        ("Avoid adding a hard finish to prove readiness.", "Use familiar terrain so signals are interpretable."),
        (
            _choose_main(
                [
                    _option("Easy Response Check", [_part("Easy Check Run", "Run easy and observe breathing, soreness, coordination, and mood.", "20-45 minutes", "2-4")]),
                    _option("Downhill/Stairs Check", [_part("Gentle Mechanical Check", "Use very mild downhill or stairs only if relevant and safe.", "10-30 minutes", "1-3")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_043",
        "Transition Preview Session",
        CONTROLLED_QUALITY_SESSION_FAMILY,
        ("micro_042", "micro_051"),
        "25-75 minutes",
        "A small preview of the next training emphasis used to bridge blocks safely.",
        "Introduce the next block's feel without starting the full demand early.",
        ("transition", "preview"),
        ("Low-dose preview of a future emphasis.", "Intensity and terrain are deliberately constrained."),
        ("Better readiness for the next block.", "Reduced abruptness between training emphases."),
        ("Avoid turning the preview into a full workout.", "Use the easiest meaningful version."),
        (
            _choose_main(
                [
                    _option("Threshold Preview", [_part("Short Controlled Touch", "Run a very short controlled threshold-like segment.", "5-10 minutes", "6-7")]),
                    _option("Hill Preview", [_part("Short Hill Touch", "Practice a few controlled uphill efforts.", "30-60 seconds", "5-7"), _part("Easy Recovery", "Recover easily.", "1-3 minutes", "1-2")], repeat="3-5 rounds"),
                    _option("Terrain Preview", [_part("Small Terrain Exposure", "Use a small dose of upcoming terrain demand.", "15-45 minutes", "2-5")]),
                ]
            ),
            _easy_cooldown(),
        ),
    ),
    _SessionSpec(
        "session_044",
        "Targeted Lesson Practice",
        RACE_PRACTICE_SESSION_FAMILY,
        ("micro_031", "micro_045", "micro_046"),
        "25-120 minutes",
        "A focused session that practices one clear lesson from recent training or racing.",
        "Turn feedback into one manageable behavior change rather than rewriting the whole plan.",
        ("lesson_practice", "race_feedback"),
        ("Low-to-moderate movement with one practical lesson focus.", "The lesson determines the option selected."),
        ("Improved race or training execution.", "Clearer learning from previous experience."),
        ("Do not practice every lesson at once.", "Keep the session low cost if recovery is still the priority."),
        (
            _choose_main(
                [
                    _option("Pacing Correction", [_part("Pacing Practice", "Run easy or steady while practicing the specific pacing correction.", "30-90 minutes", "2-5")]),
                    _option("Fueling Timing Fix", [_part("Fueling Practice", "Practice the specific intake timing or carrying correction.", "30-120 minutes", "2-5")]),
                    _option("Descent-Control Practice", [_part("Controlled Descent Cue", "Practice one descent-control cue on safe terrain.", "10-30 minutes descent focus", "2-5")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_045",
        "Race Debrief Easy Run",
        RECOVERY_SESSION_FAMILY,
        ("micro_045",),
        "20-60 minutes",
        "An easy recovery run paired with simple reflection on a recent race.",
        "Let the athlete move gently while identifying one useful lesson from competition.",
        ("race_debrief", "recovery"),
        ("Very easy movement plus practical reflection.", "Physical recovery remains the priority."),
        ("Better race learning.", "Maintained recovery rhythm."),
        ("Avoid making the debrief emotionally or physically exhausting.", "Do not turn reflection into immediate overcorrection."),
        (
            _choose_main(
                [
                    _option("Easy Debrief Run", [_part("Easy Recovery Run", "Run very easily and note one or two observations afterward.", "20-45 minutes", "1-3")]),
                    _option("Walk-And-Reflect", [_part("Gentle Walk", "Walk easily and reflect on one practical lesson.", "20-60 minutes", "1-2")]),
                ]
            ),
        ),
    ),
    _SessionSpec(
        "session_046",
        "Constraint Priority Session",
        EASY_SESSION_FAMILY,
        ("micro_063",),
        "10-45 minutes",
        "A short high-value session chosen when constraints make a normal workout unrealistic.",
        "Preserve the most useful training connection without forcing a full template into limited time or energy.",
        ("constraints", "minimum_effective", "easy"),
        ("Small flexible dose matched to real constraints.", "Low complexity and low friction."),
        ("Maintained continuity.", "Reduced guilt-driven training decisions."),
        ("Avoid cramming hard work into a constrained day.", "Choose the simplest session that protects the week."),
        (
            _choose_main(
                [
                    _option("Minimum Easy Run", [_part("Short Easy Run", "Run easy for the smallest useful dose.", "10-30 minutes", "2-4")]),
                    _option("Short Support Session", [_part("Light Support Work", "Use easy mobility, activation, or walking if running is not realistic.", "10-25 minutes", "1-3")]),
                ]
            ),
        ),
    ),
)


MAINSTREAM_SESSION_CARDS = [_mainstream_session(spec) for spec in _SPECS]
