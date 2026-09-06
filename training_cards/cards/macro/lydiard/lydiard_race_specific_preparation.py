from training_cards.philosophy_profiles import LYDIARD
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

lydiard_race_specific_preparation = MacroCard(
    id = 'macro_018',
    slug = 'lydiard-race-specific-preparation',
    title = 'Lydiard Race-Specific Preparation',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [LYDIARD],
    summary = 'A late preparation phase that integrates previously built capacities toward the target race.',
    purpose = 'Connect the aerobic base, strength, faster work, pacing judgement, and goal demands before peaking.',
    tags = ['lydiard', 'race_specific', 'integration', 'backward_planning'],
    goal_race_context = [
        'After base and later capacity layers have been substantially absorbed.',
        'When the target race is close enough for specific integration to matter.',
        'When backward planning shows that the athlete needs connection more than another isolated development block.',
        'For trail goals when terrain elements are added transparently as modern adaptations.'
    ],
    training_profile = [
        'Race-relevant work integrates capacities rather than replacing the sequence.',
        'Pacing, rhythm, and effort judgement remain central.',
        'Trail specificity can include terrain, hiking, or technical confidence, but should be named as an adaptation.',
        'Recovery response determines whether the athlete is integrating or just accumulating fatigue.'
    ],
    expected_adaptations = [
        'Improved ability to access built capacities in race-relevant conditions.',
        'Better pacing judgement and confidence near the goal.',
        'Clearer readiness for final peaking and tapering.'
    ],
    progression_rules = [
        'Increase race relevance only when prior capacities remain stable.',
        'Use backward timing to protect enough space for taper and recovery.',
        'Move to Lydiard peak and taper when integration is sufficient and freshness becomes the limiting factor.'
    ],
    regression_rules = [
        'Return to hill resistance transition if that bridge layer is clearly missing.',
        'Simplify race-specific terrain if it disrupts recovery or coordination.',
        'Choose an honest reduced goal if the sequence has been interrupted too much to compress safely.'
    ],
    references = [
        CardReference(card_id = 'macro_004', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_017', relationship = CardRelationship.PREVIOUS, tags = ['lydiard_sequence']),
        CardReference(card_id = 'macro_019', relationship = CardRelationship.NEXT, tags = ['lydiard_sequence'])
    ],
    recommended_duration_weeks = '3-8',
    timing_guidance = [
        'Use late enough to transfer to the goal and early enough to taper.',
        'The target race should give the sequence direction without making the plan rigid.'
    ],
    watchouts = [
        'Do not skip integration and hope taper will solve missing preparation.',
        'Avoid attributing trail-specific skills to Lydiard unless the adaptation is explicit.',
        'Do not make late specific work so costly that it hides the peak.',
        'Poor recovery suggests the sequence is not being absorbed.'
    ],
    additional_information = 'This phase translates Lydiard sequencing into modern race preparation. It asks how the runner will use what was built, then adds only the specific demands that help the athlete arrive ready rather than overloaded.'
)
