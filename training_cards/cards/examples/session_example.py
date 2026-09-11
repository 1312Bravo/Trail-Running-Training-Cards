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
from training_cards.session_families import AEROBIC_POWER_SESSION_FAMILY


example_session_card = SessionCard(
    id="example_session_001",
    slug="example-aerobic-power-intervals",
    title="Example Aerobic Power Intervals",
    card_type=CardType.SESSION,
    philosophy_profile_ids=[MAINSTREAM_ENDURANCE],
    suitable_levels=[TrainingLevel.INTERMEDIATE, TrainingLevel.ADVANCED],
    session_family=AEROBIC_POWER_SESSION_FAMILY,
    typical_duration="50-75 minutes",
    summary="Example session card showing workout blocks, options, repeats, and concrete parts.",
    purpose="Use this as an authoring reference, not as a publishable card.",
    workout_blocks=[
        WorkoutBlock(
            block_type=WorkoutBlockType.WARMUP,
            execution_mode=WorkoutBlockExecutionMode.DO_ALL,
            options=[
                WorkoutOption(
                    title="Standard Warm-Up",
                    parts=[
                        SessionPart(
                            title="Easy Running",
                            prescription="Run easily until breathing, rhythm, and mechanics feel settled.",
                            duration="15-20 minutes",
                            rpe="2-3",
                        ),
                        SessionPart(
                            title="Relaxed Strides",
                            prescription="Run 4 x 20 sec relaxed fast with easy jogging between.",
                            duration="4-6 minutes",
                            rpe="5-7",
                            coaching_notes="Keep these smooth; they prepare the legs but are not the workout.",
                        ),
                    ],
                )
            ],
        ),
        WorkoutBlock(
            block_type=WorkoutBlockType.MAIN,
            execution_mode=WorkoutBlockExecutionMode.CHOOSE_ONE,
            options=[
                WorkoutOption(
                    title="Four-Minute Repetitions",
                    repeat="4 rounds",
                    selection_notes="Use when the athlete is experienced and ready for longer hard repetitions.",
                    load_notes="Higher sustained aerobic-power load.",
                    parts=[
                        SessionPart(
                            title="Hard Repetition",
                            prescription="Run 4 min hard at controlled aerobic-power effort.",
                            rpe="8-9",
                            coaching_notes="Hard but repeatable; avoid racing the first repetition.",
                        ),
                        SessionPart(
                            title="Easy Recovery",
                            prescription="Jog easily for 3 min before the next repetition.",
                            rpe="1-3",
                        ),
                    ],
                ),
                WorkoutOption(
                    title="Introductory Repetitions",
                    repeat="5 rounds",
                    selection_notes="Use when the athlete needs a gentler entry into the same session family.",
                    load_notes="Lower hard-duration cost than the four-minute option.",
                    parts=[
                        SessionPart(
                            title="Hard Repetition",
                            prescription="Run 3 min hard at controlled aerobic-power effort.",
                            rpe="8",
                        ),
                        SessionPart(
                            title="Easy Recovery",
                            prescription="Jog easily for 2-3 min before the next repetition.",
                            rpe="1-3",
                        ),
                    ],
                ),
            ],
        ),
        WorkoutBlock(
            block_type=WorkoutBlockType.COOLDOWN,
            execution_mode=WorkoutBlockExecutionMode.DO_ALL,
            options=[
                WorkoutOption(
                    title="Easy Cool-Down",
                    parts=[
                        SessionPart(
                            title="Easy Running",
                            prescription="Run easily until breathing and legs settle.",
                            duration="10-15 minutes",
                            rpe="1-2",
                        )
                    ],
                )
            ],
        ),
    ],
    watchouts=["Do not use this example as a finished prescription without coaching review."],
    progression_rules=["Progress only when all repetitions stay technically clean and controlled."],
    regression_rules=["Choose the introductory option, shorten repetitions, or extend recoveries if form fades."],
    additional_information=(
        "Session cards prescribe reusable workout patterns. Similar variants can be options inside "
        "one card, while terrain-specific, risk-specific, or adaptation-specific workouts should become separate cards."
    ),
    references=[
        CardReference(
            card_id="example_micro_001",
            relationship=CardRelationship.PARENT,
            tags=["example_parent"],
        )
    ],
)
