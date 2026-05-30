# 🦞→☤ Migration Plan: OpenClaw → Hermes Agent

**Target:** SD Negeri Pasirhalang OpenCode Configuration  
**Tanggal:** 15 Mei 2026  
**Status:** DRAFT v2 - Updated per User Decisions  
**Keputusan User:**
1. Install Hermes via PowerShell (Windows native) — tanpa WSL2
2. Hapus integrasi Google Sheets MCP terlebih dahulu
3. Langsung ganti OpenClaw MCP → Hermes MCP (tanpa disable dulu)  

---

## 📌 GOAL

Migrasi dari OpenClaw ke Hermes Agent sebagai AI gateway utama, dengan:
1. Zero downtime pada Telegram bot (`@santo_xcode_bot`)
2. Semua MCP servers di OpenCode tetap berfungsi
3. Credentials, skills, dan konfigurasi tersimpan aman
4. OpenCode bisa tetap berjalan normal selama dan setelah migrasi

---

## 📋 INSTRUCTIONS

### Phase 0: PRE-MIGRATION (Backup & Audit)

#### 0.1 Backup Full OpenClaw Directory
```powershell
# Backup seluruh folder .openclaw
robocopy C:\Users\USER\.openclaw C:\Users\USER\.openclaw-backup /E /COPYALL /R:3 /W:5
```
**Verifikasi:** Pastikan folder backup ada dan ukurannya sama.

#### 0.2 Backup OpenCode Config
```powershell
# Backup opencode.json
copy C:\Users\USER\.config\opencode\opencode.json C:\Users\USER\.config\opencode\opencode.json.pre-hermes
copy C:\Users\USER\.config\opencode\README.md C:\Users\USER\.config\opencode\README.md.pre-hermes
```

#### 0.3 Audit OpenClaw yang Sedang Running
```powershell
# Cek apakah OpenClaw gateway running
netstat -ano | findstr 18789
tasklist | findstr openclaw
```
**Catatan:** Jika running, catat PID untuk shutdown nanti.

