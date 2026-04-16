param([string]$TargetModel)

$envPath = "C:\Users\USER\AppData\Roaming\opencode-telegram-bot\.env"
$controlScript = "C:\Users\USER\AppData\Roaming\opencode-telegram-bot\opencode-telegram-bot-control.ps1"

# Gunakan provider 'opencode' agar auth menggunakan akun belajar.id via OpenCode Server
$provider = "opencode" 
$modelId = ""
$friendlyName = ""

if ($TargetModel -like "*gemini*") {
    # Model Gemini Flash terbaru yang tersedia di provider opencode
    $modelId = "gemini-3-flash" 
    $friendlyName = "Gemini Flash (via OpenCode Server)"
} elseif ($TargetModel -like "*pickle*") {
    # Model Big Pickle (Gemini Pro)
    $modelId = "big-pickle"
    $friendlyName = "Big Pickle (via OpenCode Server)"
} else {
    Write-Error "Model tidak dikenal."
    return
}

Write-Host "Mengonfigurasi bot ke mode: $friendlyName..." -ForegroundColor Cyan

$content = Get-Content $envPath
$newContent = $content -replace "OPENCODE_MODEL_PROVIDER=.*", "OPENCODE_MODEL_PROVIDER=$provider"
$newContent = $newContent -replace "OPENCODE_MODEL_ID=.*", "OPENCODE_MODEL_ID=$modelId"
$newContent | Set-Content $envPath

Write-Host "Merestart bot..." -ForegroundColor Yellow
powershell -ExecutionPolicy Bypass -File $controlScript restart

Write-Host "✅ Sukses! Bot sekarang menggunakan otak: $friendlyName" -ForegroundColor Green
