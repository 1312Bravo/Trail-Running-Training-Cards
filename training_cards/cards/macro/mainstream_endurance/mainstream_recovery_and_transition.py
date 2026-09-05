from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MacroCard,
    TrainingLevel,
)

mainstream_recovery_and_transition = MacroCard(
    id = 'macro_007',
    slug = 'mainstream-recovery-and-transition',
    title = 'Recovery And Transition',
    card_type = CardType.MACRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A restorative bridge phase for absorbing prior stress and preparing for the next training direction.',
    purpose = 'Reduce accumulated load, restore readiness, and create a clean transition into the next appropriate phase.',
    tags = [
        'recovery',
        'transition',
        'absorption',
        'reset'
    ],
    goal_race_context = [
        'After a race, demanding block, heavy training period, or accumulated fatigue.',
        'When recovery is the main training problem and the next phase should not start yet.',
        'After a goal cycle before choosing off-season, maintenance, return-to-consistency, or a new base.',
        'For trail runners after high descent, long-duration, technical, travel, or environmental stress.'
    ],
    training_profile = [
        'Reduced structure and lower total cost while maintaining gentle movement where appropriate.',
        'Easy running, walking, hiking, mobility, or cross-training may be used if they support restoration.',
        'The phase observes soreness, energy, motivation, sleep, and easy-run feel before progressing.',
        'Trail and mountain load should be simplified if mechanical or technical fatigue remains high.'
    ],
    expected_adaptations = [
        'Reduced accumulated fatigue and soreness.',
        'Improved readiness for the next training cycle.',
        'Better understanding of how the previous race or block affected the athlete.'
    ],
    progression_rules = [
        'Progress only when easy movement feels normal and recovery markers improve.',
        'Move to off-season if the athlete needs a longer mental and physical decompression.',
        'Move to maintenance, return-to-consistency, or base development based on the next goal and readiness.'
    ],
    regression_rules = [
        'Use rest, walking, or very light cross-training if easy running is not restoring the athlete.',
        'Extend recovery if soreness, mood, sleep, or easy effort remains abnormal.',
        'Seek appropriate professional support when pain, illness, or health concerns are outside coaching scope.'
    ],
    references = [
        CardReference(
            card_id = 'macro_005',
            relationship = CardRelationship.PREVIOUS,
            tags = [
                'post_goal'
            ]
        ),
        CardReference(
            card_id = 'macro_006',
            relationship = CardRelationship.PREVIOUS,
            tags = [
                'season_complete'
            ]
        ),
        CardReference(
            card_id = 'macro_008',
            relationship = CardRelationship.NEXT,
            tags = [
                'decompression'
            ]
        ),
        CardReference(
            card_id = 'macro_002',
            relationship = CardRelationship.NEXT,
            tags = [
                'new_cycle'
            ]
        )
    ],
    recommended_duration_weeks = '1-6',
    timing_guidance = [
        'Use immediately after large stress or when accumulated fatigue blocks productive training.',
        'Length depends on the actual cost of the prior phase, not only on race distance.'
    ],
    watchouts = [
        'Do not hide training inside recovery because the athlete feels restless.',
        'Avoid interpreting one good day as full readiness.',
        'Do not force technical descents or long outings while muscle damage is still present.',
        'Low mood, persistent soreness, or abnormal fatigue deserves a conservative response.'
    ],
    additional_information = 'Recovery and transition is an active coaching decision, not a pause button. It protects the value of the previous work by allowing the athlete to absorb it and by preventing the next phase from starting on a fatigued foundation.'
)
