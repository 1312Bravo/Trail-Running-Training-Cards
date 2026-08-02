# Trail Running Training Cards

This repository stores the standalone training-card library used by the Training Platform app.

The active card source is Google Drive JSON. The local cache is downloaded into training_cards/local_cache/cloud_library/ and validated by the Python schemas.

## Project Structure

- `training_cards/`: importable Python package with schemas, registry, JSON/Drive sync, scripts, and seed cards.
- `prompts/`: coach prompt used when changing card content or coaching logic.
- `notes/`: durable schema, evidence, and cloud-storage notes.

## Useful Commands

```powershell
py -m training_cards.scripts.print_cloud_config
py -m training_cards.scripts.download_cloud_library
py -m training_cards.scripts.validate_cache
py -m training_cards.scripts.build_bundle
py -m training_cards.scripts.upload_cache
```

See `notes/cloud_storage_notes.md`, `notes/schema_notes.md`, and `notes/evidence_sources.md` for details.
