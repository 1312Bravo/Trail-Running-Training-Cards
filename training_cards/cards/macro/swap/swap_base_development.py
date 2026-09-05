from training_cards.philosophy_profiles import SWAP
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

swap_base_development = MacroCard(
    id = 'macro_028',
    slug = 'swap-base-development',
    title = 'SWAP Base Development',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [SWAP],
    summary = 'A foundation phase that builds aerobic durability while protecting health, joy, and early economy skills.',
    purpose = 'Develop the aerobic and emotional foundation for long-term training, with sustainable rhythm and purposeful economy touches.',
    tags = ['swap', 'base', 'joy', 'economy'],
    goal_race_context = [
        'Early in a season or long-term development cycle.',
        'When the athlete needs aerobic foundation and a positive training relationship.',
        'When small speed or economy touches can be introduced without pressure.',
        'For trail runners who benefit from joyful route variety while protecting effort.'
    ],
    training_profile = [
        'Easy aerobic consistency remains central.',
        'Small relaxed strides, hills, drills, or economy touches may appear when the athlete is ready.',
        'Enjoyment and route choice support adherence without overriding the training purpose.',
        'Fueling, recovery, and health habits are treated as part of sustainable performance.'
    ],
    expected_adaptations = [
        'Improved aerobic durability and routine.',
        'Better movement confidence and early economy development.',
        'Stronger long-term engagement with training.'
    ],
    progression_rules = [
        'Progress aerobic consistency while keeping the athlete eager to return.',
        'Add speed or economy touches only when mechanics stay relaxed.',
        'Move to SWAP capacity development when the athlete is ready for more directed stress.'
    ],
    regression_rules = [
        'Remove optional faster work if it creates strain or anxiety.',
        'Simplify route demands if adventure keeps turning easy days hard.',
        'Return to SWAP consistency if routine becomes fragile.'
    ],
    references = [
        CardReference(card_id = 'macro_002', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_027', relationship = CardRelationship.PREVIOUS, tags = ['swap_sequence']),
        CardReference(card_id = 'macro_029', relationship = CardRelationship.NEXT, tags = ['swap_sequence'])
    ],
    recommended_duration_weeks = '6-16+',
    timing_guidance = [
        'Use early enough that the athlete can build without race pressure.',
        'The phase may be extended when health, confidence, or consistency are still improving.'
    ],
    watchouts = [
        'Do not make joy an excuse for uncontrolled intensity.',
        'Avoid turning speed touches into tests.',
        'Do not ignore fueling and recovery because the training feels fun.',
        'If the athlete finishes depleted rather than engaged, the dose is too high.'
    ],
    additional_information = 'SWAP base development builds more than aerobic fitness. It tries to make the runner more durable, more economical, and more connected to the process that lets training compound across seasons.'
)
