from training_cards.schemas import CardRelationship, CardReference, CardType, MicroCard, TrainingLevel

strength_support_week = MicroCard(
    id = 'micro_004',
    slug = 'strength-support-week',
    title = 'Strength Support Week',
    card_type = CardType.MICRO,
    suitable_levels = [
        TrainingLevel.INTERMEDIATE,
        TrainingLevel.ADVANCED,
        TrainingLevel.ELITE
    ],
    summary = 'A week that includes running-specific strength support without overwhelming run quality.',
    purpose = 'Improve force support, durability, and form under fatigue.',
    tags = [
        'strength',
        'support',
        'durability'
    ],
    goal_race_context = [
        'Useful when strength, hills, or late-run form are limiters.',
        'When base load is stable.',
        'When the athlete tolerates strength work without soreness dominating running.'
    ],
    expected_adaptations = [
        'Improved strength support.',
        'Better durability.',
        'Reduced form breakdown under fatigue.'
    ],
    progression_rules = [
        'Progress repetitions or duration before intensity.',
        'Keep the next day easy.'
    ],
    regression_rules = [
        'Reduce hill or gym load if soreness changes running mechanics.'
    ],
    references = [
        CardReference(
            card_id = 'mezzo_003',
            relationship = CardRelationship.PARENT,
            tags = [
                'core_week'
            ]
        ),
        CardReference(
            card_id = 'session_010',
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
        'One strength-focused key session.',
        'Easy running before and after.',
        'Optional light strength support.'
    ],
    key_sessions = [
        'Strength Endurance Hills',
        'Easy Run'
    ],
    load_pattern = 'Moderate muscular load.',
    placement_guidance = [
        'Use in build phases or before more specific terrain work.'
    ],
    training_profile = [
        'One strength-endurance run or hill session.',
        'Optional gym strength.',
        'Easy running around key stress.',
        'Use hills only as needed.',
        'Limit hard descents when strength soreness is present.'
    ],
    watchouts = [
        'Do not use during tendon or muscle irritation.',
        'Do not combine with sudden volume jumps.',
        'Making strength and running both maximal.',
        'Ignoring soreness from eccentric work.',
        'Calf, Achilles, knee, or hamstring soreness increases.',
        'Running mechanics feel guarded.'
    ],
    additional_information = """This week pairs easy running with one or two strength-oriented stresses. That may be hill work, gym strength, or controlled muscular endurance depending on the athlete. Trail runners should watch total eccentric load because strength work plus downhill running can stack quickly.

Recovery requirements: At least one easy day after the key strength stress."""
)
