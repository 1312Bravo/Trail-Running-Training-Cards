from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MacroCard,
    TrainingLevel,
)

mainstream_base_development = MacroCard(
    id = 'macro_002',
    slug = 'mainstream-base-development',
    title = 'Base Development',
    card_type = CardType.MACRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A foundation-building phase for aerobic capacity, durable routine, strength support, and load tolerance.',
    purpose = 'Build the broad capacity that makes later performance, specificity, and harder training more useful.',
    tags = [
        'base',
        'aerobic',
        'durability',
        'foundation'
    ],
    goal_race_context = [
        'Early in a preparation cycle before demanding race-specific work.',
        'When the athlete needs better aerobic durability or more consistent training tolerance.',
        'After return-to-consistency work is stable enough to support gradual progression.',
        'For long-range goals where a wider foundation is more valuable than early specificity.'
    ],
    training_profile = [
        'High proportion of easy aerobic running with controlled progression.',
        'Gradual long-run development and enough recovery to make volume repeatable.',
        'Strength, mobility, strides, or coordination work may support durability without dominating the phase.',
        'Trail terrain can be varied, but technicality, climbing, and descent load should increase gradually.'
    ],
    expected_adaptations = [
        'Improved aerobic efficiency and endurance.',
        'Greater tolerance for weekly running load and long-run duration.',
        'Better readiness for more directed capacity or race-specific training.'
    ],
    progression_rules = [
        'Increase load gradually through frequency, duration, or long-run progression before frequent intensity.',
        'Keep most work easy enough that the athlete can repeat the week well.',
        'Move toward capacity development when volume, routine, and recovery are stable.'
    ],
    regression_rules = [
        'Hold weekly load steady if easy running becomes less easy.',
        'Reduce vertical gain, technicality, or downhill exposure before abandoning the aerobic purpose.',
        'Return to consistency work if the routine itself becomes unreliable.'
    ],
    references = [
        CardReference(
            card_id = 'macro_001',
            relationship = CardRelationship.PREVIOUS,
            tags = [
                'common_sequence'
            ]
        ),
        CardReference(
            card_id = 'macro_003',
            relationship = CardRelationship.NEXT,
            tags = [
                'development_sequence'
            ]
        ),
        CardReference(
            card_id = 'macro_009',
            relationship = CardRelationship.ALTERNATIVE,
            tags = [
                'lower_cost'
            ]
        )
    ],
    recommended_duration_weeks = '8-16',
    timing_guidance = [
        'Usually belongs early in the training cycle.',
        'Longer goals or less durable athletes may need a longer base before specific work.'
    ],
    watchouts = [
        'Do not make the phase a race-specific block too early.',
        'Avoid chronic moderate-hard running that makes easy volume less repeatable.',
        'Do not increase volume, vertical gain, and long-run difficulty together too aggressively.',
        'Persistent heaviness or soreness means the base is not being absorbed.'
    ],
    additional_information = 'Base development is not filler before the real training starts. It is where the athlete becomes more trainable: able to run regularly, absorb load, move well, and carry enough aerobic capacity for later work to matter.'
)
