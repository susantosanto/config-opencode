---
name: arkas-dbops
description: "Use when connecting to ARKAS SQLCipher database for eksplorasi tabel, query kustom, export ke Excel, cek schema, atau analisis data ARKAS (Aplikasi Rencana Kegiatan dan Anggaran Sekolah)"
license: MIT
compatibility: opencode
metadata:
  audience: sd-operator
  workflow: data-operations
  source: custom
---

# ARKAS DB Ops Skill

Koneksi, eksplorasi, query, dan export database ARKAS (SQLCipher) dari CLI menggunakan `sqlcipher.exe`.

## Trigger Phrases

- "lihat tabel arkas"
- "cek struktur database arkas"
- "query data arkas"
- "export data arkas ke excel"
- "cari tabel di arkas"
- "analisis database arkas"
- "cek schema tabel [nama]"
- "jalankan SQL di arkas"
- "info sekolah arkas"
- "ringkasan anggaran arkas"
- "backup database arkas"

## Prerequisites

- `sqlcipher.exe` sudah terinstall di `C:\Users\USER\sqlcipher.exe`
- Database ARKAS SQLCipher di `C:\Users\USER\AppData\Roaming\Arkas\arkas.db`
- Konfigurasi di: `~\.config\opencode\arkas_config.json`

## Script Location

**Script sudah tersedia** di folder skill ini: `arkas-query.ps1`

```powershell
# Jalankan langsung dari folder skill
powershell -ExecutionPolicy Bypass -File .config/opencode/skills/arkas-dbops/arkas-query.ps1 [perintah]
```

Atau gunakan script global yang sudah dibuat:
```powershell
C:\Users\USER\arkas-query.ps1 [perintah]
```

## CLI Usage

| Perintah | Deskripsi | Contoh |
|----------|-----------|--------|
| `tables` | Daftar semua tabel | `arkas-query.ps1 tables` |
| `schema [tabel]` | Lihat struktur tabel | `arkas-query.ps1 schema kas_umum` |
| `query "SQL"` | Jalankan SQL kustom | `arkas-query.ps1 query "SELECT * FROM kas_umum LIMIT 10"` |
| `query "SQL" -Export` | Query + export ke Excel | `arkas-query.ps1 query "SELECT * FROM anggaran" -Export` |
| `sekolah` | Info profil sekolah | `arkas-query.ps1 sekolah` |
| `anggaran [tahun]` | Ringkasan anggaran | `arkas-query.ps1 anggaran 2026` |
| `triggers` | Daftar trigger database | `arkas-query.ps1 triggers` |
| `interactive` | Mode interaktif | `arkas-query.ps1 interactive` |
| `backup [nama]` | Backup database | `arkas-query.ps1 backup` |

## Workflow

### 1. Quick Check Status
```powershell
C:\Users\USER\arkas-query.ps1 sekolah
C:\Users\USER\arkas-query.ps1 tables
```

### 2. Eksplorasi Database
```powershell
# Lihat struktur tabel tertentu
C:\Users\USER\arkas-query.ps1 schema kas_umum

# Lihat semua trigger
C:\Users\USER\arkas-query.ps1 triggers
```

### 3. Query Data
```powershell
# 10 transaksi terbaru
C:\Users\USER\arkas-query.ps1 query "SELECT * FROM kas_umum WHERE soft_delete=0 ORDER BY create_date DESC LIMIT 10"

# Ringkasan anggaran per tahun
C:\Users\USER\arkas-query.ps1 query "SELECT tahun_anggaran, COUNT(*), SUM(jumlah) FROM anggaran WHERE soft_delete=0 GROUP BY tahun_anggaran"
```

### 4. Export ke Excel
```powershell
C:\Users\USER\arkas-query.ps1 query "SELECT * FROM kas_umum WHERE tanggal_transaksi LIKE '2026-03-%' AND soft_delete=0" -Export
```

### 5. Mode Interaktif
```powershell
C:\Users\USER\arkas-query.ps1 interactive
# Lalu ketik SQL langsung:
# SELECT * FROM kas_umum LIMIT 5;
# .quit
```

### 6. Backup Database
```powershell
C:\Users\USER\arkas-query.ps1 backup
C:\Users\USER\arkas-query.ps1 backup my_backup_2026.db
```

## Output Format

Output console menampilkan:
- **Tables**: Nama tabel + jumlah baris
- **Schema**: Kolom, tipe, primary key
- **Query**: Tabel hasil dengan header
- **Excel**: File `.xlsx` di `~/Documents/arkas_analysis/exports/`

## Error Handling

| Error | Penyebab | Solusi |
|-------|----------|--------|
| `sqlcipher.exe tidak ditemukan` | Binary belum diinstall | Download dari `https://github.com/Katecca/sqlcipher-static-binary` |
| `Config tidak ditemukan` | `arkas_config.json` belum ada | Buat file config di `~/.config/opencode/` |
| `Database tidak ditemukan` | Path DB salah | Cek `db_path` di config |
| `Python tidak ditemukan` | Export butuh Python | Install Python 3.11+ |

## Config Format

```json
{
  "arkas": {
    "db_path": "C:\\Users\\USER\\AppData\\Roaming\\Arkas\\arkas.db",
    "key": "K3md1kbudRIS3n4yan",
    "cipher_compatibility": 4,
    "sekolah": "SD NEGERI PASIRHALANG",
    "npsn": "20205293"
  }
}
```

## Direct sqlcipher.exe Usage

Jika ingin menggunakan sqlcipher.exe langsung tanpa wrapper:

```powershell
# Lihat semua tabel
& "$env:USERPROFILE\sqlcipher.exe" "C:\Users\USER\AppData\Roaming\Arkas\arkas.db" -cmd "PRAGMA key = 'K3md1kbudRIS3n4yan';" ".mode column" ".headers on" "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"

# Query data
& "$env:USERPROFILE\sqlcipher.exe" "C:\Users\USER\AppData\Roaming\Arkas\arkas.db" -cmd "PRAGMA key = 'K3md1kbudRIS3n4yan';" ".mode column" ".headers on" "SELECT * FROM kas_umum LIMIT 10;"

# Export ke CSV
& "$env:USERPROFILE\sqlcipher.exe" "C:\Users\USER\AppData\Roaming\Arkas\arkas.db" -cmd "PRAGMA key = 'K3md1kbudRIS3n4yan';" ".mode csv" ".output C:/temp/export.csv" "SELECT * FROM kas_umum;"
```
