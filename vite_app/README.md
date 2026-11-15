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

The generated `public/data/library.json` is ignored by Git because the accepted card library remains in Google Drive and the local cache remains a working copy.

## Publish updated cards

After cards change in Google Drive, run this from the repository root:

```powershell
./vite_app/scripts/publish.ps1
```

The command downloads and validates the current Drive library, builds the Vite app, and creates `vite_app/training-cards-vite-dist.zip`. In the [existing Netlify project](https://app.netlify.com/projects/run-companion-deck), upload that ZIP as a new deploy. Upload to this project so the public URL stays `https://run-companion-deck.netlify.app/`. The ZIP and downloaded card cache are ignored by Git.

To publish from the same command, set a Netlify personal access token in your local terminal and add `-Deploy`:

```powershell
$env:NETLIFY_AUTH_TOKEN = "your-token"
./vite_app/scripts/publish.ps1 -Deploy
```

The script sends the built ZIP to the existing Netlify project and waits for Netlify to report that it is live. Keep the token in your terminal or a private credential store; do not put it in Git or the app's public environment. This deployment remains manual or command driven until a separate continuous deployment workflow is configured.
