from training_cards.schemas import CardRelationship, CardReference, CardType, SessionCard, SessionPart, TrainingLevel

short_hill_repeats = SessionCard(
    id = 'session_009',
    slug = 'short-hill-repeats',
    title = 'Short Hill Repeats',
    card_type = CardType.SESSION,
    suitable_levels = [
        TrainingLevel.INTERMEDIATE,
        TrainingLevel.ADVANCED,
        TrainingLevel.ELITE
    ],
    summary = 'Short uphill efforts used for power, mechanics, and neuromuscular stimulus.',
    purpose = 'Develop strong running mechanics and power with limited total volume.',
    tags = [
        'hills',
        'power',
        'neuromuscular'
    ],
    goal_race_context = [
        'Useful when power, stride quality, or climbing snap is useful.',
        'When the athlete is fresh.',
        'As a support session in build phases.'
    ],
    expected_adaptations = [
        'Improved power.',
        'Better mechanics.',
        'Neuromuscular sharpness.'
    ],
    progression_rules = [
        'Add reps sparingly.',
        'Keep technique crisp.'
    ],
    regression_rules = [
        'Use strides on flat terrain if hill load is too much.'
    ],
    references = [
        CardReference(
            card_id = 'micro_004',
            relationship = CardRelationship.PARENT,
            tags = [
                'option'
            ]
        )
    ],
    session_family = 'hill_power',
    typical_duration = '6-15 short repetitions',
    workout_parts = [
        SessionPart(
            name = 'Warm-Up',
            duration = '15-25 min',
            rpe = '2-4',
            instructions = 'Run easy and prepare calves and hips gradually.'
        ),
        SessionPart(
            name = 'Short Uphill Repeats',
            duration = '8-20 sec each',
            rpe = '8-9',
            instructions = 'Run fast, tall, and relaxed; stop before mechanics fade.',
            terrain_notes = 'Use a safe moderate hill with stable footing.'
        ),
        SessionPart(
            name = 'Walk/Jog Recovery',
            duration = 'Full recovery between reps',
            rpe = '1-2',
            instructions = 'Recover fully; do not rush downhill.'
        ),
        SessionPart(
            name = 'Cool Down',
            duration = '10-15 min',
            rpe = '2-3',
            instructions = 'Jog easily.'
        )
    ],
    training_profile = [
        'Short uphill efforts.',
        'Full or generous recovery.',
        'Low total volume.',
        'Moderate safe hill.',
        'Stable footing.'
    ],
    watchouts = [
        'Do not use with calf, Achilles, or hamstring irritation.',
        'Using too steep a hill.',
        'Too many reps.',
        'Jogging down hard.',
        'Tight calves or Achilles discomfort.',
        'Power drops quickly.'
    ],
    additional_information = """Short hill repeats should be crisp and controlled, not long grinding climbs. They can support speed and strength with less impact than flat sprinting for some athletes. Trail runners should choose safe footing and avoid hard downhill recovery if soreness risk is high.

Intensity guidance: Fast but controlled.; Stop before mechanics degrade.

Execution notes: Walk or jog easily back down.

Recovery requirements: Monitor calf and Achilles response."""
)
