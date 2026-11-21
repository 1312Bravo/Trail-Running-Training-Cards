Add-Type -AssemblyName System.Drawing

$output = Join-Path $PSScriptRoot "../public/share-preview.png"
$image = New-Object System.Drawing.Bitmap(1200, 627)
$graphics = [System.Drawing.Graphics]::FromImage($image)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

$white = [System.Drawing.Color]::White
$ink = [System.Drawing.Color]::FromArgb(37, 37, 37)
$muted = [System.Drawing.Color]::FromArgb(88, 91, 84)
$gold = [System.Drawing.Color]::FromArgb(185, 154, 63)
$pale = [System.Drawing.Color]::FromArgb(251, 249, 242)
$inkBrush = New-Object System.Drawing.SolidBrush($ink)
$mutedBrush = New-Object System.Drawing.SolidBrush($muted)
$goldBrush = New-Object System.Drawing.SolidBrush($gold)
$paleBrush = New-Object System.Drawing.SolidBrush($pale)
$goldPen = New-Object System.Drawing.Pen($gold, 2)
$titleFont = New-Object System.Drawing.Font("Segoe UI", 56, [System.Drawing.FontStyle]::Bold)
$subtitleFont = New-Object System.Drawing.Font("Segoe UI", 22, [System.Drawing.FontStyle]::Regular)
$cardFont = New-Object System.Drawing.Font("Segoe UI", 21, [System.Drawing.FontStyle]::Regular)
$smallFont = New-Object System.Drawing.Font("Segoe UI", 17, [System.Drawing.FontStyle]::Regular)

try {
    $graphics.Clear($white)
    $graphics.FillRectangle($paleBrush, 0, 0, 1200, 18)
    $graphics.FillRectangle($goldBrush, 0, 18, 1200, 5)
    $graphics.DrawString("Run Companion Deck", $titleFont, $inkBrush, 85, 93)
    $graphics.DrawString("Explore training ideas. Build a connected pathway.", $subtitleFont, $mutedBrush, 90, 248)

    $labels = @("MACRO", "MEZZO", "MICRO", "SESSION")
    for ($index = 0; $index -lt $labels.Count; $index++) {
        $x = 86 + $index * 263
        $graphics.FillRectangle($paleBrush, $x, 356, 242, 151)
        $graphics.DrawRectangle($goldPen, $x, 356, 242, 151)
        $graphics.DrawString($labels[$index], $cardFont, $inkBrush, $x + 25, 381)
        $graphics.FillRectangle($goldBrush, $x + 25, 434, 75, 3)
        $graphics.DrawString(("★" * (4 - $index)), $smallFont, $goldBrush, $x + 25, 457)
    }

    $graphics.DrawString("RUN & TRAIN WITH DECK OF CARDS", $smallFont, $mutedBrush, 89, 548)
    $image.Save($output, [System.Drawing.Imaging.ImageFormat]::Png)
}
finally {
    $graphics.Dispose()
    $image.Dispose()
    $inkBrush.Dispose()
    $mutedBrush.Dispose()
    $goldBrush.Dispose()
    $paleBrush.Dispose()
    $goldPen.Dispose()
    $titleFont.Dispose()
    $subtitleFont.Dispose()
    $cardFont.Dispose()
    $smallFont.Dispose()
}
