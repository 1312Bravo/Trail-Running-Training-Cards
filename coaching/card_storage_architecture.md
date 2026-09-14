# Card Storage Architecture

This note defines how training cards are stored locally and in the cloud-style JSON library.

## Goals

- Make card storage reflect the planning hierarchy and coaching philosophy structure.
- Keep philosophy ownership visible during authoring.
- Allow multiple philosophies to have cards with similar visible names.
- Reserve a clear home for genuinely integrated multi-profile cards.
- Keep the app and JSON exports driven by card metadata, not by folder inference.

## Local Python Authoring Examples

Accepted card content does not live as a full Python seed library anymore. Google Drive JSON is the source of truth, and `training_cards/local_cache/cloud_library/` is the temporary working copy.

Python card files are now only examples or temporary authoring scaffolds. The permanent examples live under:

```text
training_cards/cards/examples/
  macro_example.py
  mezzo_example.py
  micro_example.py
  session_example.py
```

When Python authoring is helpful, use one of the workflow templates:

```text
training_cards/scripts/template_cloud_json_to_python_card.py
training_cards/scripts/template_targeted_authoring_helper.py
```

The temporary Python object must be converted back into cache JSON, validated, bundled, uploaded, and verified before it becomes accepted library content.

The hierarchy/profile folders under `training_cards/cards/<level>/<profile>/` are kept with `.gitkeep` placeholders so the intended local authoring structure remains visible in Git. They do not contain accepted card content.

## Cloud-Style JSON Cache

Exported JSON mirrors the same level/profile-folder shape:

```text
training_cards/local_cache/cloud_library/cards/<level>/<profile_folder>/<slug>.json
```

Examples:

```text
training_cards/local_cache/cloud_library/cards/session/mainstream_endurance/mainstream-easy-aerobic-run.json
training_cards/local_cache/cloud_library/cards/session/multi_profile/cts-lydiard-taper-activation.json
```

Google Drive replacement libraries should use the same folder shape under `cards/`.

## Profile Folder Rule

- If a card has exactly one `philosophy_profile_ids` value, store it under that profile ID.
- If a card has more than one `philosophy_profile_ids` value, store it under `multi_profile`.
- `multi_profile` is not a philosophy profile. It is a storage folder for genuinely integrated cards.
- Do not use `multi_profile` for unclear cards. If the card is unclear, rewrite or review it.

## Naming Rule

Visible card titles should be readable coaching titles:

```text
Easy Aerobic Run
Controlled Quality Intervals
```

Implementation names should be unique and traceable:

```text
mainstream_easy_aerobic_run.py
mainstream-easy-aerobic-run.json
evoke_easy_aerobic_run.py
evoke-easy-aerobic-run.json
```

The card `id` remains the stable reference identity. The `slug` remains the app/cloud filename identity. The title remains the human-facing coaching label.

## Metadata Remains Authoritative

Folder location does not replace card metadata.

Every card JSON record must still include:

```json
"philosophy_profile_ids": [
  "mainstream_endurance"
]
```

This keeps the JSON portable outside Python and keeps app filtering independent from filesystem assumptions.

## Current Library Shape

The active Drive/cache library stores accepted cards by planning level and philosophy folder:

```text
cards/<level>/<profile_folder>/<slug>.json
```

The current Drive-backed library has 365 accepted cards across macro, mezzo, micro, and session levels. The cards were planned from `training_cards/cards/card_matrix.md`. Future cards should follow the same specificity standard: create a named-philosophy version only when that philosophy meaningfully changes the app choice, explanation, structure, filtering, or sequencing.
