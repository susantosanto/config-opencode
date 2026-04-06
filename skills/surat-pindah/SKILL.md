---
name: surat-pindah
description: "Buat surat pindah sekolah otomatis berdasarkan data siswa dari Dapodik. Mendukung konfirmasi jika nama ditemukan lebih dari satu siswa."
license: MIT
compatibility: opencode
metadata:
  audience: sd-operator
  workflow: document-generation
  source: custom
---

# Surat Pindah Sekolah Skill

Buat surat pindah sekolah otomatis berdasarkan data siswa dari Dapodik.

## Trigger Phrases
- "buat surat pindah [nama siswa]"
- "generate surat mutasi [nama siswa]"
- "surat pindah sekolah untuk [nama]"
- "cetak surat pindah [nama]"
- "SK pindah [nama siswa]"

## Prerequisites
- Aplikasi Dapodik harus berjalan di `http://localhost:5774`
- Token Web Service dan NPSN harus tersedia
- Package `python-docx` harus terinstall (`pip install python-docx`)
- Folder `Documents/SK_Pindah` akan dibuat otomatis

## Token & NPSN (SDN Pasirhalang)
- **Token**: `AlAiyPRTaYFDKLE`
- **NPSN**: `20205293`
- **URL**: `http://localhost:5774`
- **Sekolah**: SD NEGERI PASIRHALANG

## Workflow

### 1. Pastikan Dapodik Berjalan
Pastikan aplikasi Dapodik sudah running di `http://localhost:5774`.

### 2. Jalankan Script Generate Surat
Script tersedia di: `C:\Users\USER\Documents\opencode-skills\surat-pindah\generate_surat_pindah.py`

```bash
# Mode interaktif (via terminal)
python C:\Users\USER\Documents\opencode-skills\surat-pindah\generate_surat_pindah.py "[nama_siswa]"

# Mode auto (via OpenCode/Telegram, auto-select jika multiple)
python C:\Users\USER\Documents\opencode-skills\surat-pindah\generate_surat_pindah.py "[nama_siswa]" --auto

# Mode pilih siswa spesifik (1, 2, 3, dst)
python C:\Users\USER\Documents\opencode-skills\surat-pindah\generate_surat_pindah.py "[nama_siswa]" 2
```

### 3. Proses Konfirmasi (jika lebih dari 1 siswa)
Jika ditemukan lebih dari satu siswa dengan nama yang sama:
- Script menampilkan daftar semua siswa yang cocok
- User diminta memilih nomor siswa yang dimaksud
- Jika mode `--auto`, otomatis memilih siswa pertama
- Jika mode `[nomor]`, langsung pilih siswa sesuai nomor

### 4. Output
Script akan generate file DOCX di:
`C:\Users\USER\Documents\SK_Pindah\surat_mutasi_(nama_siswa).docx`

## Fitur

### ✅ Otomatis dari Dapodik
- Mengambil data siswa langsung dari Dapodik Web Service
- Data yang digunakan: nama, NISN, NIK, kelas, jenis kelamin, alamat, orang tua

### ✅ Template Berdasarkan SK Asli
- Menggunakan format asli "SK Pindah Sekolah.docx" yang sudah ada
- Kop surat sekolah lengkap
- Format sesuai standar Kemendikdasmen

### ✅ Multi-Halaman
- Halaman 1: Surat keterangan pindah dengan data siswa
- Halaman 2: Formulir untuk diisi sekolah tujuan

### ✅ Konfirmasi Siswa
- Jika nama ditemukan lebih dari 1, tampilkan pilihan
- User bisa memilih siswa yang tepat
- Mode auto untuk integrasi dengan bot

### ✅ JSON Output
- Output dalam format JSON untuk parsing oleh Telegram bot
- Status: `multiple_found` atau `success`
- Data siswa dan path file disertakan

## Struktur Surat

### Halaman 1 - Surat Keterangan
```
SURAT KETERANGAN PINDAH SEKOLAH
Nomor: 421.2/2026/SD - 007/2026

Yang bertanda tangan dibawah ini, Kepala Sekolah Dasar Negeri Pasirhalang
Desa Mandalamukti Kecamatan Cikalongwetan Kabupaten Bandung Barat
dengan ini menyatakan bahwa :

Nama            : [Nama Siswa]
NISN/ No. Induk : [NISN]
Jenis Kelamin   : [L/P]
Murid Kelas     : [Kelas]

Sesuai dengan Surat Keterangan Permohonan Pindah dari orang tua/wali murid :
Nama            : [Nama Ayah]
Ibu             : [Nama Ibu]
Alamat          : [Alamat Lengkap]

Telah mengajukan pindah sekolah ke SD Negeri Girimukti di Kecamatan
Cikalongwetan Kabupaten Bandung Barat - Jawabarat, bersama ini sertakan
Laporan Hasil Belajar Siswa (LAPOR).

[Mandalamukti, Tanggal]
Kepala Sekolah
(.........................)
```

