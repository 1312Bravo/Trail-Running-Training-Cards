from .micro_cards_class import MicroCard

micro_race_taper_race_pace = MicroCard(
    title="Race Taper - Race Pace Session",
    card_id=8001,
    parent_mezzo="Race Preparation & Taper",
    tags=["Race Pace", "Sharpening"],
    session_type="Race Pace Intervals",
    duration="20-30 min",
    intensity="Race Pace",
    main_focus=[
        "Maintain race-specific intensity",
        "Sharpen neuromuscular readiness"
    ],
    key_workouts=[
        "2x10-15 min race pace intervals with full recovery"
    ],
    guidance=[
        "Keep effort controlled and precise",
        "Do not exceed planned race pace"
    ],
    expected_fatigue="Low to Moderate",
    notes=[
        "Include warmup and cooldown",
        "Focus on form and relaxation"
    ]
)

micro_race_taper_sharpening = MicroCard(
    title="Race Taper - Short Sharpening Intervals",
    card_id=8002,
    parent_mezzo="Race Preparation & Taper",
    tags=["Sharpening", "Neuromuscular"],
    session_type="Short Intervals",
    duration="20-35 min",
    intensity="High, short efforts",
    main_focus=[
        "Activate fast-twitch fibers",
        "Improve leg turnover and race readiness"
    ],
    key_workouts=[
        "6x1 min sharp efforts with full recovery"
    ],
    guidance=[
        "Focus on crisp technique",
        "Keep rest complete between efforts"
    ],
    expected_fatigue="Low",
    notes=[
        "Include warmup and cooldown",
        "Avoid long continuous effort"
    ]
)

micro_race_taper_easy = MicroCard(
    title="Race Taper - Easy Aerobic",
    card_id=8003,
    parent_mezzo="Race Preparation & Taper",
    tags=["Aerobic", "Easy"],
    session_type="Easy Aerobic",
    duration="30-45 min",
    intensity="Low aerobic",
    main_focus=[
        "Promote recovery",
        "Maintain aerobic rhythm"
    ],
    key_workouts=[
        "Continuous easy pace"
    ],
    guidance=[
        "Keep effort very light",
        "Focus on smooth movement and relaxed breathing"
    ],
    expected_fatigue="Very Low",
    notes=[
        "Optional light mobility exercises"
    ]
)

micro_race_taper_rest = MicroCard(
    title="Race Taper - Recovery / Rest",
    card_id=8004,
    parent_mezzo="Race Preparation & Taper",
    tags=["Recovery", "Rest"],
    session_type="Rest",
    duration=None,
    intensity=None,
    main_focus=[
        "Allow body to recover and consolidate adaptations",
        "Maximize freshness for upcoming race"
    ],
    key_workouts=[
        "Optional gentle walk or light mobility"
    ],
    guidance=[
        "Do not perform structured training",
        "Focus on sleep, nutrition, and mental preparation"
    ],
    expected_fatigue="None",
    notes=[
        "Mental preparation for race day",
        "Keep activity very easy if moving"
    ]
)

RACE_TAPER_MICRO_LIBRARY = [
    micro_race_taper_race_pace,
    micro_race_taper_sharpening,
    micro_race_taper_easy,
    micro_race_taper_rest
]