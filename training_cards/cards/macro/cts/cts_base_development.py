from training_cards.philosophy_profiles import CTS
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

cts_base_development = MacroCard(
    id = 'macro_020',
    slug = 'cts-base-development',
    title = 'CTS Base Development',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [CTS],
    summary = 'A workload-building phase that develops the fundamentals needed for later ultra-specific preparation.',
    purpose = 'Build earned, repeatable workload capacity before using focused blocks or event-specific rehearsal.',
    tags = ['cts', 'base', 'workload', 'ultrarunning'],
    goal_race_context = [
        'Early in preparation for a trail or ultra goal.',
        'When the athlete needs more durable workload before specific interventions.',
        'When consistency, recovery, and basic execution are more limiting than advanced methods.',
        'Before focused limiter blocks or demanding race-specific work.'
    ],
    training_profile = [
        'Training expands repeatable workload rather than chasing symbolic mileage.',
        'Volume is interpreted through time, frequency, vertical gain, density, intensity, and recovery cost.',
        'Low-intensity endurance work supports the ability to absorb later quality.',
        'Terrain is included when it helps build relevant capacity without overwhelming fundamentals.'
    ],
    expected_adaptations = [
        'Greater ability to complete useful training week after week.',
        'Improved readiness for focused block work and specific ultra demands.',
        'Better understanding of what workload the athlete can actually absorb.'
    ],
    progression_rules = [
        'Progress workload patiently and make the chosen variable explicit.',
        'Keep recovery and execution quality visible before adding complexity.',
        'Move to CTS capacity development when the athlete can repeat the base load reliably.'
    ],
    regression_rules = [
        'Reduce density, long-run cost, or terrain before assuming the athlete lacks motivation.',
        'Return to mainstream return-to-consistency if routine is not stable.',
        'Delay focused blocks if basic workload is not yet repeatable.'
    ],
    references = [
        CardReference(card_id = 'macro_002', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_021', relationship = CardRelationship.NEXT, tags = ['cts_sequence'])
    ],
    recommended_duration_weeks = '6-16+',
    timing_guidance = [
        'Use before event-specific work becomes the main planning problem.',
        'Longer ultra goals often need a longer runway for workload to become durable.'
    ],
    watchouts = [
        'Do not treat weekly distance as the only measure of base.',
        'Avoid adding complexity before fundamentals are stable.',
        'Do not ignore life stress when judging the absorbable workload.',
        'A dramatic single week is not evidence of durable workload capacity.'
    ],
    additional_information = 'CTS base development is practical and long-viewed. The question is what workload the athlete can repeat, recover from, and later convert into specific preparation for the actual event.'
)
