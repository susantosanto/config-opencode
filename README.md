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

### Langkah 4: Verifikasi

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
├── AGENTS.md                  # System prompt utama (v2.0)
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

### MCP Servers Aktif (16 servers):

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
| `windows-mcp` | local | `uvx windows-mcp --transport stdio` | Windows automation (via uvx) |
| `windows-desktop-automation` | local | Node.js custom path | Desktop UI automation |
| `winapp-mcp` | local | `winapp-mcp` | Windows app UI automation |
| `shell` | local | `super-shell-mcp` | Shell execution |
| `pdf` | local | `uvx mcp-pdf` | PDF processing (via uvx) |
| `superpowers` | local | `superpowers-mcp` | Superpowers MCP server |
| `vision-mcp-server` | local | `python -m vision_mcp_server.server` | Image analysis (GROQ API) |

### Environment Variables yang Diperlukan:

| Variable | Sumber | Digunakan Oleh |
|----------|--------|----------------|
| `GROQ_API_KEY` | [groq.com](https://groq.com) | `vision-mcp-server` |

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
| `browser-use` | Browser automation AI untuk web scraping, Dapodik automation |
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

## 📱 Telegram Bot

### Status Telegram

Telegram bot `@santo_xcode_bot` sebelumnya dikelola oleh OpenClaw Gateway. Setelah OpenClaw dihapus, bot ini **tidak aktif**.

Untuk mengaktifkan kembali Telegram bot, gunakan alternatif:
- **Hermes Agent** — `hermes gateway setup` (mendukung Telegram)
- **OpenCode Telegram Bot** (`@grinev/opencode-telegram-bot`) — konfigurasi terpisah di `%APPDATA%\opencode-telegram-bot\.env`

---

## ⚙️ Konfigurasi Detail

### Model Utama:
| Setting | Value |
|---------|-------|
| **Default Model** | `qwen-code/coder-model` |
| **Mode** | `primary` |
| **Prompt Source** | `{file:./AGENTS.md}` |

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

// Contoh Windows Desktop Automation
await winapp_mcp.click_element({ appId: "...", name: "Button" })
```

### Dapodik:
```bash
# Pastikan Dapodik berjalan di localhost:5774
# Gunakan skill dapodik-scraper untuk download data
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
