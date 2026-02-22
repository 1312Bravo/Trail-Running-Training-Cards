class MezzoCard:
    def __init__(
            self,
            title: str = "N/A",
            card_id: int = 0,
            parent_macro: str | None = None,
            week_type: str | None = None, 
            tags: list | None = None,
            level: str | None = None,
            volume_target: str | None = None,
            fatigue_risk: str | None = None, 
            focus: list | None = None,
            focus_summary: str | None = None,
            weekly_structure: list | None = None,
            key_sessions: list | None = None,
            intensity_distribution: list | None = None,
            volume_guidance: list | None = None,
            athlete_feel: list | None = None,
            progression_logic: list | None = None,
        ):

        self.title = title
        self.card_id = card_id
        self.parent_macro = parent_macro if parent_macro is not None else "N/A"
        self.week_type = week_type if week_type is not None else "N/A"
        self.tags = tags if tags is not None else ["N/A"]
        self.level = level if level is not None else "N/A"
        self.volume_target = volume_target if volume_target is not None else "N/A"
        self.fatigue_risk = fatigue_risk if fatigue_risk is not None else "N/A"
        self.focus = focus if focus is not None else ["N/A"]
        self.focus_summary = focus_summary if focus_summary is not None else "N/A"
        self.weekly_structure = weekly_structure if weekly_structure is not None else ["N/A"]
        self.key_sessions = key_sessions if key_sessions is not None else ["N/A"]
        self.intensity_distribution = intensity_distribution if intensity_distribution is not None else ["N/A"]
        self.volume_guidance = volume_guidance if volume_guidance is not None else ["N/A"]
        self.athlete_feel = athlete_feel if athlete_feel is not None else ["N/A"]
        self.progression_logic = progression_logic if progression_logic is not None else ["N/A"]

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"\nCard ID: {self.card_id}")
        print(f"\nParent Macro: {self.parent_macro}")
        print(f"Week Type: {self.week_type}")
        print(f"\nTags:\n- {'\n- '.join(self.tags)}")
        print(f"\nLevel: {self.level}")
        print(f"\nVolume Target: {self.volume_target}")
        print(f"Fatigue Risk: {self.fatigue_risk}")
        print(f"\nWeekly Focus:\n- {'\n- '.join(self.focus)}")
        print(f"\nWeekly Structure:\n- {'\n- '.join(self.weekly_structure)}")
        print(f"\nKey Sessions:\n- {'\n- '.join(self.key_sessions)}")
        print(f"\nIntensity Distribution:\n- {'\n- '.join(self.intensity_distribution)}")
        print(f"\nVolume Guidance:\n- {'\n- '.join(self.volume_guidance)}")
        print(f"\nAthlete Experience:\n- {'\n- '.join(self.athlete_feel)}")
        print(f"\nProgression Logic:\n- {'\n- '.join(self.progression_logic)}")

    def display_preview(self):
        print(f"{self.title}")
        print(f"Level: {self.level}")
        print(f"Week Type: {self.week_type}")
        print(f"Key Focus: {self.focus_summary}")