# Product Backlog

This is the shared place for future product, workflow, and automation work that should be designed deliberately before implementation.

## Future Feature: Controlled Tag Taxonomy

Create a smart tag taxonomy for card filtering, validation, and future app UX.

Current direction:

- keep tags flexible while the card library is still growing
- group known tags into meaningful coaching categories
- report unknown tags as warnings, not errors
- use the taxonomy during card creation, cache validation, and pre-upload checks
- avoid blocking new card creation unless a tag is clearly invalid after the taxonomy matures

Questions to resolve:

- what tag groups should exist first?
- should tags stay simple strings or become grouped objects?
- when should unknown tags move from warnings to errors, if ever?
- how should the Streamlit app expose tag groups without making the UI heavy?

## Future Feature: Today Session Decision Helper

Turn the Today session tab into a real coaching helper, not only a session-card browser.

Current direction:

- leave ranking unimplemented until card metadata and tags are more stable
- avoid changing card content only to support ranking too early
- start with coach-relevant inputs such as readiness, available time, terrain, goal, and desired intensity
- choose or rank session cards only when the scoring logic is clear and explainable

Questions to resolve:

- what does "best session today" mean?
- should the app filter sessions, rank them, or both?
- should ranking be based on existing fields first, or should new metadata be added?
- how should the app explain why a session was recommended?

## Future Workflow: Automated Checks

Decide where project tests should run automatically.

Current direction:

- validation should protect card data before export/upload
- tests should protect code behavior, especially pathway indexing and validation rules
- tests should not run inside the Streamlit app
- a future CI or pre-upload command can run both tests and validation as one project check

Questions to resolve:

- should this repo use GitHub Actions?
- should upload scripts run tests, or only validation?
- should there be one command such as `py -m training_cards.scripts.reports.check_project`?
