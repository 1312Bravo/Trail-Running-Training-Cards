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

See `notes/cloud_library_storage_workflow.md`, `notes/card_library_rebuild_workflow.md`, and `notes/schema_design_and_validation.md` for details.