### Halaman 2 - Formulir Sekolah Tujuan
```
SURAT KETERANGAN PINDAH SEKOLAH
Nomor: 421.2/2026/SD - 007/2026

Setelah anak tersebut diterima di sekolah ini, isian dibawah ini harap
diisi dan lembar kedua di kirim kembali pada kami.

Nama Sekolah    : ............................................................
Status Sekolah  : ............................................................
Alamat          : ............................................................
Desa/ Kelurahan : ............................................................
Kec/ Kab        : ............................................................
Provinsi        : ............................................................
Diterima Tanggal: ............................................................
Di Tingkat/ Kelas: ............................................................

Kepala Sekolah
(.........................)
```

## Contoh Penggunaan

### Via OpenCode
```
User: "buat surat pindah Ardi Firmansyah"
Aksi: 
1. Cari siswa "Ardi Firmansyah" di Dapodik
2. Jika ketemu 1, langsung generate surat
3. Jika ketemu >1, tampilkan pilihan
4. Simpan ke Documents/SK_Pindah/surat_mutasi_ardi_firmansyah.docx
```

### Via Telegram Bot
```
User: /suratpindah Ardi Firmansyah
Bot: 
  Ditemukan 2 siswa:
  1. Ardiansyah - Kelas 6 - NISN: 0146117215
  2. Ardi Firmansyah - Kelas 4a - NISN: 3153896240
  
  Pilih nomor (1-2) atau ketik nama lengkap:

User: 2
Bot: 
  ✅ Surat pindah berhasil dibuat!
  📄 File: surat_mutasi_ardi_firmansyah.docx
  📍 Lokasi: C:\Users\USER\Documents\SK_Pindah\
```

### Via Command Line
```bash
# Nama unik (langsung generate)
python generate_surat_pindah.py "Ardi Firmansyah"

# Nama ambigu (tampilkan pilihan)
python generate_surat_pindah.py "ardi"

# Auto-select siswa pertama
python generate_surat_pindah.py "ardi" --auto

# Pilih siswa ke-2
python generate_surat_pindah.py "ardi" 2
```

## JSON Output Format

### Multiple Found
```json
{
  "status": "multiple_found",
  "count": 2,
  "students": [
    {
      "number": 1,
      "nama": "Ardiansyah",
      "nisn": "0146117215",
      "kelas": "Kelas 6",
      "ttl": "BANDUNG BARAT, 2014-01-15"
    },
    {
      "number": 2,
      "nama": "Ardi Firmansyah",
      "nisn": "3153896240",
      "kelas": "Kelas 4a",
      "ttl": "Bandung Barat, 2015-07-03"
    }
  ]
}
```

### Success
```json
{
  "status": "success",
  "student": {
    "nama": "Ardi Firmansyah",
    "nisn": "3153896240",
    "kelas": "Kelas 4a"
  },
  "file": "C:\\Users\\USER\\Documents\\SK_Pindah\\surat_mutasi_ardi_firmansyah.docx"
}
```

## Error Handling

| Error | Penyebab | Solusi |
|-------|----------|--------|
| Dapodik tidak merespons | Aplikasi Dapodik tidak berjalan | Buka aplikasi Dapodik |
| Tidak ditemukan siswa | Nama salah/ejaan berbeda | Coba nama depan saja |
| Multiple students | Nama umum/sering dipakai | Pilih nomor siswa |
| Gagal generate surat | python-docx tidak terinstall | `pip install python-docx` |

## Customization

Edit file `generate_surat_pindah.py` untuk:
- Mengubah nama sekolah tujuan (default: SD Negeri Girimukti)
- Menambahkan data tambahan dari Dapodik
- Mengubah format nomor surat
- Menyesuaikan dengan template sekolah lain

## Files
- **Script**: `C:\Users\USER\Documents\opencode-skills\surat-pindah\generate_surat_pindah.py`
- **Output**: `C:\Users\USER\Documents\SK_Pindah\surat_mutasi_(nama).docx`
- **Template**: `C:\Users\USER\Documents\SK Pindah Sekolah.docx` (referensi)
