from training_cards.philosophy_profiles import LYDIARD
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

lydiard_hill_resistance_transition = MacroCard(
    id = 'macro_017',
    slug = 'lydiard-hill-resistance-transition',
    title = 'Lydiard Hill Resistance Transition',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [LYDIARD],
    summary = 'A bridge phase that turns an earned aerobic base into stronger, more resilient running before later race work.',
    purpose = 'Develop hill resistance, coordination, and leg resilience so the athlete can move from base toward faster or more integrated work.',
    tags = ['lydiard', 'hill_resistance', 'transition', 'sequence'],
    goal_race_context = [
        'After a sufficient aerobic base has been built.',
        'When the athlete needs a bridge between aerobic conditioning and later faster or more race-relevant training.',
        'When hill resistance would prepare the runner better than jumping straight into hard race-like work.',
        'For trail runners when hills are used for strength, coordination, and resilience rather than uncontrolled climbing difficulty.'
    ],
    training_profile = [
        'Hill resistance is introduced as a sequential bridge, not as a random hard hill block.',
        'Aerobic running remains the support system around the new strength and coordination demand.',
        'The phase protects smooth mechanics and repeatable recovery rather than chasing maximal climbing fatigue.',
        'Effort, leg response, and ordinary aerobic running decide whether the athlete is ready to progress.'
    ],
    expected_adaptations = [
        'Greater hill resistance and leg resilience on top of the aerobic base.',
        'Improved coordination and strength for later faster or race-relevant work.',
        'A cleaner transition from base development toward integration without skipping a needed layer.'
    ],
    progression_rules = [
        'Progress hill resistance only when the aerobic base remains stable.',
        'Increase one demand at a time: duration, grade, repetition count, or mechanical complexity.',
        'Move toward Lydiard race-specific preparation when the bridge has been absorbed and the athlete can integrate capacities without losing recovery.'
    ],
    regression_rules = [
        'Return to base development if the athlete cannot recover from added layers.',
        'Simplify hill work if it becomes maximal climbing, uncontrolled descending, or soreness chasing.',
        'Delay faster work if coordination or ordinary aerobic running deteriorates.'
    ],
    references = [
        CardReference(card_id = 'macro_003', relationship = CardRelationship.ALTERNATIVE, tags = ['closest_mainstream_context']),
        CardReference(card_id = 'macro_016', relationship = CardRelationship.PREVIOUS, tags = ['lydiard_sequence']),
        CardReference(card_id = 'macro_018', relationship = CardRelationship.NEXT, tags = ['lydiard_sequence'])
    ],
    recommended_duration_weeks = '4-10',
    timing_guidance = [
        'Use after base, not as a replacement for base.',
        'Use before late race-specific integration when the athlete still needs the hill-resistance bridge.',
        'Exact phase length should follow goal timing and athlete response rather than historical templates.'
    ],
    watchouts = [
        'Do not call any hill session Lydiard simply because it is uphill.',
        'Avoid treating hill resistance, intervals, and speed as interchangeable hard work.',
        'Do not compress the sequence to make up for a late start.',
        'If the athlete cannot recover, the next layer is not ready.'
    ],
    additional_information = 'Lydiard hill resistance transition is about order. The phase asks what the aerobic base has made possible, whether the athlete needs a strength-and-coordination bridge, and whether that bridge is being absorbed before later race-relevant work.'
)
