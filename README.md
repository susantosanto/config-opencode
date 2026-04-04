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
├── opencode.json          # Konfigurasi utama
├── AGENTS.md              # System prompt
├── SYSTEM_PROMPT.md       # User profile
├── user-settings.json     # Settings tambahan
├── skills/
│   └── skill-list-install/
│       └── SKILL.md       # Menu installer skills
├── TELEGRAM.md            # Dokumentasi Telegram Bot
├── package.json
└── bun.lock
```

---

## 🤖 Fitur & MCP

### MCP Servers Aktif:

| MCP | Fungsi |
|-----|--------|
| `filesystem` | Akses file system |
| `playwright` | Browser automation |
| `memory` | Knowledge storage |
| `sequential-thinking` | Structured reasoning |
| `fetch` | Web fetching |
| `git` | Version control |
| `context7` | Documentation lookup |
| `gh_grep` | GitHub code search |
| `excel-control` | Live Excel editing |
| `excel-mcp` | Python Excel operations |
| `google-sheets` | Google Sheets API |
| `google-drive` | Google Drive API |
| `windows-mcp` | Windows automation |
| `windows-desktop-automation` | Desktop UI automation |
| `openclaw` | OpenClaw integration |
| `shell` | Shell execution |
| `pdf` | PDF processing |

---

## 🎯 Custom Skills

### Superpowers Collection:
- `brainstorming` - Socratic design refinement
- `systematic-debugging` - 4-phase debugging
- `writing-plans` - Implementation planning
- `test-driven-development` - TDD workflow
- `requesting-code-review` - Code review
- `receiving-code-review` - Receive feedback
- `subagent-driven-development` - Multi-agent execution
- `finishing-a-development-branch` - Merge/PR workflow

### Custom Skills:
- `opencode-system-prompt` - System prompt management
- `skill-list-install` - Menu installer dari skills.sh
- `ai-engineer-path` - AI learning path
- `excel-live-editing` - Live Excel editing

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

### MCP Usage:
```javascript
// Contoh penggunaan Excel MCP
await excel_mcp.read_excel({ filepath: "data.xlsx" })
```

---

## 📜 License

MIT License

---

## 👤 Author

**Owner:** santo x/code  
**Built with:** ❤️ for education

---

*Last Updated: April 2026*
