from training_cards.philosophy_profiles import SWAP
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

swap_capacity_development = MacroCard(
    id = 'macro_029',
    slug = 'swap-capacity-development',
    title = 'SWAP Capacity Development',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [SWAP],
    summary = 'A development phase for speed, economy, and fatigue-resistance questions inside a sustainable plan.',
    purpose = 'Develop performance capacity while keeping the athlete healthy, curious, confident, and engaged.',
    tags = ['swap', 'capacity', 'speed', 'fatigue_resistance'],
    goal_race_context = [
        'After aerobic rhythm is stable enough for more purposeful work.',
        'When the athlete can benefit from economy, speed, hills, threshold, or fatigue-resistance development.',
        'When the plan needs a clear hypothesis rather than a punishment block.',
        'Before race-specific preparation if the athlete needs stronger capabilities first.'
    ],
    training_profile = [
        'Selected quality work is used to develop economy, speed skill, or event-relevant capacity.',
        'Fatigue resistance is treated as a question about what degrades, not an order to seek exhaustion.',
        'The phase protects fueling, recovery, and athlete enthusiasm around demanding work.',
        'Trail terrain may support skill, confidence, and economy if the purpose remains clear.'
    ],
    expected_adaptations = [
        'Improved selected capacity without sacrificing long-term engagement.',
        'Better economy or confidence at faster or more demanding movement.',
        'Clearer understanding of how the athlete responds to fatigue.'
    ],
    progression_rules = [
        'Progress quality only while mechanics, recovery, and motivation remain healthy.',
        'Use response review to refine the training hypothesis.',
        'Move to race-specific preparation when capacities are ready to be applied.'
    ],
    regression_rules = [
        'Reduce or pause speed work if mechanics become forced.',
        'Return to base if health, recovery, or enthusiasm begins to erode.',
        'Simplify terrain if fun routes hide too much cost.'
    ],
    references = [
        CardReference(card_id = 'macro_003', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_028', relationship = CardRelationship.PREVIOUS, tags = ['swap_sequence']),
        CardReference(card_id = 'macro_030', relationship = CardRelationship.NEXT, tags = ['swap_sequence'])
    ],
    recommended_duration_weeks = '4-10',
    timing_guidance = [
        'Use when the athlete is ready for useful challenge, not when they need to prove worth.',
        'The phase should leave the runner more capable and still excited to train.'
    ],
    watchouts = [
        'Do not treat fatigue resistance as permission for reckless exhaustion.',
        'Avoid speed work that becomes strained or punitive.',
        'Do not ignore underfueling or overtraining signals.',
        'If curiosity disappears and pressure dominates, revise the phase.'
    ],
    additional_information = 'SWAP capacity development keeps ambition and affection for the process in the same room. The coach can pursue speed, economy, and hard questions while still protecting the athlete who has to live inside the plan.'
)
