from training_cards.philosophy_profiles import LYDIARD
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

lydiard_peak_and_taper = MacroCard(
    id = 'macro_019',
    slug = 'lydiard-peak-and-taper',
    title = 'Lydiard Peak And Taper',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [LYDIARD],
    summary = 'A timed final phase that expresses the completed sequence rather than forcing missing fitness late.',
    purpose = 'Let accumulated preparation show by reducing fatigue while preserving readiness and confidence.',
    tags = ['lydiard', 'peak', 'taper', 'timing'],
    goal_race_context = [
        'Final phase before a target race after the sequence has been substantially completed.',
        'When the athlete needs freshness, coordination, and confidence more than new load.',
        'When backward planning has protected enough space for the peak.',
        'For trail goals where late terrain exposure should preserve confidence rather than create damage.'
    ],
    training_profile = [
        'Training load is reduced while useful rhythm and race readiness are maintained.',
        'The phase expresses the base, strength, faster work, and integration already built.',
        'Athlete feel and recovery response remain important guides.',
        'Trail-specific touches should be familiar and low risk.'
    ],
    expected_adaptations = [
        'Reduced fatigue with retained access to built capacities.',
        'Better confidence that preparation is complete enough to race.',
        'Improved readiness to execute without last-minute forcing.'
    ],
    progression_rules = [
        'Progress by removing unnecessary cost while maintaining race rhythm.',
        'Keep sharpening controlled and connected to the sequence.',
        'After the race, move to recovery or mainstream competition management depending on the calendar.'
    ],
    regression_rules = [
        'Reduce work further if fatigue from earlier phases remains high.',
        'Avoid compensating for incomplete preparation with last-minute intensity.',
        'Use easy aerobic running if confidence needs rhythm but the body needs lower cost.'
    ],
    references = [
        CardReference(card_id = 'macro_005', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_018', relationship = CardRelationship.PREVIOUS, tags = ['lydiard_sequence'])
    ],
    recommended_duration_weeks = '1-3',
    timing_guidance = [
        'The peak should be timed from the goal rather than improvised at the end.',
        'If prior phases were incomplete, the taper should be honest about what can and cannot be expressed.'
    ],
    watchouts = [
        'Do not force a peak that the previous sequence did not prepare.',
        'Avoid late workouts designed to prove fitness.',
        'Do not remove all rhythm unless recovery requires it.',
        'Last-minute technical or downhill stress can ruin freshness.'
    ],
    additional_information = 'A Lydiard peak is the visible end of an invisible sequence. It works because the athlete has built enough aerobic base, strength, and integration to reveal, not because the final days create a miracle.'
)
