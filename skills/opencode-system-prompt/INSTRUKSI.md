# Instruksi Penggunaan System Prompt OpenCode

## 📁 File yang Telah Dibuat

### 1. System Prompt Utama
**Lokasi**: `C:\Users\USER\Documents\AGENTS.md`
- File system prompt lengkap untuk operator sekolah & web developer
- Siap untuk di-copy ke lokasi auto-load

### 2. Konfigurasi OpenCode
**Lokasi**: `C:\Users\USER\Documents\.opencode.json`
- Konfigurasi global OpenCode
- Menggunakan `contextPaths` untuk auto-load

### 3. Skill Menu Khusus
**Lokasi**: `C:\Users\USER\Documents\opencode-skills\opencode-system-prompt\`
- `SKILL.md`: Skill untuk load/update system prompt
- `versions/`: Berbagai versi system prompt
- `INSTRUKSI.md`: File instruksi ini

## 🚀 Langkah-langkah Auto-load

### Langkah 1: Pindahkan AGENTS.md ke Direktori Home
```bash
# Buat direktori .opencode jika belum ada
mkdir C:\Users\USER\.opencode

# Copy file AGENTS.md
copy "C:\Users\USER\Documents\AGENTS.md" "C:\Users\USER\.opencode\AGENTS.md"
```

### Langkah 2: Pindahkan .opencode.json ke Direktori Home
```bash
# Copy file konfigurasi
copy "C:\Users\USER\Documents\.opencode.json" "C:\Users\USER\.opencode.json"
```

### Langkah 3: Restart OpenCode
Tutup dan buka kembali OpenCode. System prompt akan otomatis dimuat.

## 🔄 Cara Menggunakan Skill Menu

### Load System Prompt
1. Buka OpenCode
2. Ketik: `/use opencode-system-prompt`
3. Pilih versi yang diinginkan:
   - `full`: Versi lengkap
   - `concise`: Versi ringkas
   - `admin`: Fokus administrasi
   - `dev`: Fokus development
   - `ai`: Fokus AI engineering

### Update System Prompt
1. Edit file `AGENTS.md` di direktori home
2. Atau gunakan skill update: `/update opencode-system-prompt`

### Backup System Prompt
```bash
# Backup otomatis akan tersimpan di:
C:\Users\USER\Documents\opencode-skills\opencode-system-prompt\backup\
```

## 📋 Struktur Direktori Final

```
C:\Users\USER\
├── .opencode\
│   └── AGENTS.md                 # ← AUTO-LOAD (system prompt utama)
├── .opencode.json                # ← KONFIGURASI GLOBAL
└── Documents\
    ├── AGENTS.md                 # ← Backup di Documents
    ├── .opencode.json            # ← Backup konfigurasi
    └── opencode-skills\
        └── opencode-system-prompt\
            ├── SKILL.md          # ← Skill menu utama
            ├── INSTRUKSI.md      # ← File instruksi ini
            ├── versions\
            │   ├── full.md       # ← Versi lengkap
            │   ├── concise.md    # ← Versi ringkas
            │   ├── admin.md      # ← Fokus administrasi
            │   ├── dev.md        # ← Fokus development
            │   └── ai.md         # ← Fokus AI engineering
            └── backup\           # ← Backup system prompt
```

## ⚙️ Konfigurasi yang Dibuat

### .opencode.json
```json
{
  "contextPaths": [
    ".opencode/AGENTS.md",
    "system-prompt-opencode.md"
  ],
  "agents": {
    "coder": {
      "model": "claude-4-sonnet",
      "maxTokens": 50000,
      "reasoningEffort": "medium"
    },
    "title": {
      "model": "gpt-4o-mini",
      "maxTokens": 80
    }
  },
  "tui": {
    "theme": "opencode"
  },
  "debug": false,
  "autoCompact": true
}
```

### AGENTS.md (Ringkasan)
- **Identitas**: Operator sekolah, web developer, AI learner
- **Tools**: Semua tools OpenCode dan MCP
- **Workflow**: Aturan untuk administrasi, development, AI
- **Auto-load**: Konfigurasi untuk otomatis dimuat

## 🛠️ Troubleshooting

### Jika System Prompt Tidak Auto-load
1. Pastikan file ada di `C:\Users\USER\.opencode\AGENTS.md`
2. Pastikan `.opencode.json` ada di `C:\Users\USER\.opencode.json`
3. Restart OpenCode
4. Periksa log error jika ada

### Jika Skill Tidak Muncul
1. Pastikan direktori skill ada: `opencode-skills/opencode-system-prompt/`
2. Pastikan file `SKILL.md` ada dan valid
3. Reload skills jika diperlukan

### Untuk Update System Prompt
1. Edit file di `C:\Users\USER\.opencode\AGENTS.md`
2. Atau edit file di `versions/` lalu copy ke lokasi utama
3. Backup otomatis akan dibuat sebelum update

## 📞 Dukungan
Untuk masalah atau pertanyaan:
1. Periksa file INSTRUKSI.md ini
2. Baca dokumentasi OpenCode
3. Gunakan skill troubleshooting jika ada

---
**Dibuat pada**: 2 April 2026  
**Versi**: 1.0  
**Status**: Siap digunakan