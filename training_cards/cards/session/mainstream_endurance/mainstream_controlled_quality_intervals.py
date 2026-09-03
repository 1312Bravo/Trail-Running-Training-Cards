from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    SessionCard,
    SessionPart,
    TrainingLevel,
)
from training_cards.session_families import THRESHOLD_SESSION_FAMILY

mainstream_controlled_quality_intervals = SessionCard(
    id = 'session_018',
    slug = 'mainstream-controlled-quality-intervals',
    title = 'Controlled Quality Intervals',
    card_type = CardType.SESSION,
    suitable_levels = [
        TrainingLevel.INTERMEDIATE,
        TrainingLevel.ADVANCED,
        TrainingLevel.ELITE
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A structured interval session for sustainable quality without racing the workout.',
    purpose = 'Develop controlled moderate-to-hard running while preserving mechanics, pacing discipline, and recovery.',
    tags = [
        'mainstream_endurance',
        'quality',
        'threshold',
        'intervals'
    ],
    goal_race_context = [
        'Use when the athlete is ready for one purposeful quality session in the week.',
        'Useful for threshold support, aerobic-power support, or controlled faster running depending on interval length.',
        'Appropriate before race-specific work when the athlete needs general quality development.'
    ],
    expected_adaptations = [
        'Improved sustainable output.',
        'Better pacing control.',
        'Greater confidence with structured intensity.',
        'More reliable recovery from quality work.'
    ],
    progression_rules = [
        'Add total controlled work before increasing pace or reducing recovery.',
        'Stop progression when the final repetition requires straining or mechanics deteriorate.',
        'Use the next easy day as part of the evaluation.'
    ],
    regression_rules = [
        'Reduce repetitions or duration if pace and effort cannot stay controlled.',
        'Extend recovery intervals when form quality is the limiting factor.',
        'Convert to a steady aerobic run if readiness is poor.'
    ],
    references = [
        CardReference(
            card_id = 'micro_011',
            relationship = CardRelationship.PARENT,
            tags = [
                'key_session'
            ]
        )
    ],
    session_family = THRESHOLD_SESSION_FAMILY,
    typical_duration = '45-80 minutes',
    workout_parts = [
        SessionPart(
            name = 'Warm-Up',
            duration = '15-20 min',
            rpe = '2-3',
            instructions = 'Run easily, then add a few relaxed accelerations if they improve rhythm.',
            terrain_notes = 'Choose terrain where effort can be controlled and footing does not dominate the session.'
        ),
        SessionPart(
            name = 'Controlled Intervals',
            duration = '3-6 x 3-8 min',
            rpe = '6-8',
            instructions = 'Run strong but repeatable; recover easily enough that the next repetition starts controlled rather than desperate.',
            terrain_notes = 'Use RPE, breathing, power, or pace according to the reliability of the terrain.'
        ),
        SessionPart(
            name = 'Cool-Down',
            duration = '10-15 min',
            rpe = '1-2',
            instructions = 'Return to easy movement and protect the next day from becoming hidden quality.'
        )
    ],
    training_profile = [
        'Moderate-to-hard structured quality.',
        'Clear work and recovery intervals.',
        'Controlled execution over maximal output.',
        'Surrounding week must include enough easy running and recovery.'
    ],
    watchouts = [
        'Racing the last repetition.',
        'Using technical trail to hide that the target intensity is not controlled.',
        'Shortening recoveries until mechanics collapse.',
        'Adding another hard session before recovery is confirmed.'
    ],
    additional_information = 'This session uses mainstream interval design without claiming one exact zone model. The useful stimulus is controlled quality: hard enough to develop sustainable output, restrained enough to repeat and absorb. Trail runners may execute the session on a smooth climb, road, track, treadmill, or runnable trail depending on which option best preserves the intended effort.'
)
