from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MezzoCard,
    TrainingLevel,
)

mainstream_controlled_quality_development_block = MezzoCard(
    id = 'mezzo_011',
    slug = 'mainstream-controlled-quality-development-block',
    title = 'Controlled Quality Development Block',
    card_type = CardType.MEZZO,
    suitable_levels = [
        TrainingLevel.INTERMEDIATE,
        TrainingLevel.ADVANCED,
        TrainingLevel.ELITE
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A mainstream block that adds purposeful intensity while protecting easy volume and recovery.',
    purpose = 'Improve sustainable output or aerobic power through quality sessions that are placed, limited, and recoverable.',
    tags = [
        'mainstream_endurance',
        'quality',
        'threshold',
        'aerobic_power',
        'recovery'
    ],
    goal_race_context = [
        'Use when aerobic consistency is stable and the athlete needs a stronger performance ceiling.',
        'Useful when threshold control, aerobic power, or controlled faster running is a current limiter.',
        'Appropriate before race-specific preparation when quality is needed but full event rehearsal is premature.',
        'Fits trail runners when smoother terrain or effort-based targets protect the intended intensity.'
    ],
    expected_adaptations = [
        'Improved ability to sustain controlled moderate-to-hard effort.',
        'Better separation between quality work and easy running.',
        'Improved pacing discipline under defined intensity.',
        'More reliable recovery from key sessions.'
    ],
    progression_rules = [
        'Increase total quality time or repetitions before increasing intensity.',
        'Keep easy days genuinely easy so the key session remains useful.',
        'Progress only when the quality session and the following recovery pattern are both stable.'
    ],
    regression_rules = [
        'Reduce repetitions, extend recoveries, or switch to steady running if quality fades.',
        'Remove secondary intensity before reducing all aerobic support.',
        'Move quality to flatter or smoother terrain when trail variability hides the target stimulus.'
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
            card_id = 'mezzo_010',
            relationship = CardRelationship.PREVIOUS,
            tags = [
                'aerobic_prerequisite'
            ]
        ),
        CardReference(
            card_id = 'mezzo_012',
            relationship = CardRelationship.NEXT,
            tags = [
                'after_quality_load'
            ]
        ),
        CardReference(
            card_id = 'micro_011',
            relationship = CardRelationship.CHILD,
            tags = [
                'core_week'
            ]
        )
    ],
    recommended_duration_weeks = '2-6',
    placement_guidance = [
        'Place after a stable aerobic progression block or maintenance period.',
        'Use when the athlete can recover from one purposeful quality session per week.',
        'Avoid when easy running is already drifting upward or recovery is inconsistent.'
    ],
    training_profile = [
        'One primary quality session in most weeks.',
        'Easy aerobic work surrounds the key session.',
        'Intensity targets can use RPE, pace, heart rate, power, or threshold estimates, depending on terrain and reliability.',
        'Quality stops when mechanics, pacing, or recovery purpose is lost.'
    ],
    watchouts = [
        'Turning every run into moderate work.',
        'Using high intensity to compensate for missing aerobic consistency.',
        'Adding technical descending after quality work when the session purpose is metabolic control.',
        'Progressing because the athlete survived the workout rather than because they absorbed it.'
    ],
    additional_information = 'This block reflects mainstream intensity design: quality work has a purpose, a dose, a recovery cost, and a place in the broader week. It does not prescribe one universal zone model. On trails, the coach should choose terrain and metrics that protect the intended stimulus; sometimes that means using a road, track, treadmill, or smooth climb instead of technical singletrack.'
)
