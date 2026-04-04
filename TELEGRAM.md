# 📱 Panduan Lengkap: Integrasi OpenCode dengan Telegram

## Daftar Isi

1. [Pendahuluan](#pendahuluan)
2. [Arsitektur Sistem](#arsitektur-sistem)
3. [Persiapan Awal](#persiapan-awal)
4. [Instalasi OpenCode](#instalasi-opencode)
5. [Instalasi Telegram Bot](#instalasi-telegram-bot)
6. [Konfigurasi Telegram Bot](#konfigurasi-telegram-bot)
7. [Menjalankan Bot](#menjalankan-bot)
8. [Verifikasi & Troubleshooting](#verifikasi--troubleshooting)
9. [Menu Kontrol Otomatis](#menu-kontrol-otomatis)
   - [Bagian A: Script PowerShell](#bagian-a-script-powershell)
   - [Bagian B: Membuat Menu Skill OpenCode](#bagian-b-membuat-menu-skill-opencode-opsional)
   - [Bagian C: Script Control Lengkap](#bagian-c-script-control-lengkap)
10. [Cara Penggunaan](#cara-penggunaan)
11. [Tips & Trik](#tips--trik)

---

## Pendahuluan

### Apa itu OpenCode Telegram Bot?

OpenCode Telegram Bot adalah client Telegram untuk OpenCode CLI yang memungkinkan Anda:
- **Remote coding** - Kirim perintah coding dari mana saja via Telegram
- **Monitoring** - Lihat progress task secara real-time
- **Session management** - Kelola sesi coding dari hp
- **Model switching** - Ganti model AI langsung dari Telegram
- **Scheduled tasks** - Jadwalkan task untuk dijalankan otomatis

### Keunggulan

- 🔒 **Secure** - Tidak perlu membuka port, semua berjalan lokal
- 📱 **Mobile-friendly** - Kontrol OpenCode dari hp
- ⚡ **Real-time** - Lihat progress langsung
- 🌍 **Cross-platform** - Windows, macOS, Linux

---

## Arsitektur Sistem

```
┌─────────────────────────────────────────────────────────────────┐
│                         TELEGRAM                                │
│                    (@santo_xcode_bot)                          │
└─────────────────────────────┬───────────────────────────────────┘
                              │ Telegram Bot API (HTTPS/443)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              OpenCode Telegram Bot (@grinev)                   │
│                  (Node.js - Local)                              │
│                                                                 │
│  • Message handling                                            │
│  • Session management                                          │
│  • Command processing                                          │
└─────────────────────────────┬───────────────────────────────────┘
                              │ HTTP/4096
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                 OpenCode Server (Local)                        │
│                   Port: 4096                                   │
│                                                                 │
│  • AI Code Execution                                            │
│  • File Operations                                             │
│  • MCP Tools                                                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Persiapan Awal

### Kebutuhan Sistem

| Persyaratan | Detail |
|-------------|--------|
| **OS** | Windows 10/11, macOS, Linux |
| **Node.js** | versi 20 atau lebih baru |
| **npm** | versi 9 atau lebih baru |
| **OpenCode** | Sudah terinstall |
| **Akun Telegram** | Sudah memiliki akun |

### Cek Versi Node.js

Buka terminal/Command Prompt dan ketik:

```bash
node --version
npm --version
```

Hasilnya harus seperti:
```
v20.x.x atau lebih baru
9.x.x atau lebih baru
```

---

## Instalasi OpenCode

### Langkah 1: Install OpenCode

Jika belum install OpenCode, jalankan:

```bash
npm install -g opencode-ai
```

### Langkah 2: Verifikasi Instalasi

```bash
opencode --version
```

### Langkah 3: Setup Awal (Opsional)

```bash
opencode
```

Ikuti wizard untuk setup:
- Pilih model AI yang ingin digunakan
- Tentukan working directory
- Konfigurasi API keys jika diperlukan

---

## Instalasi Telegram Bot

### Langkah 1: Install Package

```bash
npm install -g @grinev/opencode-telegram-bot
```

Atau gunakan npx (tanpa install):

```bash
npx @grinev/opencode-telegram-bot
```

### Langkah 2: Verifikasi Instalasi

```bash
opencode-telegram --version
```

---

## Konfigurasi Telegram Bot

### Bagian A: Membuat Telegram Bot

#### 1. Buka BotFather

Di Telegram, cari dan buka **@BotFather**

#### 2. Buat Bot Baru

Kirim perintah:
```
/newbot
```

#### 3. Ikuti Instruksi

BotFather akan meminta:
1. **Nama bot** - Contoh: "X/Code Assistant"
2. **Username bot** - Contoh: `santo_xcode_bot` (harus unik dan berakhir dengan `bot`)

#### 4. Simpan Bot Token

Setelah berhasil, BotFather akan memberikan token seperti:
```
123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
```

**SIMPAN TOKEN INI** - akan digunakan untuk konfigurasi

---

### Bagian B: Mendapatkan User ID

#### 1. Buka UserInfoBot

Di Telegram, cari dan buka **@userinfobot**

#### 2. Kirim Pesan

Kirim pesan apapun ke bot tersebut

#### 3. Catat User ID

Bot akan membalas dengan informasi termasuk **ID** (angka panjang)
- Contoh: `1234567890`

**SIMPAN USER ID INI** - untuk whitelist

---

### Bagian C: Konfigurasi Environment

#### 1. Buat Directory Konfigurasi

```bash
# Windows
mkdir "%APPDATA%\opencode-telegram-bot"

# macOS/Linux
mkdir -p ~/Library/Application\ Support/opencode-telegram-bot
```

#### 2. Buat File .env

Buat file `.env` di directory konfigurasi dengan konten berikut:

```env
# ============================================
# OpenCode Telegram Bot Configuration
# ============================================

# Telegram Bot Token (dari @BotFather)
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN_HERE

# Telegram User ID yang diizinkan (dari @userinfobot)
TELEGRAM_ALLOWED_USER_ID=YOUR_USER_ID_HERE

# OpenCode Server URL
OPENCODE_API_URL=http://localhost:4096

# Default Model (sesuaikan dengan setup Anda)
OPENCODE_MODEL_PROVIDER=opencode
OPENCODE_MODEL_ID=big-pickle

# Bahasa UI (en, de, es, fr, ru, zh)
BOT_LOCALE=en

# Log Level (debug, info, warn, error)
LOG_LEVEL=info
```

#### 3. Ganti Nilai Konfigurasi

Ganti `YOUR_BOT_TOKEN_HERE` dan `YOUR_USER_ID_HERE` dengan nilai sebenarnya:

Contoh hasil akhir:
```env
TELEGRAM_BOT_TOKEN=8726299618:AAFX_ZEQO-5oW-8uhlxc5wIv0rl2Go55swE
TELEGRAM_ALLOWED_USER_ID=6776956601
OPENCODE_API_URL=http://localhost:4096
OPENCODE_MODEL_PROVIDER=opencode
OPENCODE_MODEL_ID=big-pickle
BOT_LOCALE=en
LOG_LEVEL=info
```

---

## Menjalankan Bot

### Langkah 1: Jalankan OpenCode Server

Buka terminal baru dan jalankan:

```bash
opencode serve
```

Akan muncul output:
```
Warning: OPENCODE_SERVER_PASSWORD is not set; server is unsecured.
opencode server listening on http://127.0.0.1:4096
```

**Catatan:** Biarkan terminal ini terbuka

### Langkah 2: Jalankan Telegram Bot

Buka terminal baru (atau tab baru) dan jalankan:

```bash
opencode-telegram start
```

Akan muncul output:
```
[INFO] Starting OpenCode Telegram Bot v0.14.x...
[INFO] Config loaded from C:\Users\XCODE\AppData\Roaming\opencode-telegram-bot\.env
[INFO] Allowed User ID: 6776956601
[INFO] Bot @your_bot_username started!
```

### Langkah 3: Verifikasi di Telegram

1. Buka Telegram
2. Cari bot Anda (contoh: `@santo_xcode_bot`)
3. Kirim pesan pertama, misalnya: `Hello`

Bot harusnya merespon!

---

## Verifikasi & Troubleshooting

### Cara Cek Status Bot

#### via Terminal

```bash
# Cek apakah OpenCode server running
netstat -ano | grep 4096

# Cek apakah Telegram bot running
ps aux | grep opencode-telegram
```

#### via Telegram API

```bash
# Cek info bot
curl https://api.telegram.org/bot<TOKEN>/getMe

# Cek updates
curl https://api.telegram.org/bot<TOKEN>/getUpdates
```

#### Kirim Test Message

```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" \
  -d "chat_id=<USER_ID>" \
  -d "text=Test message from bot!"
```

### Masalah Umum dan Solusi

#### 1. Bot Tidak Merespon Pesan

**Penyebab:** User ID tidak cocok

**Solusi:**
1. Cek user ID Anda di @userinfobot
2. Pastikan `TELEGRAM_ALLOWED_USER_ID` di .env sesuai
3. Restart bot

```bash
# Stop bot
pkill -f opencode-telegram

# Start ulang
opencode-telegram start
```

#### 2. "OpenCode server is not available"

**Penyebab:** OpenCode server tidak berjalan

**Solusi:**
```bash
opencode serve
```

#### 3. Tidak Ada Model di Model Picker

**Penyebab:** Belum ada model di favorites

**Solusi:**
1. Buka OpenCode (`opencode`)
2. Pilih model
3. Tekan `Ctrl+F` untuk add ke favorites

#### 4. Bot Running tapi Tidak Bisa Kirim Pesan

**Penyebab:** Privacy mode masih aktif

**Solusi:**
1. Buka @BotFather
2. Kirim `/setprivacy`
3. Pilih bot Anda
4. Pilih **"Disable privacy"**

---

## Menu Kontrol Otomatis

### Bagian A: Script PowerShell

Saya sudah membuatkan script kontrol otomatis. File terletak di:
- `C:\Users\XCODE\.config\opencode\opencode-telegram-bot-control.ps1`

### Cara Penggunaan

#### Via PowerShell

```powershell
# Pindah ke directory
cd C:\Users\XCODE\.config\opencode

# Lihat status
.\opencode-telegram-bot-control.ps1 status

# Start bot
.\opencode-telegram-bot-control.ps1 start

# Stop bot
.\opencode-telegram-bot-control.ps1 stop

# Restart bot
.\opencode-telegram-bot-control.ps1 restart
```

#### Via Batch File

```cmd
cd C:\Users\XCODE\.config\opencode

# Status
bot status

# Start
bot start

# Stop
bot stop
```

### Menu Skill OpenCode

Saya juga sudah membuatkan skill menu untuk OpenCode yang terletak di:
- `C:\Users\XCODE\.config\opencode\skills\opencode-telegram-bot-control\SKILL.md`

Skill ini akan auto-loaded saat OpenCode dimulai dan menyediakan menu interaktif untuk kontrol bot.

---

### Bagian B: Membuat Menu Skill OpenCode (Opsional)

Jika Anda ingin membuat menu skill sendiri, berikut langkah-langkahnya:

#### 1. Lokasi Skill

Skills OpenCode terletak di:
```
%APPDATA%\.config\opencode\skills\
```

Atau di Linux/macOS:
```
~/.config/opencode/skills/
```

#### 2. Struktur Folder

Buat folder baru untuk skill:
```
opencode-telegram-bot-control/
└── SKILL.md
```

#### 3. Format File SKILL.md

```markdown
---
name: opencode-telegram-bot-control
description: "Menu interaktif untuk mengontrol OpenCode Telegram Bot"
license: MIT
compatibility: opencode
metadata:
  audience: sd-operator
  workflow: development
  source: custom
---

# 🤖 OpenCode Telegram Bot Control

## Deskripsi

Menu ini menyediakan opsi untuk mengontrol bot.

## Menu Interaktif

Ketika user meminta mengontrol bot, TAMPILKAN MENU INI:

```
╔════════════════════════════════════╗
║  🤖 Bot Control Menu               ║
╠════════════════════════════════════╣
║  1. 📊 Status    - Lihat status    ║
║  2. ▶️  Start    - Mulai bot       ║
║  3. ⏹️  Stop     - Hentikan bot    ║
║  4. 🔄 Restart  - Restart bot       ║
╚════════════════════════════════════╝
```

## Cara Penggunaan

Ketik perintah:
| Perintah | Aksi |
|----------|------|
| bot status | Lihat status |
| bot start | Mulai bot |
| bot stop | Hentikan bot |
| bot restart | Restart bot |
```

#### 4. Auto-Load Skill

Skill di folder `~/.config/opencode/skills/` akan otomatis ter-load saat OpenCode dimulai.

#### 5. Verifikasi Skill Terload

Buka OpenCode dan coba ketik nama skill atau perintah yang相关的. Skill akan muncul di menu.

---

### Bagian C: Script Control Lengkap

Selain skill, Anda juga bisa menggunakan script PowerShell langsung:

#### File: opencode-telegram-bot-control.ps1

```powershell
# OpenCode Telegram Bot Control Script

param(
    [string]$Action = "status"
)

$ErrorActionPreference = "Continue"

function Get-BotStatus {
    Write-Host "`n=== OpenCode Telegram Bot Status ===" -ForegroundColor Cyan
    
    # Check if OpenCode server is running (port 4096 or 2804)
    $opencodePort = Get-NetTCPConnection -LocalPort 4096,2804 -ErrorAction SilentlyContinue
    if ($opencodePort) {
        Write-Host "[OK] OpenCode server is listening" -ForegroundColor Green
    } else {
        Write-Host "[NOT RUNNING] OpenCode server" -ForegroundColor Red
    }
    
    # Check config
    $configPath = "$env:APPDATA\opencode-telegram-bot\.env"
    if (Test-Path $configPath) {
        Write-Host "[OK] Config file exists" -ForegroundColor Green
    } else {
        Write-Host "[NOT FOUND] Config file" -ForegroundColor Red
    }
    
    Write-Host "`nBot: @santo_xcode_bot" -ForegroundColor White
    Write-Host "User ID: 6776956601`n" -ForegroundColor White
}

function Start-OpenCodeServer {
    Write-Host "Starting OpenCode server..." -ForegroundColor Cyan
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "opencode serve" -WindowStyle Normal
    Start-Sleep 3
    Write-Host "OpenCode server started on http://localhost:4096" -ForegroundColor Green
}

function Start-TelegramBot {
    Write-Host "Starting OpenCode Telegram Bot..." -ForegroundColor Cyan
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "opencode-telegram start" -WindowStyle Normal
    Start-Sleep 3
    Write-Host "Telegram bot started: @santo_xcode_bot" -ForegroundColor Green
}

function Stop-TelegramBot {
    Write-Host "Stopping OpenCode Telegram Bot..." -ForegroundColor Yellow
    
    # Find node processes related to opencode-telegram
    $nodeProcesses = Get-WmiObject Win32_Process -Filter "Name='node.exe'" | Where-Object {
        $_.CommandLine -like "*opencode-telegram*" -or $_.CommandLine -like "*@grinev*"
    }
    
    if ($nodeProcesses) {
        foreach ($proc in $nodeProcesses) {
            Write-Host "   Stopping process ID: $($proc.ProcessId)" -ForegroundColor Gray
            Stop-Process -Id $proc.ProcessId -Force -ErrorAction SilentlyContinue
        }
        Write-Host "Telegram bot stopped" -ForegroundColor Green
    } else {
        Write-Host "No Telegram bot process found" -ForegroundColor Yellow
    }
}

# Execute action
switch ($Action.ToLower()) {
    "start" { 
        Start-OpenCodeServer
        Start-TelegramBot
    }
    "start-server" { Start-OpenCodeServer }
    "start-bot" { Start-TelegramBot }
    "stop" { Stop-TelegramBot }
    "status" { Get-BotStatus }
    "restart" { 
        Stop-TelegramBot
        Start-Sleep 2
        Start-OpenCodeServer
        Start-TelegramBot
    }
    default { 
        Write-Host "OpenCode Telegram Bot Control" -ForegroundColor Cyan
        Write-Host "Usage: .\opencode-telegram-bot-control.ps1 [action]`n" -ForegroundColor White
        Write-Host "Actions:" -ForegroundColor Cyan
        Write-Host "  start         - Start both OpenCode server and Telegram bot"
        Write-Host "  start-server  - Start OpenCode server only"
        Write-Host "  start-bot     - Start Telegram bot only"
        Write-Host "  stop          - Stop Telegram bot"
        Write-Host "  status        - Show status (default)"
        Write-Host "  restart       - Restart bot"
    }
}
```

#### Cara Pakai Script

```powershell
# Simpan script ke
C:\Users\XCODE\.config\opencode\opencode-telegram-bot-control.ps1

# Kemudian jalankan
cd C:\Users\XCODE\.config\opencode

# Start everything
.\opencode-telegram-bot-control.ps1 start

# Check status
.\opencode-telegram-bot-control.ps1 status

# Stop bot
.\opencode-telegram-bot-control.ps1 stop

# Restart
.\opencode-telegram-bot-control.ps1 restart
```

#### Alternatif: Batch File (bot.bat)

```bat
@echo off
REM OpenCode Telegram Bot Control

if "%1"=="" goto status
if "%1"=="start" goto start
if "%1"=="stop" goto stop
if "%1"=="status" goto status
if "%1"=="restart" goto restart

:start
echo Starting OpenCode Telegram Bot...
start powershell -NoExit -Command "opencode serve"
timeout /t 3 /nobreak >nul
start powershell -NoExit -Command "opencode-telegram start"
echo Bot started!
goto end

:stop
echo Stopping Telegram Bot...
powershell -Command "Get-Process -Name 'node' -ErrorAction SilentlyContinue | Where-Object {$_.MainModule.FileName -like '*opencode-telegram*'} | Stop-Process -Force"
echo Bot stopped!
goto end

:status
echo.
echo === OpenCode Telegram Bot Status ===
echo Bot: @santo_xcode_bot
echo User ID: 6776956601
goto end

:restart
echo Restarting Telegram Bot...
goto stop
timeout /t 2 /nobreak >nul
goto start

:end
```

#### Jalankan Batch File

```cmd
cd C:\Users\XCODE\.config\opencode
bot status
bot start
bot stop
bot restart
```

---

Skill ini akan auto-loaded saat OpenCode dimulai dan menyediakan menu interaktif untuk kontrol bot.

---

## Cara Penggunaan

### Command Dasar di Telegram

| Command | Deskripsi |
|---------|-----------|
| `/status` | Lihat status server, project, session |
| `/new` | Buat sesi baru |
| `/abort` | Batalkan task sedang berjalan |
| `/sessions` | Lihat dan switch sesi |
| `/projects` | Switch project |
| `/tts` | Toggle audio replies |
| `/help` | Lihat semua command |

### Mengirim Task Coding

Cara termudah adalah langsung mengirim pesan prompt:

**Contoh:**
1. Kirim: `"Buat file hello.txt dengan isi Hello World"`
2. Bot akan:
   - Mengirim ke OpenCode server
   - Mengeksekusi task
   - Mengirim hasil balik ke Telegram
   - Jika ada file dibuat, bisa dikirim sebagai dokumen

### Fitur Lanjutan

#### 1. Voice Messages
Jika configure STT (Speech-to-Text):
- Kirim voice message
- Bot akan transcribe dan eksekusi

#### 2. File Attachments
- Kirim gambar/PDF/code
- Bot akan proses dan gunakan sebagai konteks

#### 3. Scheduled Tasks
Buat task terjadwal dengan `/task`:
- Untuk periodic code maintenance
- Untuk automated checks

#### 4. Model Switching
Ganti model langsung dari Telegram:
1. Ketik `/models` atau pilih dari menu
2. Pilih model yang ingin digunakan
3. Task berikutnya akan menggunakan model tersebut

---

## Tips & Trik

### 1. Running di Background (Windows)

Gunakan PowerShell untuk menjalankan di background:

```powershell
# Start sebagai background process
Start-Process powershell -ArgumentList "-NoExit", "-Command", "opencode serve"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "opencode-telegram start"
```

### 2. Running sebagai Service (Linux/macOS)

Gunakan screen atau tmux:

```bash
# Install screen jika belum
apt install screen  # Ubuntu/Debian
brew install screen # macOS

# Buat screen session
screen -S opencode

# Jalankan OpenCode server
opencode serve

# Ctrl+A, D untuk detach

# Buat screen session baru untuk bot
screen -S telegram-bot

# Jalankan bot
opencode-telegram start

# Ctrl+A, D untuk detach
```

### 3. Auto-start saat Boot (Windows)

Buat Task Scheduler:
1. Buka Task Scheduler
2. Create Basic Task
3. Set trigger: "At log on"
4. Action: "Start a program"
5. Program: `powershell.exe`
6. Arguments: `-NoExit -Command "opencode serve; opencode-telegram start"`

### 4. Keamanan

- **JANGAN** share bot token ke orang lain
- Pastikan `TELEGRAM_ALLOWED_USER_ID` benar
- Bot hanya merespon dari user yang di-whitelist
- Semua eksekusi terjadi secara lokal

### 5. Monitoring

Cek log di:
- Windows: `%APPDATA%\opencode-telegram-bot\logs\`
- macOS: `~/Library/Application Support/opencode-telegram-bot/logs/`
- Linux: `~/.config/opencode-telegram-bot/logs/`

---

## Konfigurasi Lanjutan

### Environment Variables Lengkap

```env
# Required
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_ALLOWED_USER_ID=your_user_id

# Optional - OpenCode Server
OPENCODE_API_URL=http://localhost:4096
OPENCODE_SERVER_USERNAME=opencode
OPENCODE_SERVER_PASSWORD=your_password

# Optional - Model
OPENCODE_MODEL_PROVIDER=opencode
OPENCODE_MODEL_ID=big-pickle

# Optional - UI
BOT_LOCALE=en  # en, de, es, fr, ru, zh
LOG_LEVEL=info

# Optional - Limits
SESSIONS_LIST_LIMIT=10
PROJECTS_LIST_LIMIT=10
TASK_LIMIT=10
SERVICE_MESSAGES_INTERVAL_SEC=5

# Optional - Voice (STT)
STT_API_URL=https://api.openai.com/v1
STT_API_KEY=your_api_key
STT_MODEL=whisper-1

# Optional - Voice (TTS)
TTS_API_URL=https://api.openai.com/v1
TTS_API_KEY=your_api_key
TTS_MODEL=gpt-4o-mini-tts
TTS_VOICE=alloy
```

### Proxy Configuration

Jika perlu gunakan proxy:

```env
TELEGRAM_PROXY_URL=socks5://proxy:1080
```

---

## Referensi

### Link Resmi

- **OpenCode Telegram Bot:** https://github.com/grinev/opencode-telegram-bot
- **npm Package:** https://www.npmjs.com/package/@grinev/opencode-telegram-bot
- **OpenCode Official:** https://opencode.ai

### Command Reference

```
/start        - Welcome message
/help         - Help information
/status       - Server status
/sessions     - List sessions
/projects     - List projects
/new          - New session
/abort        - Abort task
/tts          - Toggle TTS
/clear        - Clear session
/rename       - Rename session
/task         - Create scheduled task
/tasklist     - List scheduled tasks
/commands     - List custom commands
```

---

## Catatan

Dokumen ini dibuat untuk memudahkan integrasi OpenCode dengan Telegram menggunakan @grinev/opencode-telegram-bot.

**Versi:** 1.0
**Tanggal:** 3 April 2026
**Author:** Santo X/Code (SD Operator & Web Developer)

---

Happy Coding! 🚀
