from training_cards.philosophy_profiles import SWAP
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

swap_race_specific_preparation = MacroCard(
    id = 'macro_030',
    slug = 'swap-race-specific-preparation',
    title = 'SWAP Race-Specific Preparation',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [SWAP],
    summary = 'A specific phase that prepares the goal while preserving confidence, agency, joy, and health.',
    purpose = 'Apply fitness to the target event in a way that supports performance and the athlete’s relationship with the goal.',
    tags = ['swap', 'race_specific', 'confidence', 'adventure'],
    goal_race_context = [
        'Late in preparation for a meaningful race or adventure goal.',
        'When terrain, fueling, pacing, or confidence must be practised without fear-based overloading.',
        'When the goal should motivate the athlete rather than shrink the whole plan around anxiety.',
        'For trail runners who need specificity, exploration, and boundaries at the same time.'
    ],
    training_profile = [
        'Specific work rehearses goal demands with clear purpose and athlete agency.',
        'Adventure and route choice are used when they support confidence and transfer.',
        'Fueling, recovery, and health behaviours remain part of execution.',
        'The phase observes both performance response and emotional response to specificity.'
    ],
    expected_adaptations = [
        'Improved goal-specific readiness and confidence.',
        'Better pacing, fueling, terrain, and problem-solving habits.',
        'A healthier relationship with race pressure.'
    ],
    progression_rules = [
        'Progress specificity only while confidence and recovery stay intact.',
        'Use positive and negative responses to adjust the next rehearsal.',
        'Move to mainstream peak and taper when readiness is built and freshness matters most.'
    ],
    regression_rules = [
        'Simplify rehearsals if the goal starts creating fear or excessive fatigue.',
        'Return to capacity development if a key skill or fitness quality is missing.',
        'Choose less demanding terrain if adventure is overwhelming the purpose.'
    ],
    references = [
        CardReference(card_id = 'macro_004', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_029', relationship = CardRelationship.PREVIOUS, tags = ['swap_sequence']),
        CardReference(card_id = 'macro_005', relationship = CardRelationship.NEXT, tags = ['peak_and_taper'])
    ],
    recommended_duration_weeks = '4-8',
    timing_guidance = [
        'Use late enough that specificity transfers and early enough to absorb the work.',
        'Specificity should make the athlete feel prepared, not trapped by the goal.'
    ],
    watchouts = [
        'Do not turn every adventure into a race simulation.',
        'Avoid fear-based last-minute specificity.',
        'Do not let excitement hide fueling, recovery, or injury warning signs.',
        'If the goal becomes emotionally narrowing, reduce pressure and clarify purpose.'
    ],
    additional_information = 'SWAP race-specific preparation lets the athlete practise the race without becoming consumed by it. The goal matters, and so does the person moving toward it.'
)
