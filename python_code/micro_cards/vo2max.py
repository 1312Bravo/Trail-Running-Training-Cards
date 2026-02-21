from .micro_cards_class import MicroCard

micro_vo2max_intervals = MicroCard(
    title="VO₂max - Interval Session",
    card_id=8201,
    parent_mezzo="VO₂max Development",
    tags=["VO₂max", "High Intensity", "Aerobic"],
    session_type="VO₂max Intervals",
    duration="35-55 min",
    intensity="High / VO₂max",
    main_focus=[
        "Increase maximal oxygen uptake",
        "Enhance high-intensity endurance and cardiovascular power"
    ],
    key_workouts=[
        "6-8x3-5 min at VO₂max intensity with full recovery"
    ],
    guidance=[
        "Maintain precise VO₂max effort",
        "Do not overreach beyond planned intensity"
    ],
    expected_fatigue="High",
    notes=[
        "Include 10-15 min warmup and cooldown",
        "Focus on smooth, controlled intervals"
    ]
)

micro_vo2max_tempo = MicroCard(
    title="VO₂max - Tempo / Upper Aerobic",
    card_id=8202,
    parent_mezzo="VO₂max Development",
    tags=["Tempo", "Aerobic", "Bridge"],
    session_type="Tempo / Upper Aerobic",
    duration="30-50 min",
    intensity="Moderate-High aerobic / Tempo",
    main_focus=[
        "Bridge aerobic base with VO₂max work",
        "Prepare for high-intensity intervals"
    ],
    key_workouts=[
        "2x12-15 min steady tempo segments with short recovery"
    ],
    guidance=[
        "Keep tempo effort controlled and smooth",
        "Focus on consistent pacing"
    ],
    expected_fatigue="Moderate",
    notes=[
        "Include warmup and cooldown",
        "Tempo sessions should feel comfortably hard but sustainable"
    ]
)

micro_vo2max_recovery = MicroCard(
    title="VO₂max - Moderate / Recovery Aerobic",
    card_id=8203,
    parent_mezzo="VO₂max Development",
    tags=["Recovery", "Aerobic", "Moderate"],
    session_type="Moderate / Recovery Aerobic",
    duration="30-50 min",
    intensity="Low to Moderate aerobic",
    main_focus=[
        "Promote recovery between high-intensity VO₂max sessions",
        "Maintain aerobic rhythm and volume"
    ],
    key_workouts=[
        "Continuous low-moderate pace"
    ],
    guidance=[
        "Keep effort below VO₂max intensity",
        "Focus on smooth, relaxed movement"
    ],
    expected_fatigue="Low",
    notes=[
        "Optional light mobility after session"
    ]
)

micro_vo2max_long = MicroCard(
    title="VO₂max - Long Aerobic Maintenance",
    card_id=8204,
    parent_mezzo="VO₂max Development",
    tags=["Aerobic", "Endurance", "Long"],
    session_type="Long Duration Aerobic",
    duration="80-120 min",
    intensity="Low-moderate aerobic",
    main_focus=[
        "Maintain endurance base",
        "Support recovery and volume around VO₂max intervals"
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

micro_vo2max_rest = MicroCard(
    title="VO₂max - Recovery / Rest",
    card_id=8205,
    parent_mezzo="VO₂max Development",
    tags=["Recovery", "Rest"],
    session_type="Rest",
    duration=None,
    intensity=None,
    main_focus=[
        "Allow adaptation to high-intensity VO₂max work",
        "Maximize freshness for next sessions"
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
        "Essential for consolidating VO₂max adaptations"
    ]
)

VO2MAX_MICRO_LIBRARY = [
    micro_vo2max_intervals,
    micro_vo2max_tempo,
    micro_vo2max_recovery,
    micro_vo2max_long,
    micro_vo2max_rest
]