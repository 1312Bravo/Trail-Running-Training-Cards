class MacroCard:
    def __init__(
            self, 
            title: str = "N/A", 
            card_id: int = 0,
            tags: list | None = None,
            level: str | None = None,
            recommended_duration: str | None = None,
            primary_focus: list | None = None, 
            primary_focus_summary: str | None = None,
            adaptations: list | None = None, 
            training_types: list | None = None, 
            expectations: list | None = None, 
            when_to_choose: list | None = None,
            when_to_choose_summary: str | None = None,
            next_mezzo_options: list | None = None,
        ):

        self.title = title
        self.card_id = card_id
        self.tags = tags if tags is not None else ["N/A"]
        self.level = level if level is not None else "N/A"
        self.recommended_duration = recommended_duration if recommended_duration is not None else "N/A"
        self.primary_focus = primary_focus if primary_focus is not None else ["N/A"]
        self.primary_focus_summary = primary_focus_summary if primary_focus_summary is not None else "N/A"
        self.adaptations = adaptations if adaptations is not None else ["N/A"]
        self.training_types = training_types if training_types is not None else ["N/A"]
        self.expectations = expectations if expectations is not None else ["N/A"]
        self.when_to_choose = when_to_choose if when_to_choose is not None else ["N/A"]
        self.when_to_choose_summary = when_to_choose_summary if when_to_choose_summary is not None else "N/A"
        self.next_mezzo_options = next_mezzo_options if next_mezzo_options is not None else ["N/A"]

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"\nCard ID: {self.card_id}")
        print(f"\nTags:\n- {'\n- '.join(self.tags)}")
        print(f"\nLevel: {self.level}")
        print(f"\nRecommended Duration: {self.recommended_duration}")
        print(f"\nPrimary Focus:\n- {'\n- '.join(self.primary_focus)}")
        print(f"\nKey Benefits / Adaptations:\n- {'\n- '.join(self.adaptations)}")
        print(f"\nWhat will the trainings look like:\n- {'\n- '.join(self.training_types)}")
        print(f"\nWhat to expect:\n- {'\n- '.join(self.expectations)}")
        print(f"\nWhen to choose:\n- {'\n- '.join(self.when_to_choose)}")
        print(f"\nNext Mezzo-Cycle Options:\n- {'\n- '.join(self.next_mezzo_options)}")

    def display_preview(self):
        print(f"{self.title}")
        print(f"\nLevel: {self.level}")
        print(f"\nDuration: {self.recommended_duration}")
        print(f"\nKey Focus: {self.primary_focus_summary}")
        print(f"\nWhen To Choose: {self.when_to_choose_summary}")