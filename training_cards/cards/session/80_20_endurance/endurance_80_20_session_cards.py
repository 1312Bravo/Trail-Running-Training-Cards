from __future__ import annotations

from training_cards.cards.session._philosophy_session_builder import (
    PhilosophySessionSpec,
    build_philosophy_session_cards,
    choose_main,
    easy_cooldown,
    option,
    part,
    running_warmup,
    support_notes,
)
from training_cards.philosophy_profiles import ENDURANCE_80_20
from training_cards.session_families import (
    AEROBIC_POWER_SESSION_FAMILY,
    CONTROLLED_QUALITY_SESSION_FAMILY,
    EASY_SESSION_FAMILY,
    ENDURANCE_SESSION_FAMILY,
    STRENGTH_ENDURANCE_SESSION_FAMILY,
)


_SPECS: tuple[PhilosophySessionSpec, ...] = (
    PhilosophySessionSpec(
        id="session_047",
        title="80/20 Low-Intensity Discipline Run",
        philosophy_profile_id=ENDURANCE_80_20,
        session_family=EASY_SESSION_FAMILY,
        parent_micro_ids=("micro_065", "micro_066", "micro_067", "micro_083", "micro_084"),
        typical_duration="25-75 minutes",
        summary="An easy run defined by disciplined low-intensity control rather than by pace ambition.",
        purpose="Protect the low-intensity majority of an 80/20 plan and correct moderate drift before it becomes the normal rhythm.",
        tags=("80_20", "low_intensity", "easy_discipline"),
        training_profile=(
            "Low-intensity running with an explicit ceiling.",
            "Best when the athlete tends to turn easy days into moderate days.",
        ),
        expected_adaptations=(
            "More reliable easy-volume accumulation.",
            "Better separation between easy days and quality days.",
        ),
        watchouts=(
            "Do not chase pace, vertical gain, or segment performance.",
            "If the run drifts moderate, shorten it or move to flatter terrain.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option(
                        "Ceiling-Controlled Easy Run",
                        [
                            part(
                                "Easy Running",
                                "Run below the planned low-intensity ceiling for the whole session.",
                                "25-60 minutes",
                                "2-4",
                                coaching_notes="The athlete should finish feeling that another easy session tomorrow would be realistic.",
                                terrain_notes="Use terrain that allows effort control; walk short climbs if needed.",
                                adjustment_notes="If effort drifts moderate for more than a few minutes, slow down, walk, or end the run.",
                            )
                        ],
                    ),
                    option(
                        "Drift-Correction Easy Run",
                        [
                            part(
                                "Easy Reset",
                                "Run on simple terrain with a deliberately conservative ceiling.",
                                "20-45 minutes",
                                "1-3",
                                coaching_notes="Use this after several easy runs have become too hard.",
                                adjustment_notes="Keep the next quality session out until easy control returns.",
                            )
                        ],
                    ),
                ]
            ),
            support_notes(
                "The distinctive 80/20 decision is the ceiling, not the exact duration.",
                "This card should replace a normal easy run only when low-intensity discipline is the session's main purpose.",
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_048",
        title="80/20 Distribution-Protected Long Endurance Run",
        philosophy_profile_id=ENDURANCE_80_20,
        session_family=ENDURANCE_SESSION_FAMILY,
        parent_micro_ids=("micro_068", "micro_069", "micro_081"),
        typical_duration="75-180 minutes",
        summary="A long endurance run that extends low-intensity duration while accounting honestly for terrain and muscular cost.",
        purpose="Build endurance without letting the long run quietly become the week's hidden moderate or hard session.",
        tags=("80_20", "long_run", "distribution_protection"),
        training_profile=(
            "Long low-intensity running, hiking, or trail movement.",
            "Terrain is selected to preserve the intended intensity distribution.",
        ),
        expected_adaptations=(
            "Improved endurance through repeatable low-intensity duration.",
            "Better ability to extend long work without disrupting hard/easy balance.",
        ),
        watchouts=(
            "Steep climbs, technical descents, and heat can make a nominal easy long run costly.",
            "Do not add a fast finish unless the week explicitly allows planned moderate work.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option(
                        "Protected Low-Intensity Long Run",
                        [
                            part(
                                "Long Easy Movement",
                                "Run or hike-run mostly below the low-intensity ceiling.",
                                "75-150 minutes",
                                "2-4",
                                terrain_notes="Walk sustained climbs early enough to keep the session aerobic.",
                                adjustment_notes="Shorten if terrain, heat, or fueling turns the day into moderate stress.",
                            )
                        ],
                    ),
                    option(
                        "Trail-Cost Accounted Long Run",
                        [
                            part(
                                "Controlled Trail Endurance",
                                "Move easily on trail while counting vertical, descent, heat, and footing as load.",
                                "90-180 minutes",
                                "2-5",
                                coaching_notes="A slightly higher RPE may be acceptable only when terrain cost is unavoidable and planned.",
                                adjustment_notes="Reduce total duration when vertical or descent load is high.",
                            )
                        ],
                    ),
                ]
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_049",
        title="80/20 Planned Moderate Session",
        philosophy_profile_id=ENDURANCE_80_20,
        session_family=CONTROLLED_QUALITY_SESSION_FAMILY,
        parent_micro_ids=("micro_070", "micro_071", "micro_072"),
        typical_duration="35-80 minutes",
        summary="A deliberate moderate session used as a controlled exception, not accidental grey-zone drift.",
        purpose="Use moderate work only when it has a clear role inside the overall 80/20 intensity distribution.",
        tags=("80_20", "moderate", "controlled_quality"),
        training_profile=(
            "Planned moderate running with clear start and stop boundaries.",
            "Surrounding training protects the low-intensity majority.",
        ),
        expected_adaptations=(
            "Improved controlled stamina without eroding easy discipline.",
            "Better awareness of planned moderate work versus drift.",
        ),
        watchouts=(
            "Do not extend the moderate segment just because it feels sustainable.",
            "Avoid adding moderate running to warm-up, cooldown, or recovery days.",
        ),
        workout_blocks=(
            running_warmup(),
            choose_main(
                [
                    option(
                        "Continuous Planned Moderate",
                        [
                            part(
                                "Moderate Running",
                                "Run steadily at the planned moderate effort, below threshold strain.",
                                "15-35 minutes",
                                "5-6",
                                coaching_notes="The point is deliberate moderate control, not proving threshold fitness.",
                            )
                        ],
                    ),
                    option(
                        "Segmented Planned Moderate",
                        [
                            part("Moderate Repetitions", "Run 2-4 controlled moderate repetitions.", "8-12 minutes each", "5-6"),
                            part("Easy Recoveries", "Jog easily between moderate repetitions.", "2-4 minutes each", "1-3"),
                        ],
                        repeat="2-4 rounds",
                        load_notes="Use fewer rounds when the week already contains race stress, hills, or long duration.",
                    ),
                ]
            ),
            easy_cooldown(),
        ),
    ),
    PhilosophySessionSpec(
        id="session_050",
        title="80/20 Distribution-Protected High-Intensity Session",
        philosophy_profile_id=ENDURANCE_80_20,
        session_family=AEROBIC_POWER_SESSION_FAMILY,
        parent_micro_ids=("micro_073", "micro_074", "micro_075", "micro_082", "micro_085"),
        typical_duration="35-75 minutes",
        summary="A high-intensity session that keeps the hard work hard, the recoveries easy, and the rest of the week protected.",
        purpose="Develop high-end aerobic quality without allowing warm-up, recovery, or extra moderate work to blur the 80/20 distribution.",
        tags=("80_20", "high_intensity", "polarized"),
        training_profile=(
            "Short controlled hard work with easy recoveries.",
            "Designed to preserve hard/easy contrast rather than accumulate grey-zone volume.",
        ),
        expected_adaptations=(
            "Improved aerobic power or hard-effort tolerance.",
            "Cleaner separation between quality stress and low-intensity support.",
        ),
        watchouts=(
            "Do not turn recoveries into steady running.",
            "Stop before mechanics or effort control collapse into racing.",
        ),
        workout_blocks=(
            running_warmup(),
            choose_main(
                [
                    option(
                        "Short Hard / Easy Contrast",
                        [
                            part("Hard Repetition", "Run hard but controlled.", "1-3 minutes", "8-9"),
                            part("Easy Recovery", "Jog or walk very easily.", "equal to longer than hard repetition", "1-3"),
                        ],
                        repeat="6-10 rounds",
                        load_notes="Keep the hard minutes purposeful and the easy minutes truly easy.",
                    ),
                    option(
                        "Reduced High-Intensity Touch",
                        [
                            part("Hard Touch", "Run a small number of controlled high-intensity repetitions.", "30-90 seconds", "8-9"),
                            part("Easy Recovery", "Recover very easily until breathing and mechanics reset.", "90 seconds-3 minutes", "1-3"),
                        ],
                        repeat="4-6 rounds",
                        selection_notes="Use when the goal is to preserve quality without adding a full development load.",
                    ),
                ]
            ),
            easy_cooldown(),
        ),
    ),
    PhilosophySessionSpec(
        id="session_051",
        title="80/20 Distribution-Protected Hill-Strength Session",
        philosophy_profile_id=ENDURANCE_80_20,
        session_family=STRENGTH_ENDURANCE_SESSION_FAMILY,
        parent_micro_ids=("micro_076", "micro_077", "micro_078"),
        typical_duration="35-80 minutes",
        summary="A hill-strength session that treats grade, force, and residual soreness as intensity cost.",
        purpose="Develop hill strength while preserving 80/20 recovery logic and avoiding hidden muscular overload.",
        tags=("80_20", "hill_strength", "muscular_cost"),
        training_profile=(
            "Uphill work with conservative volume and clear recovery.",
            "Load accounting includes muscular stress, not only heart rate or pace.",
        ),
        expected_adaptations=(
            "Improved climbing strength with cleaner recovery.",
            "Better judgment of hill work as a hard or moderate stressor.",
        ),
        watchouts=(
            "Delayed soreness can make the next easy days less easy.",
            "Avoid steep or technical descents after hard climbing repeats.",
        ),
        workout_blocks=(
            running_warmup(),
            choose_main(
                [
                    option(
                        "Controlled Uphill Strength Repeats",
                        [
                            part("Uphill Strength Repetition", "Climb at controlled strong effort with tall posture and stable mechanics.", "2-5 minutes", "6-8"),
                            part("Easy Downhill Or Flat Recovery", "Recover very easily and minimize downhill pounding.", "3-6 minutes", "1-3"),
                        ],
                        repeat="4-8 rounds",
                        load_notes="Count this as quality load even if breathing stays below classic interval intensity.",
                    ),
                    option(
                        "Intro Hill-Strength Touch",
                        [
                            part("Short Uphill Repetition", "Run or hike uphill with smooth force, not strain.", "60-120 seconds", "5-7"),
                            part("Easy Recovery", "Walk or jog easily until the next repetition feels controlled.", "2-4 minutes", "1-3"),
                        ],
                        repeat="4-6 rounds",
                        selection_notes="Use when hill-strength work is new or the week needs a smaller dose.",
                    ),
                ]
            ),
            easy_cooldown(),
        ),
    ),
)


ENDURANCE_80_20_SESSION_CARDS = build_philosophy_session_cards(_SPECS)
