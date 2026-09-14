# User Experience Plan

## Goal

Evolve the existing Streamlit card browser into an approachable, personalized trail-running training experience for the portfolio site. The first version should help a runner choose a training direction, understand the connected card pathway, and track progress during an active visit without requiring accounts or a database.

## Current Understanding

- The app already supports Browse cards, Today session, Card library, Build pathway, and Coaching philosophies.
- Card content is shared and driven by validated Google Drive JSON downloaded into the local cache.
- The current interface is interactive, but user progress is not persistent across visits.
- The immediate target is a polished deployed web application, not a native mobile app or a large multi-user service.

## Product Direction

The app should gradually move from a card library toward a guided training journey:

```text
Choose a focus → Select a Macro → Explore the pathway → Use Today session → Track progress
```

The card library remains important, but the primary experience should help a runner decide what to do next.

## Primary User Journey

1. The user opens the app and understands what the training cards represent.
2. The user chooses a goal, training focus, level, or another useful starting point.
3. The user selects a Macro card as an active training direction.
4. The app presents the related Mezzo, Micro, and Session cards.
5. The user marks cards as planned, active, or completed during the current session.
6. The app shows pathway progress and a useful Today session view.

## Implementation Phases

### Phase 1 — Build the experience

- Use `st.session_state` as temporary storage while the product flow is being shaped.
- Define what planned, active, and completed mean for each card level.
- Add the active Macro pathway experience.
- Connect pathway selection to the Today session view.
- Add a compact progress summary.
- Review the experience at desktop and phone widths.

### Phase 2 — Evaluate persistence

After Phase 1 is usable, decide whether progress must survive closing the app:

- session-only progress: simplest, but only an interactive walkthrough
- browser-local progress: survives on one browser/device without login
- export/import: user saves and restores a small progress file
- account-backed progress: login and hosted database for cross-device history

Do not add authentication or database infrastructure until the user-facing progress behavior is clear and worth preserving.

## Initial Feature Priorities

### First implementation

- [ ] Clear onboarding or explanation of the card system.
- [ ] Choose a training focus or starting context.
- [ ] Select and activate a Macro card.
- [ ] Display the connected Macro → Mezzo → Micro → Session pathway.
- [ ] Define and display progress states.
- [ ] Improve the Today session experience for an active pathway.
- [ ] Show a compact in-session progress summary.

### Later, if valuable

- [ ] Saved or favourite cards.
- [ ] Pathway export or sharing.
- [ ] Notes or lightweight reflections.
- [ ] Browser-local persistence.
- [ ] Email login and user accounts.
- [ ] Hosted database-backed history.
- [ ] Notifications or reminders.

## Critical Review

- A native mobile rewrite is unnecessary for the current portfolio scope.
- Authentication and a database would add real value only if users need to return and continue their progress.
- The most important uncertainty is the user experience, not the storage technology.
- Progress rules should be designed before persistence is implemented.
- The shared card library should remain separate from any future user-owned progress data.

## Decisions

- Keep Streamlit as the first frontend.
- Keep Google Drive JSON as the shared card-content source of truth.
- Build the personalized experience before adding login or a database.
- Treat persistent accounts as an optional later phase.

## Open Questions

- What should be the first entry point: goal, race, training level, philosophy, or available time?
- Is the Macro card the correct starting point for every user?
- Should progress apply to Sessions only, to all four card levels, or to both pathway stages and Sessions?
- Should the first portfolio version use session-only progress, browser-local progress, or export/import?
- What should the user see when there is no active pathway?

## Progress

- Existing design-focused `PLAN.md` replaced with this user-experience plan.
- Phased direction agreed: build the experience first, then evaluate persistence.
