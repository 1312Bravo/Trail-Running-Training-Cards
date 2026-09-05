from training_cards.philosophy_profiles import SHARMAN_ULTRA
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

sharman_competition_management = MacroCard(
    id = 'macro_038',
    slug = 'sharman-competition-management',
    title = 'Sharman Ultra Competition Management',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [SHARMAN_ULTRA],
    summary = 'An adaptive race-season phase shaped by athlete context, race feedback, and practical ultra experience.',
    purpose = 'Manage multiple events by fitting training, recovery, and learning to the runner’s real life and goals.',
    tags = ['sharman_ultra', 'competition', 'race_season', 'adaptation'],
    goal_race_context = [
        'During an ultra season, race series, or sequence of trail goals.',
        'When each event creates different practical and recovery demands.',
        'When the athlete’s lifestyle and success definition should shape between-race choices.',
        'When learning from racing matters as much as filling the calendar.'
    ],
    training_profile = [
        'Each race is reviewed for physical cost, practical lessons, confidence, and next-event relevance.',
        'Between-race training is adapted to life, recovery, and the next course’s demands.',
        'The phase teaches the runner how to interpret response and adjust expectations.',
        'Fitness touchpoints, terrain practice, and recovery are selected for maximum useful benefit.'
    ],
    expected_adaptations = [
        'Improved race-season decision-making.',
        'Better fit between training, life, recovery, and racing goals.',
        'More useful learning from each event.'
    ],
    progression_rules = [
        'Add work only when the previous race cost has been understood and absorbed.',
        'Use each event to refine the next training and execution choice.',
        'Move to recovery, maintenance, or race-specific preparation as the season changes.'
    ],
    regression_rules = [
        'Reduce between-race work when lifestyle or recovery cannot support it.',
        'Shift goals if the race sequence no longer fits the athlete’s current state.',
        'Use mainstream competition management if athlete-specific ultra reasoning is not central.'
    ],
    references = [
        CardReference(card_id = 'macro_006', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_037', relationship = CardRelationship.ALTERNATIVE, tags = ['single_goal_specificity']),
        CardReference(card_id = 'macro_007', relationship = CardRelationship.NEXT, tags = ['season_complete'])
    ],
    recommended_duration_weeks = '2-12+',
    timing_guidance = [
        'Use when race timing and athlete context are too important for a generic between-race plan.',
        'Every race should create a clearer next decision.'
    ],
    watchouts = [
        'Do not apply one between-race template to every athlete.',
        'Avoid racing often without learning from the pattern.',
        'Do not ignore travel, logistics, family, or work stress.',
        'If the athlete’s definition of success has changed, update the plan.'
    ],
    additional_information = 'Sharman Ultra competition management puts coaching judgement in the gap between events. The goal is not simply to keep training; it is to choose the useful work this athlete can absorb before the next race.'
)
