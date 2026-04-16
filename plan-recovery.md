# Analisis Mendalam System Prompt OpenCode untuk Operator Sekolah

## Pendahuluan

Terima kasih telah mempercayakan system prompt Anda untuk dianalisis. Setelah membaca seluruh konten AGENTS.md Anda sepanjang 292 baris dan melakukan riset mendalam terkait best practices OpenCode serta jobdesk operator sekolah, saya memiliki gambaran komprehensif untuk memberikan penilaian dan rekomendasi perbaikan.

System prompt Anda sudah menunjukkan fondasi yang baik dengan penggabungan tiga konteks utama: operator sekolah, web developer, dan AI engineering learner. Namun, ada beberapa area yang perlu diperkuat berdasarkan temuan riset tentang OpenCode system prompts dan kebutuhan aktual operator sekolah di Indonesia.

---

## Kekuatan System Prompt Saat Ini

### Struktur yang Terorganisir

Sistem 6 fase workflow (GOAL, INSTRUCTIONS, DISCOVERIES, ACCOMPLISHED, RELEVANT FILES/DIRECTORIES, NEXT_STEPS) sudah implementasi yang baik. Riset dari OpenCode Improvement Plan menunjukkan bahwa verification checkpoints dengan 3-5 langkah sebelum completion adalah salah satu prioritas tinggi (PR #6 dengan score 9.4). Dengan forced output format seperti yang Anda terapkan, AI tidak bisa "melewatkan" fase penting.

### Penggabungan Konteks Multi-Domain

Tidak banyak system prompt yang menggabungkan tiga konteks berbeda seperti yours — administrasi sekolah, development, dan AI learning. Ini menunjukkan pemahaman bahwa operator sekolah modern membutuhkanskillset teknologi yang luas.

### Referensi Konfigurasi yang Spesifik

Anda sudah menyertakan referensi ke file konfigurasi spesifik (`dapodik_config.json`) yang merupakan praktik terbaik. Riset dari OpenCode documentation menunjukkan bahwa environment-specific configurations membantu AI memahami konteks spesifik daripada general instructions.

---

## Area yang Perlu Perbaikan

### 1. Overspecification — Melebihi Batas Optimal

**Temuan riset**: OpenCode Improvement Plan PR #1 menentukan target overspecification audit dengan batas **5-7 constraints per kategori dan kurang dari 1500 tokens**. System prompt Anda saat ini memiliki sekitar 292 baris yang kemungkinan sudah melampaui batas optimal.

**Analisis**: Ketika system prompt terlalu panjang, AI cenderung:

- Mengabaikan detail penting karena "kebanyakan informasi"
- Memproduksi output yang tidak sesuai format
- Kelelahan dalam mengikuti semua aturan

**Rekomendasi**: Rampingkan menjadi struktur yang lebih modular. Pisahkan menjadi:

- **Core identity** (100-200 tokens max)
- **Workflow rules** (200-300 tokens)
- **Domain-specific** (pisahkan per konteks, load sesuai kebutuhan)

### 2. Task Workflow — Terlalu Rigid untuk Semua Perintah

Saat ini Anda mewajibkan 6 fase untuk **SEMUA** perintah user. Riset menunjukkan bahwa pendekatan ini bisa menyebabkan inefficiency. OpenCode documentation menyarankan:

- **Simple questions**: tidak membutuhkan formal workflow
- **Complex tasks**: Gunakan workflow penuh
- **Implementations**: Delegate ke subagent

**Rekomendasi**: Modifikasi dengan conditional workflow:

```
JIKA:
- Task sederhana → Response langsung
- Task kompleks → Ikuti 6 fase
- Task multi-step → Gunakan todo list + delegation
```

### 3. Skill Integration — Tidak Ada Definition Format

Anda menyebutkan skills tetapi tidak mendefinisikan bagaimana skills harus di-load atau digunakan. Best practices dari OpenCode Skills documentation memerlukan **YAML frontmatter** dengan fields:

- `name` (required)
- `description` (required)
- `compatibility` (optional)

**Rekomendasi**: Tambahkan skill definitions dengan format yang benar untuk skills yang Anda sebutkan seperti:

- `dapodik-gtk-lookup`
- `dapodik-student-lookup`
- `surat-pindah`

### 4. Dapodik Workflow — Kurang Detail Operasional

Jobdesk operator sekolah yang saya temukan dari riset menyebutkan **11-17 tugas spesifik** yang harus dikuasai. Workflow Dapodik Anda hanya berisi:

- Baca konfigurasi dari `C:\Users\USER\.config\opencode\dapodik_config.json`
- Ikuti template resmi
- Validasi data sebelum input
- Backup data berkala
- Monitor update regulasi

Ini belum enough untuk tugas aktual. Berdasarkan riset, operator sekolah juga perlu mengerti:

**Data yang harus diinput ke Dapodik**:

- Data profil sekolah (nama, alamat, akreditasi)
- Data siswa (NISN, nama, tempat lahir, orang tua)
- Data guru dan tenaga kependidikan (NIP, sertifikasi)
- Data rombel dan jadwal
- Data sarana prasana

**Aplikasi pendukung yang perlu dikenal**:

- Dapodik (core)
- ARKAS (keuangan BOS)
- PMP (Pemetaan Mutu Pendidikan)
- Verval PD/GTK (verifikasi-validasi)
- Manajemen PD
- BOS Online

### 5. Tool References — Tidak Akurat dengan OpenCode

Anda menyebutkan tool names yang tidak sepenuhnya sesuai dengan OpenCode. Contoh:

- `bash` → Di OpenCode menggunakan `shell_execute_command`
- `question` → Tidak ada tool khusus, gunakan `question` function jika ada
- `sequential-thinking` → Tergantung platform

**Rekomendasi**: Sesuaikan dengan tool names yang valid untuk OpenCode. Lihat referensi dari OpenCode documentation untuk tool names yang benar.

### 6. Tidak Ada Turn Reminder System

**Temuan riset**: OpenCode Improvement Plan PR #5 (score 8.6) merekomendasikan injecting warnings pada "10 turns remaining" dan "5 turns remaining" untuk mencegah cost overruns. System prompt Anda tidak memiliki mekanisme untuk mengingatkan user atau membatasi conversation length.

### 7. Agent Delegation — Kurang Detail

Anda menyebutkan `task` untuk menjalankan subagent tetapi tidak menjelaskan:

- Kapan harus delegate
- Bagaimana cara memilih specialist yang tepat
- Apa bounded execution constraints

---

## Rekomendasi Perbaikan Spesifik

### Segmen 1: Core Identity (Sederhanakan)

```
## Identitas dan Konteks

### A. Operator Sekolah
Membantu administrasi digital sekolah:
- Dapodik: input, validasi, sinkronisasi data sekolah
- BOS: perencanaan, laporan, pertanggungjawaban
- Administrasi: dokumen, surat, inventaris

### B. Web Developer (sekunder)
JavaScript, Google Apps Script, HTML/CSS - untuk tugas desarrollo
```

### Segmen 2: Task Workflow (Conditional)

```
## Task Workflow (Fleksibel)

### Trigger: Task kompleks (3+ langkah)
Gunakan 6 fase: GOAL → INSTRUCTIONS → DISCOVERIES → ACCOMPLISHED → RELEVANT FILES → NEXT_STEPS

### Trigger: Task sederhana
Response langsung tanpa formal workflow

### Trigger: Implementasi multi-file
Buat todo list + pertimbangkan delegation ke @fixer atau specialist lain
```

### Segmen 3: Dapodik Specific (Perluas)

```
## Workflow Dapodik (Detail)

### Sebelum input:
1. Cek NPSN dan token dari dapodik_config.json
2. Pastikan Dapodik service running di localhost:5774
3. Backup data sebelumnya

### Data wajib divalidasi:
- NISN dan nama siswa
- NIP dan sertifikasi guru
- Data rombel dan jadwal
- Kondisi sarana

### Aplikasi pendukung:
- Dapodik: dapo.kemdikbud.go.id
- ARKAS: Rencana Kegiatan Anggaran
- Verval: verifikasi data PD/GTK
- BOS: bos.kemdikbud.go.id
```

### Segmen 4: Skills (Tambahkan Format)

```
## Available Skills

Trigger untuk:
- "cara lookup GTK" → Load skill dapodik-gtk-lookup
- "download data siswa" → Load skill dapodik-scraper
- "buat surat pindah" → Load skill surat-pindah
- Inventaris → Load skill yang sesuai
- Brainstorming → superpowers-brainstorm
- Debugging → systematic-debugging
```

### Segmen 5: Delegation Rules (Tambahkan)

```
## Kapan Delegate

| Kondisi | Action |
|---------|--------|
| exploration/pencarian | @explorer |
| dokumentasi library | @librarian |
| keputusan kompleks | @oracle |
| UI/UX user-facing | @designer |
| implementasi bounded | @fixer |
| multiple model opinion | @council |

## Cara Delegate:
Berikan context: "Lokasi: file path, Line: nomer"
Berikan ringkasan, biarkan specialist baca sendiri
```

---

## Penutup

System prompt Anda sudah memiliki fondasi yang solid dengan struktur workflow yang jelas dan penggabungan konteks yang unik. Kekuatan utama ada pada penggabungan tiga role (operator sekolah, web developer, AI learner) yang mencerminkan realitas pekerjaan Anda.

Area utama perbaikan adalah:

1. **Merampingkan** - Kurangi overspecification ke threshold optimal
2. **Fleksibilitas workflow** - Bukan semua task butuh formal 6 fase
3. **Detil operasional** - Perluas Dapodik workflow dengan tugas spesifik
4. **Skills format** - Gunakan standard YAML frontmatter
5. **Tool accuracy** - Sesuaikan dengan tool names OpenCode yang valid
6. **Delegation clarity** - Tambahkan kapan dan bagaimana harus delegate

Jika Anda ingin, saya bisa membantu membuat versi revisi dari system prompt ini dengan rekomendasi-rekomendasi di atas. Atau jika ada bagian spesifik yang ingin didalami terlebih dahulu, boleh указа.

---

**Referensi Riset yang Digunakan**:

- OpenCode Improvement Plan (GitHub issue #14395) - Prioritas P0-P3 dengan scores
- OpenCode Skills Documentation - Format dan best practices
- OpenCode Agents Configuration - Tools dan permissions
- Jobdesk Operator Sekolah (multiple sources) - 11-17 tugas spesifik
- OpenCode System Prompts Documentation - Hierarchy dan customization

---

**Metadata**:

- Tanggal analisis: 16 April 2026
- File sumber: C:\Users\USER\.config\opencode\AGENTS.md
- Total baris asli: 292 baris
- Versi: 1.0 (analisis pertama)