---
name: superpowers-writing-plans
description: "Use when: Sudah punya spec/requirements - Buat implementation plan detail SEBELUM coding"
---

# Writing Plans - Superpowers

**Gunakan setelah design di-approve!**

## Kapan Digunakan
- Mau buat implementation plan dari spec
- Mau breakdown tasks jadi bite-sized (2-5 menit per task)
- Mau structure file yang akan dibuat/dimodifikasi

## Struktur Plan
- **Goal** - One sentence describing what this builds
- **Architecture** - 2-3 sentences about approach
- **Tech Stack** - Key technologies/libraries
- **Tasks** - Each task with:
  - File paths (Create/Modify/Test)
  - Step-by-step (TDD: test → fail → code → pass → commit)
  - Complete code blocks
  - Exact commands with expected output

## Setiap Task Include:
1. Write failing test
2. Run test verify fail
3. Write minimal code
4. Run test verify pass
5. Commit

## Contoh Penggunaan
```
use skill tool to load superpowers/writing-plans
```

## Simpan ke:
`docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`