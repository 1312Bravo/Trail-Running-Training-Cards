from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MacroCard,
    TrainingLevel,
)

mainstream_peak_and_taper = MacroCard(
    id = 'macro_005',
    slug = 'mainstream-peak-and-taper',
    title = 'Peak And Taper',
    card_type = CardType.MACRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A final readiness phase that preserves fitness and rhythm while reducing unnecessary fatigue.',
    purpose = 'Help the athlete arrive fresh, confident, coordinated, and ready to express existing fitness.',
    tags = [
        'peak',
        'taper',
        'freshness',
        'readiness'
    ],
    goal_race_context = [
        'In the final period before an important race or objective.',
        'When major fitness and specific preparation are already complete.',
        'When the athlete needs freshness more than additional training load.',
        'Before demanding trail or ultra goals where residual soreness and logistical confidence matter.'
    ],
    training_profile = [
        'Reduced total load with enough short rhythm or intensity touches to avoid feeling stale.',
        'Lower long-run, descent, strength, and technical terrain cost late in the phase.',
        'Familiar sessions, familiar equipment, and familiar terrain are preferred.',
        'Race logistics, fueling confidence, pacing cues, and recovery behaviours become central.'
    ],
    expected_adaptations = [
        'Reduced accumulated fatigue.',
        'Preserved aerobic readiness, coordination, and neuromuscular rhythm.',
        'Improved confidence and calm before the target event.'
    ],
    progression_rules = [
        'Progress by reducing cost while preserving enough training rhythm.',
        'Keep short quality controlled and familiar rather than using it as a test.',
        'Move to competition management after the event if another race follows soon, or recovery if the goal cycle is complete.'
    ],
    regression_rules = [
        'Reduce volume further if fatigue or soreness remains high.',
        'Replace workouts with easy running if illness, pain, or unusual heaviness appears.',
        'Remove unfamiliar terrain or strength work that could create late soreness.'
    ],
    references = [
        CardReference(
            card_id = 'macro_004',
            relationship = CardRelationship.PREVIOUS,
            tags = [
                'race_countdown'
            ]
        ),
        CardReference(
            card_id = 'macro_006',
            relationship = CardRelationship.NEXT,
            tags = [
                'race_series'
            ]
        ),
        CardReference(
            card_id = 'macro_007',
            relationship = CardRelationship.NEXT,
            tags = [
                'post_goal'
            ]
        )
    ],
    recommended_duration_weeks = '1-3',
    timing_guidance = [
        'Use only when the goal is close and the main preparation work is already done.',
        'Taper length should reflect race duration, prior load, fatigue state, and athlete history.'
    ],
    watchouts = [
        'Do not test fitness too close to the race.',
        'Avoid last-minute workout, gear, fueling, or terrain experiments.',
        'Do not reduce all training so much that the athlete feels flat unless recovery demands it.',
        'Restlessness is not evidence that more work is needed.'
    ],
    additional_information = 'Peak and taper is not where fitness is built; it is where fitness is revealed. The coach keeps enough rhythm to preserve confidence and coordination while removing the avoidable fatigue that would hide readiness on race day.'
)
