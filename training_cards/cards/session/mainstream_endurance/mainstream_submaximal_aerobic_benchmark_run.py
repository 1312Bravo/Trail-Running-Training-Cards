from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    SessionCard,
    SessionPart,
    TrainingLevel,
)
from training_cards.session_families import EASY_SESSION_FAMILY

mainstream_submaximal_aerobic_benchmark_run = SessionCard(
    id = 'session_015',
    slug = 'mainstream-submaximal-aerobic-benchmark-run',
    title = 'Submaximal Aerobic Benchmark Run',
    card_type = CardType.SESSION,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A repeatable easy-to-steady run used to observe aerobic response without racing.',
    purpose = 'Collect practical information about aerobic control, recovery state, and training response.',
    tags = [
        'mainstream_endurance',
        'assessment',
        'aerobic',
        'monitoring'
    ],
    goal_race_context = [
        'Use during aerobic progression or consolidation when a low-cost readiness check is useful.',
        'Useful after a block when the coach needs comparable response information before progressing.',
        'Appropriate when conditions can be kept reasonably consistent.'
    ],
    expected_adaptations = [
        'Better intensity awareness.',
        'More reliable feedback for progression decisions.',
        'Improved ability to hold a controlled aerobic effort.'
    ],
    progression_rules = [
        'Repeat under similar conditions before drawing conclusions.',
        'Use the result to adjust training load, not to label the athlete permanently.',
        'Only lengthen the benchmark if the added duration remains low-cost and useful.'
    ],
    regression_rules = [
        'Shorten the controlled segment if the athlete is returning from fatigue or interruption.',
        'Use RPE and breathing when pace, heart rate, or power is distorted by terrain or weather.',
        'Skip the benchmark if it would become a test of toughness rather than useful information.'
    ],
    references = [
        CardReference(
            card_id = 'micro_010',
            relationship = CardRelationship.SUPPORT,
            tags = [
                'progression_check'
            ]
        ),
        CardReference(
            card_id = 'micro_012',
            relationship = CardRelationship.PARENT,
            tags = [
                'optional_check'
            ]
        )
    ],
    session_family = EASY_SESSION_FAMILY,
    typical_duration = '35-70 minutes',
    workout_parts = [
        SessionPart(
            name = 'Warm-Up',
            duration = '10-15 min',
            rpe = '2-3',
            instructions = 'Run easily until breathing, rhythm, and movement feel settled.',
            terrain_notes = 'Use familiar terrain with minimal interruptions when possible.'
        ),
        SessionPart(
            name = 'Controlled Benchmark',
            duration = '20-40 min',
            rpe = '3-4',
            instructions = 'Hold a sustainable aerobic effort and record pace, heart rate or power if useful, RPE, breathing, and movement quality.',
            terrain_notes = 'Keep route, surface, and elevation as comparable as practical between repeats.'
        ),
        SessionPart(
            name = 'Cool-Down And Notes',
            duration = '5-15 min',
            rpe = '1-2',
            instructions = 'Finish easily and note conditions, fatigue, sleep, soreness, and any reason the result may not compare cleanly.'
        )
    ],
    training_profile = [
        'Submaximal aerobic assessment.',
        'Repeatable conditions matter more than impressive output.',
        'Intensity stays easy to steady, not threshold.',
        'Data is interpreted alongside fatigue, heat, terrain, and recovery context.'
    ],
    watchouts = [
        'Do not turn the benchmark into a time trial.',
        'Do not compare different terrain or weather as if the dose was identical.',
        'Do not progress training from a single unusually good or bad result.',
        'Avoid the session when pain, illness, or excessive fatigue makes the information unreliable.'
    ],
    additional_information = 'This session reflects mainstream assessment practice: test only what helps the next decision and keep the cost proportionate. A useful benchmark is repeatable and contextual. For trail runners, a flat or rolling route may give cleaner aerobic information than a technical trail; if trail terrain is used, the coach should record vertical gain, footing, and descent cost.'
)
