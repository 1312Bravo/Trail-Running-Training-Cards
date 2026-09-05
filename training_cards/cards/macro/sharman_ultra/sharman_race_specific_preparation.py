from training_cards.philosophy_profiles import SHARMAN_ULTRA
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

sharman_race_specific_preparation = MacroCard(
    id = 'macro_037',
    slug = 'sharman-race-specific-preparation',
    title = 'Sharman Ultra Race-Specific Preparation',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [SHARMAN_ULTRA],
    summary = 'An ultra-specific phase connecting fitness to the athlete’s course, logistics, pacing, fueling, and success definition.',
    purpose = 'Prepare the runner to use their fitness in the practical reality of the target ultra.',
    tags = ['sharman_ultra', 'race_specific', 'ultra_execution', 'individualisation'],
    goal_race_context = [
        'Late preparation for an ultramarathon or demanding trail objective.',
        'When course demands, athlete context, and definition of success shape the plan.',
        'When fueling, pacing, hiking, gear, logistics, and problem-solving need practice.',
        'When the runner needs practical education alongside physical preparation.'
    ],
    training_profile = [
        'The phase adapts established endurance principles to this athlete and this event.',
        'Specific work connects physical training to pacing, fueling, hiking, terrain, gear, and logistics.',
        'The card teaches what the athlete should observe and adjust.',
        'Substitutions are honest about what they preserve and what direct course exposure may still require.'
    ],
    expected_adaptations = [
        'Better practical readiness for the target ultra.',
        'Improved ability to make race decisions under fatigue.',
        'Clearer athlete confidence in their own execution plan.'
    ],
    progression_rules = [
        'Progress rehearsal complexity only when the athlete understands and absorbs the current version.',
        'Use training and race-practice feedback to refine strategy.',
        'Move to taper when the key practical questions have been tested enough.'
    ],
    regression_rules = [
        'Reduce rehearsal scope if it becomes too costly or confusing.',
        'Return to capacity or base work if the athlete lacks a physical prerequisite.',
        'Simplify execution goals if life stress or recovery capacity is constrained.'
    ],
    references = [
        CardReference(card_id = 'macro_004', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_001', relationship = CardRelationship.PREVIOUS, tags = ['if_return_needed']),
        CardReference(card_id = 'macro_038', relationship = CardRelationship.ALTERNATIVE, tags = ['race_series'])
    ],
    recommended_duration_weeks = '4-10',
    timing_guidance = [
        'Use close enough to the ultra that practice is relevant and early enough that lessons can be applied.',
        'The athlete’s definition of success should shape acceptable risk and rehearsal detail.'
    ],
    watchouts = [
        'Do not treat all ultras as the same because they share distance.',
        'Avoid adding every possible execution skill to every session.',
        'Do not use anecdotal ultra experience as a universal rule.',
        'If the athlete cannot explain the purpose, the guidance needs to be clearer.'
    ],
    additional_information = 'Sharman Ultra race-specific preparation is practical and personal. It takes broad endurance knowledge and asks how this runner will move, eat, pace, decide, and adapt in this particular ultra context.'
)
