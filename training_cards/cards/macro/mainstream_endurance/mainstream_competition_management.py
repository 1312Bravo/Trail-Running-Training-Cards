from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MacroCard,
    TrainingLevel,
)

mainstream_competition_management = MacroCard(
    id = 'macro_006',
    slug = 'mainstream-competition-management',
    title = 'Competition Management',
    card_type = CardType.MACRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A race-season phase for balancing recovery, freshness, learning, and small fitness touchpoints between events.',
    purpose = 'Manage training between multiple meaningful events without treating every gap as a full build or full recovery cycle.',
    tags = [
        'competition',
        'race_season',
        'freshness',
        'between_races'
    ],
    goal_race_context = [
        'During a race series, multi-race season, or closely spaced goal events.',
        'When competition itself creates meaningful training and recovery cost.',
        'When the athlete needs to stay ready without chasing a new fitness peak between every race.',
        'For trail races where mechanical, travel, environmental, or technical cost varies greatly between events.'
    ],
    training_profile = [
        'Training load is adjusted around race stress and recovery response.',
        'Small aerobic, intensity, strength, or terrain touchpoints preserve key qualities without major fatigue.',
        'Post-race review informs the next training decision.',
        'Trail race cost is judged by duration, descent damage, technical stress, travel, conditions, and emotional load.'
    ],
    expected_adaptations = [
        'Better readiness across a race season rather than only for one event.',
        'Improved ability to recover, learn, and adjust between competitions.',
        'Preserved useful fitness with less risk of overreaching.'
    ],
    progression_rules = [
        'Progress by improving how accurately training responds to each race cost.',
        'Use small fitness touchpoints only when recovery signs are stable.',
        'Shift to maintenance, recovery, or a new build when the race sequence ends.'
    ],
    regression_rules = [
        'Prioritize recovery if soreness, motivation, sleep, or easy effort remains abnormal after racing.',
        'Remove intensity between events if race stress already supplied enough high cost.',
        'Use maintenance rather than competition management when there is no meaningful race pressure.'
    ],
    references = [
        CardReference(
            card_id = 'macro_005',
            relationship = CardRelationship.PREVIOUS,
            tags = [
                'after_race'
            ]
        ),
        CardReference(
            card_id = 'macro_007',
            relationship = CardRelationship.NEXT,
            tags = [
                'season_complete'
            ]
        ),
        CardReference(
            card_id = 'macro_009',
            relationship = CardRelationship.ALTERNATIVE,
            tags = [
                'lower_race_pressure'
            ]
        )
    ],
    recommended_duration_weeks = '2-12+',
    timing_guidance = [
        'Use when multiple events are close enough that they shape the training plan.',
        'Each race should reset the next decision rather than automatically repeating the same between-race template.'
    ],
    watchouts = [
        'Do not treat every race as both a maximal performance and a training workout.',
        'Avoid squeezing full development blocks into gaps that only allow recovery and touchpoints.',
        'Do not ignore hidden trail costs such as descents, travel, heat, or technical fatigue.',
        'Repeatedly flat races or worsening recovery indicate the season is too dense.'
    ],
    additional_information = 'Competition management recognizes that races are not separate from training. Each event creates information, stress, and recovery needs; the coach uses the space between events to preserve readiness rather than forcing a normal build into an abnormal calendar.'
)
