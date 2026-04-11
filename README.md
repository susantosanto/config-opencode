# ⚙️ OpenCode Configuration

Konfigurasi personal untuk OpenCode AI - dikustomasi untuk Operator Sekolah & Web Developer.

---

## 📋 Contents

- [Tentang](#-tentang)
- [Panduan Install dari 0](#-panduan-install-dari-0)
- [Struktur Folder](#-struktur-folder)
- [Fitur & MCP](#-fitur--mcp)
- [Plugin](#-plugin)
- [Custom Skills](#-custom-skills)
- [Agent Configuration](#-agent-configuration)
- [OpenClaw Integration](#-openclaw-integration)
- [Telegram Bot](#-telegram-bot)
- [Cara Penggunaan](#-cara-penggunaan)
- [Troubleshooting](#-troubleshooting)

---

## 🔧 Tentang

Konfigurasi ini dibuat untuk:
- **Operator Sekolah Dasar** - Administrasi, BOS, Dapodik
- **Web Developer** - JavaScript, Google Apps Script
- **AI Engineering Learner** - Prompt Engineering, Agentic AI

---

## 🚀 Panduan Install dari 0

### Prerequisites

| Komponen | Versi Minimum | Keterangan |
|----------|---------------|------------|
| **Node.js** | v20+ | Runtime utama |
| **npm** | v9+ | Package manager |
| **Python** | 3.13+ | Untuk Excel MCP, Vision MCP |
| **Git** | terbaru | Version control |
| **uv** | terbaru | Python package manager (untuk Windows MCP, PDF MCP) |

### Langkah 1: Install OpenCode

```bash
# Install OpenCode CLI secara global
npm install -g opencode-ai

# Verifikasi instalasi
opencode --version
```

### Langkah 2: Setup Konfigurasi

```bash
# Clone repository konfigurasi
git clone https://github.com/[YOUR-USERNAME]/opencode-config.git
cd opencode-config

# Copy semua file ke folder config OpenCode
xcopy /E /I /Y . "%USERPROFILE%\.config\opencode\"

# Install dependencies
npm install
```

### Langkah 3: Install MCP Servers

```bash
# === Node.js based MCP ===
npm install -g @modelcontextprotocol/server-memory
npm install -g @modelcontextprotocol/server-sequential-thinking
npm install -g mcp-fetch-server
npm install -g git-mcp-server
npm install -g mcp-time
npm install -g excel-mcp-server
npm install -g doc-tools-mcp
npm install -g google-spreadsheet-mcp
npm install -g superpowers-mcp

# === Python based MCP ===
# Pastikan Python 3.13+ sudah terinstall
pip install excel-mcp
pip install vision-mcp-server

# === uvx based MCP ===
# Install uv terlebih dahulu: https://docs.astral.sh/uv/
uvx windows-mcp --help  # Verifikasi
uvx mcp-pdf --help       # Verifikasi

# === Custom MCP ===
# Windows Desktop Automation
git clone https://github.com/[repo]/mcp-windows-desktop-automation.git
cd mcp-windows-desktop-automation
npm install
```

### Langkah 4: Install OpenClaw

Lihat section [OpenClaw Integration](#-openclaw-integration) di bawah untuk panduan lengkap.

### Langkah 5: Verifikasi

```bash
# Jalankan OpenCode
opencode

# Semua MCP servers akan otomatis ter-connect saat startup
# Cek status di dalam OpenCode TUI
```

---

## 📁 Struktur Folder

```
opencode-config/
├── opencode.json              # Konfigurasi utama (MCP, skills, plugins, agents)
├── AGENTS.md                  # System prompt utama
├── SYSTEM_PROMPT.md           # User profile & identitas
├── user-settings.json         # Settings tambahan (theme, agents, context paths)
├── dapodik_config.json        # Konfigurasi Dapodik (token, NPSN, URL)
├── playwright-config.json     # Konfigurasi Playwright browser
├── opencode-image-proxy.json  # Konfigurasi image reader untuk model incapable
├── oh-my-opencode-slim.json   # Konfigurasi Oh-My-Opencode preset
├── .gitignore                 # Git ignore rules
├── package.json               # NPM dependencies
├── package-lock.json          # NPM lock file
├── bun.lock                   # Bun lock file
├── TELEGRAM.md                # Dokumentasi lengkap Telegram Bot
├── skills/                    # Custom skills lokal (19 skills)
│   ├── agent-models/
│   ├── agent-table/
│   ├── ai-engineer-path/
│   ├── dapodik-gtk-lookup/
│   ├── dapodik-scraper/
│   ├── dapodik-student-lookup/
│   ├── excel-live-editing/
│   ├── opencode-system-prompt/
│   ├── skill-list-install/
│   ├── superpowers-brainstorm/
│   ├── superpowers-code-review/
│   ├── superpowers-finish/
│   ├── superpowers-menu/
│   ├── superpowers-subagent/
│   ├── superpowers-systematic-debugging/
│   ├── superpowers-tdd/
│   ├── superpowers-writing-plans/
│   ├── surat-pindah/
│   └── task-workflow/
├── oh-my-opencode-slim/       # Plugin oh-my-opencode
├── dapodik_analyze.py         # Script analisis Dapodik
├── dapodik_explore.py         # Script eksplorasi Dapodik
└── dapodik_rest_test.py       # Script test REST API Dapodik
```

---

## 🤖 Fitur & MCP

### MCP Servers Aktif (18 servers):

| MCP | Type | Command | Fungsi |
|-----|------|---------|--------|
| `filesystem` | local | `playwright-mcp --browser chromium --headless` | Browser automation (Chromium headless) |
| `chrome-devtools` | local | `chrome-devtools-mcp --headless` | Chrome DevTools protocol (headless) |
| `memory` | local | `@modelcontextprotocol/server-memory` | Knowledge graph storage |
| `sequential-thinking` | local | `@modelcontextprotocol/server-sequential-thinking` | Structured reasoning |
| `fetch` | local | `mcp-fetch-server` | Web fetching |
| `git` | local | `git-mcp-server` | Version control |
| `time` | local | `mcp-time` | Time & timezone utilities |
| `context7` | remote | `https://mcp.context7.com/mcp` | Documentation lookup (**disabled** by default) |
| `excel-control` | local | `excel-mcp-server` | Live Excel editing via COM |
| `excel-mcp` | local | `python -m excel_mcp stdio` | Python Excel operations (Python 3.13) |
| `word` | local | `doc-tools-mcp` | Word document processing |
| `google-sheets` | local | `google-spreadsheet-mcp` | Google Sheets API (service account) |
| `windows-mcp` | local | `uvx windows-mcp --transport stdio` | Windows automation (via uvx) |
| `windows-desktop-automation` | local | Node.js custom path | Desktop UI automation |
| `openclaw` | local | `openclaw-mcp --openclaw-url http://127.0.0.1:18789` | OpenClaw integration |
| `winapp-mcp` | local | `winapp-mcp` | Windows app UI automation |
| `shell` | local | `super-shell-mcp` | Shell execution |
| `pdf` | local | `uvx mcp-pdf` | PDF processing (via uvx) |
| `superpowers` | local | `superpowers-mcp` | Superpowers MCP server |
| `vision-mcp-server` | local | `python -m vision_mcp_server.server` | Image analysis (GROQ API) |

### Environment Variables yang Diperlukan:

| Variable | Sumber | Digunakan Oleh |
|----------|--------|----------------|
| `GROQ_API_KEY` | [groq.com](https://groq.com) | `vision-mcp-server` |
| `GOOGLE_SERVICE_ACCOUNT_KEY_PATH` | `C:\Users\USER\.openclaw\credentials\google-service-account.json` | `google-sheets` |

---

## 🔌 Plugin

| Plugin | Sumber | Fungsi |
|--------|--------|--------|
| `superpowers` | `git+https://github.com/obra/superpowers.git` | Multi-agent workflow (brainstorming, TDD, debugging, dll) |
| `@warp-dot-dev/opencode-warp` | npm | Warp integration |
| `oh-my-opencode-slim` | `file:///C:/Users/USER/.config/opencode/oh-my-opencode-slim` | Preset model configuration (minimax preset) |
| `opencode-qwen-cli-auth` | npm (`^3.1.2`) | Qwen authentication provider |

---

## 🎯 Custom Skills

### Skill Paths:
| Path | Deskripsi |
|------|-----------|
| `C:/Users/USER/.config/opencode/skills` | Skills lokal (19 skills) |

### Superpowers Skills (via Plugin):
| Skill | Fungsi |
|-------|--------|
| `brainstorming` | Socratic design refinement sebelum implementasi |
| `systematic-debugging` | 4-phase debugging sebelum fix |
| `writing-plans` | Implementation planning sebelum coding |
| `test-driven-development` | TDD workflow - test dulu, baru production code |
| `requesting-code-review` | Pre-merge code review |
| `receiving-code-review` | Menerima dan memproses feedback review |
| `subagent-driven-development` | Multi-agent parallel execution |
| `finishing-a-development-branch` | Merge/PR/cleanup workflow |
| `verification-before-completion` | Pre-commit verification |
| `executing-plans` | Plan execution dengan review checkpoints |
| `using-git-worktrees` | Git worktree management |
| `using-superpowers` | Superpowers workflow entry point |
| `dispatching-parallel-agents` | Parallel task execution |

### Custom Skills (Lokal):
| Skill | Fungsi |
|-------|--------|
| `dapodik-scraper` | Download data peserta didik dari Dapodik Web Service |
| `dapodik-gtk-lookup` | Cari data GTK dari Dapodik Web Service |
| `dapodik-student-lookup` | Cari data siswa dari Dapodik Web Service |
| `surat-pindah` | Buat surat pindah sekolah otomatis |
| `opencode-system-prompt` | Kelola system prompt (5 versi tersedia) |
| `ai-engineer-path` | Learning path AI Engineer 90 hari |
| `agent-table` | Tabel agent model shortcut |
| `skill-list-install` | Menu installer skills dari skills.sh |
| `task-workflow` | 6-phase workflow otomatis |
| `excel-live-editing` | Live editing Excel |
| `superpowers-*` | Wrapper lokal untuk superpowers skills |
| `agent-models` | Konfigurasi model per agent |

---

## 🤖 Agent Configuration

### Primary Agent (Orchestrator):
| Setting | Value |
|---------|-------|
| **Model** | `opencode/minimax-m2.5-free` |
| **Temperature** | 0.3 |
| **Tools** | task ✅, write ✅, edit ✅, read ✅, bash ❌ |
| **Permission** | task deny all (subagent task dibatasi) |

### Subagents:
| Agent | Model | Fungsi | Status |
|-------|-------|--------|--------|
| `researcher-dapodik` | `google/gemini-2.5-flash-lite` | Cari data GTK & Peserta Didik | ❌ disabled |
| `coder-dokumen` | `opencode/minimax-m2.5-free` | Buat surat, laporan, dokumen | ❌ disabled |
| `analyzer` | `openrouter/z-ai/glm-4.5-air:free` | Analisis kompleks, debug | ❌ disabled |
| `validator` | `opencode/nemotron-3-super-free` | Validasi dokumen | ❌ disabled |
| `explorer` | `opencode/big-pickle` | Explore project, long context | ❌ disabled |
| `flash-research` | `google/gemini-2.5-flash` | Quick research & lookup | ❌ disabled |
| `web-developer` | `opencode/minimax-m2.5-free` | JavaScript, React, debugging | ❌ disabled |
| `ai-learner` | `opencode/nemotron-3-super-free` | Belajar prompt engineering, AI | ❌ disabled |
| `system-checker` | `openrouter/z-ai/glm-4.5-air:free` | Cek error config, diagnostics | ❌ disabled |

> **Note:** Semua subagent dalam status **disabled** by default. Aktifkan sesuai kebutuhan di `opencode.json`.

### Oh-My-Opencode Preset (minimax):
| Agent | Model | Variant | MCPs |
|-------|-------|---------|------|
| `orchestrator` | minimax-m2.5-free | high | all |
| `oracle` | minimax-m2.5-free | high | none |
| `librarian` | minimax-m2.5-free | low | websearch, context7 |
| `explorer` | minimax-m2.5-free | low | none |
| `designer` | minimax-m2.5-free | medium | agent-browser |
| `fixer` | minimax-m2.5-free | low | none |

---

## 🦞 OpenClaw Integration

### Apa itu OpenClaw?

OpenClaw adalah AI gateway autonom yang berjalan sebagai service lokal, menyediakan:
- **Multi-provider AI** - Google, Qwen, Groq, OpenRouter, Mistral, OpenCode
- **Telegram Bot** built-in - Remote access via Telegram
- **MCP Server Hub** - Excel, Word, PDF, Google Workspace, Playwright, Security Tools
- **Workspace Management** - File system, knowledge base, skills
- **Gateway API** - Port `18789` untuk integrasi dengan OpenCode

### Arsitektur Integrasi

```
┌──────────────────────────────────────────────────────────────┐
│                        Telegram                              │
│                   (@santo_xcode_bot)                         │
└──────────────────────────┬───────────────────────────────────┘
                           │ Telegram Bot API
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                    OpenClaw Gateway                          │
│                  Port: 18789 (loopback)                      │
│                                                              │
│  • Multi-provider AI (Google, Qwen, Groq, OpenRouter)       │
│  • MCP Servers (Excel, Word, PDF, Sheets, Drive, etc.)      │
│  • Telegram Bot Integration                                 │
│  • Workspace & Skills Management                            │
│  • Hooks: session-memory, command-logger, boot-md           │
└───────────┬──────────────────────────────┬───────────────────┘
            │ openclaw-mcp                 │ HTTP API
            ▼                              ▼
┌───────────────────────┐    ┌─────────────────────────────────┐
│    OpenCode CLI       │    │  External Tools / Scripts       │
│  (MCP Client)         │    │  (curl, webhooks, etc.)         │
└───────────────────────┘    └─────────────────────────────────┘
```

### Cara Install OpenClaw dari 0

#### Langkah 1: Install OpenClaw

```bash
# Install via npm (global)
npm install -g openclaw

# Atau gunakan installer resmi
# Kunjungi: https://openclaw.ai (cek docs resmi untuk cara terbaru)
```

#### Langkah 2: Setup Awal

```bash
# Jalankan wizard setup
openclaw onboard

# Wizard akan meminta:
# - API keys untuk berbagai provider (Google, Qwen, OpenRouter, dll)
# - Telegram bot token (dari @BotFather)
# - Workspace directory
```

#### Langkah 3: Konfigurasi OpenClaw

File konfigurasi: `C:\Users\USER\.openclaw\openclaw.json`

Konfigurasi yang sudah terpasang:
| Komponen | Setting |
|----------|---------|
| **Gateway Port** | `18789` (loopback) |
| **Auth Mode** | `token` |
| **Primary Model** | `groq/llama-3.3-70b-versatile` |
| **Fallback Models** | `gemini-2.5-flash-lite`, `llama-3.1-8b-instant`, `kimi-k2.5` |
| **Workspace** | `C:\Users\USER\.openclaw\workspace` |
| **Telegram** | Enabled (DM policy: allowlist) |
| **Allowed User ID** | `6776956601` |

#### Langkah 4: Setup Provider API Keys

```bash
# Buka konfigurasi
notepad "%USERPROFILE%\.openclaw\openclaw.json"

# Pastikan auth profiles sudah terkonfigurasi:
# - opencode:default (API key)
# - openrouter:default (API key)
# - google:default (API key)
# - groq: API key (gratis, signup di groq.com)
# - qwen: Dashscope API key
```

#### Langkah 5: Jalankan OpenClaw Gateway

```bash
# Via batch file (sudah tersedia)
"%USERPROFILE%\.openclaw\start-gateway-user.bat"

# Atau langsung
openclaw gateway

# Gateway akan berjalan di http://127.0.0.1:18789
```

#### Langkah 6: Verifikasi OpenClaw

```bash
# Cek status gateway
curl http://127.0.0.1:18789/api/status

# Cek via OpenCode
# openclaw-mcp sudah terkonfigurasi di opencode.json
# Saat OpenCode start, otomatis connect ke OpenClaw
```

### Integrasi OpenClaw dengan OpenCode

OpenClaw terintegrasi dengan OpenCode melalui **openclaw MCP server**:

```json
// opencode.json
{
  "mcp": {
    "openclaw": {
      "type": "local",
      "command": ["openclaw-mcp", "--openclaw-url", "http://127.0.0.1:18789"],
      "enabled": true
    }
  }
}
```

#### Yang Memungkinkan:
1. **OpenCode → OpenClaw** - Kirim task ke OpenClaw gateway via MCP
2. **Shared MCP Servers** - Google Sheets MCP menggunakan credentials yang sama
3. **Telegram Bot** - OpenClaw menangani Telegram, OpenCode bisa akses via MCP
4. **Multi-Provider AI** - OpenClaw menyediakan akses ke banyak model provider

### OpenClaw MCP Servers (10 servers):

| MCP | Command | Fungsi |
|-----|---------|--------|
| `excel` | `mcp-excel.exe` | Excel COM automation |
| `filesystem` | `npx @modelcontextprotocol/server-filesystem` | File access (Downloads folder) |
| `pdf` | `npx @modelcontextprotocol/server-pdf` | PDF text extraction |
| `word` | `word_mcp_server.exe` | Word COM automation |
| `screenshot` | `python -m windows_capture_mcp.server` | Windows screenshot |
| `playwright` | `npx @playwright/mcp` | Browser automation (Arc) |
| `google-apps-script` | Node.js custom | Manage Apps Script projects |
| `google-sheets` | `npx google-spreadsheet-mcp` | Google Sheets API |
| `google-drive` | `npx @modelcontextprotocol/server-gdrive` | Google Drive access |
| `security-tools` | Node.js custom | Security testing tools |
| `mcp-for-security` | Docker `cyprox/mcp-for-security` | 22+ security tools (nmap, nuclei, dll) |

### OpenClaw Folder Structure:

```
C:\Users\USER\.openclaw\
├── openclaw.json              # Konfigurasi utama OpenClaw
├── credentials/
│   ├── google-service-account.json   # Google service account
│   └── telegram-pairing.json        # Telegram pairing info
├── workspace/                 # Workspace directory
├── skills/                    # OpenClaw skills
├── mcp-servers/               # MCP server binaries
├── agents/                    # Agent configurations
├── commands/                  # Custom commands
├── config/                    # Additional configs
├── logs/                      # Log files
├── cache/                     # Cache directory
├── telegram/                  # Telegram bot data
├── security-tools/            # Security testing tools
└── *.md                       # Dokumentasi setup & guides
```

---

## 📱 Telegram Bot

### Dua Sistem Telegram:

Konfigurasi ini memiliki **dua sistem Telegram** yang berbeda:

#### 1. OpenClaw Telegram (Primary)
- **Dikelola oleh:** OpenClaw Gateway
- **Bot:** `@santo_xcode_bot`
- **Konfigurasi:** `C:\Users\USER\.openclaw\openclaw.json` → `channels.telegram`
- **Status:** ✅ Enabled
- **Fitur:** Remote AI access, multi-provider, MCP tools

#### 2. OpenCode Telegram Bot (@grinev)
- **Dikelola oleh:** `@grinev/opencode-telegram-bot`
- **Konfigurasi:** `%APPDATA%\opencode-telegram-bot\.env`
- **Status:** Konfigurasi terpisah
- **Dokumentasi:** Lihat [`TELEGRAM.md`](TELEGRAM.md)

### Quick Start Telegram (via OpenClaw):

```bash
# 1. Pastikan OpenClaw gateway running
openclaw gateway

# 2. Bot otomatis connect ke Telegram
# Kirim pesan ke @santo_xcode_bot di Telegram

# 3. Commands yang tersedia:
# /start    - Mulai sesi
# /status   - Cek status
# /sessions - List sesi
# /new      - Sesi baru
# /abort    - Batalkan task
```

---

## ⚙️ Konfigurasi Detail

### Model Utama:
| Setting | Value |
|---------|-------|
| **Default Model** | `qwen-code/coder-model` |
| **Mode** | `primary` |
| **Prompt Source** | `{file:./SYSTEM_PROMPT.md}` |

### User Settings:
| Setting | Value |
|---------|-------|
| **Coder Agent Model** | `claude-4-sonnet` |
| **Coder Max Tokens** | 50,000 |
| **Title Model** | `gpt-4o-mini` |
| **Theme** | `opencode` |
| **Auto Compact** | ✅ enabled |
| **Debug** | ❌ disabled |

### Context Paths:
- `AGENTS.md` - System prompt utama
- `system-prompt-opencode.md` - Additional context

### Image Proxy:
| Setting | Value |
|---------|-------|
| **Image Reader Model** | `opencode/kimi-k2.5-free` |
| **Incapable Models** | none (semua model support image) |

### Dapodik:
| Setting | Value |
|---------|-------|
| **Sekolah** | SD NEGERI PASIRHALANG |
| **NPSN** | 20205293 |
| **URL** | `http://localhost:5774` |
| **Token** | Tersimpan di `dapodik_config.json` |

---

## 📝 Cara Penggunaan

### Load Skill:
Ketik di OpenCode:
- `/brainstorm` - Mulai brainstorming
- `/tdd` - TDD workflow
- `/debug` - Systematic debugging
- `/skill-list-install` - Install skills dari marketplace
- `/dapodik-scraper` - Download data peserta didik

### MCP Usage:
```javascript
// Contoh penggunaan Excel MCP
await excel_mcp.read_excel({ filepath: "data.xlsx" })

// Contoh Google Sheets
await google_sheets.read_values({ spreadsheetId: "...", range: "Sheet1!A1:D10" })

// Contoh OpenClaw
await openclaw.chat({ message: "Buatkan laporan BOS" })
```

### Dapodik:
```bash
# Pastikan Dapodik berjalan di localhost:5774
# Gunakan skill dapodik-scraper untuk download data
```

### OpenClaw:
```bash
# Start gateway
openclaw gateway

# Via Telegram: kirim pesan ke @santo_xcode_bot
# Via OpenCode: gunakan openclaw MCP
```

---

## 🔧 Troubleshooting

### MCP Server Tidak Connect:
```bash
# Cek apakah MCP terinstall
npm list -g | grep mcp
pip list | grep mcp
uvx --help

# Cek log OpenCode untuk error detail
# Pastikan command path di opencode.json benar
```

### OpenClaw Gateway Tidak Response:
```bash
# Cek apakah gateway running
netstat -ano | findstr 18789

# Restart gateway
taskkill /F /IM openclaw.exe
openclaw gateway
```

### Google Sheets Error:
```bash
# Pastikan service account file ada
dir "%USERPROFILE%\.openclaw\credentials\google-service-account.json"

# Pastikan sheet sudah di-share ke email service account
```

### Vision MCP Error:
```bash
# Pastikan GROQ_API_KEY di-set
echo %GROQAPI_KEY%

# Set jika belum
setx GROQ_API_KEY "your-groq-api-key"
```

### Dapodik Connection Error:
```bash
# Pastikan Dapodik Web Service running
netstat -ano | findstr 5774

# Cek token di dapodik_config.json
```

---

## 📜 License

MIT License

---

## 👤 Author

**Owner:** santo x/code  
**Built with:** ❤️ for education

---

*Last Updated: 12 April 2026*
