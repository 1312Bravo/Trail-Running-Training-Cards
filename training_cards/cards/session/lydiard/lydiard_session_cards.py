from __future__ import annotations

from training_cards.cards.session._philosophy_session_builder import (
    PhilosophySessionSpec,
    build_philosophy_session_cards,
    block,
    choose_main,
    easy_cooldown,
    option,
    part,
    running_warmup,
)
from training_cards.philosophy_profiles import LYDIARD
from training_cards.schemas import WorkoutBlockType
from training_cards.session_families import (
    CONTROLLED_QUALITY_SESSION_FAMILY,
    EASY_SESSION_FAMILY,
    ENDURANCE_SESSION_FAMILY,
    STRENGTH_ENDURANCE_SESSION_FAMILY,
)


_SPECS: tuple[PhilosophySessionSpec, ...] = (
    PhilosophySessionSpec(
        id="session_052",
        title="Lydiard Sustainable Aerobic Conditioning Run",
        philosophy_profile_id=LYDIARD,
        session_family=EASY_SESSION_FAMILY,
        parent_micro_ids=("micro_087", "micro_088", "micro_089"),
        typical_duration="45-100 minutes",
        summary="A sustainable aerobic run used to build the Lydiard foundation without premature intensity.",
        purpose="Accumulate aerobic conditioning that can support later hill, coordination, and sharpening phases.",
        tags=("lydiard", "aerobic_conditioning", "foundation"),
        training_profile=(
            "Steady-enough aerobic work that remains sustainable across the week.",
            "Effort is controlled by repeatability and aerobic response, not isolated pace.",
        ),
        expected_adaptations=(
            "Improved aerobic conditioning and resilience.",
            "Better ability to absorb later sequence layers.",
        ),
        watchouts=(
            "Do not turn aerobic conditioning into premature anaerobic work.",
            "If the athlete cannot repeat the week's aerobic rhythm, the run was too costly.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option(
                        "Sustainable Aerobic Run",
                        [
                            part(
                                "Aerobic Conditioning",
                                "Run at a controlled aerobic effort that feels sustainable and repeatable.",
                                "45-80 minutes",
                                "3-5",
                                coaching_notes="The effort may be stronger than very easy, but it must not become a race or threshold test.",
                            )
                        ],
                    ),
                    option(
                        "Longer Aerobic Conditioning",
                        [
                            part(
                                "Extended Aerobic Conditioning",
                                "Extend the same sustainable aerobic effort only when recent response is stable.",
                                "75-100 minutes",
                                "3-5",
                                adjustment_notes="Shorten or ease off if the run starts to compromise the next aerobic day.",
                            )
                        ],
                    ),
                ]
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_053",
        title="Lydiard Long Aerobic Conditioning Run",
        philosophy_profile_id=LYDIARD,
        session_family=ENDURANCE_SESSION_FAMILY,
        parent_micro_ids=("micro_090", "micro_091", "micro_092"),
        typical_duration="90-180 minutes",
        summary="A long aerobic run that anchors the endurance foundation inside a coherent Lydiard sequence.",
        purpose="Build stamina through controlled duration while preserving the larger aerobic-conditioning system.",
        tags=("lydiard", "long_aerobic", "stamina"),
        training_profile=(
            "Long aerobic duration with restraint.",
            "The run supports the sequence instead of becoming a one-day heroic effort.",
        ),
        expected_adaptations=(
            "Improved aerobic stamina and fatigue resistance.",
            "Greater readiness for later hill resistance and race-preparation work.",
        ),
        watchouts=(
            "Do not use the long run to compensate for missed aerobic rhythm.",
            "Terrain should not add so much muscular cost that it disrupts the next layer.",
        ),
        workout_blocks=(
            choose_main(
                [
                    option(
                        "Long Aerobic Conditioning",
                        [
                            part(
                                "Long Aerobic Running",
                                "Run long at a controlled aerobic effort, keeping the final third composed.",
                                "90-150 minutes",
                                "3-5",
                                terrain_notes="Use rolling or familiar terrain when possible; technical trail cost should be planned.",
                            )
                        ],
                    ),
                    option(
                        "Supported Long Aerobic Outing",
                        [
                            part(
                                "Run-Hike Endurance",
                                "Use easy running and purposeful hiking to preserve aerobic control over longer duration.",
                                "120-180 minutes",
                                "3-5",
                                selection_notes="Best for trail and mountain goals when continuous running would add too much cost.",
                            )
                        ],
                    ),
                ]
            ),
        ),
    ),
    PhilosophySessionSpec(
        id="session_054",
        title="Lydiard Hill Resistance Circuit",
        philosophy_profile_id=LYDIARD,
        session_family=STRENGTH_ENDURANCE_SESSION_FAMILY,
        parent_micro_ids=("micro_093", "micro_094", "micro_095", "micro_096"),
        typical_duration="45-80 minutes",
        summary="A hill-resistance circuit that bridges aerobic conditioning toward stronger mechanics and later faster work.",
        purpose="Develop hill strength, spring, and coordination without treating the session as a simple fitness interval workout.",
        tags=("lydiard", "hill_resistance", "circuit"),
        training_profile=(
            "Circuit-style hill resistance with controlled mechanics.",
            "Sequenced after aerobic preparation and before sharper race expression.",
        ),
        expected_adaptations=(
            "Improved force application and running mechanics.",
            "Better transition from aerobic conditioning to faster coordinated work.",
        ),
        watchouts=(
            "Avoid maximal hill sprinting or heavy eccentric damage.",
            "Do not add the circuit before the athlete is prepared for hill resistance.",
        ),
        workout_blocks=(
            running_warmup(),
            block(
                WorkoutBlockType.MAIN,
                [
                    option(
                        "Hill Resistance Circuit",
                        [
                            part("Uphill Bounding Or Springing", "Move uphill with controlled spring and posture.", "30-60 seconds", "6-8"),
                            part("Easy Jog Float", "Jog easily on safer terrain to reset mechanics.", "60-120 seconds", "1-3"),
                            part("Uphill Running", "Run uphill smoothly with strong but relaxed form.", "60-120 seconds", "6-7"),
                            part("Easy Recovery", "Recover fully enough to keep the next round coordinated.", "2-4 minutes", "1-3"),
                        ],
                        repeat="3-6 rounds",
                        load_notes="Keep the circuit technical and sequenced; more rounds are not better if mechanics fade.",
                    )
                ],
            ),
            easy_cooldown(),
        ),
    ),
    PhilosophySessionSpec(
        id="session_055",
        title="Lydiard Sequence-Expression Sharpening Session",
        philosophy_profile_id=LYDIARD,
        session_family=CONTROLLED_QUALITY_SESSION_FAMILY,
        parent_micro_ids=("micro_098", "micro_099", "micro_100"),
        typical_duration="30-65 minutes",
        summary="A sharpening session that expresses completed preparation rather than trying to add missing fitness.",
        purpose="Preserve rhythm, confidence, and race feel while protecting freshness at the end of the sequence.",
        tags=("lydiard", "sharpening", "sequence_expression"),
        training_profile=(
            "Small familiar quality doses after the main preparation layers are complete.",
            "Designed to reveal readiness, not create fatigue.",
        ),
        expected_adaptations=(
            "Sharper rhythm and confidence.",
            "Better freshness protection before competition.",
        ),
        watchouts=(
            "Do not use sharpening to make up for missed base or hill work.",
            "Stop while the athlete still feels composed and eager.",
        ),
        workout_blocks=(
            running_warmup(),
            choose_main(
                [
                    option(
                        "Relaxed Sharpening Repetitions",
                        [
                            part("Relaxed Repetition", "Run fast but smooth, staying in control.", "30-90 seconds", "7-8"),
                            part("Full Easy Recovery", "Jog or walk easily until rhythm feels reset.", "2-4 minutes", "1-2"),
                        ],
                        repeat="4-8 rounds",
                    ),
                    option(
                        "Race-Feel Touch",
                        [
                            part(
                                "Short Race-Feel Segments",
                                "Run several short controlled segments at familiar race rhythm, never straining.",
                                "2-4 minutes each",
                                "6-7",
                            ),
                            part("Easy Recovery", "Jog easily between segments.", "2-4 minutes", "1-3"),
                        ],
                        repeat="2-4 rounds",
                    ),
                ]
            ),
            easy_cooldown(),
        ),
    ),
)


LYDIARD_SESSION_CARDS = build_philosophy_session_cards(_SPECS)
