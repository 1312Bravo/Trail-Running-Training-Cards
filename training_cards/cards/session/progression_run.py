from training_cards.schemas import CardRelationship, CardReference, CardType, SessionCard, SessionPart, TrainingLevel

progression_run = SessionCard(
    id = 'session_004',
    slug = 'progression-run',
    title = 'Progression Run',
    card_type = CardType.SESSION,
    suitable_levels = [
        TrainingLevel.INTERMEDIATE,
        TrainingLevel.ADVANCED,
        TrainingLevel.ELITE
    ],
    summary = 'A run that starts easy and finishes stronger while staying controlled.',
    purpose = 'Practice controlled effort change without turning the session into a race.',
    tags = [
        'progression',
        'pacing',
        'control'
    ],
    goal_race_context = [
        'Useful for athletes who struggle with pacing or late-run control.',
        'When a light quality stimulus is useful.',
        'When threshold work would be too much.'
    ],
    expected_adaptations = [
        'Pacing discipline.',
        'Smooth effort control.',
        'Light stamina stimulus.'
    ],
    progression_rules = [
        'Extend the steady finish gradually.'
    ],
    regression_rules = [
        'Keep the whole run easy if control is poor.'
    ],
    references = [
        CardReference(
            card_id = 'micro_005',
            relationship = CardRelationship.PARENT,
            tags = [
                'light_quality'
            ]
        )
    ],
    session_family = 'controlled_quality',
    typical_duration = '30-90 minutes',
    workout_parts = [
        SessionPart(
            name = 'Easy Start',
            duration = '10-25 min',
            rpe = '2-4',
            instructions = 'Begin clearly easier than the final effort.'
        ),
        SessionPart(
            name = 'Gradual Build',
            duration = '15-50 min',
            rpe = '4-6',
            instructions = 'Progress smoothly; effort should rise in steps, not jump.'
        ),
        SessionPart(
            name = 'Controlled Finish',
            duration = '5-15 min',
            rpe = '6-7',
            instructions = 'Finish strong but not all-out.'
        ),
        SessionPart(
            name = 'Cool Down',
            duration = '5-10 min',
            rpe = '2-3',
            instructions = 'Jog easily until breathing settles.'
        )
    ],
    training_profile = [
        'Easy start.',
        'Gradual controlled finish.',
        'No sprint finish.',
        'Use terrain that allows controlled effort.'
    ],
    watchouts = [
        'Do not use when easy running already feels hard.',
        'Starting too fast.',
        'Finishing like a race.',
        'Effort jumps abruptly.',
        'Recovery cost feels like a hard workout.'
    ],
    additional_information = """Progression runs teach patience and pacing. The athlete should finish strong but not emptied. For trail runners, progression may be effort-based rather than pace-based, especially on rolling or climbing routes.

Intensity guidance: Easy to moderate/steady.; Finish controlled.

Execution notes: The last part should feel focused, not desperate.

Recovery requirements: Usually moderate-low if controlled."""
)
