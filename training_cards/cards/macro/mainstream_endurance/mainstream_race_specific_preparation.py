from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MacroCard,
    TrainingLevel,
)

mainstream_race_specific_preparation = MacroCard(
    id = 'macro_004',
    slug = 'mainstream-race-specific-preparation',
    title = 'Race-Specific Preparation',
    card_type = CardType.MACRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A goal-focused phase that turns developed fitness into race-relevant capacity and execution readiness.',
    purpose = 'Prepare the athlete for the demands that will matter most in the target race or objective.',
    tags = [
        'race_specific',
        'specificity',
        'execution',
        'preparation'
    ],
    goal_race_context = [
        'After base and capacity work have created enough fitness to apply toward the goal.',
        'When the athlete needs terrain, pacing, fueling, equipment, or environmental rehearsal.',
        'For trail and mountain goals where the race demand is not described well by pace alone.',
        'Before peak and taper, when there is still time to practise specific demands and recover from them.'
    ],
    training_profile = [
        'Sessions and blocks increasingly resemble key goal demands without copying the race blindly.',
        'Pacing, fueling, terrain choice, equipment, and environmental practice become more important.',
        'General aerobic support and recovery remain in the plan.',
        'Trail specificity may include climbing, descending, technical footing, hiking transitions, heat, altitude, or long time on feet.'
    ],
    expected_adaptations = [
        'Better transfer from general fitness to goal-specific performance.',
        'Improved confidence and decision-making under race-relevant demands.',
        'Clearer execution habits for pacing, fueling, terrain, and equipment.'
    ],
    progression_rules = [
        'Progress specificity from partial resemblance toward more goal-relevant rehearsals.',
        'Keep race-like work proportionate to the recovery cost.',
        'Move to peak and taper when major specific preparation is complete and freshness becomes the priority.'
    ],
    regression_rules = [
        'Return to capacity development if a missing fitness quality limits specific work.',
        'Reduce terrain, duration, or mechanical cost if specificity disrupts recovery.',
        'Use safer substitutions when conditions or access make the planned specific session inappropriate.'
    ],
    references = [
        CardReference(
            card_id = 'macro_003',
            relationship = CardRelationship.PREVIOUS,
            tags = [
                'capacity_to_specificity'
            ]
        ),
        CardReference(
            card_id = 'macro_005',
            relationship = CardRelationship.NEXT,
            tags = [
                'race_countdown'
            ]
        ),
        CardReference(
            card_id = 'macro_006',
            relationship = CardRelationship.ALTERNATIVE,
            tags = [
                'multi_race_context'
            ]
        )
    ],
    recommended_duration_weeks = '4-8',
    timing_guidance = [
        'Best used close enough to the goal that specificity transfers, but not so late that it cannot be absorbed.',
        'Longer or more technical events may need a longer specific preparation window.'
    ],
    watchouts = [
        'Do not mistake copying race terrain for preparing well.',
        'Avoid introducing unfamiliar technical, environmental, or fueling demands too late.',
        'Do not let specific work erase recovery or aerobic support.',
        'Repeated soreness after specific sessions means the dose is too costly.'
    ],
    additional_information = 'Race-specific preparation asks what the athlete must actually be able to do on the day. For trail runners, this often means preparing for gradient, technicality, descent load, fueling, weather, equipment, and judgement, not simply running faster workouts.'
)
