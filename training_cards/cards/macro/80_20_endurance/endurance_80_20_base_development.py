from training_cards.philosophy_profiles import ENDURANCE_80_20
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

endurance_80_20_base_development = MacroCard(
    id = 'macro_010',
    slug = '80-20-base-development',
    title = '80/20 Base Development',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [ENDURANCE_80_20],
    summary = 'A base phase that protects a low-intensity majority while gradually expanding repeatable aerobic volume.',
    purpose = 'Build aerobic durability by making easy work genuinely easy and progressing load through manageable cycles.',
    tags = ['80_20', 'base', 'aerobic', 'intensity_distribution'],
    goal_race_context = [
        'Early in preparation when the athlete needs more repeatable aerobic volume.',
        'When ordinary runs often drift into moderate effort.',
        'Before harder blocks that require fresh enough legs to execute quality well.',
        'For trail runners who need terrain-aware easy discipline before specific demands increase.'
    ],
    training_profile = [
        'Most running stays low intensity across the phase, not merely on selected days.',
        'Volume grows mainly through easy duration or frequency rather than frequent moderate effort.',
        'Harder touches, if used, are small, purposeful, and surrounded by easy work.',
        'On hills or trails, hiking, slower routes, or flatter alternatives may be needed to preserve the easy stimulus.'
    ],
    expected_adaptations = [
        'Improved aerobic durability with less hidden fatigue from grey-zone training.',
        'Better ability to execute future quality sessions because easy days remain restorative.',
        'Clearer athlete understanding of what low-intensity work should feel like.'
    ],
    progression_rules = [
        'Increase mostly low-intensity volume before adding more intensity.',
        'Keep the distribution visible across the phase rather than forcing exact arithmetic into every workout.',
        'Move to 80/20 capacity development when the athlete can repeat easy volume and recover predictably.'
    ],
    regression_rules = [
        'Lower intensity, simplify terrain, or add recovery days if easy work stops feeling easy.',
        'Reduce volume before adding more hard/easy contrast if fatigue is already high.',
        'Use mainstream return-to-consistency work if routine is not yet stable.'
    ],
    references = [
        CardReference(card_id = 'macro_002', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_011', relationship = CardRelationship.NEXT, tags = ['80_20_sequence'])
    ],
    recommended_duration_weeks = '6-16',
    timing_guidance = [
        'Best early in a cycle, before race-specific pressure becomes dominant.',
        'The useful review window is the phase or block, not one isolated session.'
    ],
    watchouts = [
        'Do not turn 80/20 into anxious daily ratio accounting.',
        'Avoid easy runs that repeatedly become steady or threshold-adjacent.',
        'Do not ignore trail mechanical cost just because heart rate stayed low.',
        'If added volume is not easy, it is not serving the base phase.'
    ],
    additional_information = 'An 80/20 base phase uses intensity distribution as a behaviour-changing tool. The athlete learns that easy volume is not low-value filler; it is the work that makes later quality possible and keeps the training pattern sustainable.'
)
