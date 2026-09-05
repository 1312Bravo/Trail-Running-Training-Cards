from training_cards.philosophy_profiles import EVOKE_ENDURANCE
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

evoke_capacity_development = MacroCard(
    id = 'macro_025',
    slug = 'evoke-capacity-development',
    title = 'Evoke Capacity Development',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [EVOKE_ENDURANCE],
    summary = 'A layered capacity phase for developing strength reserve and muscular endurance on top of aerobic capacity.',
    purpose = 'Build the mountain-specific layers the athlete needs before trying to use them in objective-like work.',
    tags = ['evoke', 'capacity', 'strength_reserve', 'muscular_endurance'],
    goal_race_context = [
        'After the aerobic base is strong enough to support more specific work.',
        'When sustained climbing, hiking, load, or local muscular fatigue is a likely limiter.',
        'When the athlete needs strength reserve or muscular endurance before race rehearsal.',
        'For mountain objectives where general fitness does not fully solve the propelling demand.'
    ],
    training_profile = [
        'The phase identifies which layer is being built: strength reserve, muscular endurance, or another supporting capacity.',
        'Muscular-endurance work is layered onto adequate aerobic capacity and strength reserve.',
        'The local muscular demand and recovery cost are made explicit.',
        'Terrain and equipment choices preserve the target layer rather than becoming random difficulty.'
    ],
    expected_adaptations = [
        'Greater force reserve or repeated-force capacity for mountain movement.',
        'Improved ability to climb, hike, or move uphill under local fatigue.',
        'Better readiness for later utilisation and race-specific rehearsal.'
    ],
    progression_rules = [
        'Progress the chosen layer before adding another major variable.',
        'Keep aerobic support present while specialised work is introduced.',
        'Move to Evoke race-specific preparation when the athlete can use the developed layer without excessive recovery cost.'
    ],
    regression_rules = [
        'Return to base if aerobic support is not strong enough.',
        'Use general strength before muscular endurance if force reserve is inadequate.',
        'Reduce grade, load, duration, or frequency if local damage disrupts the rest of training.'
    ],
    references = [
        CardReference(card_id = 'macro_003', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_024', relationship = CardRelationship.PREVIOUS, tags = ['evoke_layering']),
        CardReference(card_id = 'macro_026', relationship = CardRelationship.NEXT, tags = ['evoke_layering'])
    ],
    recommended_duration_weeks = '4-10',
    timing_guidance = [
        'Use when the next useful adaptation is a specific layer, not more general base.',
        'The phase should end with enough recovery to reveal whether the layer was absorbed.'
    ],
    watchouts = [
        'Do not use muscular-endurance work as a substitute for missing base.',
        'Avoid severe soreness as a success marker.',
        'Do not increase grade, load, duration, and frequency together.',
        'A route is not Evoke-specific unless it trains the intended layer.'
    ],
    additional_information = 'Evoke capacity development is precise: the coach decides which layer limits the objective, builds it with a recoverable dose, and keeps the athlete from confusing hard mountain work with useful mountain work.'
)
