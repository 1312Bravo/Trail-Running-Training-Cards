from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MacroCard,
    TrainingLevel,
)

mainstream_off_season = MacroCard(
    id = 'macro_008',
    slug = 'mainstream-off-season',
    title = 'Off-Season',
    card_type = CardType.MACRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'An intentional decompression phase away from race preparation and structured performance pressure.',
    purpose = 'Restore freshness, broaden movement, preserve enough rhythm, and prepare the athlete for a healthier next cycle.',
    tags = [
        'off_season',
        'decompression',
        'general_health',
        'reset'
    ],
    goal_race_context = [
        'After the main race season or a demanding goal cycle.',
        'When the athlete needs a mental and physical break from performance-focused structure.',
        'Before returning to base development or maintenance.',
        'When broader movement, strength, mobility, or life balance needs attention.'
    ],
    training_profile = [
        'Less formal structure and less race-specific pressure.',
        'Easy aerobic rhythm may continue, but training should not quietly become another build.',
        'Alternative movement, strength, mobility, hiking, and playful outdoor time can have more space.',
        'Trail running may stay present, but technical, downhill, and long-duration cost should be optional and controlled.'
    ],
    expected_adaptations = [
        'Improved mental freshness and renewed motivation.',
        'Preserved basic aerobic rhythm without high performance pressure.',
        'Opportunity to address general strength, mobility, movement variety, and life balance.'
    ],
    progression_rules = [
        'Progress toward base development when motivation, routine, and readiness naturally return.',
        'Keep enough gentle rhythm that the next phase does not require starting from zero.',
        'Use the phase to resolve small durability or lifestyle issues before structured training resumes.'
    ],
    regression_rules = [
        'Move toward recovery and transition if fatigue or soreness is still the dominant issue.',
        'Move toward maintenance if the athlete needs more structure to preserve readiness.',
        'Reduce expectations if life stress is the main reason for the off-season.'
    ],
    references = [
        CardReference(
            card_id = 'macro_007',
            relationship = CardRelationship.PREVIOUS,
            tags = [
                'after_recovery'
            ]
        ),
        CardReference(
            card_id = 'macro_002',
            relationship = CardRelationship.NEXT,
            tags = [
                'new_cycle'
            ]
        ),
        CardReference(
            card_id = 'macro_009',
            relationship = CardRelationship.ALTERNATIVE,
            tags = [
                'more_structure'
            ]
        )
    ],
    recommended_duration_weeks = '4-12+',
    timing_guidance = [
        'Usually follows the main goal season rather than appearing randomly inside race preparation.',
        'The phase can be longer when the athlete needs more life, mental, or physical reset.'
    ],
    watchouts = [
        'Do not confuse off-season with total neglect of health and movement.',
        'Avoid turning the phase into secret high-load training.',
        'Do not preserve so much race specificity that the athlete never truly decompresses.',
        'Loss of all routine may require a later return-to-consistency phase.'
    ],
    additional_information = 'Off-season has a positive coaching purpose: it gives the athlete space to recover identity, movement variety, motivation, and general durability outside the pressure of imminent performance. It is looser than maintenance and broader than recovery.'
)
