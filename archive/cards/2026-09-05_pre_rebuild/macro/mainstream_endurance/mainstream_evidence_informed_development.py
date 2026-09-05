from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MacroCard,
    TrainingLevel,
)

mainstream_evidence_informed_development = MacroCard(
    id = 'macro_007',
    slug = 'mainstream-evidence-informed-development',
    title = 'Mainstream Evidence-Informed Development',
    card_type = CardType.MACRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A general development phase using evidence-informed progression, specificity, recovery, and monitoring.',
    purpose = 'Build trainable endurance capacity by matching the training dose to the athlete, adaptation target, and goal timing.',
    tags = [
        'mainstream_endurance',
        'periodisation',
        'progression',
        'aerobic',
        'recovery'
    ],
    goal_race_context = [
        'Useful when the runner needs a clear evidence-informed structure but not a named coaching system.',
        'Appropriate early to middle in a preparation cycle before highly specific race rehearsal dominates.',
        'Useful after inconsistent training when the athlete can train regularly but still needs controlled progression.',
        'Fits road, trail, and mountain goals when the main need is general endurance development.'
    ],
    expected_adaptations = [
        'Improved aerobic capacity and durability.',
        'Better tolerance for progressive training load.',
        'Clearer separation between easy work, quality work, recovery, and specific preparation.',
        'More useful feedback from training response and submaximal monitoring.'
    ],
    progression_rules = [
        'Progress one major variable at a time: frequency, duration, weekly volume, intensity, vertical gain, technicality, or strength load.',
        'Use repeated recoverable weeks before adding a more specific or more demanding stress.',
        'Move toward race-specific preparation only when the athlete can absorb the general training load.'
    ],
    regression_rules = [
        'Hold the current dose when easy effort, mood, soreness, or sleep suggest incomplete recovery.',
        'Reduce the least necessary stressor first, usually intensity, technical terrain, or long-run extension.',
        'Return to recovery or consistency work if normal easy running stops feeling repeatable.'
    ],
    references = [
        CardReference(
            card_id = 'macro_006',
            relationship = CardRelationship.PREVIOUS,
            tags = [
                'after_reset'
            ]
        ),
        CardReference(
            card_id = 'macro_004',
            relationship = CardRelationship.NEXT,
            tags = [
                'toward_specificity'
            ]
        ),
        CardReference(
            card_id = 'mezzo_010',
            relationship = CardRelationship.CHILD,
            tags = [
                'aerobic_progression'
            ]
        ),
        CardReference(
            card_id = 'mezzo_011',
            relationship = CardRelationship.CHILD,
            tags = [
                'controlled_quality'
            ]
        ),
        CardReference(
            card_id = 'mezzo_012',
            relationship = CardRelationship.CHILD,
            tags = [
                'adaptation_block'
            ]
        )
    ],
    recommended_duration_weeks = '6-16',
    timing_guidance = [
        'Use when there is enough time to build capacity before sharpening or race-specific rehearsal.',
        'Lengthen the phase when training history is thin, recovery is inconsistent, or the target event is long.',
        'Shorten or simplify the phase when the athlete is returning from illness, injury, or high life stress.'
    ],
    training_profile = [
        'Mostly easy aerobic running with selected quality only when it has a defined adaptation target.',
        'Progressive overload is planned through one main variable at a time.',
        'Regular easier weeks or consolidation blocks protect adaptation.',
        'Strength, mobility, strides, and skill work support the running load without becoming the main stress.',
        'For trail runners, terrain, vertical gain, technicality, hiking, and descent load are treated as dose variables.'
    ],
    watchouts = [
        'Do not use this as a generic label when a named coaching philosophy is actually shaping the card.',
        'Do not chase volume, intensity, and terrain specificity at the same time.',
        'Do not treat watch metrics as more important than the athlete response pattern.',
        'Avoid race simulation before the general load is recoverable.'
    ],
    additional_information = 'This phase expresses the mainstream sport-science model: define the target adaptation, select a dose, place recovery, observe response, and progress only when the previous layer is absorbed. It is intentionally not a branded system. The coach can use zones, RPE, pace, power, heart rate, or field tests, but the metric must serve the session purpose rather than replace judgement. For trail runners, the same principles apply with terrain-aware load accounting: vertical gain, downhill damage, technical coordination, hiking, heat, and fueling can change the effective dose even when pace looks easy.'
)
