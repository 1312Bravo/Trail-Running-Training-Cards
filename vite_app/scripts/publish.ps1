param(
    [switch]$Deploy,
    [string]$SiteId = "47c9d56d-15ed-40d6-92b7-330ae74c1fbc"
)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path
$viteRoot = Join-Path $repoRoot "vite_app"
$python = Join-Path $repoRoot ".venv/Scripts/python.exe"
$archive = Join-Path $viteRoot "training-cards-vite-dist.zip"

if ($Deploy -and -not $env:NETLIFY_AUTH_TOKEN) {
    throw "Set NETLIFY_AUTH_TOKEN in this terminal before using -Deploy. The token must not be saved in the repository."
}
if (-not (Test-Path -LiteralPath $python)) {
    throw "Python environment missing. Create .venv and install requirements.txt first."
}
if (-not (Get-Command pnpm -ErrorAction SilentlyContinue)) {
    throw "pnpm is required to build the Vite app."
}

Push-Location $repoRoot
try {
    & $python -m training_cards.scripts.cloud.download_cloud_library
    if ($LASTEXITCODE -ne 0) { throw "Google Drive download failed." }

    & $python -m training_cards.scripts.cache.validate_cache
    if ($LASTEXITCODE -ne 0) { throw "Card validation failed." }

    Push-Location $viteRoot
    try {
        if (-not (Test-Path -LiteralPath (Join-Path $viteRoot "node_modules"))) {
            & pnpm install --frozen-lockfile
            if ($LASTEXITCODE -ne 0) { throw "Dependency installation failed." }
        }
        & pnpm build
        if ($LASTEXITCODE -ne 0) { throw "Vite build failed." }
    }
    finally { Pop-Location }

    Compress-Archive -Path (Join-Path $viteRoot "dist/*") -DestinationPath $archive -Force
    Write-Host "Ready to upload: $archive"

    if ($Deploy) {
        $headers = @{ Authorization = "Bearer $env:NETLIFY_AUTH_TOKEN" }
        $uri = "https://api.netlify.com/api/v1/sites/$SiteId/deploys"
        $result = Invoke-RestMethod -Method Post -Uri $uri -Headers $headers -ContentType "application/zip" -InFile $archive
        if (-not $result.id) { throw "Netlify did not return a deploy ID." }

        for ($attempt = 0; $attempt -lt 30; $attempt++) {
            $status = Invoke-RestMethod -Method Get -Uri "https://api.netlify.com/api/v1/deploys/$($result.id)" -Headers $headers
            if ($status.state -eq "ready") {
                $liveUrl = if ($status.ssl_url) { $status.ssl_url } else { $status.url }
                Write-Host "Published: $liveUrl"
                return
            }
            if ($status.state -in @("error", "failed")) { throw "Netlify deploy failed: $($status.state)" }
            Start-Sleep -Seconds 2
        }
        throw "Netlify did not confirm the deploy within one minute. Check the deploy in the Netlify dashboard."
    }
}
finally { Pop-Location }
