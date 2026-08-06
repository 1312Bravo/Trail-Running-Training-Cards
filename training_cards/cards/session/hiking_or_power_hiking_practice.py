from training_cards.schemas import CardRelationship, CardReference, CardType, SessionCard, SessionPart, TrainingLevel

hiking_or_power_hiking_practice = SessionCard(
    id = 'session_013',
    slug = 'hiking-or-power-hiking-practice',
    title = 'Hiking Or Power-Hiking Practice',
    card_type = CardType.SESSION,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    summary = 'A specific session for practicing efficient hiking when running is not always the best choice.',
    purpose = 'Improve uphill efficiency, pacing, and transitions between running and hiking.',
    tags = [
        'hiking',
        'power_hiking',
        'trail_specific',
        'climbing'
    ],
    goal_race_context = [
        'Useful for hilly, mountain, or long events where hiking may be efficient.',
        'When climbs are part of the goal demands.',
        'When running every climb creates excessive cost.'
    ],
    expected_adaptations = [
        'Improved uphill efficiency.',
        'Better pacing decisions.',
        'Smoother run-hike transitions.'
    ],
    progression_rules = [
        'Progress duration or climbing load gradually.'
    ],
    regression_rules = [
        'Reduce grade, duration, or pack load.'
    ],
    references = [
        CardReference(
            card_id = 'micro_006',
            relationship = CardRelationship.PARENT,
            tags = [
                'trail_option'
            ]
        ),
        CardReference(
            card_id = 'micro_008',
            relationship = CardRelationship.PARENT,
            tags = [
                'trail_option'
            ]
        )
    ],
    session_family = 'trail_specific',
    typical_duration = '20-90 minutes within a run or hike-run session',
    workout_parts = [
        SessionPart(
            name = 'Easy Approach',
            duration = '10-20 min',
            rpe = '2-4',
            instructions = 'Warm up with easy running or hiking.'
        ),
        SessionPart(
            name = 'Hiking Or Power-Hiking Practice',
            duration = '10-60 min total',
            rpe = '4-7',
            instructions = 'Practice efficient posture, cadence, and sustainable effort.',
            terrain_notes = 'Use climbs that fit the athlete and goal; do not chase an exact gradient.'
        ),
        SessionPart(
            name = 'Run-Hike Transitions',
            duration = 'Optional short repeats',
            rpe = '4-6',
            instructions = 'Practice shifting smoothly between running and hiking.'
        ),
        SessionPart(
            name = 'Easy Finish',
            duration = '10-15 min',
            rpe = '2-3',
            instructions = 'Finish relaxed.'
        )
    ],
    training_profile = [
        'Sustained hiking or run-hike intervals.',
        'Controlled aerobic effort.',
        'Technique focus.',
        'Climb or incline required.',
        'Grade should match the athlete, not an arbitrary number.'
    ],
    watchouts = [
        'Do not use if the goal has no relevant climbing demand unless general low-impact aerobic work is desired.',
        'Hiking too hard.',
        'Waiting until race day to practice transitions.',
        'Calf or hip flexor irritation.',
        'Effort becomes too high.'
    ],
    additional_information = """This is a running-support session, especially useful when the goal includes climbs where hiking may be efficient. It should not be treated as a failure to run. For mountain runners, the skill is deciding when to hike, how hard to hike, and how to resume running smoothly.

Intensity guidance: Easy to steady.; Keep effort sustainable.

Execution notes: Practice smooth transitions and posture.

Recovery requirements: Watch calf, hip, and foot response."""
)
