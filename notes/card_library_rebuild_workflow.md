# Card Library Rebuild Workflow

This workflow governs deliberate replacement of the current Training Cards library with a newly authored library. It applies when we replace card content from the coaching foundation, card matrix, and philosophy profiles rather than incrementally editing the current library.

For normal download, edit, validate, bundle, and upload work, use `cloud_library_storage_workflow.md` instead. For schema rules, use `schema_design_and_validation.md`.

It does **not** author cards. It protects the current source of truth and defines the cutover process once the new cards are ready.

## Decision

Use an explicit **validated replacement** process, not ordinary upload.

The current upload command only creates or updates files that exist in the local cache. It does not delete remote card files that are no longer present locally. Clearing the local cache and running that command would therefore leave obsolete cards on Google Drive.

The replacement library should instead be prepared as a complete, validated source directory. The `replace-active` action then deletes only the known active root files and `cards` folder, recreates the expected folder structure, uploads the complete replacement, and verifies the result. This keeps the root Drive folder stable while still removing obsolete card files.

## Terms

- **Active library:** the Google Drive folder configured in `training_cards/cloud_config.py`. It is the card-content source of truth used by the app and normal sync commands.
- **Replacement source:** a complete local JSON library that has already been exported and validated.
- **Verification cache:** a temporary downloaded copy of the replaced Drive library used to confirm the remote result.
- **Archive library:** an optional dated Drive copy of the active library before replacement. It is not loaded by the app.
- **Cutover:** the deliberate update that records any newly created Drive subfolder IDs in `training_cards/cloud_config.py`.

## Rebuild Principles

- Do not delete or overwrite the active Google Drive library while cards are still being authored or reviewed.
- Do not use `upload_cache` to clear a library. It cannot remove obsolete remote files.
- Use `replace-active` only with a complete replacement source, never a partial card export.
- Create every replacement card with a valid training-method `philosophy_profile_ids` value from `training_cards/philosophy_profiles.py`.
- Do not use `common`; the shared coaching foundation is always-on and is not card-level provenance.
- Treat the replacement library as complete only when its manifest, card files, bundle, display configuration, schema validation, and reference validation agree.
- Do not permanently delete any archive or former active folder without separate, explicit approval.

## Stage 1: Prepare The Replacement Source

1. Build or edit the replacement JSON library locally.
2. Use temporary Python authoring scaffolding only when it makes new card creation safer.
3. Validate schema, manifest count, duplicate IDs and slugs, philosophy IDs, and pathway references.
4. Build reuse metadata files and the bundled `training_cards_library.json`.
5. Review the replacement as content before any Drive operation.

The replacement source must be complete. It must not rely on files left behind from the old library.

## Stage 2: Optional Archive

1. Download the active Drive library before replacement if a recoverable snapshot is needed.
2. Create a dated local or Drive archive from that frozen copy.
3. Verify file count and manifest consistency.
4. Record the archive location if retained.

The archive stage is a safety choice. It is not required when we intentionally delete old content and have accepted that the new library is the source of truth.

## Stage 3: Replace The Active Drive Contents

Run the explicit replacement command with the validated source directory:

```powershell
py -m training_cards.scripts.rebuild_drive_library replace-active --source-dir training_cards\local_cache\cloud_library
```

The replacement action must:

- refuse to run against a missing or incomplete source directory
- delete only known active root items: `manifest.json`, `display_config.json`, reuse metadata files, `training_cards_library.json`, and `cards`
- refuse unexpected root files or unexpected root folder shape
- recreate `cards/macro`, `cards/mezzo`, `cards/micro`, and `cards/session`
- upload the complete replacement library
- verify the uploaded library by downloading and validating it

## Stage 4: Record New Folder IDs

The active root folder remains the same, but the `cards` and level subfolders are recreated. Update `training_cards/cloud_config.py` with the verified new folder IDs printed by the replacement workflow.

Then refresh the active local cache from Drive and validate it.

## Stage 5: Post-Replacement Review

1. Open the app and verify preview, detail, search, pathway navigation, tags, and philosophy-profile filtering against the replacement cards.
2. Confirm that every card renders a readable coaching philosophy display name from the local registry.
3. Remove obsolete one-off migration or staging scripts once the replacement is verified.
4. Record the replacement date, card count, library version, and validation result in project notes.

## Required Approval Checkpoints

The following actions require explicit approval in the moment; previous general agreement is not enough:

1. Replace active Drive contents.
2. Permanently delete any retained Drive archive or former active folder.
3. Change the configured active root folder, if a future rebuild uses a new root instead of in-place replacement.

## Current Replacement Record

On 2026-09-06, the active `training_cards_library` Drive folder was replaced in place with a 33-card macro JSON library. The library used schema `1.2.0`, library version `0.4.1`, and stored cards under level/profile folders.