#### 0.4 Inventory OpenClaw Assets yang Perlu Migrasi
| Asset | Lokasi | Status |
|-------|--------|--------|
| `openclaw.json` | `C:\Users\USER\.openclaw\openclaw.json` | ✅ Config utama |
| Google Service Account | `C:\Users\USER\.openclaw\credentials\google-service-account.json` | ✅ Critical |
| Telegram pairing | `C:\Users\USER\.openclaw\credentials\telegram-pairing.json` | ⚠️ Perlu re-pair |
| Workspace | `C:\Users\USER\.openclaw\workspace\` | ✅ Files |
| Skills | `C:\Users\USER\.openclaw\skills\` | ⚠️ Format conversion |
| AGENTS.md | `C:\Users\USER\.openclaw\workspace\AGENTS.md` | ✅ Workspace instructions |
| API Keys | Di `openclaw.json` (inline/env) | ✅ Auto-migrate |
| `start-gateway-user.bat` | `C:\Users\USER\.openclaw\start-gateway-user.bat` | ❌ Tidak applicable |

---

### Phase 1: HAPUS GOOGLE SHEETS INTEGRASI

**Keputusan:** Google Sheets MCP dihapus terlebih dahulu untuk menghindari dependency ke `.openclaw/credentials/` saat migrasi.

#### 1.1 Hapus Google Sheets MCP dari `opencode.json`
Hapus block berikut dari `opencode.json` (line ~338-347):
```json
"google-sheets": {
  "type": "local",
  "command": ["google-spreadsheet-mcp"],
  "environment": {
    "GOOGLE_SERVICE_ACCOUNT_KEY_PATH": "C:\\Users\\USER\\.openclaw\\credentials\\google-service-account.json"
  },
  "enabled": true
}
```

#### 1.2 Backup Credential (Tetap Simpan untuk Jaga-jaga)
```powershell
# Backup credential ke folder aman
robocopy C:\Users\USER\.openclaw\credentials C:\Users\USER\.openclaw-backup\credentials google-service-account.json
```

#### 1.3 Verifikasi
```powershell
# Cek opencode.json - pastikan tidak ada referensi ke google-sheets
findstr /i "google-sheets" C:\Users\USER\.config\opencode\opencode.json
findstr /i "google-service-account" C:\Users\USER\.config\opencode\opencode.json
```
Harus **tidak ada output** (sudah bersih).

---

### Phase 2: INSTALL HERMES

#### 2.1 Install Hermes (Windows Native via PowerShell)
```powershell
# Install via PowerShell one-liner
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex
```

**Catatan:** Windows native = early beta. Jika ada error saat install, catat error-nya untuk troubleshooting.

#### 2.2 Verifikasi Instalasi
```powershell
hermes --version
hermes doctor
```

#### 2.3 Setup Awal (Tanpa Migration Dulu)
```powershell
# Setup wizard - pilih SKIP migration saat ditanya
hermes setup
```
**Penting:** Saat wizard menawarkan migration dari OpenClaw, pilih **SKIP** dulu. Kita akan jalankan migration manual dengan `--dry-run` terlebih dahulu.

---

### Phase 2: DRY-RUN MIGRATION

#### 2.1 Preview Migration
```powershell
hermes claw migrate --dry-run
```

**Output yang diharapkan:**
- List file yang akan di-copy
- API keys yang akan di-resolve
- Skills yang akan di-convert
- Items yang TIDAK bisa auto-migrate (perlu manual)

#### 2.2 Review Dry-Run Report
Periksa:
- [ ] SOUL.md terdeteksi?
- [ ] MEMORY.md / USER.md terdeteksi?
- [ ] API keys ter-resolve semua? (khususnya yang `source: "file"` atau `source: "exec"`)
- [ ] Skills format conversion - mana yang perlu manual review?
- [ ] Telegram config terdeteksi?
- [ ] Workspace files terdeteksi?

#### 2.3 Jika Ada Masalah di Dry-Run
| Masalah | Solusi |
|---------|--------|
| API key tidak ter-resolve | Manual: `hermes config set <key> <value>` |
| Skill conversion gagal | Manual review di `~/.hermes/skills/openclaw-imports/` |
| Telegram token tidak ditemukan | Copy manual dari `openclaw.json` |

---

### Phase 3: EKSEKUSI MIGRASI

#### 3.1 Jalankan Migration
```powershell
hermes claw migrate
```

**Mode interaktif** - akan konfirmasi per item. Pilih **yes** untuk semua yang aman.

#### 3.2 Migrasi Tanpa Secrets (Opsional - Lebih Aman)
```powershell
hermes claw migrate --preset user-data
```
Gunakan ini jika ingin API keys di-set manual saja.

#### 3.3 Verifikasi Hasil Migration
```powershell
# Cek Hermes home directory
dir %LOCALAPPDATA%\hermes\
# Atau jika WSL2:
ls ~/.hermes/

# Cek config
hermes config list

# Cek skills ter-import
hermes skills list

# Cek model config
hermes model
```

---

### Phase 4: SETUP TELEGRAM DI HERMES

#### 4.1 Konfigurasi Telegram
```powershell
hermes gateway setup
```
Pilih Telegram, masukkan:
- **Bot Token:** Sama seperti di OpenClaw (`@santo_xcode_bot`)
- **Allowed Users:** `6776956601` (sama seperti OpenClaw)

#### 4.2 Pairing (Jika Diperlukan)
```powershell
# Kirim pesan ke bot di Telegram
# Bot akan kasih pairing code
hermes pairing approve telegram <CODE>
```

#### 4.3 Test Telegram
```powershell
# Start gateway di foreground dulu untuk test
hermes gateway
```
Kirim pesan ke `@santo_xcode_bot` → harus ada response.

---

### Phase 5: UPDATE OPENCODE CONFIG

#### 5.1 Edit `opencode.json` - Ganti OpenClaw MCP → Hermes MCP

**Langsung replace** block OpenClaw dengan Hermes:
```json
// HAPUS block ini (line ~367-375):
"openclaw": {
  "type": "local",
  "command": ["openclaw-mcp", "--openclaw-url", "http://127.0.0.1:18789"],
  "enabled": true
}

