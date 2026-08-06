from training_cards.schemas import CardRelationship, CardReference, CardType, SessionCard, SessionPart, TrainingLevel

steady_run = SessionCard(
    id = 'session_005',
    slug = 'steady-run',
    title = 'Steady Run',
    card_type = CardType.SESSION,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    summary = 'A controlled aerobic run slightly stronger than easy effort.',
    purpose = 'Build aerobic stamina without the cost of a true threshold workout.',
    tags = [
        'steady',
        'aerobic',
        'stamina'
    ],
    goal_race_context = [
        'Useful in base, build, or race-specific phases when controlled stamina is needed.',
        'When the athlete needs a moderate aerobic stimulus.',
        'When full threshold work is not needed.'
    ],
    expected_adaptations = [
        'Aerobic stamina.',
        'Effort control.'
    ],
    progression_rules = [
        'Extend duration before increasing effort.'
    ],
    regression_rules = [
        'Convert to easy run if fatigue is present.'
    ],
    references = [
        CardReference(
            card_id = 'micro_002',
            relationship = CardRelationship.PARENT,
            tags = [
                'option'
            ]
        )
    ],
    session_family = 'steady',
    typical_duration = '30-90 minutes',
    workout_parts = [
        SessionPart(
            name = 'Warm-Up',
            duration = '10-20 min',
            rpe = '2-3',
            instructions = 'Start easy.'
        ),
        SessionPart(
            name = 'Steady Aerobic Running',
            duration = '20-60 min',
            rpe = '5-6',
            instructions = 'Stay controlled and below threshold.',
            terrain_notes = 'On rolling trails, judge by breathing and effort rather than pace.'
        ),
        SessionPart(
            name = 'Cool Down',
            duration = '5-15 min',
            rpe = '2-3',
            instructions = 'Return to easy running.'
        )
    ],
    training_profile = [
        'Sustained controlled effort.',
        'Lower cost than threshold.',
        'Choose terrain where effort stays stable.'
    ],
    watchouts = [
        'Do not use too often if it crowds out easy recovery.',
        'Letting steady become hard.',
        'Doing too many moderate days.',
        'Easy days become stale.',
        'Steady pace drifts into strain.'
    ],
    additional_information = """Steady running can be useful, but it is easy to overuse. It should be clearly controlled and not replace easy volume. Trail runners can use effort on rolling terrain, but should avoid letting climbs push the session into threshold.

Intensity guidance: Moderate but controlled.; Below threshold.

Execution notes: Keep the session repeatable.

Recovery requirements: Usually modest if controlled."""
)
