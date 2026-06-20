---
name: arkas-query
description: "Use when querying ARKAS SQLCipher database using sqlcipher.exe binary. Quick access to query, export, and analyze ARKAS data without Python dependencies."
license: MIT
compatibility: opencode
metadata:
  audience: sd-operator
  workflow: data-operations
  source: custom
---

# ARKAS Query Skill

Query database ARKAS (SQLCipher) menggunakan `sqlcipher.exe` binary langsung dari terminal.

## Trigger Phrases

- "query arkas"
- "lihat data arkas"
- "cek tabel arkas"
- "export arkas"
- "sqlcipher arkas"
- "database sekolah"
- "anggaran sekolah"
- "kas umum"
- "bku arkas"
- "rapbs arkas"

## Prerequisites

- `sqlcipher.exe` di `C:\Users\USER\sqlcipher.exe`
- Database ARKAS di `C:\Users\USER\AppData\Roaming\Arkas\arkas.db`

## Quick Usage

```powershell
# Set alias sementara
Set-Alias arkas C:\Users\USER\arkas-query.ps1

# Gunakan
arkas tables
arkas sekolah
arkas query "SELECT * FROM kas_umum LIMIT 5"
```

## Commands

| Perintah | Fungsi |
|----------|--------|
| `tables` | Semua tabel |
| `schema [tabel]` | Struktur tabel |
| `query "SQL"` | Jalankan SQL |
| `query "SQL" -Export` | Export ke Excel |
| `sekolah` | Info sekolah |
| `anggaran [tahun]` | Ringkasan anggaran |
| `triggers` | Daftar trigger |
| `interactive` | Mode interaktif |
| `backup` | Backup database |

## Contoh Query

```powershell
# 10 transaksi terbaru
C:\Users\USER\arkas-query.ps1 query "SELECT id_kas_umum, tanggal_transaksi, uraian, saldo FROM kas_umum WHERE soft_delete=0 ORDER BY create_date DESC LIMIT 10"

# Anggaran per tahun
C:\Users\USER\arkas-query.ps1 query "SELECT tahun_anggaran, COUNT(*) as jumlah, SUM(jumlah) as total FROM anggaran WHERE soft_delete=0 GROUP BY tahun_anggaran"

# PTK/Guru
C:\Users\USER\arkas-query.ps1 query "SELECT nama, jenis_ptk FROM ptk WHERE soft_delete=0"

# Export ke Excel
C:\Users\USER\arkas-query.ps1 query "SELECT * FROM kas_umum WHERE soft_delete=0" -Export
```

## Direct sqlcipher.exe

```powershell
& "$env:USERPROFILE\sqlcipher.exe" "C:\Users\USER\AppData\Roaming\Arkas\arkas.db" -cmd "PRAGMA key = 'K3md1kbudRIS3n4yan';" ".mode column" ".headers on" "SELECT name FROM sqlite_master WHERE type='table';"
```

## Database Info

- **Sekolah**: SD NEGERI PASIRHALANG
- **NPSN**: 20205293
- **Path**: `C:\Users\USER\AppData\Roaming\Arkas\arkas.db`
- **Key**: `K3md1kbudRIS3n4yan`
- **Cipher**: SQLCipher 4.4.0
