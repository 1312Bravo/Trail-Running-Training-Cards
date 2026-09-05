from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MacroCard,
    TrainingLevel,
)

mainstream_maintenance = MacroCard(
    id = 'macro_009',
    slug = 'mainstream-maintenance',
    title = 'Maintenance',
    card_type = CardType.MACRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A low-cost phase for preserving useful fitness when full development is not the priority.',
    purpose = 'Hold enough aerobic rhythm, durability, and key qualities to stay ready without forcing a build.',
    tags = [
        'maintenance',
        'sustainability',
        'low_cost',
        'between_goals'
    ],
    goal_race_context = [
        'Between goals when the next full build has not started.',
        'During busy life periods, travel, uncertain schedules, or reduced training availability.',
        'When the athlete benefits from structure but not from progressive overload.',
        'When preserving readiness matters more than creating a new performance peak.'
    ],
    training_profile = [
        'Consistent but controlled aerobic running with lower total cost than a build.',
        'Small touches of intensity, strength, or terrain may preserve key qualities.',
        'The plan should be simple enough to survive real-life constraints.',
        'Trail familiarity, climbing rhythm, and descent tolerance can be maintained without chasing big outings.'
    ],
    expected_adaptations = [
        'Preserved aerobic fitness and training rhythm.',
        'Reduced loss of durability between development cycles.',
        'Lower stress cost during periods when adaptation is not the main target.'
    ],
    progression_rules = [
        'Progress toward base development when time, readiness, and goals support renewed development.',
        'Keep the minimum effective structure rather than adding work because the athlete feels capable.',
        'Use small quality touchpoints only if they do not threaten consistency.'
    ],
    regression_rules = [
        'Reduce to return-to-consistency work if routine becomes unreliable.',
        'Shift to recovery and transition if fatigue, soreness, or low motivation dominates.',
        'Drop optional quality before cutting the whole routine.'
    ],
    references = [
        CardReference(
            card_id = 'macro_008',
            relationship = CardRelationship.ALTERNATIVE,
            tags = [
                'less_performance_pressure'
            ]
        ),
        CardReference(
            card_id = 'macro_002',
            relationship = CardRelationship.NEXT,
            tags = [
                'resume_development'
            ]
        ),
        CardReference(
            card_id = 'macro_001',
            relationship = CardRelationship.NEXT,
            tags = [
                'if_consistency_lost'
            ]
        )
    ],
    recommended_duration_weeks = '2-12+',
    timing_guidance = [
        'Use when a full development cycle would be too costly or unnecessary.',
        'The phase may last as long as life context or goal timing requires.'
    ],
    watchouts = [
        'Do not let maintenance gradually become an unplanned build.',
        'Avoid removing all intensity, strength, or terrain exposure if those qualities will be needed soon.',
        'Do not treat low motivation or fatigue as proof that more structure is needed.',
        'If the athlete loses routine, switch the goal from maintenance to consistency.'
    ],
    additional_information = 'Maintenance is a disciplined choice to preserve what matters with the least useful cost. It is valuable because real athletes have life periods where forcing development would make the next good training cycle harder, not better.'
)
