---
name: skill-list-install
description: "Menu interaktif untuk install OpenCode skills dari skills.sh marketplace"
license: MIT
compatibility: opencode
metadata:
  audience: sd-operator
  workflow: installation
  source: skills-sh
---

# 📦 OpenCode Skill Installer - Menu Pemilihan

Menu ini memungkinkan Anda untuk memilih dan menginstall skills dari skills.sh marketplace secara interaktif.

---

## Cara Penggunaan

Ketik perintah sesuai keinginan Anda:

| Perintah | Aksi |
|----------|------|
| `/skill-list-install` atau `skill list` | Tampilkan menu utama |
| `install [kategori]` | Install semua skill dalam kategori |
| `install [skill-name]` | Install skill tertentu |
| `install all` | Install semua skill yang tersedia |
| `search [keyword]` | Cari skill berdasarkan keyword |

---

## 📋 Menu Utama - Pilih Kategori

Ketik nomor kategori untuk melihat detail skill:

```
╔════════════════════════════════════════════════════════════╗
║            📦 OPENCODE SKILL INSTALLER MENU                 ║
╠════════════════════════════════════════════════════════════╣
║  1. 🔥 TRENDING      - Skill paling popular saat ini       ║
║  2. ⚡ SUPERPOWERS   - Koleksi superpowers (REKOMENDASI)    ║
║  3. 🎨 UI/UX        - Design & frontend development        ║
║  4. 🧪 TESTING      - Testing & QA                          ║
║  5. ☁️ CLOUD        - Cloud & DevOps                        ║
║  6. 🤖 AI/ML        - Artificial Intelligence & ML          ║
║  7. 📝 PRODUCTIVITY - PDF, Docx, Excel, PPTX               ║
║  8. 🛠️ DEV TOOLS   - Development tools                    ║
║  9. 📱 MOBILE       - Mobile development                    ║
║ 10. 🔒 SECURITY     - Security best practices              ║
║ 11. 🔍 SEO/MARKETING - SEO & Marketing                      ║
║ 12. 📊 DATA         - Data & Analytics                      ║
╠════════════════════════════════════════════════════════════╣
║  Ketik nomor (1-12) untuk memilih kategori                 ║
║  Ketik 'all' untuk install semua skill                     ║
║  Ketik 'recommended' untuk install yang direkomendasikan   ║
╚════════════════════════════════════════════════════════════╝
```

---

## 📖 Detail Kategori

### 1. 🔥 TRENDING - Skill Paling Popular

| # | Skill | Repo | Deskripsi |
|---|-------|------|-----------|
| 1 | browser-use | browser-use/browser-use | Browser automation |
| 2 | vercel-cli-with-tokens | vercel-labs/agent-skills | Vercel CLI with tokens |
| 3 | web-design-guidelines | vercel-labs/agent-skills | Web design guidelines |
| 4 | playwright-best-practices | currents-dev/playwright-best-practices-skill | Playwright testing |
| 5 | frontend-design | anthropics/skills | Frontend design patterns |
| 6 | mcp-builder | anthropics/skills | Build MCP servers |
| 7 | skill-creator | anthropics/skills | Create custom skills |
| 8 | pdf | anthropics/skills | PDF processing |
| 9 | supabase-postgres | supabase/agent-skills | Supabase best practices |
| 10 | deploy-to-vercel | vercel-labs/agent-skills | Deploy to Vercel |

**Install**: `npx skills add browser-use/browser-use -a opencode`

---

### 2. ⚡ SUPERPOWERS - Koleksi Superpowers (REKOMENDASI)

| # | Skill | Deskripsi |
|---|-------|-----------|
| 1 | brainstorming | Socratic design refinement SEBELUM implementasi |
| 2 | systematic-debugging | 4-phase root cause debugging |
| 3 | writing-plans | Buat implementation plan detail SEBELUM coding |
| 4 | test-driven-development | TDD workflow RED-GREEN-REFACTOR |
| 5 | requesting-code-review | Pre-merge code review |
| 6 | receiving-code-review | Receive feedback professionally |
| 7 | executing-plans | Execute implementation plans |
| 8 | subagent-driven-development | Multi-agent parallel execution |
| 9 | finishing-a-development-branch | Merge/PR decision workflow |
| 10 | using-git-worktrees | Parallel branch development |

**Install Semua**: `npx skills add obra/superpowers -a opencode --all`

---

### 3. 🎨 UI/UX - Design & Frontend

