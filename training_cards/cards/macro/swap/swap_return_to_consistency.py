from training_cards.philosophy_profiles import SWAP
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

swap_return_to_consistency = MacroCard(
    id = 'macro_027',
    slug = 'swap-return-to-consistency',
    title = 'SWAP Return To Consistency',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [SWAP],
    summary = 'A confidence-restoring phase that rebuilds rhythm through support, agency, and low-pressure consistency.',
    purpose = 'Help the athlete return to training without shame while rebuilding a sustainable relationship with routine.',
    tags = ['swap', 'return', 'consistency', 'confidence'],
    goal_race_context = [
        'After interruption, burnout, injury clearance, illness, life stress, or lost confidence.',
        'When the athlete needs consistency to feel emotionally safe and repeatable.',
        'When joy, agency, and simple wins matter as much as fitness markers.',
        'Before base development if the runner needs to reconnect with training first.'
    ],
    training_profile = [
        'Short, easy, flexible training exposures rebuild trust in the process.',
        'Route choice, walk breaks, playful terrain, or low-pressure movement are used when they protect consistency.',
        'The athlete learns that adjustment is information, not failure.',
        'Speed, terrain, and long duration wait until rhythm and confidence are stable.'
    ],
    expected_adaptations = [
        'Renewed confidence and willingness to train again.',
        'Restored basic rhythm without fear-based overcompensation.',
        'Better athlete agency around sensible adjustments.'
    ],
    progression_rules = [
        'Progress by adding repeatability before challenge.',
        'Let positive response, eagerness, and stable recovery support the next step.',
        'Move to SWAP base when consistency feels supportive rather than fragile.'
    ],
    regression_rules = [
        'Simplify the routine if pressure, soreness, or dread rises.',
        'Use more flexible movement if running feels emotionally or physically loaded.',
        'Stay in the phase longer rather than forcing identity back too fast.'
    ],
    references = [
        CardReference(card_id = 'macro_001', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_028', relationship = CardRelationship.NEXT, tags = ['swap_sequence'])
    ],
    recommended_duration_weeks = '2-8+',
    timing_guidance = [
        'Use before a build when the athlete needs trust and rhythm more than pressure.',
        'The phase ends when consistency feels repeatable and emotionally lighter.'
    ],
    watchouts = [
        'Do not use positivity to hide real fatigue or pain.',
        'Avoid turning the comeback into proof of toughness.',
        'Do not rush speed work before confidence and durability return.',
        'Shame language is a sign the phase is losing its purpose.'
    ],
    additional_information = 'SWAP return to consistency treats the comeback as a human process. The athlete is not behind; they are rebuilding the conditions that let training become a positive and durable part of life again.'
)
