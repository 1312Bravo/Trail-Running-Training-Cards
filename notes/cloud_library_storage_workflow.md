# Cloud Library Storage Workflow

These notes own storage and sync workflow for the training-card cloud library. Keep schema details in `schema_design_and_validation.md`, full replacement safeguards in `card_library_rebuild_workflow.md`, and card taxonomy decisions in `training_cards/cards/card_matrix.md`.

## Direction

The source of truth is the cloud JSON card library.

Python is the tooling layer around that library. It validates, downloads, uploads, bundles, and can help author new card content, but real accepted cards should not be maintained as a full duplicate Python seed library.

There are three supported workflow paths:

1. Existing-card edits use the Drive/cache path.
2. New-card authoring can use temporary Python class-based scaffolding when it makes complex card creation safer.
3. Existing cloud/cache JSON cards can be converted one at a time into temporary Python authoring files when Python editing is useful.

In both workflows, the accepted result must be JSON in the local cache, validated by the Python schemas, bundled, uploaded to Drive, and verified when the change is substantial.

The Training Platform app should eventually load cards from cloud JSON, validate them with the Python schemas, and then use the validated card objects in the app.

For a full replacement of the card library, use `notes/card_library_rebuild_workflow.md`. The normal upload workflow only adds or updates files and must not be used to clear obsolete cards from Google Drive.

## Recommended Cloud Location

Use Google Drive first.

Why Google Drive fits this phase:

- It is simple file storage, which matches one JSON file per card.
- It is easy to inspect and replace files manually when needed.
- It can hold a normal folder structure with `manifest.json` and `cards/`.
- It fits a private personal library better than a public static file setup.
- Python can later download and upload the files through the Google Drive connector/API.

GitHub is also a good option if we want version history and review for every card change. It is less convenient as a private editable card library for the app unless we intentionally treat card changes like code changes.

A database such as Supabase can wait until the app needs in-app editing, multi-user access, permissions, or search/filtering that becomes awkward with plain files.

## Current Google Drive Library

Replaced in place and verified on 2026-09-06. The macro layer was uploaded first, then root metadata, mezzo files, and micro files were uploaded incrementally so existing accepted cloud files were not disturbed. The macro-plus-mezzo-plus-micro library was downloaded and verified from Drive on 2026-09-09. The session-card schema/display metadata was then uploaded as root metadata only and verified from Drive as schema `1.3.0`, library `0.7.0`. The session layer and updated root metadata were uploaded and verified by Drive readback on 2026-09-10.

```text
training_cards_library
https://drive.google.com/drive/folders/1Y7lXD-wr3kQH9QVbsi_nrkK9ihDrKKPV
```

Folder IDs:

- Root library folder: `1Y7lXD-wr3kQH9QVbsi_nrkK9ihDrKKPV`
- `cards`: `1l2GNAN348_Q3kXnCVOUZHoHxpEbpPeKv`
- `cards/macro`: `18IABJtzFkQdzaZFcAa1ulVriSgCv0Zr0`
- `cards/mezzo`: `1gQbOltntSbLD4Geapz8VIifJ63QHZg_w`
- `cards/micro`: `14uD_WS3RosZeQ8HRP6xOvBDA41lVi16N`
- `cards/session`: `1NuzKGJSHSis0jNQkPUhsLenfp00fjlV2`

Current Drive library contents:

- `manifest.json`: 1 file
- `display_config.json`: 1 file
- `macro_mezzo_reuse.json`: 1 app-facing reuse metadata file
- `mezzo_micro_reuse.json`: 1 app-facing reuse metadata file
- `micro_session_reuse.json`: 1 app-facing reuse metadata file
- `card_library_index.json`: 1 app-facing browse/index metadata file
- `training_cards_library.json`: 1 bundled app-facing file
- `cards/macro`: 33 files
- `cards/mezzo`: 78 files
- `cards/micro`: 177 files
- `cards/session`: 77 files

The current Drive library contains accepted macro cards, accepted mezzo cards, accepted micro cards, accepted session cards, explicit macro-to-reused-mezzo mapping metadata, explicit mezzo-to-reused-micro mapping metadata, explicit micro-to-reused-session mapping metadata, and an app-facing card library index for quick philosophy/block browsing.

Verified Drive/readback status: the library contains 365 cards: 33 macro, 78 mezzo, 177 micro, and 77 session cards. The session cards include 46 mainstream session cards and 31 named-philosophy session cards. The uploaded `micro_session_reuse.json` contains 1087 entries and is included in `training_cards_library.json`.

## Python Cloud Reference

The Google Drive library location is stored in:

```text
training_cards/cloud_config.py
```

