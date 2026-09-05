from training_cards.philosophy_profiles import SWAP
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

swap_off_season = MacroCard(
    id = 'macro_034',
    slug = 'swap-off-season',
    title = 'SWAP Off-Season',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [SWAP],
    summary = 'An off-season phase for play, movement variety, identity reset, and renewed motivation.',
    purpose = 'Step away from performance pressure while preserving enough joyful movement to support the next cycle.',
    tags = ['swap', 'off_season', 'play', 'motivation'],
    goal_race_context = [
        'After a goal season or emotionally demanding preparation cycle.',
        'When the athlete needs decompression and broader movement options.',
        'When reconnecting with play matters more than preserving race-specific sharpness.',
        'Before returning to base, maintenance, or consistency work.'
    ],
    training_profile = [
        'Running can continue, but pressure and race-specific structure are reduced.',
        'Playful movement, hiking, strength, mobility, cross-training, and route freedom have more room.',
        'The phase protects basic rhythm without making every choice performance-based.',
        'Trail time can be exploratory and confidence-building with controlled technical and downhill cost.'
    ],
    expected_adaptations = [
        'Renewed motivation and emotional space from competition pressure.',
        'Preserved general movement capacity and basic aerobic rhythm.',
        'A more durable relationship with running.'
    ],
    progression_rules = [
        'Progress when curiosity about structured training naturally returns.',
        'Let movement variety solve small durability or confidence gaps.',
        'Move to SWAP base when the athlete wants more direction and can absorb it.'
    ],
    regression_rules = [
        'Move to recovery if fatigue is still the main issue.',
        'Move to maintenance if the athlete needs more structure.',
        'Simplify if play becomes hidden training stress.'
    ],
    references = [
        CardReference(card_id = 'macro_008', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_007', relationship = CardRelationship.PREVIOUS, tags = ['after_recovery']),
        CardReference(card_id = 'macro_028', relationship = CardRelationship.NEXT, tags = ['new_cycle'])
    ],
    recommended_duration_weeks = '4-12+',
    timing_guidance = [
        'Use after the main goal season or when the athlete needs real decompression.',
        'The phase should feel spacious, not like a renamed build.'
    ],
    watchouts = [
        'Do not confuse playful with careless.',
        'Avoid letting the athlete lose all routine if that would make return stressful.',
        'Do not turn every adventure into a stealth workout.',
        'If identity pressure remains high, reduce performance language.'
    ],
    additional_information = 'SWAP off-season is almost a love letter to future training. It lets the runner remember that movement can be expansive, playful, and restorative before the next structured cycle asks more of them.'
)
