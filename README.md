# ⚙️ OpenCode Configuration

Konfigurasi personal untuk OpenCode AI - dikustomasi untuk Operator Sekolah & Web Developer.

---

## 📋 Contents

- [Tentang](#-tentang)
- [Struktur Folder](#-struktur-folder)
- [Fitur & MCP](#-fitur--mcp)
- [Custom Skills](#-custom-skills)
- [Telegram Bot](#-telegram-bot)
- [Installation](#-installation)
- [Cara Penggunaan](#-cara-penggunaan)

---

## 🔧 Tentang

Konfigurasi ini dibuat untuk:
- **Operator Sekolah Dasar** - Administrasi, BOS, Dapodik
- **Web Developer** - JavaScript, Google Apps Script
- **AI Engineering Learner** - Prompt Engineering, Agentic AI

---

## 📁 Struktur Folder

```
opencode-config/
├── opencode.json              # Konfigurasi utama (MCP, skills, plugin)
├── AGENTS.md                  # System prompt utama
├── SYSTEM_PROMPT.md           # User profile & identitas
├── user-settings.json         # Settings tambahan
├── dapodik_config.json        # Konfigurasi Dapodik (token, NPSN, URL)
├── playwright-config.json     # Konfigurasi Playwright browser
├── skills/
│   ├── dapodik-scraper/       # Skill download data Dapodik
│   └── skill-list-install/    # Menu installer skills
│       └── SKILL.md
├── TELEGRAM.md                # Dokumentasi Telegram Bot
├── package.json
└── package-lock.json
```

---

## 🤖 Fitur & MCP

### MCP Servers Aktif:

| MCP | Type | Fungsi |
|-----|------|--------|
| `filesystem` | local | Akses file system (C:/Users/USER/Documents) |
| `playwright` | local | Browser automation (Chromium headless) |
| `chrome-devtools` | local | Chrome DevTools protocol (headless) |
| `memory` | local | Knowledge graph storage |
| `sequential-thinking` | local | Structured reasoning |
| `fetch` | local | Web fetching (mcp-fetch-server) |
| `git` | local | Version control (git-mcp-server) |
| `time` | local | Time & timezone utilities |
| `context7` | remote | Documentation lookup (mcp.context7.com) |
| `excel-control` | local | Live Excel editing (excel-mcp-server) |
| `excel-mcp` | local | Python Excel operations (Python 3.13) |
| `word` | local | Word document processing (doc-tools-mcp) |
| `google-sheets` | local | Google Sheets API (service account) |
| `windows-mcp` | local | Windows automation (uvx) |
| `windows-desktop-automation` | local | Desktop UI automation (Node.js) |
| `openclaw` | local | OpenClaw integration (port 18789) |
| `winapp-mcp` | local | Windows app UI automation |
| `shell` | local | Shell execution (super-shell-mcp) |
| `pdf` | local | PDF processing (uvx mcp-pdf) |
| `superpowers` | local | Superpowers MCP server |

### Plugin:
- `superpowers` - Git plugin dari https://github.com/obra/superpowers.git

---

## 🎯 Custom Skills

### Skill Paths:
- `C:/Users/USER/Documents/opencode-skills` - Skills eksternal
- `C:/Users/USER/.config/opencode/skills` - Skills lokal

### Superpowers Skills (Plugin):
- `brainstorming` - Socratic design refinement
- `systematic-debugging` - 4-phase debugging
- `writing-plans` - Implementation planning
- `test-driven-development` - TDD workflow
- `requesting-code-review` - Code review
- `receiving-code-review` - Receive feedback
- `subagent-driven-development` - Multi-agent execution
- `finishing-a-development-branch` - Merge/PR workflow
- `verification-before-completion` - Pre-commit verification
- `executing-plans` - Plan execution
- `using-git-worktrees` - Git worktree management
- `using-superpowers` - Superpowers workflow
- `dispatching-parallel-agents` - Parallel task execution

### Custom Skills (Lokal):
- `dapodik-scraper` - Download data peserta didik dari Dapodik Web Service
- `skill-list-install` - Menu installer skills dari skills.sh marketplace

---

## 🤖 Telegram Bot

### Apa itu OpenCode Telegram Bot?

Client Telegram untuk OpenCode CLI yang memungkinkan:
- **Remote coding** - Kirim perintah coding dari mana saja via Telegram
- **Monitoring** - Lihat progress task secara real-time
- **Session management** - Kelola sesi coding dari hp
- **Model switching** - Ganti model AI langsung dari Telegram

### 🚀 Fitur Utama (All Remote via Telegram)

#### 1. 📝 Automasi Administrasi Sekolah
| Fitur | Deskripsi Remote |
|-------|------------------|
| 📨 **Surat Otomatis** | Buat surat izin, undangan, laporan - semua dari HP |
| 📄 **Dokumen Dynamic** | Generate Word/Excel via command Telegram |
| 🏫 **Dapodik Input** | Input data siswa/guru dari mana saja |
| 📊 **Laporan BOS/SPJ** | Buat laporan keuangan otomatis - cukup kirim perintah |

#### 2. 🌐 Web Automasi
| Fitur | Deskripsi Remote |
|-------|------------------|
| 🌍 **Browser Control** | Kontrol browser dari Telegram - tanpa PC |
| ⚙️ **Script Execution** | Jalankan script automasi web jarak jauh |
| 👁️ **Website Monitor** | Monitoring website sekolah realtime |
| 🕸️ **Data Scraping** | Ambil data dari website via chat |

#### 3. 💻 Remote Coding
| Fitur | Deskripsi Remote |
|-------|------------------|
| ⌨️ **Code from Anywhere** | Kirim code dari HP - laptop eksekusi |
| 📁 **File Management** | Edit/baca/write file via chat |
| 🖥️ **Terminal Access** | Akses terminal tanpa perlu di depan PC |
| 🚀 **Build & Deploy** | Build & deploy project dari sofa |

### Install

```bash
# Install via npm
npm install -g @grinev/opencode-telegram-bot

# Atau gunakan npx
npx @grinev/opencode-telegram-bot
```

### Cara Penggunaan

```bash
# Start bot
opencode-telegram

# Atau dengan pairing code
npx @grinev/opencode-telegram-bot pair
```

### Commands

| Command | Deskripsi |
|---------|-----------|
| `/start` | Mulai sesi |
| `/status` | Lihat status server |
| `/projects` | List semua project |
| `/new` | Buat sesi baru |
| `/sessions` | List dan switch sesi |
| `/abort` | Batalkan task |

### Dokumentasi Lengkap

Lihat [`TELEGRAM.md`](TELEGRAM.md) untuk panduan lengkap.

---

## ⚙️ Konfigurasi Utama

### Mode & Prompt
- **Mode**: `primary`
- **Prompt Source**: `SYSTEM_PROMPT.md` (file-based prompt)

### Plugin
- **Superpowers**: `superpowers@git+https://github.com/obra/superpowers.git`

### Skill Paths
| Path | Deskripsi |
|------|-----------|
| `C:/Users/USER/Documents/opencode-skills` | Skills eksternal (opencode-system-prompt, ai-engineer-path, dll) |
| `C:/Users/USER/.config/opencode/skills` | Skills lokal (dapodik-scraper, skill-list-install) |

### Konfigurasi Dapodik
- **Sekolah**: SD NEGERI PASIRHALANG
- **NPSN**: 20205293
- **URL**: http://localhost:5774
- **Token**: Tersimpan di `dapodik_config.json`

---

## 📥 Installation

```bash
# Clone repository
git clone https://github.com/[YOUR-USERNAME]/opencode-config.git

# Copy ke folder config
cp -r opencode-config/* ~/.config/opencode/

# Restart OpenCode
opencode
```

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
```

### Dapodik:
```bash
# Pastikan Dapodik berjalan di localhost:5774
# Gunakan skill dapodik-scraper untuk download data
```

---

## 📜 License

MIT License

---

## 👤 Author

**Owner:** santo x/code  
**Built with:** ❤️ for education

---

*Last Updated: 5 April 2026*
