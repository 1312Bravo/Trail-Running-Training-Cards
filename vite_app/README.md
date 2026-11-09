# Vite Web App

This is the browser-based interface for the training-card library. The Streamlit app remains available during the transition.

The Python package remains responsible for Google Drive sync, JSON validation, card schemas, and library authoring. The web app reads a public static bundle prepared from the validated local cache; no Drive credentials are used by the browser.

## Local development

Install the web dependencies once:

```powershell
pnpm install
```

Prepare the browser data from the validated local Drive cache and start the app:

```powershell
pnpm prepare:data
pnpm dev
```

Create a production build with:

```powershell
pnpm build
```

The generated `public/data/library.json` is ignored by Git because the accepted card library remains in Google Drive and the local cache remains a working copy. Before a public deployment, the hosting build needs to download or otherwise receive the current validated bundle, then run the web build.
