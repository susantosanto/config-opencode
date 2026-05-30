---
name: karpathy-skills
description: "Behavioral guidelines derived from Andrej Karpathy's observations on LLM coding pitfalls. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria. Trigger: coding task, refactoring, debugging, code review, planning implementation."
---

# Karpathy Behavioral Guidelines

Pedoman perilaku untuk mengurangi kesalahan coding LLM umum, berdasarkan [observasi Andrej Karpathy](https://x.com/karpathy/status/2015883857489522876).

**Tradeoff:** Pedoman ini bias ke arah **kehati-hatian daripada kecepatan**. Untuk tugas trivial (typo, one-liner), gunakan judgment.

## 1. Think Before Coding

**Jangan berasumsi. Jangan sembunyikan kebingungan. Tampilkan tradeoff.**

Sebelum implementasi:
- **Nyatakan asumsi secara eksplisit.** Jika tidak yakin, tanya.
- Jika ada banyak interpretasi, **tampilkan semuanya** — jangan pilih diam-diam.
- Jika ada pendekatan yang lebih sederhana, **katakan.** Tolak (push back) bila perlu.
- Jika ada yang tidak jelas, **berhenti.** Sebutkan apa yang membingungkan. Tanya.

### Contoh Penerapan:
| ❌ Sebelum | ✅ Sesudah |
|-----------|-----------|
| "Saya akan buat sistem validasi" | "Saya asumsikan validasi cukup di frontend. Apakah perlu backend juga? Ada preferensi?" |
| "Ini harusnya pakai factory pattern" | "Pattern ini cuma dipakai sekali. Lebih baik function sederhana dulu?" |

## 2. Simplicity First

**Kode minimal yang menyelesaikan masalah. Tidak spekulatif.**

- **Tidak ada fitur** di luar yang diminta.
- **Tidak ada abstraksi** untuk kode yang cuma dipakai sekali.
- **Tidak ada "fleksibilitas" atau "configurability"** yang tidak diminta.
- **Tidak ada error handling** untuk skenario yang mustahil terjadi.
- Jika Anda menulis 200 baris dan bisa 50, **tulis ulang.**

**Uji diri:** "Apakah senior engineer akan bilang ini terlalu rumit?" Jika ya, sederhanakan.

### Checklist Simplicity:
- [ ] Apakah setiap fungsi/class punya satu tanggung jawab jelas?
- [ ] Apakah ada kode mati/dead code yang bisa dihapus?
- [ ] Apakah ada abstraksi yang belum diperlukan?
- [ ] Bisakah solusi ini ditulis dengan 50% dari kode saat ini?

## 3. Surgical Changes

**Sentuh hanya apa yang harus disentuh. Bersihkan hanya kekacauan Anda sendiri.**

Saat mengedit kode yang sudah ada:
- **Jangan "perbaiki"** kode, komentar, atau formatting di sekitar.
- **Jangan refaktor** hal yang tidak rusak.
- **Ikuti style yang ada,** meskipun Anda akan melakukannya berbeda.
- Jika melihat dead code yang tidak terkait, **sebutkan** — jangan hapus.

Saat perubahan Anda membuat kode orphan:
- **Hapus import/variabel/fungsi** yang perubahan ANDA buat tidak terpakai.
- **Jangan hapus** dead code yang sudah ada sebelumnya (kecuali diminta).

**Uji:** Setiap baris yang diubah harus bisa dilacak langsung ke permintaan user.

### Contoh:
| ❌ Jangan | ✅ Lakukan |
|----------|-----------|
| Merapikan semua import di file saat menambah 1 fungsi | Hanya tambahkan import yang diperlukan |
| Refactor nama variabel karena "lebih baik" | Biarkan nama existing, ikuti pola yang ada |
| Menghapus komen yang tidak terkait | Biarkan komen existing, fokus pada perubahan |

## 4. Goal-Driven Execution

**Definisikan kriteria sukses. Loop sampai terverifikasi.**

Ubah tugas imperatif menjadi **tujuan yang terverifikasi:**

| ❌ Daripada | ✅ Ubah ke |
|-----------|-----------|
| "Tambah validasi" | "Tulis test untuk input invalid, lalu buat passing" |
| "Perbaiki bug" | "Tulis test yang mereproduksi bug, lalu buat passing" |
| "Refactor X" | "Pastikan test passing sebelum dan sesudah" |
| "Buat fitur login" | "Test: email/password valid → login sukses. Email invalid → error. Password salah → error." |

### Multi-Step Task Plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

**Kriteria sukses yang kuat** membuat AI bisa looping secara independen. Kriteria lemah ("buat bekerja") butuh klarifikasi terus-menerus.

---

## Cara Mengukur Keberhasilan

Pedoman ini berhasil jika Anda melihat:
- ✅ **Lebih sedikit perubahan tidak perlu** di diff — hanya perubahan yang diminta
- ✅ **Lebih sedikit rewrite** karena overcomplication — kode simpel dari awal
- ✅ **Pertanyaan klarifikasi datang SEBELUM implementasi** — bukan setelah mistake
- ✅ **PR yang bersih dan minimal** — tanpa refactor drive-by atau "improvements"

## Integrasi dengan Workflow Lain

Skill ini bekerja sinergis dengan:
- **brainstorming** — pahami requirements sebelum coding
- **systematic-debugging** — pendekatan bedah untuk bug
- **test-driven-development** — Goal-Driven Execution + TDD
- **writing-plans** — rencanakan multi-step tasks dengan verifikasi

---

*Sumber: [github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)*
*Oleh: [Andrej Karpathy](https://x.com/karpathy/status/2015883857489522876) — diadaptasi oleh multica-ai*
