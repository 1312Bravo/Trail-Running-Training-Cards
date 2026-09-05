from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MacroCard,
    TrainingLevel,
)

mainstream_return_to_consistency = MacroCard(
    id = 'macro_001',
    slug = 'mainstream-return-to-consistency',
    title = 'Return To Consistency',
    card_type = CardType.MACRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A conservative phase for restoring dependable rhythm, frequency, and basic running tolerance before development.',
    purpose = 'Rebuild a repeatable training routine before asking the athlete to absorb harder or more specific work.',
    tags = [
        'return',
        'consistency',
        'routine',
        'low_risk'
    ],
    goal_race_context = [
        'After illness, travel, life disruption, off-season, or any period of inconsistent running.',
        'When the athlete is cleared to train but not yet ready for normal development load.',
        'When confidence, rhythm, and simple repeatability matter more than performance gains.',
        'Before base development if recent training has been too irregular to progress safely.'
    ],
    training_profile = [
        'Mostly easy running with conservative volume, terrain, and intensity choices.',
        'Progress frequency and routine before demanding longer, faster, or more technical sessions.',
        'Use walk-run, hiking, cross-training, or short easy outings when they preserve consistency.',
        'Keep trail exposure simple and reduce downhill or technical cost until tolerance is clear.'
    ],
    expected_adaptations = [
        'Restored habit strength and confidence in regular training.',
        'Improved basic musculoskeletal tolerance for repeatable running.',
        'A clearer picture of readiness before entering a development phase.'
    ],
    progression_rules = [
        'Progress one simple variable at a time, usually frequency or duration before intensity.',
        'Repeat a stable week before increasing load if readiness is uncertain.',
        'Move to base development only when easy running is repeatable and recovery is predictable.'
    ],
    regression_rules = [
        'Shorten runs or add walk breaks if soreness, fatigue, or anxiety about training rises.',
        'Use smoother terrain or cross-training if trail impact or downhill load is the limiting factor.',
        'Hold the phase longer instead of forcing a calendar-based transition.'
    ],
    references = [
        CardReference(
            card_id = 'macro_002',
            relationship = CardRelationship.NEXT,
            tags = [
                'common_sequence'
            ]
        ),
        CardReference(
            card_id = 'macro_007',
            relationship = CardRelationship.ALTERNATIVE,
            tags = [
                'fatigue_limited'
            ]
        )
    ],
    recommended_duration_weeks = '2-8',
    timing_guidance = [
        'Use before a normal build when recent consistency is the main limiter.',
        'Duration should be driven by response, not by pressure to catch up.'
    ],
    watchouts = [
        'Do not turn this phase into hidden fitness chasing.',
        'Avoid adding intensity, volume, and difficult terrain at the same time.',
        'Do not treat former fitness as proof of current tissue tolerance.',
        'Escalating soreness, poor sleep, or dread of training means the dose is too high.'
    ],
    additional_information = 'Return to consistency protects the athlete from the common mistake of trying to restart at the level they remember rather than the level they can currently absorb. The win is not a dramatic workout; it is a dependable training rhythm that can support the next phase.'
)
