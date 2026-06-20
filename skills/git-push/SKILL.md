---
name: git-push
description: "Use when perlu push commit ke remote repository git, membuat branch baru, atau pull sebelum push untuk hindari konflik"
license: MIT
compatibility: opencode
metadata:
  workflow: version-control
  source: custom
---

# Git Push Skill

Push commit lokal ke remote repository (GitHub, GitLab, Bitbucket, dll).

## Trigger Phrases

- "push ke remote"
- "git push"
- "upload ke github"
- "push branch"
- "kirim commit ke remote"
- "push perubahan"
- "git push origin"
- "deploy via git push"
- "buat branch baru"
- "pull sebelum push"

## CLI Usage

```bash
# Push ke remote default (origin, branch saat ini)
git push

# Push branch spesifik
git push origin main

# Push branch baru ke remote (auto-create)
git push -u origin nama-branch

# Push semua branch
git push --all origin

# Push tags
git push --tags

# Force push (HATI-HATI! timpa remote)
git push --force origin nama-branch

# Force push dengan lease (lebih aman)
git push --force-with-lease origin nama-branch

# Hapus branch remote
git push origin --delete nama-branch
```

## Workflow

### 1. Pastikan Commit Sudah Siap
```bash
git status
git log --oneline -5
```

### 2. Pull Dulu Sebelum Push (Hindari Konflik)
```bash
git pull --rebase origin main
```

### 3. Push ke Remote
```bash
git push origin main
```

### 4. Untuk Branch Baru (Pertama Kali)
```bash
git push -u origin nama-branch-baru
```
Flag `-u` (set upstream) membuat tracking, jadi next tinggal `git push`.

### 5. Jika Konflik

```bash
# Pull + rebase
git pull --rebase origin main
# Selesaikan konflik
git add .
git rebase --continue
# Push
git push origin nama-branch
```

## Force Push Safety

| Situasi | Perintah | Risiko |
|---------|----------|--------|
| Solo branch | `git push --force` | Rendah (sendiri) |
| Shared branch | `git push --force-with-lease` | Sedang (cek remote) |
| Branch orang lain | **JANGAN** | Tinggi |

**Aturan:**
- **Jangan** `--force` push ke branch shared (main, develop, dll)
- **Gunakan** `--force-with-lease` lebih aman dari `--force`
- **Hanya** force push ke branch pribadi / feature

## Common Mistakes

| Mistake | Akibat | Solusi |
|---------|--------|--------|
| Push tanpa pull dulu | Konflik merge | `git pull --rebase` dulu |
| Lupa `-u` di branch baru | Push gagal | `git push -u origin [branch]` |
| Force push ke shared branch | History remote rusak | Jangan lakukan! |
| Push commit belum di-test | Bug di remote | Cek dulu sebelum push |
| Push file besar | Gagal atau lambat | Setup `.gitignore` / Git LFS |

## Best Practices

- **Pull sebelum push** — `git pull --rebase` untuk history bersih
- **Push sering** — jangan nunggu banyak commit
- **Jangan force push ke main/production**
- **Gunakan `--force-with-lease`** jika terpaksa force push
- **Cek remote URL** dengan `git remote -v`
- **Untuk branch baru**, selalu pakai `-u` agar tracking otomatis
