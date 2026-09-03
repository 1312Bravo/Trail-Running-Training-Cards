from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MicroCard,
    TrainingLevel,
)

mainstream_consolidation_week = MicroCard(
    id = 'micro_012',
    slug = 'mainstream-consolidation-week',
    title = 'Consolidation Week',
    card_type = CardType.MICRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A lower-load mainstream week used to absorb recent training and check readiness.',
    purpose = 'Reduce fatigue while preserving rhythm, then use the response to guide the next training decision.',
    tags = [
        'mainstream_endurance',
        'recovery',
        'consolidation',
        'monitoring'
    ],
    goal_race_context = [
        'Use after two or more building weeks.',
        'Useful after demanding quality, long-run, downhill, or race-practice stress.',
        'Appropriate when fatigue signs are present but the athlete does not need full time off.',
        'Useful before a more specific or more intense block.'
    ],
    expected_adaptations = [
        'Reduced accumulated fatigue.',
        'Restored easy-running rhythm.',
        'Better readiness for the next progression.',
        'More reliable interpretation of current fitness.'
    ],
    progression_rules = [
        'Return to normal training only when easy effort and movement quality have normalized.',
        'Use a short benchmark only if it supports the next decision without adding meaningful fatigue.',
        'Progress from the response pattern, not from the calendar alone.'
    ],
    regression_rules = [
        'Reduce load further if easy running remains unusually hard.',
        'Use cross-training, walking, or rest if running does not feel restorative.',
        'Stop and seek appropriate support if pain, illness, or health concerns are present.'
    ],
    references = [
        CardReference(
            card_id = 'mezzo_012',
            relationship = CardRelationship.PARENT,
            tags = [
                'core_week'
            ]
        ),
        CardReference(
            card_id = 'session_016',
            relationship = CardRelationship.CHILD,
            tags = [
                'easy_rhythm'
            ]
        ),
        CardReference(
            card_id = 'session_015',
            relationship = CardRelationship.CHILD,
            tags = [
                'optional_check'
            ]
        )
    ],
    recommended_duration_days = '7',
    week_structure = [
        'Reduced total running load.',
        'Mostly short easy runs or low-impact aerobic support.',
        'Optional submaximal benchmark only when the athlete is fresh enough for clean information.',
        'No demanding quality, long-run extension, heavy strength, or technical descent emphasis.'
    ],
    key_sessions = [
        'Easy Aerobic Run',
        'Submaximal Aerobic Benchmark Run'
    ],
    load_pattern = 'Reduced-load week focused on adaptation and readiness review.',
    placement_guidance = [
        'Use after building weeks or whenever recovery signs justify consolidation.',
        'Do not place a hidden test or hard trail adventure inside the reduced-load week.'
    ],
    recovery_requirements = [
        'Sessions should leave the athlete fresher, not merely less tired than normal.',
        'Sleep, fueling, soreness, mood, and ordinary easy effort are part of the readiness check.',
        'The week can be extended if normal readiness does not return.'
    ],
    training_profile = [
        'Low intensity.',
        'Lower volume than recent build weeks.',
        'Simple terrain and low mechanical cost.',
        'Observation of response is part of the training purpose.'
    ],
    watchouts = [
        'Turning reduced load into extra strength, chores, hiking, or technical terrain.',
        'Mistaking freshness anxiety for readiness to resume hard work.',
        'Using a benchmark when the athlete is too fatigued to produce useful data.',
        'Ignoring persistent warning signs because the plan says the next block should start.'
    ],
    additional_information = 'A consolidation week protects the mainstream idea that adaptation happens after stress, not only during it. The coach uses lower load to let the athlete absorb training and reveal the next sensible step. This is especially important in trail running, where downhill soreness, technical fatigue, and long time on feet can outlast the visible training log.'
)