// GANTI dengan block ini:
"hermes": {
  "type": "local",
  "command": ["hermes", "mcp", "serve"],
  "enabled": true
}
```

#### 5.2 Hapus Referensi Google Sheets
Sudah ditangani di **Phase 1**. Pastikan tidak ada sisa referensi:
```powershell
findstr /i "google-sheets" C:\Users\USER\.config\opencode\opencode.json
findstr /i "google-service-account" C:\Users\USER\.config\opencode\opencode.json
findstr /i "\.openclaw" C:\Users\USER\.config\opencode\opencode.json
```
Harus **tidak ada output**.

#### 5.3 Built-in OpenClaw Tools di OpenCode
OpenCode punya 6 built-in tools untuk OpenClaw:
- `openclaw_openclaw_chat`
- `openclaw_openclaw_chat_async`
- `openclaw_openclaw_instances`
- `openclaw_openclaw_status`
- `openclaw_openclaw_task_*`

Tools ini adalah **native OpenCode** (bukan MCP). Akan fail gracefully jika tidak ada gateway yang matching. Tidak perlu di-disable — Hermes MCP akan menyediakan tools alternatif:

| Hermes MCP Tool | Fungsi Pengganti |
|-----------------|------------------|
| `conversations_list` | List conversations (pengganti `openclaw_instances`) |
| `messages_read` | Read message history |
| `messages_send` | Send message (pengganti `openclaw_chat`) |
| `events_poll` | Poll events |
| `channels_list` | List channels |

#### 5.4 Full `opencode.json` Changes Summary
| Line | Sebelum | Sesudah |
|------|---------|---------|
| ~338-347 | `"google-sheets"` MCP block | **DIHAPUS** (Phase 1) |
| ~367-375 | `"openclaw"` MCP block | **DIGANTI** → `"hermes"` MCP block |
| README.md | Section OpenClaw Integration | Update → Hermes Integration (Phase 8) |

---

### Phase 6: SHUTDOWN OPENCLAW & START HERMES

#### 6.1 Stop OpenClaw Gateway
```powershell
# Cek PID
netstat -ano | findstr 18789

# Kill process
taskkill /F /IM openclaw.exe
```

#### 6.2 Start Hermes Gateway
```powershell
# Test dulu di foreground
hermes gateway

# Jika OK, install sebagai service
hermes gateway install
hermes gateway start
```

#### 6.3 Verifikasi Hermes Gateway
```powershell
hermes gateway status
```

---

### Phase 7: VERIFIKASI END-TO-END

#### 7.1 Checklist Verifikasi
| Test | Expected | Status |
|------|----------|--------|
| Hermes gateway running | `hermes gateway status` → active | ☐ |
| Telegram bot response | Kirim pesan ke `@santo_xcode_bot` → reply | ☐ |
| OpenCode startup | `opencode` → no MCP errors | ☐ |
| Google Sheets MCP | **Sudah dihapus** — tidak ada error | ☐ |
| All other MCPs | 16 MCP servers connect (minus google-sheets) | ☐ |
| Hermes MCP connect | `hermes mcp serve` → tools terdaftar | ☐ |
| Skills ter-migrate | `hermes skills list` → ada imported skills | ☐ |
| Memory ter-migrate | Hermes ingat context sebelumnya | ☐ |

#### 7.2 Rollback Plan (Jika Ada Masalah)
```powershell
# 1. Stop Hermes
hermes gateway stop

# 2. Restore OpenClaw
"C:\Users\USER\.openclaw\start-gateway-user.bat"

# 3. Restore opencode.json (kembali ke versi pre-hermes)
copy C:\Users\USER\.config\opencode\opencode.json.pre-hermes C:\Users\USER\.config\opencode\opencode.json

# 4. Restart OpenCode
opencode
```

**Catatan:** Google Sheets MCP tidak akan otomatis kembali setelah rollback — perlu ditambahkan manual ke `opencode.json` jika diperlukan lagi.

---

### Phase 8: POST-MIGRATION CLEANUP

#### 8.1 Update Dokumentasi
- Update `README.md` → ganti section OpenClaw Integration dengan Hermes Integration
- Update AGENTS.md jika ada referensi ke OpenClaw

#### 8.2 Cleanup (Setelah 1-2 Minggu Stabil)
```powershell
# Hapus backup jika sudah yakin
# rmdir /S /Q C:\Users\USER\.openclaw-backup