Use this helper to get the canonical folder URL:

```python
from training_cards.cloud_store import get_cloud_library_url

print(get_cloud_library_url())
```

Local cache/export/load helpers live in:

```text
training_cards/cloud_store.py
```

Core helper functions:

- `load_cached_cloud_library()`
- `download_cloud_library(client)`
- `upload_cached_library(client)`
- `upload_cached_root_metadata(client)`
- `upload_cached_mezzo_library(client)`
- `upload_cached_micro_library(client)`
- `upload_cached_session_library(client)`

## Drive Client Boundary

Normal project Python uses a service account, similar to the existing Google Drive and Google Sheets jobs in this repository.

The concrete client lives in:

```text
training_cards/google_drive_client.py
```

By default it reads:

```text
googleDrive_secrets.json
```

You can override that with:

```text
TRAINING_CARDS_GOOGLE_SERVICE_ACCOUNT_FILE
```

or:

```text
GOOGLE_APPLICATION_CREDENTIALS
```

The Google Drive folder must be shared with the service-account email before local Python can download or upload files.

`training_cards/cloud_store.py` expects a Drive client object with these methods:

- `list_folder(folder_id)`
- `download_file(file_id, output_path)`
- `upload_file(local_path, folder_id, file_name, mime_type)`
- `update_file(file_id, local_path, mime_type)`
- `create_folder(folder_name, parent_folder_id)`
- `delete_file(file_id)`

The current implementation is `GoogleDriveClient`. This loose shape still lets us later connect another implementation if needed:

- Google Drive API with the current service account.
- Google Drive API with OAuth credentials later, if needed.
- A Codex-only adapter when working inside Codex tools.
- A test/mock client for validation.

The important project logic already exists separately from the authentication choice.

## Local Script Commands

Run these from the repository root.

```powershell
py -m training_cards.scripts.cloud.print_cloud_config
py -m training_cards.scripts.cache.validate_cache
py -m training_cards.scripts.cache.build_bundle
py -m training_cards.scripts.cache.build_card_library_index
py -m training_cards.scripts.cloud.download_cloud_library
py -m training_cards.scripts.cache.add_cards_to_cache path\to\card.json
py -m training_cards.scripts.cache.remove_cards_from_cache card_id_001
py -m training_cards.scripts.cloud.upload_cache
py -m training_cards.scripts.cloud.upload_metadata_cache
py -m training_cards.scripts.cloud.upload_mezzo_cache
py -m training_cards.scripts.cloud.upload_micro_cache
py -m training_cards.scripts.cloud.upload_session_cache
py -m training_cards.scripts.workflow.workflow_edit_existing_cards
py -m training_cards.scripts.workflow.workflow_author_new_cards
py -m training_cards.scripts.authoring.template_cloud_json_to_python_card --card-id macro_001
py -m training_cards.scripts.authoring.template_targeted_authoring_helper
py -m training_cards.scripts.cloud.rebuild_drive_library replace-active --source-dir training_cards\local_cache\cloud_library
```

Command meanings:

- `print_cloud_config`: show the configured Drive folder IDs, URL, and local cache path.
- `validate_cache`: validate the local cache against `manifest.json`.
- `build_bundle`: validate the local cache and write `training_cards_library.json`.
- `build_card_library_index`: validate the local cache and write `card_library_index.json`.
- `download_cloud_library`: download Drive JSON into local cache and validate it.
- `add_cards_to_cache`: add or replace card JSON/Python authoring files in the downloaded local cache, then validate and refresh root metadata.
- `remove_cards_from_cache`: remove card JSON files from the downloaded local cache by card ID, then validate and refresh root metadata.
- `upload_cache`: refresh `training_cards_library.json`, then upload local cache files to Drive, updating existing files by name and creating missing files.
- `upload_metadata_cache`: refresh and upload root metadata files only, leaving all cloud card JSON files untouched.
- `upload_mezzo_cache`: refresh root metadata and upload only `cards/mezzo`, leaving existing cloud macro files untouched.
- `upload_micro_cache`: refresh root metadata and upload only `cards/micro`, leaving existing cloud macro and mezzo files untouched.
- `upload_session_cache`: refresh root metadata and upload only `cards/session`, leaving existing cloud macro, mezzo, and micro files untouched.
- `workflow_edit_existing_cards`: print the normal existing-card edit checklist.
- `workflow_author_new_cards`: print the new-card authoring checklist.
- `template_cloud_json_to_python_card`: convert one downloaded cloud/cache JSON card into a temporary local Python authoring file.
- `template_targeted_authoring_helper`: export the four example cards to a disposable example folder and show the guarded publish-to-cache plus cloud-upload path for future real authored cards.
- `rebuild_drive_library replace-active`: replace the known active Drive library contents with a complete validated source directory, deleting obsolete remote files first.

