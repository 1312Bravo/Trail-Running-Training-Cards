from training_cards.philosophy_profiles import LYDIARD
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

lydiard_base_development = MacroCard(
    id = 'macro_016',
    slug = 'lydiard-base-development',
    title = 'Lydiard Base Development',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [LYDIARD],
    summary = 'A base-first phase that develops the aerobic foundation later hill, faster, and race work depend on.',
    purpose = 'Build the greatest sustainable aerobic capacity the athlete can absorb before moving to later training layers.',
    tags = ['lydiard', 'base', 'aerobic_conditioning', 'sequence'],
    goal_race_context = [
        'Early in a goal-directed preparation sequence.',
        'When the athlete needs a stronger aerobic platform before faster or more specific work.',
        'When training has become too dependent on isolated hard sessions.',
        'For trail runners who need a running foundation before large mountain-specific demands.'
    ],
    training_profile = [
        'Substantial aerobic running scaled to the athlete rather than copied from historical mileage.',
        'Effort is guided by internal response as well as external data.',
        'The phase preserves enough recovery for the base to become durable rather than brittle.',
        'Trail terrain is used only when it supports aerobic development without excess technical or downhill cost.'
    ],
    expected_adaptations = [
        'Greater sustainable aerobic capacity.',
        'Improved ability to recover from and support later quality work.',
        'Better athlete skill in recognising aerobic effort and recovery state.'
    ],
    progression_rules = [
        'Progress aerobic workload at the rate the whole athlete can absorb.',
        'Let the slowest-adapting system limit increases in volume, terrain, or speed.',
        'Move to the Lydiard hill resistance transition only when the base is repeatable and recovery response is stable.'
    ],
    regression_rules = [
        'Reduce volume, terrain cost, or frequency if musculoskeletal tolerance lags behind aerobic confidence.',
        'Use mainstream return-to-consistency work if routine is not stable enough for base building.',
        'Delay later phases rather than compressing the sequence after interruption.'
    ],
    references = [
        CardReference(card_id = 'macro_002', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_017', relationship = CardRelationship.NEXT, tags = ['lydiard_sequence'])
    ],
    recommended_duration_weeks = '8-20+',
    timing_guidance = [
        'The base should receive enough time to support the later sequence.',
        'Backward planning from the goal should not shorten the base beyond what the athlete can actually use.'
    ],
    watchouts = [
        'Do not equate Lydiard base with copying elite mileage.',
        'Avoid rushing to hills, intervals, or race specificity because the goal feels close.',
        'Do not let aerobic running become unplanned steady testing.',
        'Persistent soreness means the base is exceeding the athlete, not building them.'
    ],
    additional_information = 'A Lydiard base phase is not merely general fitness. It is the foundation of the whole sequence: the place from which later strength, faster work, integration, and racing can be absorbed and expressed.'
)
