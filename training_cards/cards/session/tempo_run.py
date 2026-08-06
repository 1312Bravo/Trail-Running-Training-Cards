from training_cards.schemas import CardRelationship, CardReference, CardType, SessionCard, SessionPart, TrainingLevel

tempo_run = SessionCard(
    id = 'session_006',
    slug = 'tempo-run',
    title = 'Tempo Run',
    card_type = CardType.SESSION,
    suitable_levels = [
        TrainingLevel.INTERMEDIATE,
        TrainingLevel.ADVANCED,
        TrainingLevel.ELITE
    ],
    summary = 'A sustained comfortably hard run used for stamina and threshold support.',
    purpose = 'Develop controlled sustained effort without requiring interval structure.',
    tags = [
        'tempo',
        'threshold_support',
        'stamina'
    ],
    goal_race_context = [
        'Useful for goals requiring sustained strong effort.',
        'When the athlete can pace controlled hard efforts.',
        'During threshold or race-specific work.'
    ],
    expected_adaptations = [
        'Improved stamina.',
        'Better effort control.',
        'Threshold support.'
    ],
    progression_rules = [
        'Increase duration before intensity.'
    ],
    regression_rules = [
        'Use shorter threshold intervals instead.'
    ],
    references = [
        CardReference(
            card_id = 'micro_005',
            relationship = CardRelationship.PARENT,
            tags = [
                'option'
            ]
        )
    ],
    session_family = 'threshold',
    typical_duration = '20-60 minutes of quality work, adjusted by level',
    workout_parts = [
        SessionPart(
            name = 'Warm-Up',
            duration = '10-20 min',
            rpe = '2-4',
            instructions = 'Run easy, then add a few short pickups if useful.'
        ),
        SessionPart(
            name = 'Tempo Segment',
            duration = '15-45 min',
            rpe = '6-7',
            instructions = 'Hold comfortably hard, controlled effort; avoid time-trial intensity.',
            terrain_notes = 'Use smoother terrain or sustained climbs if pace is unreliable.'
        ),
        SessionPart(
            name = 'Cool Down',
            duration = '10-15 min',
            rpe = '2-3',
            instructions = 'Jog easily.'
        )
    ],
    training_profile = [
        'Sustained controlled hard segment.',
        'Warm-up and cool-down included.',
        'Use terrain that supports rhythm.',
        'Trail runners may use climbs but should control effort.'
    ],
    watchouts = [
        'Do not use when pacing discipline is poor or fatigue is high.',
        'Running too hard.',
        'Choosing technical terrain that breaks rhythm.',
        'Unable to sustain control.',
        'Excessive recovery cost.'
    ],
    additional_information = """Tempo runs are useful when the athlete can control effort well. They should not become maximal time trials. For trail runners, tempo may be best done on smoother terrain or sustained climbs where effort can stay consistent.

Intensity guidance: Comfortably hard.; Controlled and sustainable.

Execution notes: Finish with the sense that one more small segment would be possible.

Recovery requirements: Plan easy running afterward."""
)
