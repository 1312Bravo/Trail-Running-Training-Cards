from training_cards.philosophy_profiles import LYDIARD
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

lydiard_capacity_development = MacroCard(
    id = 'macro_017',
    slug = 'lydiard-capacity-development',
    title = 'Lydiard Capacity Development',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [LYDIARD],
    summary = 'A sequenced development phase that layers hill strength and faster work onto an earned aerobic base.',
    purpose = 'Develop later performance qualities in the order that lets each layer prepare the next.',
    tags = ['lydiard', 'capacity', 'hill_strength', 'sequence'],
    goal_race_context = [
        'After a sufficient aerobic base has been built.',
        'When the athlete is ready to bridge from aerobic conditioning toward faster or more integrated work.',
        'When hill strength or anaerobic development would be premature without a base.',
        'For trail runners when hills are used for the correct sequential role rather than generic climbing difficulty.'
    ],
    training_profile = [
        'Later qualities are introduced as layers, not as random quality blocks.',
        'Hill work may serve as a bridge from base to faster running when written with that purpose.',
        'Aerobic running remains the support system around demanding work.',
        'Effort and recovery response decide whether the athlete is ready to progress.'
    ],
    expected_adaptations = [
        'Improved ability to use the aerobic base for stronger and faster running.',
        'Better strength, coordination, and readiness for race-relevant integration.',
        'Clearer understanding of how one phase prepares the next.'
    ],
    progression_rules = [
        'Add the next layer only when the previous layer is absorbed.',
        'Keep the purpose of hill or faster work connected to the sequence.',
        'Move toward race-specific preparation when the athlete can integrate capacities without losing recovery.'
    ],
    regression_rules = [
        'Return to base development if the athlete cannot recover from added layers.',
        'Simplify hill work if it becomes maximal climbing, uncontrolled descending, or damage chasing.',
        'Delay faster work if coordination or ordinary aerobic running deteriorates.'
    ],
    references = [
        CardReference(card_id = 'macro_003', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_016', relationship = CardRelationship.PREVIOUS, tags = ['lydiard_sequence']),
        CardReference(card_id = 'macro_018', relationship = CardRelationship.NEXT, tags = ['lydiard_sequence'])
    ],
    recommended_duration_weeks = '4-10',
    timing_guidance = [
        'Use after base, not as a replacement for base.',
        'Exact phase length should follow goal timing and athlete response rather than historical templates.'
    ],
    watchouts = [
        'Do not call any hill session Lydiard simply because it is uphill.',
        'Avoid treating intervals, hills, and speed as interchangeable hard work.',
        'Do not compress the sequence to make up for a late start.',
        'If the athlete cannot recover, the next layer is not ready.'
    ],
    additional_information = 'Lydiard capacity development is about order. The phase asks what the base has made possible, what the next layer should build, and whether the athlete is recovering well enough for that layer to be productive.'
)
