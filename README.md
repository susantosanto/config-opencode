# ⚙️ OpenCode Configuration

Konfigurasi personal untuk OpenCode AI - dikustomasi untuk Operator Sekolah & Web Developer.

---

## 📋 Contents

- [Tentang](#-tentang)
- [Struktur Folder](#-struktur-folder)
- [Fitur & MCP](#-fitur--mcp)
- [Custom Skills](#-custom-skills)
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