## Existing-Card Edit Workflow

Use this for normal card corrections, wording changes, reference edits, taxonomy edits, and app-facing metadata updates.

```powershell
py -m training_cards.scripts.cloud.download_cloud_library
# edit JSON in training_cards\local_cache\cloud_library\
py -m training_cards.scripts.cache.validate_cache
py -m training_cards.scripts.cache.build_bundle
py -m training_cards.scripts.cloud.upload_cache
```

To add or update prepared cards without hand-copying files into the cache:

```powershell
py -m training_cards.scripts.cloud.download_cloud_library
py -m training_cards.scripts.cache.add_cards_to_cache path\to\new_or_updated_card.json
py -m training_cards.scripts.cache.validate_cache
py -m training_cards.scripts.cloud.upload_cache
```

`add_cards_to_cache` accepts a single card JSON object, a JSON list of cards, a bundle-style JSON object with a `cards` list, or a temporary Python file exposing `AUTHORED_CARD` or `AUTHORED_CARDS`.

To remove cards from the cache by ID:

```powershell
py -m training_cards.scripts.cloud.download_cloud_library
py -m training_cards.scripts.cache.remove_cards_from_cache session_999
py -m training_cards.scripts.cache.validate_cache
py -m training_cards.scripts.cloud.upload_cache
```

The removal helper validates the remaining library before writing, so it should fail before deletion if other cards still depend on the removed card.

For layer-specific additions, use the narrower upload command after validation, such as `upload_mezzo_cache`, `upload_micro_cache`, or `upload_session_cache`.

## New-Card Authoring Workflow

Use Python classes only when they help create new content safely, such as a batch of cards with repeated structure or a session card with several workout blocks and options.

The four reusable examples live in:

```text
training_cards/cards/examples/
  macro_example.py
  mezzo_example.py
  micro_example.py
  session_example.py
```

New authoring flow:

1. Start from the relevant example.
2. Write temporary Python authoring code only for the card or batch being created.
3. Convert accepted cards into JSON under `training_cards/local_cache/cloud_library/`.
4. Validate the cache.
5. Build the bundle.
6. Upload the relevant cache files to Drive.
7. Verify by Drive readback for substantial card-library changes.

After upload and verification, keep only reusable examples or deliberate tooling. Do not keep the full accepted library as Python seed-card files.

## Cloud JSON To Python Authoring File

Use this when an existing Drive card should be edited with Python structure instead of raw JSON.

```powershell
py -m training_cards.scripts.cloud.download_cloud_library
py -m training_cards.scripts.authoring.template_cloud_json_to_python_card --card-id macro_001
```

The generated file goes under:

```text
training_cards/local_cache/python_authoring/
```

It contains the downloaded card JSON as `CARD_DATA` and exposes `AUTHORED_CARD = card_from_dict(CARD_DATA)`. This gives a real card object that can be imported by a targeted helper.

This is intentionally one card at a time. Do not use it to recreate the whole cloud library as Python files.

The helper template is:

```text
training_cards/scripts/authoring/template_targeted_authoring_helper.py
```

It demonstrates the full path:

1. Import or define the authored card objects.
2. Refuse to publish `example_*` cards into the active cache.
3. Merge real authored cards into the downloaded local cache.
4. Rebuild manifest, display config, reuse metadata, and bundle.
5. Print the correct upload command for the authored layer.

The helper is intentionally a template. For a real batch, copy or adapt it so the accepted cards are explicit and reviewable.

## Cloud Folder Shape

The cloud folder should mirror the local cache shape:

```text
training_cards_library/
  manifest.json
  display_config.json
  macro_mezzo_reuse.json
  mezzo_micro_reuse.json
  micro_session_reuse.json
  training_cards_library.json
  cards/
    macro/
      mainstream_endurance/
        mainstream-return-to-consistency.json
      cts/
        cts-race-specific-preparation.json
    mezzo/
    micro/
    session/
```

Card file names use `slug`.

Card relationships use `id`.

## Display Config

`display_config.json` belongs to the Training Cards project because it describes card meaning and card display intent.

It answers:

- Which fields should appear in the card preview?
- Which fields should appear first in the detail view?
- What labels should consumers use for card fields?
- What labels should consumers use for each card type?
- Which fields are system fields that should be loaded but not necessarily shown?

The Training Platform app should read this file from Google Drive instead of owning Training Cards field order, preview choices, labels, or authoring rules.

