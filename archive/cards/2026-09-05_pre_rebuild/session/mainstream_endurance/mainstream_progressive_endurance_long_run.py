from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    SessionCard,
    SessionPart,
    TrainingLevel,
)
from training_cards.session_families import ENDURANCE_SESSION_FAMILY

mainstream_progressive_endurance_long_run = SessionCard(
    id = 'session_017',
    slug = 'mainstream-progressive-endurance-long-run',
    title = 'Progressive Endurance Long Run',
    card_type = CardType.SESSION,
    suitable_levels = [
        TrainingLevel.ALL
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A long aerobic run that progresses duration or terrain while keeping intensity controlled.',
    purpose = 'Extend endurance and durability with a clear progression variable and manageable recovery cost.',
    tags = [
        'mainstream_endurance',
        'long_run',
        'endurance',
        'progression'
    ],
    goal_race_context = [
        'Use inside aerobic progression or long-endurance development.',
        'Useful when the athlete needs more duration tolerance before race-specific work.',
        'Appropriate for trail goals when time, vertical gain, hiking, and descent load are deliberately managed.'
    ],
    expected_adaptations = [
        'Improved long-duration aerobic tolerance.',
        'Better pacing restraint over extended running.',
        'More durable mechanics late in a session.',
        'Clearer understanding of how duration or terrain affects recovery.'
    ],
    progression_rules = [
        'Increase duration before adding race-like intensity.',
        'Progress vertical gain or technicality only when duration is already recoverable.',
        'Practise fueling when duration makes it relevant, but do not add fueling complexity as a hidden stress.'
    ],
    regression_rules = [
        'Shorten the run if recovery from the previous long run was poor.',
        'Flatten or simplify the route if terrain cost is the limiting factor.',
        'Use run-walk or hiking when it preserves the intended aerobic stimulus.'
    ],
    references = [
        CardReference(
            card_id = 'micro_010',
            relationship = CardRelationship.PARENT,
            tags = [
                'key_session'
            ]
        )
    ],
    session_family = ENDURANCE_SESSION_FAMILY,
    typical_duration = '60-180 minutes, longer only for prepared athletes and goal demands',
    workout_parts = [
        SessionPart(
            name = 'Easy Start',
            duration = '10-20 min',
            rpe = '2-3',
            instructions = 'Start easier than the planned average so the session does not become a test.'
        ),
        SessionPart(
            name = 'Main Endurance',
            duration = '45-150 min',
            rpe = '3-5',
            instructions = 'Hold sustainable effort and keep the chosen progression variable visible.',
            terrain_notes = 'If the progression is duration, keep terrain familiar. If the progression is terrain, keep duration conservative.'
        ),
        SessionPart(
            name = 'Reviewable Finish',
            duration = '5-10 min',
            rpe = '2-4',
            instructions = 'Finish controlled and note fueling, effort drift, soreness, movement quality, and expected recovery.'
        )
    ],
    training_profile = [
        'Longer aerobic duration.',
        'One planned progression variable.',
        'Mostly easy to steady effort.',
        'Fueling practice when duration or goal demands justify it.',
        'Trail load includes vertical gain, descent, technicality, and time on feet.'
    ],
    watchouts = [
        'Adding a fast finish when the purpose is duration progression.',
        'Increasing distance, vertical gain, technicality, and intensity together.',
        'Treating hiking as failure on terrain where hiking protects the aerobic target.',
        'Ignoring delayed soreness from descent-heavy routes.'
    ],
    additional_information = 'This long run turns mainstream progression into a coachable session. The run should create enough endurance stress to matter, but the coach should still know what caused the stress. If recovery takes longer than expected, the next session should be adjusted instead of defending the original plan.'
)
