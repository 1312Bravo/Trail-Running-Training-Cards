from training_cards.schemas import CardRelationship, CardReference, CardType, MicroCard, TrainingLevel

volume_progression_week = MicroCard(
    id = 'micro_003',
    slug = 'volume-progression-week',
    title = 'Volume Progression Week',
    card_type = CardType.MICRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    summary = 'A week that increases aerobic load through frequency, duration, or long-run extension.',
    purpose = 'Build capacity by progressing easy volume while keeping intensity controlled.',
    tags = [
        'volume',
        'progression',
        'aerobic'
    ],
    goal_race_context = [
        'Useful during base and endurance-focused blocks.',
        'When the previous load was tolerated.',
        'When aerobic capacity is a limiter.'
    ],
    expected_adaptations = [
        'Improved volume tolerance.',
        'Better aerobic durability.',
        'More confidence with routine training.'
    ],
    progression_rules = [
        'Progress one load variable at a time.',
        'Use recovery week after repeated building weeks.'
    ],
    regression_rules = [
        'Hold volume steady or reduce terrain stress first.'
    ],
    references = [
        CardReference(
            card_id = 'mezzo_001',
            relationship = CardRelationship.PARENT,
            tags = [
                'core_week'
            ]
        ),
        CardReference(
            card_id = 'mezzo_002',
            relationship = CardRelationship.PARENT,
            tags = [
                'core_week'
            ]
        ),
        CardReference(
            card_id = 'session_001',
            relationship = CardRelationship.CHILD,
            tags = [
                'core_session'
            ]
        ),
        CardReference(
            card_id = 'session_003',
            relationship = CardRelationship.CHILD,
            tags = [
                'key_session'
            ]
        )
    ],
    recommended_duration_days = '7',
    week_structure = [
        'Easy runs across the week.',
        'One longer endurance session.',
        'No more than one light quality touch.'
    ],
    key_sessions = [
        'Easy Run',
        'Long Run'
    ],
    load_pattern = 'Building load.',
    placement_guidance = [
        'Use after a stable week, not after a fatigue spike.'
    ],
    training_profile = [
        'Mostly easy running.',
        'One longer run or added easy frequency.',
        'Minimal intensity.',
        'Keep terrain controlled.',
        'Trail runners should progress vertical gain gradually.'
    ],
    watchouts = [
        'Do not use after a week that already created excessive fatigue.',
        'Do not use during pain or unstable recovery.',
        'Adding too much load in multiple ways.',
        'Making long runs too hard.',
        'Lingering soreness.',
        'Easy runs become labored.'
    ],
    additional_information = """Use this week when the athlete is ready for more aerobic load. The progression should be boring and repeatable. For trail runners, do not increase duration, vertical gain, and technical difficulty all at once.

Recovery requirements: Easy days must stay easy enough to support the progression."""
)
