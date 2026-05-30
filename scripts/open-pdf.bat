@echo off
setlocal enabledelayedexpansion

REM Ambil file path dari argumen
set "file=%~1"

REM Konversi backslash ke forward slash untuk URL
set "url=file:///%file:\=/%"

REM Coba buka dengan Arc via default handler dulu
rundll32 url.dll,FileProtocolHandler "%file%" >nul 2>&1

REM Jika gagal, fallback ke Microsoft Edge (built-in Windows)
if errorlevel 1 (
    start "" microsoft-edge:"!url!" >nul 2>&1
)

REM Jika masih gagal, fallback ke Windows default handler
if errorlevel 1 (
    start "" "%file%" >nul 2>&1
)

endlocal
