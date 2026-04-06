---
name: opencode-system-prompt
description: "Skill untuk mengelola system prompt OpenCode khusus operator sekolah dan web developer"
---

# Skill System Prompt OpenCode

## 🎯 Fungsi Utama
Skill ini menyediakan system prompt lengkap yang telah dikustomisasi untuk:
- Operator Sekolah Dasar Negeri
- Web Developer JavaScript/Apps Script
- AI Engineering Learner

## 🚀 Cara Menggunakan

### 1. Load System Prompt
```
/use opencode-system-prompt
```
Atau pilih dari menu skill.

### 2. Update System Prompt
```
/update opencode-system-prompt
```

### 3. Export System Prompt
```
/export opencode-system-prompt --format md
```

### 4. Import System Prompt
```
/import opencode-system-prompt --file path/to/file.md
```

## 📋 Versi Tersedia
1. **Lengkap**: Semua section dengan contoh (default)
2. **Ringkas**: Hanya poin-poin utama
3. **Administrasi Sekolah**: Fokus pada tugas administrasi
4. **Web Development**: Fokus pada JavaScript/Apps Script
5. **AI Engineering**: Fokus pada pembelajaran AI

## 🔧 Konfigurasi
System prompt otomatis di-load dari:
- `C:\Users\USER\.opencode\AGENTS.md` (auto-load global)
- `.opencode.json` dengan `contextPaths`

## 📁 Struktur Direktori
```
C:\Users\USER\Documents\opencode-skills\opencode-system-prompt\
├── SKILL.md           # File skill ini
├── versions\
│   ├── full.md        # Versi lengkap
│   ├── concise.md     # Versi ringkas
│   ├── admin.md       # Fokus administrasi
│   ├── dev.md         # Fokus development
│   └── ai.md          # Fokus AI engineering
└── backup\
    └── YYYY-MM-DD.md  # Backup system prompt
```

## 🔄 Auto-load
System prompt akan otomatis dimuat di setiap sesi baru melalui:
1. File AGENTS.md di direktori home
2. Konfigurasi .opencode.json

## 📞 Dukungan
Untuk masalah atau saran hubungi:
- Email: user@example.com
- GitHub: github.com/user/opencode-config

## 🛠️ Implementasi Skill

### Load System Prompt Full
Ketika user meminta "load system prompt lengkap", baca file `versions/full.md` dan terapkan sebagai system prompt.

### Load System Prompt Ringkas
Ketika user meminta "load system prompt ringkas", baca file `versions/concise.md`.

### Update System Prompt
1. Baca file system prompt yang ada
2. Tawarkan perubahan berdasarkan kebutuhan user
3. Simpan ke direktori backup dengan timestamp
4. Update file utama

### Export System Prompt
Ekspor system prompt ke format yang diminta (Markdown, JSON, atau TXT).

### Import System Prompt
Import system prompt dari file eksternal dengan validasi format.

## 📊 Monitoring
Skill ini dapat melacak:
- Kapan terakhir system prompt di-load
- Versi yang sedang digunakan
- Ukuran file system prompt
- Perubahan terakhir