from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MezzoCard,
    TrainingLevel,
)

mainstream_recovery_and_adaptation_block = MezzoCard(
    id = 'mezzo_012',
    slug = 'mainstream-recovery-and-adaptation-block',
    title = 'Recovery And Adaptation Block',
    card_type = CardType.MEZZO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A mainstream block that reduces load so recent training can be absorbed and evaluated.',
    purpose = 'Restore readiness, consolidate adaptation, and decide whether to progress, repeat, or redirect the next block.',
    tags = [
        'mainstream_endurance',
        'recovery',
        'adaptation',
        'monitoring'
    ],
    goal_race_context = [
        'Use after demanding aerobic, quality, long-run, race, or terrain-specific loading.',
        'Useful when signs of accumulated fatigue appear before they become a larger problem.',
        'Appropriate between development blocks or after a tune-up race.',
        'Useful before increasing specificity when the athlete needs fresher feedback.'
    ],
    expected_adaptations = [
        'Lower accumulated fatigue.',
        'Restored easy-run rhythm and movement quality.',
        'Clearer readiness signal before the next progression.',
        'Better continuity across the training cycle.'
    ],
    progression_rules = [
        'Return to building only when easy effort, soreness, sleep, and motivation are stable.',
        'Use a short submaximal check when readiness is unclear.',
        'Progress from freshness, not from anxiety about a smaller training log.'
    ],
    regression_rules = [
        'Keep the block low-load longer if fatigue markers remain elevated.',
        'Replace running with low-impact aerobic work only when it supports recovery and does not mask pain.',
        'Seek appropriate professional support for injury, illness, or persistent health concerns.'
    ],
    references = [
        CardReference(
            card_id = 'macro_007',
            relationship = CardRelationship.PARENT,
            tags = [
                'mainstream_phase'
            ]
        ),
        CardReference(
            card_id = 'mezzo_011',
            relationship = CardRelationship.PREVIOUS,
            tags = [
                'after_quality'
            ]
        ),
        CardReference(
            card_id = 'micro_012',
            relationship = CardRelationship.CHILD,
            tags = [
                'core_week'
            ]
        )
    ],
    recommended_duration_weeks = '1-3',
    placement_guidance = [
        'Place after two to four demanding weeks, after a race, or whenever recovery signals justify it.',
        'Use before a more specific block when the athlete needs to shed fatigue to train well.',
        'Do not wait for complete breakdown before using this block.'
    ],
    training_profile = [
        'Reduced volume and reduced intensity.',
        'Mostly easy running or low-impact aerobic support.',
        'Optional short relaxed strides only if they improve rhythm without adding fatigue.',
        'Simple review of sleep, soreness, mood, motivation, easy-run effort, and movement quality.'
    ],
    watchouts = [
        'Using recovery weeks only after the athlete is already overreached.',
        'Filling the lower running load with extra strength, hiking, or technical terrain.',
        'Judging the block by fitness anxiety rather than the return of readiness.',
        'Restarting hard work while easy running still feels abnormal.'
    ],
    additional_information = 'Recovery is part of training, not an interruption. This block uses the mainstream stress-recovery-adaptation model to make consolidation visible. The coach lowers load enough to let recent work become useful, then reviews the response before choosing the next block. For trail runners, the reduction should include hidden costs such as descent, technical footing, heat, altitude, and long time on feet.'
)
