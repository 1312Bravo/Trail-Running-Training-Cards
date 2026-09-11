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
from training_cards.philosophy_profiles import SWAP
from training_cards.session_families import (
    CONTROLLED_QUALITY_SESSION_FAMILY,
    EASY_SESSION_FAMILY,
    ENDURANCE_SESSION_FAMILY,
    NEUROMUSCULAR_SESSION_FAMILY,
    RACE_PRACTICE_SESSION_FAMILY,
    STRENGTH_ENDURANCE_SESSION_FAMILY,
)


_SPECS: tuple[PhilosophySessionSpec, ...] = (
    PhilosophySessionSpec(
        id="session_066",
        title="SWAP Confidence Re-Entry Session",
        philosophy_profile_id=SWAP,
        session_family=EASY_SESSION_FAMILY,
        parent_micro_ids=("micro_141", "micro_142"),
        typical_duration="15-50 minutes",
        summary="A re-entry session designed to make training feel safe, possible, and athlete-owned.",
        purpose="Restore confidence and rhythm without pressure, comparison, or hidden tests.",
        tags=("swap", "confidence", "reentry"),
        training_profile=("Very easy movement with explicit permission to stop, walk, or simplify.", "Success is defined by calm completion, not pace."),
        expected_adaptations=("Improved confidence and consistency.", "Better emotional readiness for future aerobic work."),
        watchouts=("Do not frame the session as proving the athlete is back.", "Stop before confidence turns into threat or pressure."),
        workout_blocks=(
            choose_main(
                [
                    option("Supported Run-Walk", [part("Run-Walk Re-Entry", "Alternate easy running with walking in a way that feels calm and repeatable.", "15-35 minutes", "1-4")]),
                    option("Confidence Easy Run", [part("Easy Running", "Run easily on a familiar route with no performance target.", "20-50 minutes", "2-4")]),
                ]
            ),
            support_notes("The SWAP distinction is the gate: the session should increase safety and possibility, not just add aerobic minutes."),
        ),
    ),
    PhilosophySessionSpec(
        id="session_067",
        title="SWAP Health-Protected Aerobic Session",
        philosophy_profile_id=SWAP,
        session_family=EASY_SESSION_FAMILY,
        parent_micro_ids=("micro_143", "micro_144", "micro_154", "micro_162", "micro_164"),
        typical_duration="30-90 minutes",
        summary="An aerobic session with health, energy, and future training protected as the primary constraints.",
        purpose="Build aerobic rhythm only when the session supports the athlete's whole trajectory.",
        tags=("swap", "health_protected", "aerobic"),
        training_profile=("Easy to steady aerobic work with stop rules.", "The athlete's health signal outranks the planned duration."),
        expected_adaptations=("Repeatable aerobic consistency.", "Better trust in sustainable training decisions."),
        watchouts=("Do not borrow from future days to complete today's plan.", "If warning signs appear, cut the session early and call that a good decision."),
        workout_blocks=(
            choose_main(
                [
                    option("Health-Protected Easy", [part("Easy Aerobic Running", "Run easily while checking energy, soreness, mood, and form.", "30-70 minutes", "2-4")]),
                    option("Sustainable Aerobic Build", [part("Aerobic Running", "Extend aerobic work only while form and enthusiasm remain stable.", "45-90 minutes", "3-5")]),
                ]
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_068",
        title="SWAP Speed-Economy Play Session",
        philosophy_profile_id=SWAP,
        session_family=NEUROMUSCULAR_SESSION_FAMILY,
        parent_micro_ids=("micro_148", "micro_149", "micro_150", "micro_151", "micro_152", "micro_163"),
        typical_duration="25-60 minutes",
        summary="A relaxed speed and economy session treated as play and skill rather than strain.",
        purpose="Improve rhythm, coordination, and speed reserve while protecting joy and avoiding pressure.",
        tags=("swap", "speed_economy", "play"),
        training_profile=("Short relaxed speed touches.", "The session should feel crisp, curious, and non-threatening."),
        expected_adaptations=("Improved running economy and coordination.", "Greater confidence around faster running."),
        watchouts=("Stop before speed becomes forced.", "Avoid racing reps, chasing splits, or turning play into evaluation."),
        workout_blocks=(
            running_warmup(),
            choose_main(
                [
                    option(
                        "Playful Strides",
                        [
                            part("Relaxed Fast Stride", "Run fast, smooth, and playful without strain.", "15-25 seconds", "7-8"),
                            part("Full Easy Reset", "Walk or jog until the next stride feels inviting.", "60-120 seconds", "1-2"),
                        ],
                        repeat="4-10 rounds",
                    ),
                    option(
                        "Rolling Speed Play",
                        [
                            part("Terrain-Assisted Pickup", "Use gentle terrain to practice quick, relaxed rhythm.", "20-45 seconds", "6-8"),
                            part("Easy Movement", "Return to easy movement and relaxed breathing.", "1-3 minutes", "1-3"),
                        ],
                        repeat="5-8 rounds",
                    ),
                ]
            ),
            easy_cooldown(),
        ),
    ),
    PhilosophySessionSpec(
        id="session_069",
        title="SWAP Adventure Endurance Session",
        philosophy_profile_id=SWAP,
        session_family=ENDURANCE_SESSION_FAMILY,
        parent_micro_ids=("micro_145", "micro_146", "micro_147"),
        typical_duration="75-240 minutes",
        summary="An endurance outing that builds confidence and ownership through controlled adventure.",
        purpose="Make long aerobic work feel meaningful, repeatable, and athlete-owned without ignoring health cost.",
        tags=("swap", "adventure", "endurance"),
        training_profile=("Low-to-moderate endurance movement with autonomy and route meaning.", "Adventure is scaled so it supports, not threatens, consistency."),
        expected_adaptations=("Improved endurance confidence.", "Better relationship with long trail or mountain movement."),
        watchouts=("Do not use adventure as a disguise for overreach.", "Keep bailout options and post-session recovery honest."),
        workout_blocks=(
            choose_main(
                [
                    option("Controlled Adventure Run", [part("Adventure Endurance", "Run or hike-run a route that feels exciting but manageable.", "75-180 minutes", "2-5")]),
                    option("Confidence Adventure Outing", [part("Route Ownership Outing", "Choose a route with enough novelty to build confidence and enough safety to stay calm.", "90-240 minutes", "2-5")]),
                ]
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_070",
        title="SWAP Fatigue-Resistance Session",
        philosophy_profile_id=SWAP,
        session_family=STRENGTH_ENDURANCE_SESSION_FAMILY,
        parent_micro_ids=("micro_153", "micro_154"),
        typical_duration="45-100 minutes",
        summary="A fatigue-resistance session that explores durability while protecting health and response.",
        purpose="Develop late-run or terrain durability without turning resilience work into a grind contest.",
        tags=("swap", "fatigue_resistance", "durability"),
        training_profile=("Controlled durability stimulus with explicit response monitoring.", "The athlete should finish challenged but not emotionally or physically flattened."),
        expected_adaptations=("Improved fatigue resistance.", "Better understanding of sustainable durability load."),
        watchouts=("Do not celebrate surviving a session that damages the next week.", "Reduce terrain or duration if form deteriorates."),
        workout_blocks=(
            running_warmup(),
            choose_main(
                [
                    option("Controlled Durability Finish", [part("Easy Endurance", "Run easily before adding a controlled durability finish.", "35-70 minutes", "2-4"), part("Durability Finish", "Finish with controlled steady running or climbing, never straining.", "10-25 minutes", "5-6")]),
                    option("Gentle Hill Durability", [part("Hill Durability Repetition", "Climb smoothly at controlled effort.", "3-6 minutes", "5-7"), part("Easy Recovery", "Recover easily.", "3-5 minutes", "1-3")], repeat="3-6 rounds"),
                ]
            ),
            easy_cooldown(),
        ),
    ),
    PhilosophySessionSpec(
        id="session_071",
        title="SWAP Confidence Course-Practice Session",
        philosophy_profile_id=SWAP,
        session_family=RACE_PRACTICE_SESSION_FAMILY,
        parent_micro_ids=("micro_155", "micro_156", "micro_157"),
        typical_duration="45-180 minutes",
        summary="A course-practice session that makes race demands feel understandable and owned.",
        purpose="Prepare for course demands while preserving confidence, autonomy, and realistic scaling.",
        tags=("swap", "course_practice", "confidence"),
        training_profile=("Course-demand exposure with confidence-building constraints.", "Practice is scaled to create learning rather than intimidation."),
        expected_adaptations=("Improved confidence with goal terrain.", "Better ownership of course-specific skills."),
        watchouts=("Do not overmatch the athlete with too much technicality or vertical.", "A confidence course session should end with useful belief, not dread."),
        workout_blocks=(
            choose_main(
                [
                    option("Confidence Climb Practice", [part("Climb Practice", "Practice goal-style climbing at a controlled, confidence-building dose.", "30-90 minutes", "3-6")]),
                    option("Confidence Descent Practice", [part("Descent Practice", "Practice descending calmly with good choices and no racing.", "20-60 minutes", "3-6")]),
                    option("Integrated Course Practice", [part("Course Segment Practice", "Combine a small number of course-like demands at a scale the athlete can own.", "60-180 minutes", "3-6")]),
                ]
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_072",
        title="SWAP Agency Race-Practice Session",
        philosophy_profile_id=SWAP,
        session_family=RACE_PRACTICE_SESSION_FAMILY,
        parent_micro_ids=("micro_158", "micro_159", "micro_160"),
        typical_duration="40-150 minutes",
        summary="A race-practice session centered on choices, agency, and calm execution.",
        purpose="Train the athlete to make useful race decisions rather than simply comply with instructions.",
        tags=("swap", "agency", "race_practice"),
        training_profile=("Race-practice movement with decision prompts.", "The athlete rehearses choosing, adjusting, and staying calm."),
        expected_adaptations=("Better race-day agency.", "Improved confidence in adapting pacing, fueling, and terrain decisions."),
        watchouts=("Do not overload the session with too many choices.", "Agency is not improvising everything; it is practicing clear decisions."),
        workout_blocks=(
            choose_main(
                [
                    option("Pacing Choice Practice", [part("Decision Run", "Practice choosing conservative effort on climbs, flats, and descents.", "40-100 minutes", "3-6")]),
                    option("Fueling And Gear Choice Practice", [part("Decision Rehearsal", "Practice when and how to fuel, drink, adjust gear, or simplify.", "45-150 minutes", "3-6")]),
                ]
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_073",
        title="SWAP Off-Season Play Session",
        philosophy_profile_id=SWAP,
        session_family=CONTROLLED_QUALITY_SESSION_FAMILY,
        parent_micro_ids=("micro_165", "micro_166"),
        typical_duration="20-90 minutes",
        summary="A low-pressure off-season session that restores movement joy without hidden training pressure.",
        purpose="Keep movement identity alive while reducing structure, judgment, and performance demand.",
        tags=("swap", "off_season", "play"),
        training_profile=("Flexible playful movement.", "The session should feel renewing rather than productive at all costs."),
        expected_adaptations=("Improved emotional freshness.", "Maintained movement rhythm with lower pressure."),
        watchouts=("Do not convert off-season play into secret training load.", "Avoid activities that create large soreness unless deliberately chosen."),
        workout_blocks=(
            choose_main(
                [
                    option("Playful Easy Run", [part("Easy Play Run", "Run easily with route freedom and no performance target.", "20-60 minutes", "2-4")]),
                    option("Movement Play", [part("Playful Movement", "Choose low-pressure movement such as hiking, cycling, skiing, drills, or games.", "30-90 minutes", "1-4")]),
                ]
            ),
        ),
    ),
)


SWAP_SESSION_CARDS = build_philosophy_session_cards(_SPECS)
