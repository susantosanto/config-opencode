---
name: git-add
description: "Use when perlu staging file ke git sebelum commit, menambahkan file baru, atau menghapus file dari staging area di repository git"
license: MIT
compatibility: opencode
metadata:
  workflow: version-control
  source: custom
---

# Git Add Skill

Stage file ke git index (staging area) sebelum commit.

## Trigger Phrases

- "stage file ini"
- "git add file"
- "track file baru"
- "masukkan ke staging"
- "add file ke git"
- "unstaging file"
- "stage perubahan"
- "git add semua"

## CLI Usage

```bash
# Stage file spesifik
git add path/to/file.ts

# Stage semua perubahan (hati-hati)
git add .

# Stage file dengan pattern
git add src/*.ts

# Stage interaktif
git add -p

# Stage file yang sudah di-track saja (tanpa file baru)
git add -u

# Stage semua termasuk yang dihapus
git add -A

# Hapus dari staging (tanpa hapus file)
git reset HEAD path/to/file.ts

# Hapus dari staging + discard perubahan (cara modern)
git restore path/to/file.ts

# Cara lama (masih valid)
git checkout -- path/to/file.ts
```

## Workflow

### 1. Cek Status Dulu
```bash
git status
```
Lihat file mana yang modified, untracked, atau deleted sebelum add.

### 2. Stage dengan Tepat

**File baru + modified sekaligus:**
```bash
git add .
# atau
git add -A
```

**Hanya file tertentu (rekomendasi):**
```bash
git add src/components/Button.tsx
git add src/utils/helpers.ts
```

**Hanya perubahan file yang sudah di-track:**
```bash
git add -u
```

**Stage per bagian file (interaktif):**
```bash
git add -p
```
Berguna kalau satu file ada beberapa perubahan independen.

### 3. Double Check
```bash
git status
git diff --cached  # Lihat yang akan di-commit
```

### 4. Undo Jika Salah

**Unstage file (file tetap ada, perubahan aman):**
```bash
git reset HEAD file.ts
```

**Unstage + discard perubahan:**
```bash
git restore file.ts
```

## Common Mistakes

| Mistake | Akibat | Solusi |
|---------|--------|--------|
| `git add .` tanpa cek status | File tidak sengaja ikut terstage | Selalu `git status` dulu |
| Lupa `.gitignore` | File build/config ikut terstage | Setup `.gitignore` sebelum add |
| Stage file besar | Repo membengkak | Gunakan `.gitignore` atau `git LFS` |
| `git add .` di root repo | File di luar proyek ikut | `git init` di folder yang benar |

## Contoh .gitignore

Untuk project Python:
```
__pycache__/
*.pyc
.env
*.db
*.xlsx
.DS_Store
```

Untuk project Node:
```
node_modules/
.env
.next/
dist/
.DS_Store
```

## Best Practices

- **Stage per logical change** — jangan campur 2 fitur beda dalam 1 commit
- **Gunakan `git add -p`** untuk memisahkan perubahan dalam 1 file
- **Cek `git status` sebelum dan sesudah** add
- **Jangan `git add .`** tanpa tahu apa yang kamu tambahkan
- **`git commit -am`** = `git add -u` + `commit` (skip file baru, hanya tracked)
