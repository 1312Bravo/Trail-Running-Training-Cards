from training_cards.philosophy_profiles import ENDURANCE_80_20
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

endurance_80_20_race_specific_preparation = MacroCard(
    id = 'macro_012',
    slug = '80-20-race-specific-preparation',
    title = '80/20 Race-Specific Preparation',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [ENDURANCE_80_20],
    summary = 'A specific phase that rehearses goal demands while keeping intensity distribution deliberate rather than accidental.',
    purpose = 'Apply fitness to race demands without letting specificity become uncontrolled moderate-hard training.',
    tags = ['80_20', 'race_specific', 'specificity', 'distribution'],
    goal_race_context = [
        'In the final substantial preparation phase before a target event.',
        'When terrain, duration, race pace, fueling, or environmental exposure must be practised.',
        'For hilly or trail races where pace is not reliable enough to define intensity alone.',
        'When the athlete needs specific confidence without losing easy-day discipline.'
    ],
    training_profile = [
        'Race-specific sessions are selected for clear transfer and placed with recovery space.',
        'Low-intensity work remains protected around specific demands.',
        'Planned moderate work may be appropriate, but accidental moderate running should not dominate.',
        'Trail routes are judged by intensity, duration, descent damage, technicality, and recovery cost.'
    ],
    expected_adaptations = [
        'Better transfer from fitness to goal-specific execution.',
        'More disciplined use of race-pace or terrain-specific work.',
        'Improved ability to keep easy training supportive during a specific phase.'
    ],
    progression_rules = [
        'Progress specificity gradually while keeping the easy majority intact across the phase.',
        'Use terrain-safe metrics such as RPE, heart rate, power, breathing, or hiking when pace misleads.',
        'Move to mainstream peak and taper when specific work has been practised and freshness becomes the main need.'
    ],
    regression_rules = [
        'Reduce race-like density if easy days disappear or recovery becomes unreliable.',
        'Use less technical or less steep terrain when mechanical cost overwhelms the intended stimulus.',
        'Return to capacity development if the athlete lacks a key capacity needed for specific work.'
    ],
    references = [
        CardReference(card_id = 'macro_004', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_011', relationship = CardRelationship.PREVIOUS, tags = ['80_20_sequence']),
        CardReference(card_id = 'macro_005', relationship = CardRelationship.NEXT, tags = ['peak_and_taper'])
    ],
    recommended_duration_weeks = '4-8',
    timing_guidance = [
        'Use close enough to the race for transfer but early enough to recover from specific sessions.',
        'A specific phase may bend the distribution temporarily, but the bending should be intentional.'
    ],
    watchouts = [
        'Do not let race specificity become constant grey-zone effort.',
        'Avoid treating every trail long run as a hard day without admitting its cost.',
        'Do not chase road pace on terrain where it distorts intensity.',
        'If race-specific work makes quality and easy days blur together, simplify the phase.'
    ],
    additional_information = '80/20 race-specific preparation is not anti-specificity. It asks the coach to make specificity honest: what is being rehearsed, what cost does it create, and how does the rest of the phase preserve the distribution that supports adaptation?'
)