| # | Skill | Repo | Deskripsi |
|---|-------|------|-----------|
| 1 | frontend-design | anthropics/skills | Frontend design patterns |
| 2 | web-design-guidelines | vercel-labs/agent-skills | Web design guidelines |
| 3 | vercel-react-best-practices | vercel-labs/agent-skills | React best practices |
| 4 | vercel-react-view-transitions | vercel-labs/agent-skills | View transitions API |
| 5 | vercel-composition-patterns | vercel-labs/agent-skills | React composition |
| 6 | shadcn | shadcn/ui | shadcn/ui components |
| 7 | canvas-design | anthropics/skills | Canvas design patterns |
| 8 | brand-guidelines | anthropics/skills | Brand guidelines |
| 9 | algorithmic-art | anthropics/skills | Algorithmic art |
| 10 | internal-comms | anthropics/skills | Internal communications |

**Install Semua Vercel**: `npx skills add vercel-labs/agent-skills -a opencode --all`

---

### 4. 🧪 TESTING - Testing & QA

| # | Skill | Repo | Deskripsi |
|---|-------|------|-----------|
| 1 | playwright-best-practices | currents-dev/playwright-best-practices-skill | Playwright E2E testing |
| 2 | webapp-testing | anthropics/skills | Web app testing |
| 3 | test-driven-development | obra/superpowers | TDD workflow |
| 4 | slack-gif-creator | anthropics/skills | Slack GIF testing |
| 5 | template-skill | anthropics/skills | Template for testing |

**Install**: `npx skills add currents-dev/playwright-best-practices-skill -a opencode --skill playwright-best-practices`

---

### 5. ☁️ CLOUD - Cloud & DevOps

| # | Skill | Repo | Deskripsi |
|---|-------|------|-----------|
| 1 | deploy-to-vercel | vercel-labs/agent-skills | Deploy ke Vercel |
| 2 | turborepo | vercel/turborepo | Turborepo monorepo |
| 3 | supabase-postgres-best-practices | supabase/agent-skills | Supabase PostgreSQL |
| 4 | github-copilot-for-azure | microsoft/github-copilot-for-azure | Azure Copilot |
| 5 | azure-skills | microsoft/azure-skills | Azure best practices |
| 6 | vercel-cli-with-tokens | vercel-labs/agent-skills | Vercel CLI |
| 7 | ai-sdk | vercel/ai | Vercel AI SDK |
| 8 | claude-api | anthropics/skills | Claude API integration |
| 9 | doc-coauthoring | anthropics/skills | Document co-authoring |
| 10 | theme-factory | anthropics/skills | Theme factory |

**Install Azure**: `npx skills add microsoft/github-copilot-for-azure -a opencode --all`

---

### 6. 🤖 AI/ML - Artificial Intelligence

| # | Skill | Repo | Deskripsi |
|---|-------|------|-----------|
| 1 | ai-sdk | vercel/ai | Vercel AI SDK |
| 2 | ai-image-generation | inferen-sh/skills | Image generation |
| 3 | ai-video-generation | inferen-sh/skills | Video generation |
| 4 | elevenlabs-tts | inferen-sh/skills | ElevenLabs TTS |
| 5 | claude-api | anthropics/skills | Claude API |
| 6 | mcp-builder | anthropics/skills | MCP server builder |
| 7 | canvas-design | anthropics/skills | AI canvas design |
| 8 | algorithmic-art | anthropics/skills | Algorithmic art |
| 9 | slack-gif-creator | anthropics/skills | AI GIF creator |
| 10 | qwen-cli-bridge | custom | Qwen CLI bridge |

**Install AI Skills**: `npx skills add inferen-sh/skills -a opencode --all`

---

### 7. 📝 PRODUCTIVITY - Document Processing

| # | Skill | Repo | Deskripsi |
|---|-------|------|-----------|
| 1 | pdf | anthropics/skills | PDF processing |
| 2 | docx | anthropics/skills | Word document processing |
| 3 | xlsx | anthropics/skills | Excel spreadsheet processing |
| 4 | pptx | anthropics/skills | PowerPoint processing |
| 5 | doc-coauthoring | anthropics/skills | Document co-authoring |
| 6 | template-skill | anthropics/skills | Template creation |
| 7 | skill-creator | anthropics/skills | Skill creator |
| 8 | brand-guidelines | anthropics/skills | Brand guidelines |

**Install Semua**: `npx skills add anthropics/skills -a opencode --all`

---

### 8. 🛠️ DEV TOOLS - Development Tools

