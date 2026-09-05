from training_cards.philosophy_profiles import CTS
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

cts_capacity_development = MacroCard(
    id = 'macro_021',
    slug = 'cts-capacity-development',
    title = 'CTS Capacity Development',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [CTS],
    summary = 'A focused limiter-development phase that uses blocks only when they solve a real performance problem.',
    purpose = 'Develop a selected capacity that matters for the athlete and event while making trade-offs and recovery cost explicit.',
    tags = ['cts', 'capacity', 'focused_block', 'limiter'],
    goal_race_context = [
        'After enough workload foundation has been established.',
        'When a specific limiter such as intensity tolerance, long-run durability, climbing, or descending deserves focused work.',
        'When the athlete needs a clear block purpose rather than a mix of attractive sessions.',
        'Before race-specific preparation, when the limiter still needs development.'
    ],
    training_profile = [
        'The phase names one main performance problem and organizes training around it.',
        'Focused blocks have entry conditions, exits, and recovery space.',
        'Other capacities may be maintained while the priority limiter is developed.',
        'Trail variables are used only when they address the limiter and can be recovered from.'
    ],
    expected_adaptations = [
        'Improved capacity in the selected limiter.',
        'Better understanding of the trade-off created by focused work.',
        'More prepared transition into event-specific preparation.'
    ],
    progression_rules = [
        'Progress the focused exposure only while recovery and supporting workload remain stable.',
        'Exit the block when the limiter has improved enough or fatigue begins to dominate.',
        'Move to CTS race-specific preparation when the developed capacity needs application.'
    ],
    regression_rules = [
        'Return to base development if the athlete lacks workload to support focused stress.',
        'Reduce block density if completion is possible but recovery is poor.',
        'Change the focus if response shows the assumed limiter was wrong.'
    ],
    references = [
        CardReference(card_id = 'macro_003', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_020', relationship = CardRelationship.PREVIOUS, tags = ['cts_sequence']),
        CardReference(card_id = 'macro_022', relationship = CardRelationship.NEXT, tags = ['cts_sequence'])
    ],
    recommended_duration_weeks = '3-8',
    timing_guidance = [
        'Use when a limiter is important enough to justify concentrating training.',
        'Do not keep a focused block going simply because it looks serious.'
    ],
    watchouts = [
        'Do not run a block without naming the problem it solves.',
        'Avoid stacking multiple limiters into one unfocused phase.',
        'Do not let focused work displace the recovery needed to adapt.',
        'If the block leaves unresolved fatigue, it has not succeeded yet.'
    ],
    additional_information = 'CTS capacity development is not a badge for hard training. It is a temporary concentration of work around a meaningful limiter, with a clear reason, cost, and exit.'
)
