from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardRelationship,
    CardReference,
    CardType,
    MicroCard,
    TrainingLevel,
)

mainstream_quality_and_recovery_week = MicroCard(
    id = 'micro_011',
    slug = 'mainstream-quality-and-recovery-week',
    title = 'Quality And Recovery Week',
    card_type = CardType.MICRO,
    suitable_levels = [
        TrainingLevel.INTERMEDIATE,
        TrainingLevel.ADVANCED,
        TrainingLevel.ELITE
    ],
    philosophy_profile_ids = [
        MAINSTREAM_ENDURANCE
    ],
    summary = 'A mainstream week built around one key quality session and enough recovery to absorb it.',
    purpose = 'Improve a defined intensity capacity without letting hidden moderate work consume the week.',
    tags = [
        'mainstream_endurance',
        'quality',
        'recovery',
        'intensity_control'
    ],
    goal_race_context = [
        'Use inside a controlled quality development block.',
        'Appropriate when the athlete has stable aerobic consistency and can recover from one key workout.',
        'Useful when the target adaptation is threshold control, aerobic power, or controlled faster running.'
    ],
    expected_adaptations = [
        'Improved execution of one purposeful quality stimulus.',
        'Better hard/easy contrast across the week.',
        'Improved recovery discipline after intensity.',
        'Clearer signal about whether the quality dose is appropriate.'
    ],
    progression_rules = [
        'Progress total controlled quality before making the work harder.',
        'Keep the next easy day easy enough to confirm absorption.',
        'Add a second light quality touch only after one-session weeks are consistently recovered.'
    ],
    regression_rules = [
        'Reduce repetitions or duration if mechanics or pacing fade.',
        'Replace quality with steady aerobic work when recovery signs are poor.',
        'Move the session to smoother terrain if technicality prevents controlled execution.'
    ],
    references = [
        CardReference(
            card_id = 'mezzo_011',
            relationship = CardRelationship.PARENT,
            tags = [
                'core_week'
            ]
        ),
        CardReference(
            card_id = 'session_018',
            relationship = CardRelationship.CHILD,
            tags = [
                'key_session'
            ]
        ),
        CardReference(
            card_id = 'session_016',
            relationship = CardRelationship.CHILD,
            tags = [
                'support_session'
            ]
        )
    ],
    recommended_duration_days = '7',
    week_structure = [
        'One key quality session.',
        'Easy aerobic running before and after the key session.',
        'Optional relaxed strides on a separate easy day if the athlete is fresh.',
        'No additional hard downhill, strength, or race-rehearsal stress unless intentionally substituted.'
    ],
    key_sessions = [
        'Controlled Quality Intervals',
        'Easy Aerobic Run'
    ],
    load_pattern = 'One primary intensity stress surrounded by recoverable aerobic support.',
    placement_guidance = [
        'Use after aerobic progression is stable.',
        'Avoid after travel, illness, race effort, or unusually heavy terrain load.',
        'Place the key session where the athlete can arrive ready and recover afterward.'
    ],
    recovery_requirements = [
        'The day after quality should not become hidden steady running.',
        'If the athlete needs multiple compromised days after the workout, the quality dose was too large.',
        'Preserve sleep, fueling, and low-stress days around the session.'
    ],
    training_profile = [
        'One controlled moderate-to-hard workout.',
        'Mostly easy running around the key day.',
        'Quality terrain chosen to make intensity measurable and mechanics stable.',
        'Recovery judged by the next two to three days, not only by workout completion.'
    ],
    watchouts = [
        'Racing the final repetitions.',
        'Letting easy runs become moderately hard because the key workout created confidence.',
        'Adding technical descent after intensity.',
        'Using intensity when the athlete needs aerobic consistency first.'
    ],
    additional_information = 'This week is a mainstream quality-placement template. The quality session matters, but so does the space around it. The athlete should know what capacity is being trained and what signs would show the dose was too high. For trail runners, pace may be replaced by RPE, power, breathing, or controlled uphill effort, but the session should still have a defined intensity target.'
)
