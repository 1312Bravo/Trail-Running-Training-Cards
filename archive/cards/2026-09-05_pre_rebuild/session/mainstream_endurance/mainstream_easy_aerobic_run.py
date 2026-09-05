from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    SessionCard,
    SessionPart,
    TrainingLevel,
)
from training_cards.session_families import EASY_SESSION_FAMILY

mainstream_easy_aerobic_run = SessionCard(
    id = 'session_016',
    slug = 'mainstream-easy-aerobic-run',
    title = 'Easy Aerobic Run',
    card_type = CardType.SESSION,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A simple aerobic run used to build repeatable capacity with low recovery cost.',
    purpose = 'Accumulate low-intensity aerobic work while preserving the ability to train again soon.',
    tags = [
        'mainstream_endurance',
        'easy',
        'aerobic',
        'repeatability'
    ],
    goal_race_context = [
        'Useful throughout most phases as the low-cost aerobic foundation.',
        'Especially important during aerobic progression, quality weeks, consolidation, and return from interruption.',
        'Appropriate on trail when terrain does not turn easy effort into hidden muscular or technical stress.'
    ],
    expected_adaptations = [
        'Improved aerobic efficiency.',
        'Better running frequency tolerance.',
        'Preserved recovery between higher-cost sessions.',
        'More reliable effort awareness.'
    ],
    progression_rules = [
        'Progress duration or frequency only when the run remains conversational and recovery is normal.',
        'Add terrain only when it does not change the intended low-cost aerobic stimulus.',
        'Use this run to support harder training, not to prove fitness.'
    ],
    regression_rules = [
        'Shorten the run, add walking, or flatten the route if easy effort is not available.',
        'Use low-impact aerobic work when running impact is not currently recoverable.',
        'Make the session recovery-only if fatigue signs are elevated.'
    ],
    references = [
        CardReference(
            card_id = 'micro_010',
            relationship = CardRelationship.PARENT,
            tags = [
                'core_session'
            ]
        ),
        CardReference(
            card_id = 'micro_011',
            relationship = CardRelationship.PARENT,
            tags = [
                'support_session'
            ]
        ),
        CardReference(
            card_id = 'micro_012',
            relationship = CardRelationship.PARENT,
            tags = [
                'easy_rhythm'
            ]
        )
    ],
    session_family = EASY_SESSION_FAMILY,
    typical_duration = '20-90 minutes',
    workout_parts = [
        SessionPart(
            name = 'Settle In',
            duration = '5-10 min',
            rpe = '1-3',
            instructions = 'Start very easy and let the body find relaxed rhythm before judging pace.'
        ),
        SessionPart(
            name = 'Easy Aerobic Running',
            duration = '15-75 min',
            rpe = '2-4',
            instructions = 'Keep breathing conversational and movement smooth; back off if effort drifts upward without a clear reason.',
            terrain_notes = 'On hills, hiking or shorter stride is acceptable when it preserves easy aerobic effort.'
        ),
        SessionPart(
            name = 'Finish Controlled',
            duration = '5 min',
            rpe = '1-2',
            instructions = 'Finish feeling able to train again soon, unless this run was intentionally extended as the week progression.'
        )
    ],
    training_profile = [
        'Low-intensity aerobic stimulus.',
        'Low recovery cost when appropriately dosed.',
        'Effort, breathing, and recovery matter more than pace.',
        'Trail version may include hiking to keep intensity controlled.'
    ],
    watchouts = [
        'Letting easy runs drift into steady work.',
        'Choosing terrain that adds too much downhill or technical fatigue.',
        'Using pace targets that are inappropriate for heat, hills, fatigue, or surface.',
        'Extending the run when the week already has enough load.'
    ],
    additional_information = 'This card is deliberately simple because easy aerobic running is one of the most useful mainstream tools when it is executed honestly. The value is not in making the run special; it is in accumulating repeatable work that supports adaptation. For trail runners, an easy run can include climbing, hiking, or soft surfaces, but the route should not quietly become a strength-endurance or downhill-conditioning session.'
)
