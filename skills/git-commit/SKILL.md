---
name: git-commit
description: "Use when perlu commit perubahan ke git repository, menulis pesan commit, atau mengubah commit terakhir (amend)"
license: MIT
compatibility: opencode
metadata:
  workflow: version-control
  source: custom
---

# Git Commit Skill

Buat commit dengan pesan yang informatif dan terstruktur.

## Trigger Phrases

- "commit perubahan"
- "git commit"
- "buat commit"
- "simpan ke git"
- "commit dengan pesan"
- "amend commit"
- "ubah pesan commit"
- "commit staging"
- "commit perbaikan"

## CLI Usage

```bash
# Commit dengan pesan langsung
git commit -m "feat: tambah fitur login"

# Commit dengan editor (untuk pesan panjang)
git commit

# Commit semua file yang di-track (skip staging)
git commit -am "fix: perbaiki bug validasi"

# Commit + sign-off
git commit -s -m "feat: tambah API endpoint"

# Tambah ke commit terakhir (amend)
git commit --amend -m "pesan baru"

# Tambah perubahan ke commit terakhir tanpa ubah pesan
git commit --amend --no-edit
```

## Workflow

### 1. Pastikan Staging Area Benar
```bash
git status
git diff --cached
```

### 2. Tulis Pesan Commit

**Format: Conventional Commits**
```
<type>: <deskripsi singkat>

<opsional: penjelasan detail>
```

**Type:**
| Type | Kapan | Contoh |
|------|-------|--------|
| `feat` | Fitur baru | `feat: tambah halaman dashboard` |
| `fix` | Bug fix | `fix: perbaiki crash di login` |
| `refactor` | Refaktor kode | `refactor: pindah helper ke utils` |
| `docs` | Dokumentasi | `docs: update README` |
| `style` | Formatting | `style: prettier formatting` |
| `test` | Testing | `test: tambah unit test login` |
| `chore` | Tooling/tugas | `chore: update dependencies` |

**Aturan:**
- **Pertama commit** → `feat: initial commit`
- **Untuk sesi Codebuff** → pakai [caveman-commit] untuk format ringkas

### 3. Alternatif: Pesan Bahasa Indonesia

Untuk proyek ARKAS/Dapodik:
```
feat: tambah export BKU excel
fix: perbaiki koneksi database
refactor: optimasi query kas_umum
```

### 4. Commit

```bash
git commit -m "feat: tambah fitur export BKU"
```

### 5. Perbaiki Jika Salah

**ubah pesan commit terakhir:**
```bash
git commit --amend -m "feat: tambah fitur export BKU dengan filter tanggal"
```

**tambah perubahan ke commit terakhir:**
```bash
git add file_lupa.py
git commit --amend --no-edit
```

## Common Mistakes

| Mistake | Akibat | Solusi |
|---------|--------|--------|
| Pesan terlalu panjang di `-m` | Sulit dibaca | Pakai editor (tanpa `-m`) |
| Lupa file | Commit tidak lengkap | `git add` + `--amend --no-edit` |
| Campur 2 fitur dalam 1 commit | Sulit revert | Stage per fitur, commit bertahap |
| `git commit -am` untuk file baru | File baru tidak tercommit | `git add` dulu baru commit |

## Best Practices

- **Commit kecil, sering, atomic** — 1 commit = 1 logical change
- **Pesan commit dalam bahasa Inggris** untuk proyek teknis
- **Pesan dalam bahasa Indonesia** untuk proyek ARKAS/Dapodik/BOS
- **Gunakan imperative** ("tambah" bukan "menambahkan")
- **Deskripsi opsional** untuk commit kompleks (tambah baris kosong setelah subject)
- **Jangan commit file yang tidak selesai** — simpen dulu
