# Archived Artwork

This folder is a local archive for card artwork experiments.

The Streamlit app does not use these assets today. Preview cards are currently
typography-first and intentionally render without avatars, artwork backgrounds,
or block-logo overlays.

Keep this folder because the artwork may be useful again later. If avatars are
reintroduced, first test a small representative sample in the running app before
reconnecting the full catalog.

Do not upload this artwork to Google Drive unless the app starts using it again.

The previous Google Drive artwork folder was removed. Treat this local archive
as the only retained copy of the artwork experiments.

## Cloud Layout If Artwork Is Restored

If artwork is restored to Google Drive later, it should live beside the
card-library content in the cleaned library folder:

```text
My Drive/
  training_cards_library/
    cards/
    artwork/
    display_config.json
    manifest.json
    training_cards_library.json
```

Inside `artwork/`, the intended structure should mirror this local archive:

```text
artwork/
  catalog.json
  assets/
    avatars/
      macro/
      mezzo/
      micro/
      session/
    backgrounds/
    fallback/
    textures/
  prompts/
```

The cloud `artwork/` folder has been deleted. The app now ignores artwork
entirely, so these notes are future reference only.
