from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MicroCard,
    TrainingLevel,
)

mainstream_aerobic_progression_week = MicroCard(
    id = 'micro_010',
    slug = 'mainstream-aerobic-progression-week',
    title = 'Aerobic Progression Week',
    card_type = CardType.MICRO,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A mainstream week that adds one aerobic load variable while keeping the rest stable.',
    purpose = 'Create a reviewable aerobic overload without blurring the dose through multiple simultaneous progressions.',
    tags = [
        'mainstream_endurance',
        'aerobic',
        'progression',
        'load_management'
    ],
    goal_race_context = [
        'Use inside a progressive aerobic development block.',
        'Appropriate when the previous week was absorbed and easy running is stable.',
        'Useful for runners building frequency, volume, long-run tolerance, or modest vertical gain.'
    ],
    expected_adaptations = [
        'Improved tolerance for repeatable aerobic training.',
        'Better confidence with a slightly larger weekly dose.',
        'Clearer feedback about the athlete response to one changed variable.'
    ],
    progression_rules = [
        'Repeat the week or progress only if the whole week remains recoverable.',
        'Progress duration, frequency, or vertical gain, not all three together.',
        'Keep quality work minimal until the aerobic progression is stable.'
    ],
    regression_rules = [
        'Return to the previous successful load if easy effort rises across the week.',
        'Flatten or simplify terrain before removing the main aerobic purpose.',
        'Replace the added run with low-impact aerobic work only when running tolerance is the limiter.'
    ],
    references = [
        CardReference(
            card_id = 'mezzo_010',
            relationship = CardRelationship.PARENT,
            tags = [
                'core_week'
            ]
        ),
        CardReference(
            card_id = 'session_016',
            relationship = CardRelationship.CHILD,
            tags = [
                'core_session'
            ]
        ),
        CardReference(
            card_id = 'session_017',
            relationship = CardRelationship.CHILD,
            tags = [
                'key_session'
            ]
        ),
        CardReference(
            card_id = 'session_015',
            relationship = CardRelationship.SUPPORT,
            tags = [
                'monitoring'
            ]
        )
    ],
    recommended_duration_days = '7',
    week_structure = [
        'Several easy aerobic runs.',
        'One modest progression target such as a longer run, added easy frequency, or controlled vertical gain.',
        'Optional short relaxed strides only if they do not change the recovery cost.',
        'At least one lower-load day after the longest or most terrain-costly run.'
    ],
    key_sessions = [
        'Easy Aerobic Run',
        'Progressive Endurance Long Run'
    ],
    load_pattern = 'Small building week with one visible progression variable.',
    placement_guidance = [
        'Use after a stable week, not after a week that already required compensation.',
        'Place before a consolidation week if two or three building weeks have accumulated fatigue.'
    ],
    recovery_requirements = [
        'Easy days must feel conversational and mechanically normal.',
        'Do not add quality if the progression variable already creates enough training stress.',
        'Review soreness and easy effort two days after the longest run.'
    ],
    training_profile = [
        'Low-intensity majority.',
        'One deliberate aerobic overload.',
        'Stable terrain or stable duration around the progression target.',
        'Trail load tracked through time, vertical gain, technicality, and descent cost.'
    ],
    watchouts = [
        'Progressing several variables because each looks small alone.',
        'Letting a longer run become a steady or threshold effort.',
        'Using technical terrain that changes the intended dose.',
        'Ignoring delayed soreness after downhill-heavy routes.'
    ],
    additional_information = 'This week is mainstream progression made concrete. The coach should be able to say exactly what changed and what stayed controlled. If the runner finishes the week with normal easy effort, stable soreness, and no need to protect later sessions, the progression was probably useful. If not, the lesson is not failure; it is dose information for the next week.'
)
