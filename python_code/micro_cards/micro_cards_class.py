class MicroCard:
    def __init__(
            self,
            title: str = "N/A",
            card_id: int = 0,
            parent_mezzo: str | None = None,
            tags: list | None = None,
            session_type: str | None = None,
            duration: str | None = None,
            intensity: str | None = None,
            main_focus: list | None = None,
            key_workouts: list | None = None,
            guidance: list | None = None,
            expected_fatigue: str | None = None,
            notes: list | None = None
    ):

        self.title = title
        self.card_id = card_id
        self.parent_mezzo = parent_mezzo if parent_mezzo is not None else "N/A"
        self.tags = tags if tags is not None else ["N/A"]
        self.session_type = session_type if session_type is not None else "N/A"
        self.duration = duration if duration is not None else "N/A"
        self.intensity = intensity if intensity is not None else "N/A"
        self.main_focus = main_focus if main_focus is not None else ["N/A"]
        self.key_workouts = key_workouts if key_workouts is not None else ["N/A"]
        self.guidance = guidance if guidance is not None else ["N/A"]
        self.expected_fatigue = expected_fatigue if expected_fatigue is not None else "N/A"
        self.notes = notes if notes is not None else ["N/A"]

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"\nCard ID: {self.card_id}")
        print(f"\nParent Mezzo: {self.parent_mezzo}")
        print(f"\nTags:\n- {'\n- '.join(self.tags)}")
        print(f"\nSession Type: {self.session_type}")
        print(f"\nDuration: {self.duration}")
        print(f"\nIntensity: {self.intensity}")
        print(f"\nMain Focus:\n- {'\n- '.join(self.main_focus)}")
        print(f"\nKey Workouts:\n- {'\n- '.join(self.key_workouts)}")
        print(f"\nGuidance:\n- {'\n- '.join(self.guidance)}")
        print(f"\nExpected Fatigue: {self.expected_fatigue}")
        print(f"\nNotes:\n- {'\n- '.join(self.notes)}")