from training_cards.philosophy_profiles import ENDURANCE_80_20
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

endurance_80_20_capacity_development = MacroCard(
    id = 'macro_011',
    slug = '80-20-capacity-development',
    title = '80/20 Capacity Development',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [ENDURANCE_80_20],
    summary = 'A development phase that adds selected quality while preserving low-intensity dominance and hard/easy contrast.',
    purpose = 'Improve targeted performance capacity without allowing moderate or hard work to crowd out aerobic support.',
    tags = ['80_20', 'capacity', 'quality', 'hard_easy'],
    goal_race_context = [
        'After a stable aerobic base has been established.',
        'When the athlete needs threshold, aerobic power, hill, or long-endurance development.',
        'When quality should become more purposeful but not more frequent by default.',
        'Before race-specific preparation, when development still matters more than rehearsal.'
    ],
    training_profile = [
        'One or two selected quality emphases are placed inside a mostly low-intensity pattern.',
        'Hard days are protected by easy days that are genuinely easy.',
        'Moderate work appears only when it has a clear job.',
        'Trail terrain is chosen to support the intended intensity rather than accidentally increasing total stress.'
    ],
    expected_adaptations = [
        'Improved selected performance capacity with better recovery between key stresses.',
        'More disciplined separation between easy, moderate, and hard work.',
        'Greater confidence that quality sessions are supported by the rest of the phase.'
    ],
    progression_rules = [
        'Progress the chosen quality or the easy support volume, not both aggressively at once.',
        'Keep recovery spacing adequate before adding more hard work.',
        'Move to race-specific preparation when the developed capacity is ready to be applied to the goal.'
    ],
    regression_rules = [
        'Remove accidental moderate work before cutting the planned quality session.',
        'Extend recovery spacing if hard sessions are completed but not absorbed.',
        'Return to 80/20 base development if easy volume can no longer be protected.'
    ],
    references = [
        CardReference(card_id = 'macro_003', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_010', relationship = CardRelationship.PREVIOUS, tags = ['80_20_sequence']),
        CardReference(card_id = 'macro_012', relationship = CardRelationship.NEXT, tags = ['80_20_sequence'])
    ],
    recommended_duration_weeks = '4-10',
    timing_guidance = [
        'Use after low-intensity volume is stable enough to support quality.',
        'Review distribution across the block or phase rather than judging one unusual week.'
    ],
    watchouts = [
        'Do not add quality while leaving ordinary runs too hard.',
        'Avoid turning every purposeful workout into threshold work.',
        'Do not ignore downhill, heat, or technical terrain cost when classifying hard and easy days.',
        'Flat execution quality is a sign the hard/easy pattern is failing.'
    ],
    additional_information = 'This phase asks a very 80/20 question: can the athlete become fitter because the hard work is specific and the easy work is protected, rather than because every run becomes a little harder?'
)