# Hapus OpenClaw (opsional)
# npm uninstall -g openclaw
# rmdir /S /Q C:\Users\USER\.openclaw
```

**PENTING:** Jangan hapus folder `.openclaw/` sampai semua verified. Credential Google Sheets sudah di-backup di `.openclaw-backup/credentials/`.

---

## 🔍 DISCOVERIES

1. **Hermes Windows native = early beta.** Installer PowerShell tersedia. Jika ada error, fallback ke WSL2.
2. **Hermes MCP bridge** (`hermes mcp serve`) bisa langsung menggantikan `openclaw-mcp` sebagai MCP server untuk OpenCode.
3. **Google Sheets MCP dihapus** untuk menghilangkan dependency ke `.openclaw/credentials/`. Credential tetap di-backup untuk jaga-jaga.
4. **OpenCode built-in `openclaw_*` tools** adalah native tools di OpenCode binary. Akan fail gracefully, tidak crash OpenCode.
5. **Telegram bot token** bisa reuse yang sama — tidak perlu buat bot baru di BotFather.
6. **Skill format conversion** otomatis untuk simple skills, tapi skills dengan conditional logic perlu manual review.
7. **Hermes config format** = YAML (`~/.hermes/config.yaml`), berbeda dari OpenClaw JSON.
8. **Hermes home di Windows** = `%LOCALAPPDATA%\hermes\` (native install).
9. **Total MCP setelah migrasi:** 16 servers (18 sebelumnya - google-sheets - openclaw + hermes).

---

## ✅ ACCOMPLISHED

- [x] Audit semua dependensi OpenClaw di OpenCode
- [x] Research Hermes Agent capabilities & migration tool
- [x] Research Hermes MCP integration
- [x] Research Hermes Telegram setup
- [x] Buat migration plan 8 phase
- [x] Identifikasi risiko dan rollback plan
- [x] Identifikasi items yang perlu manual intervention

---

## 📁 RELEVANT FILES/DIRECTORIES

| Path | Relevansi |
|------|-----------|
| `C:\Users\USER\.config\opencode\opencode.json` | Main config — hapus google-sheets, ganti openclaw→hermes |
| `C:\Users\USER\.config\opencode\README.md` | Dokumentasi — perlu update (Phase 8) |
| `C:\Users\USER\.config\opencode\user-settings.json` | User settings — tidak perlu diubah |
| `C:\Users\USER\.openclaw\openclaw.json` | Source config untuk migrasi |
| `C:\Users\USER\.openclaw\credentials\google-service-account.json` | **Backed up** — tidak lagi dipakai |
| `C:\Users\USER\.openclaw\credentials\telegram-pairing.json` | Telegram pairing info |
| `C:\Users\USER\.openclaw\workspace\` | Workspace files |
| `%LOCALAPPDATA%\hermes\` | Hermes home (setelah install) |
| `~/.hermes/config.yaml` | Hermes config (setelah setup) |

---

## 👉 NEXT STEPS

1. **Review migration plan v2 ini** — pastikan semua perubahan sesuai keputusan
2. **Approve plan** — jika OK, lanjut eksekusi
3. **Execute Phase 0** — backup semua data
4. **Execute Phase 1** — hapus Google Sheets MCP dari `opencode.json`
5. **Execute Phase 2** — install Hermes via PowerShell
6. **Execute Phase 3** — dry-run migration (`hermes claw migrate --dry-run`)
7. **Review dry-run results** — cek apa yang bisa dan tidak bisa auto-migrate
8. **Execute Phase 4-8** — full migration + switch + verify

**Estimasi waktu:**
- Phase 0-1 (Backup + Hapus Google Sheets): ~15 menit
- Phase 2-3 (Install Hermes + Dry-run): ~20 menit
- Phase 4-5 (Migrate + Setup Telegram + Config): ~25 menit
- Phase 6-8 (Switch + Verify + Cleanup): ~20 menit
- **Total: ~1.5 jam** (termasuk testing)

---

## ⚠️ RISK MATRIX

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Hermes Windows beta bug | Medium | High | Catat error, fallback ke WSL2 jika perlu |
| Telegram bot downtime | Low | Medium | Setup Hermes Telegram sebelum shutdown OpenClaw |
| Google Sheets hilang | **N/A** | **N/A** | Sudah dihapus intentional. Credential di-backup |
| Skill conversion loss | Medium | Low | Manual review skills setelah import |
| Hermes MCP tidak connect | Low | Medium | Test `hermes mcp serve` manual sebelum update config |
| API keys tidak ter-migrate | Low | Medium | Dry-run dulu, manual set jika perlu |

---

*Migration Plan v1.0 | Created: 15 Mei 2026 | Status: DRAFT*
