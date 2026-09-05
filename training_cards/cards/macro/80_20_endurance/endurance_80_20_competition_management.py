from training_cards.philosophy_profiles import ENDURANCE_80_20
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

endurance_80_20_competition_management = MacroCard(
    id = 'macro_014',
    slug = '80-20-competition-management',
    title = '80/20 Competition Management',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [ENDURANCE_80_20],
    summary = 'A race-season phase that treats competitions as high-cost inputs inside a protected hard/easy pattern.',
    purpose = 'Maintain readiness between events while preventing races and between-race running from becoming constant moderate-hard stress.',
    tags = ['80_20', 'competition', 'race_season', 'recovery_spacing'],
    goal_race_context = [
        'During a race series or multi-race season.',
        'When races disrupt normal intensity distribution and recovery timing.',
        'When the athlete needs small fitness touchpoints but not a full new build.',
        'For trail events whose mechanical cost may exceed what intensity zones show.'
    ],
    training_profile = [
        'Each race is counted as both training stress and information.',
        'Between events, easy days restore contrast and selected quality is used sparingly.',
        'Moderate running is included only if it has a clear purpose.',
        'Trail race cost is judged by duration, descents, technicality, travel, heat, altitude, and recovery response.'
    ],
    expected_adaptations = [
        'More stable freshness across a race season.',
        'Better ability to recover hard/easy contrast after racing.',
        'Improved decisions about when to train, touch quality, or rest between events.'
    ],
    progression_rules = [
        'Add small quality touchpoints only after race recovery is clear.',
        'Use race review to decide whether the next gap needs recovery, maintenance, or specific touchpoints.',
        'Move to recovery and transition when the race sequence ends or fatigue accumulates.'
    ],
    regression_rules = [
        'Treat the race itself as the hard work if recovery is incomplete.',
        'Replace between-race workouts with easy running or rest when contrast is lost.',
        'Use mainstream maintenance if competition pressure is low.'
    ],
    references = [
        CardReference(card_id = 'macro_006', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_012', relationship = CardRelationship.PREVIOUS, tags = ['after_specific_preparation']),
        CardReference(card_id = 'macro_015', relationship = CardRelationship.ALTERNATIVE, tags = ['lower_race_pressure'])
    ],
    recommended_duration_weeks = '2-12+',
    timing_guidance = [
        'Use when races are close enough that they shape the training pattern.',
        'The relevant distribution window may need to include the race itself and the recovery that follows.'
    ],
    watchouts = [
        'Do not pretend races are outside the training distribution.',
        'Avoid stacking tune-up races, moderate workouts, and long runs without enough easy recovery.',
        'Do not let watch-based intensity hide trail muscle damage.',
        'If every week feels like race week, the season probably needs fewer demands.'
    ],
    additional_information = '80/20 competition management prevents a race season from dissolving into constant medium-hard stress. The coach uses each race, each recovery response, and each small touchpoint to rebuild contrast before the next event.'
)
