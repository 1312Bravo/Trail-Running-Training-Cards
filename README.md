# Trail Running Training Cards

This repository stores the standalone training-card library used by the Training Platform app.

The active card source is Google Drive JSON. The local cache is downloaded into `training_cards/local_cache/cloud_library/` and validated by the Python schemas.

## Project Structure

- `training_cards/`: importable Python package with schemas, registry, JSON/Drive sync, scripts, and card-authoring examples.
- `coaching/`: shared coaching foundation, card-authoring guidance, hierarchy notes, and philosophy profiles.
- `notes/`: durable schema, evidence, and cloud-storage notes.
- `streamlit_app/`: local Streamlit browser for card previews, detail views, filters, and coaching philosophy summaries.

## Card Workflow

Google Drive JSON is the source of truth for real card content. The local cache is only a working copy, and Python card files are examples or temporary authoring scaffolds.

For detailed workflows, see `notes/cloud_library_storage_workflow.md`.

## Useful Commands

```powershell
py -m training_cards.scripts.cloud.print_cloud_config
py -m training_cards.scripts.cloud.download_cloud_library
py -m training_cards.scripts.cache.validate_cache
py -m training_cards.scripts.cache.build_bundle
py -m training_cards.scripts.cloud.upload_cache
py -m training_cards.scripts.cloud.upload_metadata_cache
py -m training_cards.scripts.cloud.upload_mezzo_cache
py -m training_cards.scripts.cloud.upload_micro_cache
py -m training_cards.scripts.cloud.upload_session_cache
streamlit run streamlit_app/app.py
```

For the Streamlit UI, install the app-specific dependency file:

```powershell
py -m pip install -r streamlit_app\requirements.txt
```

Or from inside `streamlit_app\`:

```cmd
run_streamlit.cmd
```

See `notes/README.md` for the documentation map.