Current preview rule:

- `summary` is the preview-safe sentence.
- `summary` should usually be one sentence and 12-22 words.
- Longer coaching context belongs in `additional_information`.
- `id` and `slug` are system fields; the app should load them for routing and linking, even if it does not show them in the preview.

## Manifest

`manifest.json` is the library table of contents.

It answers:

- What library is this?
- Which schema version does it use?
- Which library version is this?
- How many cards should exist?
- When was it last updated?
- Where are card files stored?
- Which card IDs and slugs exist?

Example:

```json
{
  "library_id": "running_training_cards",
  "schema_version": "1.0.0",
  "library_version": "0.1.0",
  "updated_at": "2026-08-01",
  "cards_root": "cards",
  "card_count": 38,
  "cards": [
    {
      "id": "macro_001",
      "slug": "return-to-consistency",
      "card_type": "macro",
      "title": "Return To Consistency"
    }
  ]
}
```

## Published Bundle

`training_cards_library.json` is the app-facing bundle. It is generated from the validated local cache and contains:

```json
{
  "manifest": {},
  "display_config": {},
  "macro_mezzo_reuse": {},
  "mezzo_micro_reuse": {},
  "micro_session_reuse": {},
  "cards": []
}
```

The Training Platform app can read this one file instead of downloading `manifest.json`, `display_config.json`, reuse metadata files, and every individual card JSON file. Keep editing and reviewing the individual card JSON files; rebuild and upload the bundle whenever any card, manifest, display config, or reuse metadata changes.

## Local Cache

The local cache is a temporary working copy of the cloud library. It is also what `training_cards/registry.py` loads.

Current local cache path:

```text
training_cards/local_cache/cloud_library/
```

The local cache is ignored by git. It should be safe to delete and recreate from cloud.

When `download_cloud_library` runs, old cached JSON files are removed before the fresh cloud copy is downloaded. This keeps deleted cloud cards from lingering locally.

The local cache should not silently sync both ways. Use explicit steps:

1. Download cloud to local cache.
2. Validate local cache.
3. Edit or create cards locally.
4. Validate again.
5. Rebuild `training_cards_library.json`.
6. Upload local cache to cloud.

This avoids accidental overwrites when both cloud and local files changed.

Run download, validation, and upload sequentially. Do not run download and upload at the same time, because upload validates the local cache while download writes files.

## App Loading

Later, the Training Platform app should load from cloud JSON.

Recommended app behavior:

- Download/read `manifest.json`.
- Download/read `display_config.json`.
- Check `schema_version`.
- Read the card files listed in the manifest.
- Validate each card with the Python schemas.
- Use `display_config.json` for preview fields, detail field order, field labels, and card type labels.
- Check `card_count`, duplicate IDs, duplicate slugs, missing files, and broken references.
- Use validated cards inside the app.

The active `training_cards/registry.py` does not depend on Python seed card files. It loads the local JSON cache, which should be refreshed from Google Drive.

## Manifest Strictness

Manifest strictness means how strongly the app trusts and checks `manifest.json`.

Recommended default:

- Strict for schema compatibility, duplicate IDs, missing files, and broken references.
- Warning-only for `library_version` changes.
- Strict for `card_count` mismatch once cloud becomes source of truth.

In practice:

- If `schema_version` is unsupported, stop loading.
- If a referenced card ID does not exist, stop loading.
- If two cards share the same ID, stop loading.
- If two cards share the same slug, stop loading.
- If `card_count` says 38 but only 37 cards load, stop loading.

This prevents the app from quietly showing an incomplete or broken card library.

## Versioning

`schema_version` describes the shape of the JSON fields.

Bump `schema_version` when the schema changes in a way that affects JSON compatibility, such as:

- Adding a required field.
- Removing a field.
- Renaming a field.
- Changing the meaning or type of a field.

`library_version` describes the card content.

Bump `library_version` when the cards change but the schema stays compatible, such as:

- Adding a card.
- Editing card text.
- Updating references.
- Changing tags.

Current expectation:

- Schema starts at `1.0.0`.
- The schema can stay stable unless we redefine fields.
- Library starts at `0.1.0` while content is still draft.

## Current Source-Of-Truth Structure

The previous full Python seed-card library has been retired. Python examples remain as authoring references, not as a second accepted card library.

Current state:

1. Google Drive JSON is the source of truth.
2. Local cache is downloaded from Google Drive.
3. `training_cards/registry.py` loads the local JSON cache.
4. `training_cards/cards/examples/` shows how to author each card block with Python classes.
5. New accepted cards must be converted to JSON, validated, uploaded, and verified before they are treated as real library content.
