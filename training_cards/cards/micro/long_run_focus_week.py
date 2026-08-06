from training_cards.schemas import CardRelationship, CardReference, CardType, MicroCard, TrainingLevel

long_run_focus_week = MicroCard(
    id = 'micro_006',
    slug = 'long-run-focus-week',
    title = 'Long Run Focus Week',
    card_type = CardType.MICRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    summary = 'A week where the long run is the main training stress.',
    purpose = 'Develop endurance, pacing, fueling, and late-session durability.',
    tags = [
        'long_run',
        'endurance',
        'fueling'
    ],
    goal_race_context = [
        'Useful for endurance-focused goals and long-race preparation.',
        'When the athlete can recover from longer efforts.',
        'When endurance or fueling is a limiter.'
    ],
    expected_adaptations = [
        'Improved long-run tolerance.',
        'Better fueling practice.',
        'Improved pacing patience.'
    ],
    progression_rules = [
        'Progress duration or specificity gradually.',
        'Practice fueling before the longest sessions.'
    ],
    regression_rules = [
        'Shorten or simplify the long run if recovery is poor.'
    ],
    references = [
        CardReference(
            card_id = 'mezzo_002',
            relationship = CardRelationship.PARENT,
            tags = [
                'core_week'
            ]
        ),
        CardReference(
            card_id = 'mezzo_006',
            relationship = CardRelationship.PARENT,
            tags = [
                'core_week'
            ]
        ),
        CardReference(
            card_id = 'mezzo_008',
            relationship = CardRelationship.PARENT,
            tags = [
                'practice_context'
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
        'Easy running early.',
        'Long run as main stress.',
        'Recovery afterward.'
    ],
    key_sessions = [
        'Long Run'
    ],
    load_pattern = 'Long-run centered load.',
    placement_guidance = [
        'Use when the long run is the highest-priority adaptation.'
    ],
    training_profile = [
        'One main long run.',
        'Easy support runs.',
        'Optional short light workout only if recovery is stable.',
        'Choose terrain that matches the intended stress.',
        'Trail runners should progress vertical and downhill load gradually.'
    ],
    watchouts = [
        'Do not use if the previous long run was not absorbed.',
        "Do not pair with too much intensity for the athlete's level.",
        'Racing the long run.',
        'Ignoring fueling.',
        'Adding technical stress without recovery margin.',
        'Long-run fatigue dominates the week.',
        'Downhill soreness persists.'
    ],
    additional_information = """This week places the long run at the center. Other sessions should support that goal rather than compete with it. For trail runners, the long run may be defined by time, vertical gain, surface, or effort pattern instead of distance alone.

Recovery requirements: Protect recovery after the long run."""
)
