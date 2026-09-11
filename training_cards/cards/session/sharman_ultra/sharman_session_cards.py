from __future__ import annotations

from training_cards.cards.session._philosophy_session_builder import (
    PhilosophySessionSpec,
    build_philosophy_session_cards,
    choose_main,
    option,
    part,
    support_notes,
)
from training_cards.philosophy_profiles import SHARMAN_ULTRA
from training_cards.session_families import RACE_PRACTICE_SESSION_FAMILY


_SPECS: tuple[PhilosophySessionSpec, ...] = (
    PhilosophySessionSpec(
        id="session_074",
        title="Sharman Course-Reality Exposure Session",
        philosophy_profile_id=SHARMAN_ULTRA,
        session_family=RACE_PRACTICE_SESSION_FAMILY,
        parent_micro_ids=("micro_167", "micro_168"),
        typical_duration="60-240 minutes",
        summary="A course-demand exposure session shaped by realistic access, terrain, and life constraints.",
        purpose="Prepare for the course as it actually can be practiced, not as an idealized version of specificity.",
        tags=("sharman_ultra", "course_reality", "specificity"),
        training_profile=(
            "Practical course exposure using available terrain, routes, equipment, and time.",
            "Specificity is approximated intelligently when exact course access is impossible.",
        ),
        expected_adaptations=(
            "Better readiness for decisive course demands.",
            "Improved ability to translate imperfect training access into useful preparation.",
        ),
        watchouts=(
            "Do not force unrealistic course simulation when access or recovery cost is poor.",
            "Avoid turning every long outing into maximal specificity.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option("Available-Climb Exposure", [part("Climb Reality Practice", "Use available climbs, treadmill, stairs, or hiking to approximate the course climb demand.", "45-120 minutes", "3-6")]),
                    option("Descent Or Technical Exposure", [part("Terrain Reality Practice", "Practice the safest available version of technical or downhill demand.", "30-90 minutes", "3-6")]),
                    option("Imperfect Specificity Outing", [part("Practical Specificity", "Combine the best available course-like demands without pretending the match is perfect.", "90-240 minutes", "3-6")]),
                ]
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_075",
        title="Sharman Practical Ultra Execution Session",
        philosophy_profile_id=SHARMAN_ULTRA,
        session_family=RACE_PRACTICE_SESSION_FAMILY,
        parent_micro_ids=("micro_169", "micro_171"),
        typical_duration="75-240 minutes",
        summary="A practical ultra execution session for pacing, hiking, fueling, and restraint under realistic conditions.",
        purpose="Turn fitness into usable ultra behavior without making the session a race simulation every time.",
        tags=("sharman_ultra", "ultra_execution", "pacing"),
        training_profile=(
            "Ultra-specific execution practice at controlled cost.",
            "Pacing, hiking, fueling, and patience are trained together when useful.",
        ),
        expected_adaptations=(
            "Improved practical ultra pacing.",
            "Better confidence with hiking transitions and patient execution.",
        ),
        watchouts=(
            "Do not practice hero pacing.",
            "The session should teach sustainable choices, not simply accumulate fatigue.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option("Pacing And Hiking Execution", [part("Ultra Execution", "Practice conservative pacing, hiking transitions, and steady fueling on realistic terrain.", "75-180 minutes", "3-6")]),
                    option("Long Practical Execution", [part("Extended Ultra Practice", "Extend execution practice only when the athlete can recover and learn from it.", "150-240 minutes", "3-6")]),
                ]
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_076",
        title="Sharman Ultra Problem-Solving Rehearsal",
        philosophy_profile_id=SHARMAN_ULTRA,
        session_family=RACE_PRACTICE_SESSION_FAMILY,
        parent_micro_ids=("micro_170", "micro_176", "micro_177"),
        typical_duration="45-180 minutes",
        summary="A rehearsal for foreseeable ultra problems and calm practical adjustments.",
        purpose="Practice responding to problems before race day so the athlete has useful defaults under stress.",
        tags=("sharman_ultra", "problem_solving", "rehearsal"),
        training_profile=(
            "Movement session with one or two planned problem-solving prompts.",
            "Problems are rehearsed calmly, not dramatized.",
        ),
        expected_adaptations=(
            "Better race-day composure.",
            "Improved practical adjustment skill when plans stop being perfect.",
        ),
        watchouts=(
            "Do not overload the session with too many simulated problems.",
            "Avoid unsafe rehearsals; problem-solving should reduce risk, not create it.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option("Pacing Problem Rehearsal", [part("Adjustment Practice", "Practice slowing, hiking, resetting, and restarting after a planned pacing mistake or terrain change.", "45-120 minutes", "3-6")]),
                    option("Fueling Or Gear Problem Rehearsal", [part("Practical Fix Practice", "Practice a simple response to missed fueling, gear friction, weather change, or route disruption.", "45-180 minutes", "3-6")]),
                ]
            ),
            support_notes("Keep the rehearsal useful and calm. The goal is a better default response, not stress exposure for its own sake."),
        ),
    ),
    PhilosophySessionSpec(
        id="session_077",
        title="Sharman Fueling-Gear Logistics Rehearsal Session",
        philosophy_profile_id=SHARMAN_ULTRA,
        session_family=RACE_PRACTICE_SESSION_FAMILY,
        parent_micro_ids=("micro_169", "micro_172", "micro_173"),
        typical_duration="60-240 minutes",
        summary="A practical rehearsal of fueling, gear, aid-flow, and logistics as one connected ultra system.",
        purpose="Make the race-day logistics system familiar before consequences are high.",
        tags=("sharman_ultra", "fueling", "gear", "logistics"),
        training_profile=(
            "Race-practice movement with planned gear, fueling, and logistics routines.",
            "The card merges fueling-gear integration and logistics rehearsal because they function as one ultra system.",
        ),
        expected_adaptations=(
            "Improved race-day logistics confidence.",
            "Better integration of fueling, gear access, aid routines, and terrain movement.",
        ),
        watchouts=(
            "Do not test too many new products or gear pieces at once.",
            "Keep effort controlled so logistics feedback is not hidden by exhaustion.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option("Fueling-Gear Integration", [part("Integrated Practice", "Practice planned intake, carrying system, clothing, poles, lighting, or pack access while moving.", "60-150 minutes", "3-6")]),
                    option("Aid-Flow Logistics Rehearsal", [part("Aid Routine Practice", "Practice stopping, refilling, changing gear, and restarting efficiently without rushing.", "60-180 minutes", "2-5")]),
                    option("Long Logistics Rehearsal", [part("Extended Logistics Simulation", "Combine fueling, gear, aid-flow, and realistic terrain at a scale the athlete can absorb.", "150-240 minutes", "3-6")]),
                ]
            ),
        ),
    ),
)


SHARMAN_SESSION_CARDS = build_philosophy_session_cards(_SPECS)
