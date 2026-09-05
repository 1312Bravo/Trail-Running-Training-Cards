from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MezzoCard,
    TrainingLevel,
)

mainstream_progressive_aerobic_development_block = MezzoCard(
    id = 'mezzo_010',
    slug = 'mainstream-progressive-aerobic-development-block',
    title = 'Progressive Aerobic Development Block',
    card_type = CardType.MEZZO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A mainstream block that grows aerobic load through one controlled progression variable.',
    purpose = 'Develop aerobic capacity and durability while keeping the training dose clear enough to absorb and review.',
    tags = [
        'mainstream_endurance',
        'aerobic',
        'progressive_overload',
        'durability'
    ],
    goal_race_context = [
        'Use after basic running consistency is present.',
        'Useful when aerobic capacity, frequency tolerance, or long-run tolerance is the main limiter.',
        'Appropriate before controlled quality or race-specific blocks.',
        'Can support trail goals when vertical gain and terrain difficulty are progressed deliberately.'
    ],
    expected_adaptations = [
        'Improved repeatable aerobic volume.',
        'Better musculoskeletal tolerance for regular running.',
        'More stable easy-effort response across the week.',
        'Clearer evidence about which load variable the athlete can absorb.'
    ],
    progression_rules = [
        'Choose one primary progression variable for the block before it starts.',
        'Progress only after the previous week is recovered well enough to repeat.',
        'Use a consolidation week when two or three building weeks have accumulated fatigue.'
    ],
    regression_rules = [
        'Hold weekly load steady when soreness, sleep, mood, or easy-run effort worsens.',
        'Reduce terrain cost before abandoning the aerobic purpose.',
        'Use cross-training only when it preserves aerobic stimulus without hiding a running-tolerance problem.'
    ],
    references = [
        CardReference(
            card_id = 'macro_007',
            relationship = CardRelationship.PARENT,
            tags = [
                'mainstream_phase'
            ]
        ),
        CardReference(
            card_id = 'mezzo_011',
            relationship = CardRelationship.NEXT,
            tags = [
                'after_aerobic_stability'
            ]
        ),
        CardReference(
            card_id = 'micro_010',
            relationship = CardRelationship.CHILD,
            tags = [
                'core_week'
            ]
        )
    ],
    recommended_duration_weeks = '3-8',
    placement_guidance = [
        'Place after return-to-consistency work or a stable maintenance period.',
        'Use before intensity-heavy or highly specific race-preparation blocks.',
        'Avoid immediately after a race, illness, or block that already left recovery unstable.'
    ],
    training_profile = [
        'Mostly easy aerobic running.',
        'One clearly progressed load variable such as frequency, duration, long-run length, or modest vertical gain.',
        'Optional strides or light strength support only when they do not compromise the aerobic progression.',
        'Simple monitoring through RPE, recovery, soreness, and easy-run repeatability.'
    ],
    watchouts = [
        'Adding volume and intensity together.',
        'Increasing vertical gain while also extending the long run substantially.',
        'Treating fatigue as proof the block is working.',
        'Using a bigger week when the previous week was merely completed, not absorbed.'
    ],
    additional_information = 'This block is the mainstream training-principle version of aerobic development. The coaching question is not how much work can be added, but which dose creates enough overload while preserving consistency. Trail runners should count climbing, descending, and technicality as load, not scenery. A successful block leaves the runner more trainable and better prepared for controlled quality or more specific event demands.'
)
