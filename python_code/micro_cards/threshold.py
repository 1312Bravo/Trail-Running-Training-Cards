from .micro_cards_class import MicroCard

micro_threshold_intervals = MicroCard(
    title="Threshold - Interval Session",
    card_id=8101,
    parent_mezzo="Threshold Development",
    tags=["Threshold", "Intensity", "Aerobic"],
    session_type="Threshold Intervals",
    duration="40-60 min",
    intensity="Threshold / Upper Aerobic",
    main_focus=[
        "Improve sustained high-intensity endurance",
        "Increase lactate tolerance at threshold pace"
    ],
    key_workouts=[
        "4-6x8-12 min at threshold pace with equal recovery"
    ],
    guidance=[
        "Maintain precise threshold intensity",
        "Avoid going above lactate threshold"
    ],
    expected_fatigue="Moderate to High",
    notes=[
        "Include warmup and cooldown",
        "Focus on smooth pacing throughout intervals"
    ]
)

micro_threshold_tempo = MicroCard(
    title="Threshold - Tempo / Upper Aerobic",
    card_id=8102,
    parent_mezzo="Threshold Development",
    tags=["Tempo", "Aerobic", "Sustained"],
    session_type="Tempo / Upper Aerobic",
    duration="30-50 min",
    intensity="Moderate-High aerobic / Tempo",
    main_focus=[
        "Bridge aerobic base and threshold work",
        "Prepare for longer threshold intervals"
    ],
    key_workouts=[
        "2x12-15 min steady tempo segments with short recovery"
    ],
    guidance=[
        "Keep intensity controlled at tempo effort",
        "Focus on consistent form"
    ],
    expected_fatigue="Moderate",
    notes=[
        "Include 5-10 min warmup and cooldown",
        "Tempo sessions should feel comfortably hard"
    ]
)

micro_threshold_recovery = MicroCard(
    title="Threshold - Moderate / Recovery Aerobic",
    card_id=8103,
    parent_mezzo="Threshold Development",
    tags=["Recovery", "Aerobic", "Moderate"],
    session_type="Moderate / Recovery Aerobic",
    duration="30-50 min",
    intensity="Low to Moderate aerobic",
    main_focus=[
        "Promote recovery between high-intensity sessions",
        "Maintain aerobic rhythm and volume"
    ],
    key_workouts=[
        "Continuous low-moderate pace"
    ],
    guidance=[
        "Keep effort below threshold",
        "Focus on smooth, relaxed movement"
    ],
    expected_fatigue="Low",
    notes=[
        "Optional light mobility after session"
    ]
)

micro_threshold_long = MicroCard(
    title="Threshold - Long Aerobic Maintenance",
    card_id=8104,
    parent_mezzo="Threshold Development",
    tags=["Aerobic", "Endurance", "Long"],
    session_type="Long Duration Aerobic",
    duration="80-120 min",
    intensity="Low-moderate aerobic",
    main_focus=[
        "Maintain endurance base",
        "Support fatigue resistance for threshold training"
    ],
    key_workouts=[
        "Continuous long session at low-moderate intensity"
    ],
    guidance=[
        "Keep pace controlled",
        "Focus on fuel management and smooth form"
    ],
    expected_fatigue="Moderate",
    notes=[
        "Include warmup and cooldown",
        "Optional short strides at end"
    ]
)

micro_threshold_rest = MicroCard(
    title="Threshold - Recovery / Rest",
    card_id=8105,
    parent_mezzo="Threshold Development",
    tags=["Recovery", "Rest"],
    session_type="Rest",
    duration=None,
    intensity=None,
    main_focus=[
        "Allow adaptation to high-intensity work",
        "Maximize freshness for next threshold sessions"
    ],
    key_workouts=[
        "Optional gentle mobility or light walk"
    ],
    guidance=[
        "No structured training",
        "Focus on sleep, nutrition, and recovery strategies"
    ],
    expected_fatigue="None",
    notes=[
        "Essential for consolidating threshold adaptations"
    ]
)

THRESHOLD_MICRO_LIBRARY = [
    micro_threshold_intervals,
    micro_threshold_tempo,
    micro_threshold_recovery,
    micro_threshold_long,
    micro_threshold_rest
]