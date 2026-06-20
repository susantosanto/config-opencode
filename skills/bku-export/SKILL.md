---
name: bku-export
description: "Use when perlu export Buku Kas Umum (BKU) dari ARKAS ke Excel untuk laporan keuangan BOS bulanan atau tahunan, dengan format debit/kredit/saldo otomatis"
license: MIT
compatibility: opencode
metadata:
  audience: sd-operator
  workflow: financial-reporting
  source: custom
---

# BKU Export Skill

Export Buku Kas Umum (BKU) dari database ARKAS ke Excel dengan format debit, kredit, dan saldo otomatis.

## Trigger Phrases

- "export bku maret 2025"
- "buat laporan bku bulan [bulan]"
- "cetak buku kas umum"
- "export bku tahun [tahun]"
- "download bku ke excel"
- "laporan keuangan bos"
- "bku bulan ini"
- "rekapitulasi bku per bulan"
- "kas umum export"
- "bku tahunan"

## Prerequisites

- Database ARKAS SQLCipher (langsung dari `AppData/Roaming/Arkas/arkas.db`)
- Konfigurasi di: `~\.config\opencode\arkas_config.json`
- Package Python: `sqlcipher3-binary`, `pandas`, `openpyxl`

## Script Location

**Script sudah tersedia** di folder skill ini: `bku_export.py`

```bash
python .config/opencode/skills/bku-export/bku_export.py [opsi]
```

## CLI Usage

| Perintah | Deskripsi | Contoh |
|----------|-----------|--------|
| `(tanpa argumen)` | Export tahun berjalan | `bku_export.py` |
| `--bulan N` | Export bulan tertentu | `bku_export.py --bulan 3` |
| `--bulan N --tahun T` | Export bulan+tahun | `bku_export.py --bulan 3 --tahun 2025` |
| `--tahun T` | Export full tahun | `bku_export.py --tahun 2025` |
| `--bulan A-B` | Export range bulan | `bku_export.py --bulan 1-3` |
| `--format rekapitulasi` | Ringkasan per bulan | `bku_export.py --tahun 2025 --format rekapitulasi` |
| `--list` | Lihat periode tersedia | `bku_export.py --list` |
| `--output path.xlsx` | Tentukan file output | `bku_export.py --bulan 3 --output laporan.xlsx` |

## Workflow

### 1. Cari Periode Tersedia
```bash
python .config/opencode/skills/bku-export/bku_export.py --list
```

### 2. Export Bulanan
```bash
# Maret 2025
python .config/opencode/skills/bku-export/bku_export.py --bulan 3 --tahun 2025

# Bulan ini (tanpa --tahun = tahun berjalan)
python .config/opencode/skills/bku-export/bku_export.py --bulan 3
```

### 3. Export Rentang Bulan
```bash
# Januari - Juni 2025
python .config/opencode/skills/bku-export/bku_export.py --bulan 1-6 --tahun 2025
```

### 4. Export Tahunan
```bash
python .config/opencode/skills/bku-export/bku_export.py --tahun 2025
```

### 5. Rekapitulasi (Ringkasan per Bulan)
```bash
python .config/opencode/skills/bku-export/bku_export.py --tahun 2025 --format rekapitulasi
```

## Klasifikasi Transaksi

Script otomatis mengklasifikasikan transaksi berdasarkan `id_ref_bku`:

**Debit (pemasukan):**
- Tipe 1, 2, 6, 8, 9, 10, 23, 25, 26, 28, 29, 30
- Contoh: Saldo awal, penerimaan BOS, jasa bank, dll

**Kredit (pengeluaran):**
- Tipe 3, 4, 5, 7, 11, 12, 13, 14, 15, 24, 27, 31, 32, 33, 34, 35
- Contoh: Belanja barang, honor, ATK, listrik, dll

## Output Format

File Excel (`.xlsx`) dengan kolom:
| Kolom | Deskripsi |
|-------|-----------|
| Tanggal | Tanggal transaksi |
| No. Bukti | Nomor bukti transaksi |
| Uraian | Deskripsi transaksi |
| Jenis | DEBET atau KREDIT |
| Ref BKU | Nama referensi BKU |
| Debit | Jumlah pemasukan (Rp) |
| Kredit | Jumlah pengeluaran (Rp) |
| Saldo | Saldo berjalan (Rp) |

Excel sudah terformat dengan:
- Header navy dengan font putih
- Freeze pane baris pertama
- Lebar kolom otomatis
- Format Rp untuk kolom keuangan

## Output File Path

- Default: `~/Documents/arkas_analysis/exports/BKU_[Bulan]_[Tahun].xlsx`
- Bisa ditentukan dengan `--output`

## Error Handling

| Error | Penyebab | Solusi |
|-------|----------|--------|
| Tidak ada data | Periode tidak ada transaksi | Cek `--list` untuk periode valid |
| sqlcipher3 error | Package belum diinstall | `pip install sqlcipher3-binary` |
| Config error | File config belum ada | Buat `arkas_config.json` |
| Export gagal | pandas/openpyxl belum ada | `pip install pandas openpyxl` |
