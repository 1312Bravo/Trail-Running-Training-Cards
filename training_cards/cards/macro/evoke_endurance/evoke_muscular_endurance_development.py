from training_cards.philosophy_profiles import EVOKE_ENDURANCE
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

evoke_muscular_endurance_development = MacroCard(
    id = 'macro_025',
    slug = 'evoke-muscular-endurance-development',
    title = 'Evoke Muscular Endurance Development',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [EVOKE_ENDURANCE],
    summary = 'A mountain phase that develops repeated uphill force after aerobic capacity and strength reserve are ready.',
    purpose = 'Build the muscular endurance needed for sustained climbing, hiking, or mountain propulsion before objective-like utilisation.',
    tags = ['evoke', 'muscular_endurance', 'strength_reserve', 'mountain_endurance'],
    goal_race_context = [
        'After the aerobic base is strong enough to support more specific work.',
        'When sustained climbing, hiking, load, or local muscular fatigue is a likely limiter.',
        'When the athlete has enough strength reserve to make muscular-endurance work productive.',
        'For mountain objectives where general fitness does not fully solve the propelling demand.'
    ],
    training_profile = [
        'The phase targets repeated local force production rather than general hard climbing.',
        'Muscular-endurance work is layered onto adequate aerobic capacity and strength reserve.',
        'The local muscular demand and recovery cost are made explicit.',
        'Terrain and equipment choices preserve the muscular-endurance stimulus rather than becoming random difficulty.'
    ],
    expected_adaptations = [
        'Greater repeated-force capacity for climbing, hiking, or uphill running.',
        'Improved ability to keep moving under local muscular fatigue.',
        'Better readiness for later utilisation and race-specific mountain rehearsal.'
    ],
    progression_rules = [
        'Progress muscular-endurance dose only when aerobic support and strength reserve remain stable.',
        'Keep aerobic support present while specialised work is introduced.',
        'Move to Evoke race-specific preparation when the athlete can use the developed layer without excessive recovery cost.'
    ],
    regression_rules = [
        'Return to base if aerobic support is not strong enough.',
        'Use general strength before muscular endurance if force reserve is inadequate.',
        'Reduce grade, load, duration, or frequency if local damage disrupts the rest of training.'
    ],
    references = [
        CardReference(card_id = 'macro_003', relationship = CardRelationship.ALTERNATIVE, tags = ['closest_mainstream_context']),
        CardReference(card_id = 'macro_024', relationship = CardRelationship.PREVIOUS, tags = ['evoke_layering']),
        CardReference(card_id = 'macro_026', relationship = CardRelationship.NEXT, tags = ['evoke_layering'])
    ],
    recommended_duration_weeks = '4-10',
    timing_guidance = [
        'Use when the next useful adaptation is local muscular endurance, not more general base or early race simulation.',
        'Use before objective-like utilisation when uphill force production is a likely limiter.',
        'The phase should end with enough recovery to reveal whether the muscular-endurance layer was absorbed.'
    ],
    watchouts = [
        'Do not use muscular-endurance work as a substitute for missing base.',
        'Avoid severe soreness as a success marker.',
        'Do not increase grade, load, duration, and frequency together.',
        'A route is not Evoke-specific unless it trains the intended layer.'
    ],
    additional_information = 'Evoke muscular endurance development is precise: the coach decides whether repeated local force is the limiting layer, builds it with a recoverable dose, and keeps the athlete from confusing hard mountain work with useful mountain work.'
)
