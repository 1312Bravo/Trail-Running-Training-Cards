from training_cards.philosophy_profiles import EVOKE_ENDURANCE
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

evoke_base_development = MacroCard(
    id = 'macro_024',
    slug = 'evoke-base-development',
    title = 'Evoke Base Development',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [EVOKE_ENDURANCE],
    summary = 'A mountain-endurance base phase centred on substantial aerobic capacity and threshold-informed intensity control.',
    purpose = 'Build the aerobic layer that supports later strength reserve, muscular endurance, and objective-specific utilisation.',
    tags = ['evoke', 'base', 'aerobic_capacity', 'mountain_endurance'],
    goal_race_context = [
        'Early in preparation for mountain running or long climbing-heavy goals.',
        'When the athlete needs more aerobic capacity before specific muscular-endurance work.',
        'When middle-intensity habits may be limiting aerobic development.',
        'Before strength-reserve or muscular-endurance layers become prominent.'
    ],
    training_profile = [
        'Substantial low-intensity aerobic work is prioritised and individualised.',
        'Intensity may be guided by aerobic threshold, drift, breathing, RPE, or other practical cues.',
        'Progress is judged by repeatable aerobic movement and recovery, not visible fatigue.',
        'Hills, hiking, or incline may be used if they preserve the intended aerobic layer.'
    ],
    expected_adaptations = [
        'Greater aerobic capacity for long mountain duration.',
        'Better control of intensity below the costlier middle zone.',
        'Improved readiness for later strength and muscular-endurance layers.'
    ],
    progression_rules = [
        'Progress aerobic time or output at the same aerobic cost before adding specialised mountain stress.',
        'Review thresholds or field cues when response no longer matches the prescription.',
        'Move to Evoke capacity development when aerobic consistency and recovery are stable.'
    ],
    regression_rules = [
        'Lower intensity if the athlete repeatedly drifts above the intended aerobic effort.',
        'Use hiking, smoother terrain, or cross-training when impact cost limits aerobic volume.',
        'Delay muscular-endurance work if aerobic base or recovery is not ready.'
    ],
    references = [
        CardReference(card_id = 'macro_002', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_025', relationship = CardRelationship.NEXT, tags = ['evoke_layering'])
    ],
    recommended_duration_weeks = '8-20+',
    timing_guidance = [
        'Use before visible mountain-specific work becomes the priority.',
        "The right length depends on the athlete's aerobic profile, training history, and objective."
    ],
    watchouts = [
        'Do not replace base with hard uphill sessions because they feel specific.',
        'Avoid treating a threshold estimate as more precise than the terrain allows.',
        'Do not ignore mechanical cost when aerobic pace or vertical speed improves.',
        'If recovery worsens as aerobic work expands, the dose is too large.'
    ],
    additional_information = 'Evoke base development is the first layer of the mountain problem. It builds the aerobic system the athlete will later ask to support strength, muscular endurance, long climbs, and objective-like work.'
)