| # | Skill | Repo | Deskripsi |
|---|-------|------|-----------|
| 1 | skill-creator | anthropics/skills | Create custom skills |
| 2 | mcp-builder | anthropics/skills | Build MCP servers |
| 3 | vercel-cli-with-tokens | vercel-labs/agent-skills | Vercel CLI |
| 4 | browser-use | browser-use/browser-use | Browser automation |
| 5 | gh-cli | github/awesome-copilot | GitHub CLI |
| 6 | git-commit | github/awesome-copilot | Git commit best practices |
| 7 | theme-factory | anthropics/skills | Theme factory |
| 8 | template-skill | anthropics/skills | Template skill |
| 9 | canvas-design | anthropics/skills | Canvas tools |
| 10 | windows-app-launcher | custom | Windows app launcher |

**Install**: `npx skills add anthropics/skills -a opencode --skill skill-creator`

---

### 9. 📱 MOBILE - Mobile Development

| # | Skill | Repo | Deskripsi |
|---|-------|------|-----------|
| 1 | building-native-ui | expo/skills | Expo native UI |
| 2 | upgrading-expo | expo/skills | Expo upgrade guide |
| 3 | vercel-react-native-skills | vercel-labs/agent-skills | React Native |
| 4 | web-design-guidelines | vercel-labs/agent-skills | Mobile web design |
| 5 | vercel-react-best-practices | vercel-labs/agent-skills | React patterns |
| 6 | canvas-design | anthropics/skills | Mobile canvas |
| 7 | algorithmic-art | anthropics/skills | Mobile art |
| 8 | template-skill | anthropics/skills | Mobile templates |

**Install Expo**: `npx skills add expo/skills -a opencode --all`

---

### 10. 🔒 SECURITY - Security

| # | Skill | Repo | Deskripsi |
|---|-------|------|-----------|
| 1 | security-best-practices | supercent-io/skills-template | Security best practices |
| 2 | claude-api | anthropics/skills | API security |
| 3 | template-skill | anthropics/skills | Security templates |

**Install**: `npx skills add supercent-io/skills-template -a opencode --skill security-best-practices`

---

### 11. 🔍 SEO/MARKETING - SEO & Marketing

| # | Skill | Repo | Deskripsi |
|---|-------|------|-----------|
| 1 | seo-audit | coreyhaines31/marketingskills | SEO audit |
| 2 | copywriting | coreyhaines31/marketingskills | Copywriting |
| 3 | web-design-guidelines | vercel-labs/agent-skills | SEO-friendly design |
| 4 | vercel-react-best-practices | vercel-labs/agent-skills | Performance optimization |
| 5 | brand-guidelines | anthropics/skills | Brand marketing |
| 6 | internal-comms | anthropics/skills | Marketing comms |
| 7 | slack-gif-creator | anthropics/skills | Social media GIFs |
| 8 | algorithmic-art | anthropics/skills | Visual marketing |
| 9 | template-skill | anthropics/skills | Marketing templates |
| 10 | canvas-design | anthropics/skills | Marketing canvas |

**Install Marketing**: `npx skills add coreyhaines31/marketingskills -a opencode --all`

---

### 12. 📊 DATA - Data & Analytics

| # | Skill | Repo | Deskripsi |
|---|-------|------|-----------|
| 1 | xlsx | anthropics/skills | Excel data processing |
| 2 | pdf | anthropics/skills | PDF data extraction |
| 3 | supabase-postgres-best-practices | supabase/agent-skills | Database analytics |
| 4 | mcp-builder | anthropics/skills | Data pipelines |
| 5 | template-skill | anthropics/skills | Data templates |

**Install**: `npx skills add anthropics/skills -a opencode --skill xlsx`

---

## 🚀 Quick Install Commands

### Install yang Direkomendasikan (Wajib):

```bash
# Superpowers - Wajib!
npx skills add obra/superpowers -a opencode --all

# Vercel Skills
npx skills add vercel-labs/agent-skills -a opencode --all

# Anthropic Skills (PDF, Docx, dll)
npx skills add anthropics/skills -a opencode --all

# Testing
npx skills add currents-dev/playwright-best-practices-skill -a opencode

# AI Skills
npx skills add inferen-sh/skills -a opencode --all
```

---

## 📝 Cara Install Satu Skill

Contoh install skill tertentu:

```bash
# Install single skill
npx skills add obra/superpowers -a opencode --skill brainstorming

# Install ke project tertentu
npx skills add owner/repo -a opencode --skill skill-name

# Install global (semua project)
npx skills add owner/repo -a opencode --skill skill-name -g
```

---

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| Agent not detected | `npx skills add owner/repo -a opencode` |
| No skills found | Cek format: owner/repo |
| Permission denied | Run as Administrator (Windows) |
| Skill not loading | Restart OpenCode |

---

## ℹ️ Informasi

- **Marketplace**: https://skills.sh
- **Total Skills**: 1,300+ skills
- **Supported Agents**: 45+ AI agents

**Versi**: 1.0 | **Tanggal**: 3 April 2026