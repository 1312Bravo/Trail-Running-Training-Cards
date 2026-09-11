# Coaching Philosophy Profiles

This folder holds documented interpretations of actual training-method profiles: broad evidence-informed endurance training, named coaching systems, teams, or platforms. A profile may draw on textbooks, institutional guidance, research reviews, books, articles, courses, interviews, podcasts, or other published material that supports that training method.

Profiles are not official material from, endorsements by, or claims to represent the named team or platform. They are our own structured interpretation of the source material for use in this training-card library.

Every card must follow `coaching/coaching_foundation.md`. The foundation is always-on library guidance, not a card-level philosophy profile.

## What Belongs Here

- The shared rules that apply to every card live in `coaching/coaching_foundation.md`, not in a philosophy profile.
- Each profile describes a distinct training method or coaching system and how we interpret its principles for this library.
- A profile may explain how that system approaches training load, intensity, progression, trail-specific preparation, athlete feedback, and decision-making.
- Each profile records the material that informed it, along with concise notes about what each source supports.

## Profile Structure

Each profile folder should contain:

- `summary.md`: a short, practical overview of the coaching system and its main emphases.
- `philosophy.md`: our structured interpretation of that coaching system.
- `sources.md`: the sources used for that interpretation, with relevant notes, limits, and updates.

Use `_template/` when creating a new profile. Refine the template as we learn what every profile genuinely needs, rather than creating many files before they are useful.

## Profile IDs And Cards

The profile-folder name is the stable profile ID used in card data. `training_cards/philosophy_profiles.py` is the canonical registry of those IDs and their display names. Examples include `mainstream_endurance`, `cts`, `evoke_endurance`, `swap`, `sharman_ultra`, `80_20_endurance`, and `lydiard`.

- Use one or more profile-folder IDs when a card is shaped by specific training-method profiles.
- Do not use `common`; the shared coaching foundation is always-on and is not a card-level philosophy profile.
- A profile ID must exactly match its directory name.
- Do not create a profile ID until its folder and source record exist.

## Source And Interpretation Standards

- Record the source clearly enough that we can revisit it.
- Separate what the source directly says from our interpretation, adaptation, or practical implementation.
- Do not treat a source as universal proof or present one system's preference as the only valid way to coach.
- Preserve uncertainty, disagreement, and limits of transfer when they matter.
- Update the profile and its sources when new material changes our interpretation.

## Adding A Profile

1. Choose one training method, named coaching system, or team with enough accessible source material to interpret responsibly.
2. Create a lowercase, underscore-separated folder name that can serve as a stable card profile ID.
3. Copy the template and identify the source material before writing broad claims.
4. Write the interpretation in `philosophy.md`, distil it in `summary.md`, and record supporting material in `sources.md`.
5. Review the profile against the shared coaching foundation before using its ID on cards.
