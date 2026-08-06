from training_cards.schemas import CardRelationship, CardReference, CardType, SessionCard, SessionPart, TrainingLevel

long_run = SessionCard(
    id = 'session_003',
    slug = 'long-run',
    title = 'Long Run',
    card_type = CardType.SESSION,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    summary = 'A longer aerobic session that develops endurance, pacing, fueling, and durability.',
    purpose = 'Extend useful endurance while practicing controlled effort over time.',
    tags = [
        'long_run',
        'endurance',
        'fueling'
    ],
    goal_race_context = [
        'Important for events where duration and fatigue resistance matter.',
        'During endurance and race-specific phases.',
        'When the athlete can recover from the planned duration.'
    ],
    expected_adaptations = [
        'Endurance.',
        'Fueling practice.',
        'Late-session durability.'
    ],
    progression_rules = [
        'Increase duration, specificity, or terrain stress gradually.'
    ],
    regression_rules = [
        'Shorten or simplify terrain if recovery suffers.'
    ],
    references = [
        CardReference(
            card_id = 'micro_006',
            relationship = CardRelationship.PARENT,
            tags = [
                'core_session'
            ]
        ),
        CardReference(
            card_id = 'micro_003',
            relationship = CardRelationship.PARENT,
            tags = [
                'option'
            ]
        )
    ],
    session_family = 'endurance',
    typical_duration = '60 minutes to several hours, depending on athlete and goal',
    workout_parts = [
        SessionPart(
            name = 'Warm-Up Into Rhythm',
            duration = '10-20 min',
            rpe = '2-3',
            instructions = 'Start easier than expected and settle into the day.'
        ),
        SessionPart(
            name = 'Main Endurance',
            duration = '45 min to several hours',
            rpe = '3-5',
            instructions = 'Hold sustainable effort and practice fueling when duration makes it relevant.',
            terrain_notes = 'For trail goals, use time, vertical gain, hiking, and descent load as better guides than distance alone.'
        ),
        SessionPart(
            name = 'Controlled Finish',
            duration = '5-15 min',
            rpe = '2-4',
            instructions = 'Finish with stable mechanics; avoid forcing a fast ending unless prescribed.'
        )
    ],
    training_profile = [
        'Longer duration.',
        'Usually easy to steady.',
        'Fueling practice when relevant.',
        'Match terrain to the intended stimulus.',
        'Trail runners may use vertical gain and hiking as part of the session.'
    ],
    watchouts = [
        'Do not extend if the previous long run was not absorbed.',
        'Racing the long run.',
        'Underfueling.',
        'Adding too much downhill stress too soon.',
        'Recovery takes several days.',
        'Mechanics degrade late.'
    ],
    additional_information = """The long run should match the athlete's current capacity and goal context. It is not automatically better because it is longer. For trail runners, time-on-feet, vertical gain, hiking, and downhill load may be more useful than distance alone.

Intensity guidance: Mostly easy to steady.; Avoid frequent race-level effort unless it is a planned simulation.

Execution notes: Practice fueling when duration makes it relevant.; Use effort rather than pace on variable terrain.

Recovery requirements: Plan easier running afterward."""
)
