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
from training_cards.philosophy_profiles import EVOKE_ENDURANCE
from training_cards.session_families import (
    CONTROLLED_QUALITY_SESSION_FAMILY,
    RACE_PRACTICE_SESSION_FAMILY,
    STRENGTH_ENDURANCE_SESSION_FAMILY,
    STRENGTH_MOBILITY_SUPPORT_SESSION_FAMILY,
)


_SPECS: tuple[PhilosophySessionSpec, ...] = (
    PhilosophySessionSpec(
        id="session_062",
        title="Evoke Aerobic Threshold Calibration Run",
        philosophy_profile_id=EVOKE_ENDURANCE,
        session_family=CONTROLLED_QUALITY_SESSION_FAMILY,
        parent_micro_ids=("micro_130", "micro_131", "micro_132"),
        typical_duration="45-90 minutes",
        summary="A controlled run used to calibrate aerobic-threshold effort and prevent aerobic work from drifting too hard.",
        purpose="Anchor the athlete's sustainable aerobic range so later Evoke layers sit on the correct foundation.",
        tags=("evoke", "aerobic_threshold", "calibration"),
        training_profile=(
            "Controlled aerobic-threshold running with feedback from breathing, durability, and drift.",
            "The goal is calibration and control, not proving fitness.",
        ),
        expected_adaptations=(
            "Improved aerobic-threshold control.",
            "Clearer effort boundaries for later capacity and mountain work.",
        ),
        watchouts=(
            "Do not turn calibration into a threshold race.",
            "If drift appears early, reduce intensity or return to easy aerobic running.",
        ),
        workout_blocks=(
            running_warmup(),
            choose_main(
                [
                    option(
                        "Aerobic Threshold Check",
                        [
                            part("Calibration Segment", "Run at controlled aerobic-threshold effort and watch for drift.", "20-40 minutes", "4-6"),
                        ],
                    ),
                    option(
                        "Broken Aerobic Threshold",
                        [
                            part("Aerobic Threshold Repetition", "Run controlled aerobic-threshold repetitions.", "8-12 minutes", "4-6"),
                            part("Easy Reset", "Jog easily and check whether effort settles quickly.", "2-4 minutes", "1-3"),
                        ],
                        repeat="2-4 rounds",
                    ),
                ]
            ),
            easy_cooldown(),
        ),
    ),
    PhilosophySessionSpec(
        id="session_063",
        title="Evoke Strength Reserve Session",
        philosophy_profile_id=EVOKE_ENDURANCE,
        session_family=STRENGTH_MOBILITY_SUPPORT_SESSION_FAMILY,
        parent_micro_ids=("micro_127", "micro_128", "micro_129"),
        typical_duration="25-55 minutes",
        summary="A strength session that builds reserve for mountain training without replacing aerobic development.",
        purpose="Improve usable strength reserve so later uphill and objective work costs less.",
        tags=("evoke", "strength_reserve", "support"),
        training_profile=(
            "Strength work placed as support for the endurance sequence.",
            "Load is meaningful but controlled so it does not steal from aerobic progression.",
        ),
        expected_adaptations=(
            "Improved strength reserve and movement robustness.",
            "Better tolerance for later uphill muscular-endurance work.",
        ),
        watchouts=(
            "Avoid soreness that compromises key aerobic sessions.",
            "Do not turn strength reserve into a separate maximal-strength project unless the plan supports it.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option(
                        "Strength Reserve Circuit",
                        [
                            part("Lower-Body Strength", "Use controlled squats, step-ups, hinges, or lunges with clean form.", "15-25 minutes", "4-6"),
                            part("Trunk And Carry Support", "Add trunk, calf, and loaded-carry support as tolerated.", "10-20 minutes", "3-5"),
                        ],
                    ),
                    option(
                        "Reduced Strength Signal",
                        [
                            part("Low-Dose Strength", "Use a short strength signal when fatigue is present but reserve should be maintained.", "15-30 minutes", "2-4"),
                        ],
                    ),
                ]
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_064",
        title="Evoke Uphill Muscular-Endurance Session",
        philosophy_profile_id=EVOKE_ENDURANCE,
        session_family=STRENGTH_ENDURANCE_SESSION_FAMILY,
        parent_micro_ids=("micro_133", "micro_134", "micro_135", "micro_136"),
        typical_duration="50-110 minutes",
        summary="A sustained uphill muscular-endurance session for mountain objectives.",
        purpose="Build uphill force durability after the athlete has enough aerobic and strength reserve to absorb the work.",
        tags=("evoke", "uphill", "muscular_endurance"),
        training_profile=(
            "Specific uphill force-endurance work.",
            "The session belongs in the ME layer, not early aerobic foundation.",
        ),
        expected_adaptations=(
            "Improved sustained uphill force production.",
            "Better ability to use strength reserve in mountain terrain.",
        ),
        watchouts=(
            "Do not add ME work before the foundation can support it.",
            "Reduce volume if mechanics turn into grinding or soreness lingers.",
        ),
        workout_blocks=(
            running_warmup(),
            choose_main(
                [
                    option(
                        "Sustained Uphill ME",
                        [
                            part("Uphill ME Repetition", "Climb at strong sustainable effort with stable posture and cadence.", "8-15 minutes", "6-8"),
                            part("Easy Recovery", "Recover easily on safe terrain.", "5-8 minutes", "1-3"),
                        ],
                        repeat="3-5 rounds",
                    ),
                    option(
                        "Intro Uphill ME",
                        [
                            part("Short Uphill ME Repetition", "Climb with controlled force and no strain.", "4-8 minutes", "5-7"),
                            part("Easy Recovery", "Recover fully before repeating.", "4-6 minutes", "1-3"),
                        ],
                        repeat="3-4 rounds",
                    ),
                ]
            ),
            easy_cooldown(),
        ),
    ),
    PhilosophySessionSpec(
        id="session_065",
        title="Evoke Objective Utilisation Session",
        philosophy_profile_id=EVOKE_ENDURANCE,
        session_family=RACE_PRACTICE_SESSION_FAMILY,
        parent_micro_ids=("micro_137", "micro_138", "micro_139"),
        typical_duration="60-240 minutes",
        summary="A mountain-objective session that uses already built capacity instead of adding more development load.",
        purpose="Practice applying aerobic capacity, strength reserve, and ME capacity to the actual objective demands.",
        tags=("evoke", "objective", "utilisation"),
        training_profile=(
            "Objective-specific movement with controlled learning intent.",
            "The session prioritizes using capacity, not proving it.",
        ),
        expected_adaptations=(
            "Improved objective readiness and execution confidence.",
            "Better integration of terrain, fueling, pacing, and decision skills.",
        ),
        watchouts=(
            "Do not turn objective utilisation into another capacity-development block.",
            "Scale the outing if weather, route, or fatigue raises the consequence too much.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option("Objective Integration Outing", [part("Objective-Specific Movement", "Move on terrain that resembles the objective while staying within planned effort.", "60-180 minutes", "3-6")]),
                    option("Objective Simulation", [part("Controlled Simulation", "Combine route, gear, fueling, and terrain demands at a scale the athlete can absorb.", "120-240 minutes", "3-7")]),
                ]
            ),
            support_notes("The key Evoke distinction is utilisation: the session should express prepared capacity rather than create fatigue to prove it."),
        ),
    ),
)


EVOKE_SESSION_CARDS = build_philosophy_session_cards(_SPECS)
