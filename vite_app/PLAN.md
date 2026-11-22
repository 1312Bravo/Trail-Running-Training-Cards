# My Plan

## Goal
Build a calendar that gives card selection context. Start simple and iterate with the user.

## Decisions
- Keep all app labels and calendar dates in English. Date fields use YYYY-MM-DD without browser-localized picker text.
- Place My Plan immediately after Build pathway.
- Reuse the same pathway selector component in Build pathway and My Plan.
- Keep the calendar under the selector; selecting a day loads its saved pathway into the selector.
- Keep date entry in a compact inline row, without a right-side planning panel.
- Save only in this browser; no accounts, cloud sync, export, or import for now.
- Support a whole-year overview and a detailed month view first.
- Place macro phases over inclusive date ranges, then mezzo blocks, micro weeks, and sessions within their parents.
- Link placements to library card IDs; never duplicate or edit accepted card content.
- Selecting a day shows its planned hierarchy and filters card choices through existing library relationships.
- This is a planning tool, with no completion tracking or workout logging.

## First increment
- [x] Calendar with year/month navigation, Today, and selected day.
- [x] Add placements from linked card choices, with inclusive dates inside parent periods.
- [x] Let a selected day drive the shared pathway selector and searchable card choices.
- [ ] Add a clear way to edit or remove existing placements from the calendar flow.
- [x] Browser saving with visible failure feedback and missing-card handling.
- [x] Focused compile/build and browser preview.

## Review notes
- The selector is shared across Build pathway and My Plan. The calendar remains below it and drives its selected-card state.
- The previous right-side planning panel was removed. Date entry appears inline after a card is selected.
- Range editing remains possible by selecting a planned step and choosing its card again. A direct remove action is a follow-up.
- Browser preview exercised all four levels, editing a phase range, selecting another day, year view, and persistence after reload.
- Focused model checks covered leap dates, DST and year boundaries, inclusive dates, nested date limits, overlapping periods, multiple sessions, nested removal, and invalid saved data.
- Month view uses coloured daily labels. Year view uses compact markers; continuous range bands are a later refinement.
- Periods at the same level cannot overlap. Sessions can share a day.
- Filtering currently applies to choices within My Plan. Existing browsing tabs keep their own filters.

## Later candidates (review after using the first version)
- Week view and clearer range bands across calendar rows.
- A current-week indicator inside the selected block.
- Repeat a week and move placements by dragging.
- Better bulk date adjustments when moving a parent block.
- Connect calendar context to the other browsing tabs if useful.
- Cloud saving only after a separate product decision.
