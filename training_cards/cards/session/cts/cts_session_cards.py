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
from training_cards.philosophy_profiles import CTS
from training_cards.session_families import (
    CONTROLLED_QUALITY_SESSION_FAMILY,
    ENDURANCE_SESSION_FAMILY,
    RACE_PRACTICE_SESSION_FAMILY,
    STRENGTH_ENDURANCE_SESSION_FAMILY,
    THRESHOLD_SESSION_FAMILY,
)


_SPECS: tuple[PhilosophySessionSpec, ...] = (
    PhilosophySessionSpec(
        id="session_056",
        title="CTS Limiter-Focused Quality Session",
        philosophy_profile_id=CTS,
        session_family=CONTROLLED_QUALITY_SESSION_FAMILY,
        parent_micro_ids=("micro_107", "micro_108", "micro_122"),
        typical_duration="35-80 minutes",
        summary="A quality session chosen by the athlete's current limiter rather than by a generic workout progression.",
        purpose="Target the most relevant limiter while making the cost and trade-off of the session explicit.",
        tags=("cts", "limiter", "quality"),
        training_profile=(
            "Quality work selected from the limiter: climbing, threshold control, aerobic power, or fatigue resistance.",
            "The session is valuable only when the limiter choice is specific and current.",
        ),
        expected_adaptations=(
            "Improved performance in the athlete's highest-value limiter.",
            "Better decision-making about what quality is worth doing now.",
        ),
        watchouts=(
            "Do not stack multiple limiter workouts into one day.",
            "If the limiter is unclear, use a mainstream controlled session instead.",
        ),
        workout_blocks=(
            running_warmup(),
            choose_main(
                [
                    option(
                        "Threshold Limiter",
                        [
                            part("Controlled Threshold Repetition", "Run controlled threshold intervals that target sustainable speed.", "6-10 minutes", "6-7"),
                            part("Easy Recovery", "Jog easily enough to keep the next repetition useful.", "2-3 minutes", "1-3"),
                        ],
                        repeat="3-5 rounds",
                        selection_notes="Use when sustained controlled speed is the limiter.",
                    ),
                    option(
                        "Aerobic-Power Limiter",
                        [
                            part("Aerobic-Power Repetition", "Run hard controlled repetitions without sprinting.", "2-4 minutes", "8-9"),
                            part("Easy Recovery", "Recover very easily until mechanics are clean.", "2-4 minutes", "1-3"),
                        ],
                        repeat="4-6 rounds",
                        selection_notes="Use when high-end aerobic capacity is the limiter.",
                    ),
                    option(
                        "Climbing Limiter",
                        [
                            part("Climbing Repetition", "Climb strongly with the technique and grade that match the limiter.", "3-8 minutes", "6-8"),
                            part("Easy Recovery", "Recover on safe terrain without adding descent damage.", "3-5 minutes", "1-3"),
                        ],
                        repeat="3-6 rounds",
                        selection_notes="Use when climbing durability or force is the limiter.",
                    ),
                ]
            ),
            easy_cooldown(),
        ),
    ),
    PhilosophySessionSpec(
        id="session_057",
        title="CTS Long-Run Durability Session",
        philosophy_profile_id=CTS,
        session_family=ENDURANCE_SESSION_FAMILY,
        parent_micro_ids=("micro_104", "micro_105", "micro_106"),
        typical_duration="90-240 minutes",
        summary="A long run built around the durability demand most likely to matter for the goal event.",
        purpose="Improve long-run tolerance while keeping the session tied to a clear event or athlete limiter.",
        tags=("cts", "long_run", "durability"),
        training_profile=(
            "Long aerobic work with a defined durability focus.",
            "Terrain, vertical, and duration are chosen because they solve a practical limiter.",
        ),
        expected_adaptations=(
            "Improved durability under goal-relevant long-run stress.",
            "Better confidence about the specific cost of long outings.",
        ),
        watchouts=(
            "Do not add every event demand at once.",
            "A durability long run should not compromise several following days without a reason.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option(
                        "Duration Durability",
                        [
                            part("Long Controlled Endurance", "Run or hike-run long enough to challenge durability while staying aerobic.", "90-180 minutes", "3-5"),
                        ],
                        selection_notes="Use when duration itself is the limiter.",
                    ),
                    option(
                        "Terrain Durability",
                        [
                            part("Goal-Terrain Endurance", "Practice the terrain demand most likely to break form or confidence.", "90-240 minutes", "3-6"),
                        ],
                        selection_notes="Use when vertical, technicality, or descent cost is the limiter.",
                    ),
                ]
            ),
            support_notes("Choose one durability limiter per session so the lesson remains clear."),
        ),
    ),
    PhilosophySessionSpec(
        id="session_058",
        title="CTS Ultra Strength-Endurance Limiter Session",
        philosophy_profile_id=CTS,
        session_family=STRENGTH_ENDURANCE_SESSION_FAMILY,
        parent_micro_ids=("micro_109", "micro_110", "micro_111"),
        typical_duration="45-100 minutes",
        summary="A muscular-endurance session aimed at the ultra limiter that most affects performance.",
        purpose="Develop climbing, hiking, or terrain-specific force durability without adding generic hill work.",
        tags=("cts", "ultra", "strength_endurance", "limiter"),
        training_profile=(
            "Sustained or repeated muscular work matched to an ultra-specific limiter.",
            "Recovery is planned because the muscular cost may outlast the session.",
        ),
        expected_adaptations=(
            "Improved climbing or hiking durability.",
            "Better resistance to late-race muscular fade.",
        ),
        watchouts=(
            "Avoid large eccentric downhill cost unless descent durability is the limiter.",
            "Do not combine with another hard quality stimulus in the same micro week unless deliberately planned.",
        ),
        workout_blocks=(
            running_warmup(),
            choose_main(
                [
                    option(
                        "Sustained Climb Limiter",
                        [
                            part("Sustained Climb", "Climb at strong controlled effort on grade similar to the goal limiter.", "8-15 minutes", "6-8"),
                            part("Easy Recovery", "Recover easily on safe terrain.", "4-8 minutes", "1-3"),
                        ],
                        repeat="2-5 rounds",
                    ),
                    option(
                        "Hike-Run Strength-Endurance",
                        [
                            part("Power-Hike Segment", "Hike strongly with race-relevant posture and cadence.", "4-8 minutes", "5-7"),
                            part("Run Segment", "Transition into controlled uphill or rolling running.", "3-6 minutes", "5-7"),
                            part("Easy Recovery", "Recover easily before repeating.", "4-8 minutes", "1-3"),
                        ],
                        repeat="2-4 rounds",
                    ),
                ]
            ),
            easy_cooldown(),
        ),
    ),
    PhilosophySessionSpec(
        id="session_059",
        title="CTS Event-Demands Session",
        philosophy_profile_id=CTS,
        session_family=RACE_PRACTICE_SESSION_FAMILY,
        parent_micro_ids=("micro_112", "micro_113"),
        typical_duration="45-180 minutes",
        summary="A controlled exposure to the event demand most likely to shape race-day outcome.",
        purpose="Practice one or two decisive event demands instead of building a generic hard workout.",
        tags=("cts", "event_demands", "specificity"),
        training_profile=(
            "Event-specific exposure selected from course, terrain, climate, gear, or pacing demands.",
            "The session is defined by the practical demand, not by arbitrary intensity.",
        ),
        expected_adaptations=(
            "Better readiness for the event's decisive demands.",
            "Clearer understanding of what still needs adjustment.",
        ),
        watchouts=(
            "Do not simulate the whole race too often.",
            "Avoid combining heat, vertical, technicality, and fueling novelty all at once.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option("Climb Demand", [part("Climb Exposure", "Practice the climb style most relevant to the event.", "30-90 minutes", "4-7")]),
                    option("Descent Demand", [part("Descent Exposure", "Practice controlled descending with technical restraint.", "20-60 minutes", "4-7")]),
                    option("Environmental Demand", [part("Condition Exposure", "Practice heat, cold, altitude, or surface demand conservatively.", "30-120 minutes", "3-6")]),
                ]
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_060",
        title="CTS Race-Execution Strategy Rehearsal",
        philosophy_profile_id=CTS,
        session_family=RACE_PRACTICE_SESSION_FAMILY,
        parent_micro_ids=("micro_114", "micro_115", "micro_116"),
        typical_duration="45-150 minutes",
        summary="A rehearsal of pacing, gear, aid-flow, and decision routines tied to the athlete's race strategy.",
        purpose="Turn race strategy into repeatable behaviors before race day.",
        tags=("cts", "race_execution", "strategy"),
        training_profile=(
            "Movement plus practical race-execution decisions.",
            "The rehearsal focuses on a few high-value strategy points rather than every detail.",
        ),
        expected_adaptations=(
            "Improved pacing and decision reliability.",
            "Reduced race-day friction around gear, aid, and transitions.",
        ),
        watchouts=(
            "Do not let rehearsal become a fitness test.",
            "Practice strategy under enough load to learn, but not so much that recovery is compromised.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option(
                        "Pacing Strategy Rehearsal",
                        [part("Pacing Practice", "Run or hike-run with planned conservative starts, climbs, descents, and surges.", "45-120 minutes", "3-6")],
                    ),
                    option(
                        "Aid And Gear Flow Rehearsal",
                        [part("Execution Flow", "Practice carrying, accessing, and using planned gear and aid routines while moving.", "45-150 minutes", "3-6")],
                    ),
                ]
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_061",
        title="CTS Fueling Strategy Rehearsal",
        philosophy_profile_id=CTS,
        session_family=RACE_PRACTICE_SESSION_FAMILY,
        parent_micro_ids=("micro_117", "micro_118", "micro_119"),
        typical_duration="45-180 minutes",
        summary="A fueling and hydration session designed to test the actual strategy the athlete may use.",
        purpose="Improve nutrition reliability by practicing timing, products, hydration, and adjustment decisions under useful load.",
        tags=("cts", "fueling", "hydration", "strategy"),
        training_profile=(
            "Fueling plan practice during easy-to-moderate endurance movement.",
            "The session isolates useful nutrition lessons rather than testing everything at once.",
        ),
        expected_adaptations=(
            "Improved gut tolerance and confidence.",
            "Better practical knowledge of timing, products, and hydration needs.",
        ),
        watchouts=(
            "Do not combine many new products in one session.",
            "Keep physical load controlled so fueling feedback is interpretable.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option("Timing Rehearsal", [part("Planned Intake", "Take fuel and fluids on the planned interval while moving easily.", "45-120 minutes", "2-5")]),
                    option("Tolerance Rehearsal", [part("Controlled Fueling Test", "Practice the target intake rate under steady but controlled effort.", "60-180 minutes", "3-6")]),
                ]
            ),
        ),
    ),
)


CTS_SESSION_CARDS = build_philosophy_session_cards(_SPECS)
