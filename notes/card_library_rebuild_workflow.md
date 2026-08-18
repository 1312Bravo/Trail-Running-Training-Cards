# Card Library Rebuild Workflow

This workflow governs the deliberate replacement of the current Training Cards library with a newly authored library. It applies when we rebuild the cards from the coaching foundation and philosophy profiles rather than incrementally editing the current library.

It does **not** author cards. It protects the current source of truth and defines the cutover process once the new cards are ready.

## Decision

Use an **archive-and-swap** process, not an in-place deletion and ordinary upload.

The current upload command only creates or updates files that exist in the local cache. It does not delete remote card files that are no longer present locally. Clearing the local cache and running that command would therefore leave obsolete cards on Google Drive.

The rebuilt library should instead be prepared as a complete, validated replacement in a staging location. After the current library has been archived and the replacement has been independently verified, the configured Google Drive source changes to the replacement folder. The previous folder stops being active but remains a recoverable archive.

## Terms

- **Active library:** the Google Drive folder configured in `training_cards/cloud_config.py`. It is the card-content source of truth used by the app and normal sync commands.
- **Staging library:** a complete local JSON library built for the rebuild before any active cloud content changes.
- **Archive library:** an immutable dated Drive copy of the active library immediately before cutover. It is not loaded by the app.
- **Replacement library:** the new Drive folder populated from the validated staging library. It becomes active only after verification.
- **Cutover:** the one deliberate configuration change that points the project from the old active library to the replacement library.

## Rebuild Principles

- Do not delete or overwrite the active Google Drive library while cards are still being authored or reviewed.
- Do not use `upload_cache` to clear a library. It cannot remove obsolete remote files.
- Preserve one complete local archive and one complete Google Drive archive before changing the active source.
- Create every replacement card with a valid `philosophy_profile_ids` value from `training_cards/philosophy_profiles.py`.
- Use `common` only when the shared foundation alone materially shaped the card. Do not combine it with named profile IDs.
- Treat the replacement library as complete only when its manifest, card files, bundle, display configuration, schema validation, and reference validation agree.
- Do not permanently delete the archived library without a separate, explicit approval after the replacement has been in use.

## Stage 1: Freeze The Existing Library

1. Stop ordinary card edits and uploads for the current library.
2. Download the active Drive library into the active local cache.
3. Validate the downloaded cache when it uses the active schema. If a legacy library cannot pass the current validator, preserve its raw manifest and card files unchanged, record the incompatibility, and continue only with raw integrity checks for the archive.
4. Record the active Drive URL and folder IDs in the rebuild record.

The freeze establishes exactly what is being replaced. If validation fails here, fix or document the existing state before creating an archive.

## Stage 2: Create And Verify The Archive

1. Copy the frozen local cache into a timestamped local archive outside the active cache, for example `training_cards/local_cache/archives/2026-08-18_pre-rebuild/`.
2. Create a dated archive folder on Google Drive, for example `training_cards_library_archive_2026-08-18_pre-rebuild`.
3. Copy the full library to that archive folder, including `manifest.json`, `display_config.json`, `training_cards_library.json`, and every card JSON file in every planning-level folder.
4. Create `archive_metadata.json` with the archive date, reason, original Drive URL and folder IDs, manifest values, card count, and a file checksum list.
5. Download the Drive archive into a separate temporary local location and verify its manifest card count and complete card-file set independently. Use full schema validation when the archived schema remains supported.

Only continue when the archive has the expected files, card count, and either passes schema validation or has a documented legacy-schema incompatibility with successful raw integrity checks.

## Stage 3: Build The Replacement Locally

1. Create a clean staging directory, separate from the active local cache and the archive.
2. Build the replacement cards from the coaching foundation, relevant philosophy profile, hierarchy, and authoring guidance.
3. Assign `philosophy_profile_ids` deliberately on every card.
4. Build the manifest, display configuration, and generated bundle from the replacement card set.
5. Validate the staging library, including card schema, duplicate IDs and slugs, manifest count, philosophy IDs, and pathway references.
6. Review the rebuilt library as content before any Drive upload.

The replacement must be a complete library. It must not depend on files left behind from the old library.

## Stage 4: Publish A Replacement Library

1. Create a new Google Drive root folder and its `cards/macro`, `cards/mezzo`, `cards/micro`, and `cards/session` subfolders. If the service account can access the active shared folder but not its parent, create distinct archive and replacement folders inside that shared container instead.
2. Upload the complete validated staging library into those new folders.
3. Download the replacement Drive library into a separate verification cache.
4. Validate that downloaded copy against its manifest and the active Python schemas.
5. Confirm that the replacement card count, file list, and generated bundle match staging.

The previous library remains active during this stage. A failed replacement upload never alters its source-of-truth status.

## Stage 5: Cut Over The Active Source

1. Update `training_cards/cloud_config.py` with the verified replacement Drive folder IDs and URL.
2. Clear the active local cache only after the archive and replacement verification have passed.
3. Download the replacement library into the active local cache.
4. Run the normal cache validator and load the Streamlit app against the replacement cache.
5. Update `library_version` for the rebuilt content. Keep `schema_version` unchanged unless the JSON field contract changed.
6. Record the replacement URL, archive URL, validation results, card count, and cutover date in `PLAN.md` and the rebuild record.

At this point the former library is no longer active. It is an archive, not a fallback silently loaded by the app. If the replacement is nested inside an inaccessible shared container, delete only the known former root files and `cards` folder, never the shared container itself.

## Stage 6: Post-Cutover Review

1. Open the app and verify preview, detail, search, pathway navigation, tags, and philosophy-profile filtering against the replacement cards.
2. Confirm that every card renders a readable coaching philosophy display name from the local registry.
3. Remove obsolete migration scripts only when no active or supported archive workflow needs them.
4. Retain the archive until we explicitly decide that permanent deletion is appropriate. If the service account lacks permission to delete former content, record the remaining file IDs for the Drive owner rather than attempting a workaround.

## Required Approval Checkpoints

The following actions require explicit approval in the moment; previous general agreement is not enough:

1. Create the cloud archive and replacement folders.
2. Upload the complete replacement library to the new Drive folder.
3. Change `training_cards/cloud_config.py` to make the replacement the active source.
4. Permanently delete any Drive archive or former active folder.

## Implementation Work Needed Before Cutover

The current Drive client and upload workflow need dedicated rebuild support before we perform this process:

- create Drive folders and subfolders
- copy or upload a complete dated archive
- list and verify every expected remote file
- upload a replacement library to an explicitly supplied target configuration
- download and validate an explicitly supplied target configuration
- create archive metadata and checksums
- switch the active Drive configuration only after verification

Do not extend the normal `upload_cache` command into an implicit deletion command. Rebuild replacement must remain a separately named, explicit operation.
