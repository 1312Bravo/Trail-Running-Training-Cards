from training_cards.schemas import CardRelationship, CardReference, CardType, MicroCard, TrainingLevel

race_practice_week = MicroCard(
    id = 'micro_008',
    slug = 'race-practice-week',
    title = 'Race Practice Week',
    card_type = CardType.MICRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    summary = 'A week that rehearses important race demands while keeping total stress controlled.',
    purpose = 'Practice execution, pacing, fueling, gear, and specific effort without over-racing training.',
    tags = [
        'race_practice',
        'specificity',
        'execution'
    ],
    goal_race_context = [
        'Useful in the specific preparation phase before an important event.',
        'When the athlete is close enough to the race for specificity to matter.',
        'When practical execution needs rehearsal.'
    ],
    expected_adaptations = [
        'Improved race execution.',
        'Better confidence with goal demands.',
        'Improved fueling and pacing decisions.'
    ],
    progression_rules = [
        'Progress from simple practice to more specific rehearsal.',
        'Keep final rehearsals confidence-building.'
    ],
    regression_rules = [
        'Simplify practice if execution quality drops.'
    ],
    references = [
        CardReference(
            card_id = 'mezzo_007',
            relationship = CardRelationship.PARENT,
            tags = [
                'core_week'
            ]
        ),
        CardReference(
            card_id = 'session_012',
            relationship = CardRelationship.CHILD,
            tags = [
                'key_session'
            ]
        ),
        CardReference(
            card_id = 'session_003',
            relationship = CardRelationship.CHILD,
            tags = [
                'option'
            ]
        )
    ],
    recommended_duration_days = '7',
    week_structure = [
        'Easy support running.',
        'One specific practice session.',
        'Recovery afterward.'
    ],
    key_sessions = [
        'Race Simulation Run',
        'Long Run'
    ],
    load_pattern = 'Specific but controlled load.',
    placement_guidance = [
        'Use before taper, not as a last-minute test.'
    ],
    training_profile = [
        'One race-practice session.',
        'Easy support running.',
        'Reduced extra intensity.',
        'Match the important race demands broadly.',
        'Avoid copying every course detail if it adds needless stress.'
    ],
    watchouts = [
        'Do not use every week.',
        'Do not use when fatigue is already high.',
        'Turning practice into a race.',
        'Testing too many new things at once.',
        'Practice session leaves excessive fatigue.',
        'Specific terrain causes unusual soreness.'
    ],
    additional_information = """This week should reveal practical race-day issues before they matter. It may include a race simulation run, fueling practice, or goal-effort segments. For trail runners, the practice can include climbing, descending, hiking transitions, gear, poles, pack setup, or technical pacing.

Recovery requirements: Specific session should be absorbed before the next hard week."""
)
