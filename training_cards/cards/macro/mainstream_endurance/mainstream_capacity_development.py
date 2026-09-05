from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MacroCard,
    TrainingLevel,
)

mainstream_capacity_development = MacroCard(
    id = 'macro_003',
    slug = 'mainstream-capacity-development',
    title = 'Capacity Development',
    card_type = CardType.MACRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A directed development phase for improving selected performance capacities after the aerobic base is stable.',
    purpose = 'Develop stronger performance capacities through focused blocks while preserving aerobic support and recovery.',
    tags = [
        'capacity',
        'development',
        'quality',
        'progression'
    ],
    goal_race_context = [
        'After enough base development for the athlete to tolerate more directed training.',
        'When the athlete needs stronger threshold, aerobic power, long-endurance, strength-endurance, or terrain capacity.',
        'Before race-specific preparation when the goal still needs general capability development.',
        'For runners who are ready for purposeful stress but not yet ready to simulate the race.'
    ],
    training_profile = [
        'Focused blocks that emphasize one or two key qualities at a time.',
        'Aerobic support remains present so harder work does not replace the foundation.',
        'Intensity, long duration, climbing, or strength-endurance work is added with recovery space.',
        'Trail demands may become more deliberate, but the phase is still capacity-building rather than full race rehearsal.'
    ],
    expected_adaptations = [
        'Improved ability to handle purposeful training stress.',
        'Stronger selected performance determinants such as threshold control, aerobic power, or muscular endurance.',
        'Better readiness for later race-specific demands.'
    ],
    progression_rules = [
        'Select a clear primary capacity and progress that stress before adding another major demand.',
        'Keep easy work easy enough to support adaptation from key blocks.',
        'Move to race-specific preparation when the main capacity limiter is improved enough to apply it to the goal.'
    ],
    regression_rules = [
        'Reduce session density or intensity if the athlete cannot recover between key stresses.',
        'Return to base development if aerobic support or consistency starts to break down.',
        'Simplify terrain if mechanical cost hides the intended stimulus.'
    ],
    references = [
        CardReference(
            card_id = 'macro_002',
            relationship = CardRelationship.PREVIOUS,
            tags = [
                'foundation_required'
            ]
        ),
        CardReference(
            card_id = 'macro_004',
            relationship = CardRelationship.NEXT,
            tags = [
                'specificity_sequence'
            ]
        ),
        CardReference(
            card_id = 'macro_007',
            relationship = CardRelationship.ALTERNATIVE,
            tags = [
                'fatigue_limited'
            ]
        )
    ],
    recommended_duration_weeks = '4-10',
    timing_guidance = [
        'Usually follows base development and precedes race-specific preparation.',
        'The block mix should be chosen from athlete limiters, not from novelty.'
    ],
    watchouts = [
        'Do not try to improve every quality at once.',
        'Avoid making easy days drift into moderate work because key sessions feel productive.',
        'Do not let terrain difficulty accidentally double the dose.',
        'Declining movement quality or motivation often means the phase is too dense.'
    ],
    additional_information = 'Capacity development is where training becomes more directed without becoming race simulation. The coach chooses the few qualities that matter most now, develops them with clear blocks, and protects enough recovery for the work to become adaptation rather than fatigue.'
)
