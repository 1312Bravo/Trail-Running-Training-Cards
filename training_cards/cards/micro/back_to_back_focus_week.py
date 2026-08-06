from training_cards.schemas import CardRelationship, CardReference, CardType, MicroCard, TrainingLevel

back_to_back_focus_week = MicroCard(
    id = 'micro_007',
    slug = 'back-to-back-focus-week',
    title = 'Back-To-Back Focus Week',
    card_type = CardType.MICRO,
    suitable_levels = [
        TrainingLevel.ADVANCED,
        TrainingLevel.ELITE
    ],
    summary = 'An advanced endurance week using two longer runs close together to practice fatigue management.',
    purpose = 'Build long-duration durability while avoiding a single excessively long session.',
    tags = [
        'back_to_back',
        'advanced',
        'long_endurance'
    ],
    goal_race_context = [
        'Useful for long events or goals where late-fatigue durability is a limiter.',
        'When the athlete already recovers from normal long runs.',
        'When a long goal requires repeated endurance exposure.'
    ],
    expected_adaptations = [
        'Improved fatigue resistance.',
        'Better pacing restraint.',
        'Greater confidence running on tired legs.'
    ],
    progression_rules = [
        'Progress the second day gradually.',
        'Keep both days controlled.'
    ],
    regression_rules = [
        'Return to a normal long-run week if recovery is not reliable.'
    ],
    references = [
        CardReference(
            card_id = 'mezzo_006',
            relationship = CardRelationship.PARENT,
            tags = [
                'advanced_option'
            ]
        ),
        CardReference(
            card_id = 'session_003',
            relationship = CardRelationship.CHILD,
            tags = [
                'key_session'
            ]
        ),
        CardReference(
            card_id = 'session_001',
            relationship = CardRelationship.CHILD,
            tags = [
                'support_session'
            ]
        )
    ],
    recommended_duration_days = '7',
    week_structure = [
        'Easy preparation.',
        'Two longer controlled runs close together.',
        'Recovery afterward.'
    ],
    key_sessions = [
        'Long Run',
        'Easy Run'
    ],
    load_pattern = 'Advanced endurance load.',
    placement_guidance = [
        'Use sparingly in long-endurance preparation.'
    ],
    training_profile = [
        'Two longer easy-to-steady sessions on adjacent or close days.',
        'Low intensity elsewhere.',
        'Fueling practice included.',
        'Keep terrain manageable.',
        'Trail runners should be careful with cumulative downhill load.'
    ],
    watchouts = [
        'Do not use for beginners.',
        'Do not use when injury risk, soreness, or fatigue is already elevated.',
        'Making both days too hard.',
        'Adding intensity in the same week.',
        'Using overly technical terrain when tired.',
        'Second run changes mechanics.',
        'Soreness carries deep into the following week.'
    ],
    additional_information = """Back-to-back weeks are useful but costly. They should be reserved for athletes who already tolerate long runs well. For trail runners, this can simulate multi-hour fatigue, hiking, and descending tolerance without making either day a maximal outing.

Recovery requirements: Several easy days afterward are usually needed."""
)
