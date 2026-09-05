from training_cards.philosophy_profiles import SWAP
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

swap_competition_management = MacroCard(
    id = 'macro_032',
    slug = 'swap-competition-management',
    title = 'SWAP Competition Management',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [SWAP],
    summary = 'A race-season phase balancing ambition, health, joy, learning, and fatigue across multiple events.',
    purpose = 'Manage races as part of long-term development rather than letting excitement become unmanaged load.',
    tags = ['swap', 'competition', 'race_season', 'long_term'],
    goal_race_context = [
        'During a race season, race series, or sequence of meaningful events.',
        'When the athlete wants to compete often without losing health or joy.',
        'When learning and positive response matter alongside performance.',
        'For trail races where adventure excitement can hide high recovery cost.'
    ],
    training_profile = [
        'Races are treated as performance opportunities, learning inputs, and recovery costs.',
        'Between-race work preserves rhythm and confidence without chasing every possible gain.',
        'The coach watches enthusiasm, mood, fueling, soreness, and identity pressure.',
        'Trail race cost includes travel, terrain, descents, heat, and emotional load.'
    ],
    expected_adaptations = [
        'Improved ability to stay healthy and engaged across a season.',
        'Better race-to-race learning without constant overreaching.',
        'More mature balance between ambition and long-term participation.'
    ],
    progression_rules = [
        'Add between-race work only when recovery and enthusiasm remain strong.',
        'Use each race to learn what the athlete needs next.',
        'Move to recovery, off-season, or maintenance when the season stops being constructive.'
    ],
    regression_rules = [
        'Reduce racing pressure if the athlete is losing joy, health, or freshness.',
        'Use recovery instead of touchpoints when race cost remains high.',
        'Skip optional events when long-term development would benefit.'
    ],
    references = [
        CardReference(card_id = 'macro_006', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_030', relationship = CardRelationship.PREVIOUS, tags = ['after_specific_preparation']),
        CardReference(card_id = 'macro_007', relationship = CardRelationship.NEXT, tags = ['season_complete'])
    ],
    recommended_duration_weeks = '2-12+',
    timing_guidance = [
        'Use when races are close enough to shape training and recovery.',
        'The phase should protect the athlete from racing their way out of loving racing.'
    ],
    watchouts = [
        'Do not let excitement justify every race or workout.',
        'Avoid measuring the season only by results.',
        'Do not ignore fueling, sleep, soreness, or emotional fatigue.',
        'If racing becomes obligatory rather than energising, reassess.'
    ],
    additional_information = 'SWAP competition management keeps racing inside the larger life of the athlete. It respects ambition while protecting the health, joy, and curiosity that make future ambition possible.'
)
