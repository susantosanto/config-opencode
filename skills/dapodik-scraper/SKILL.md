---
name: dapodik-scraper
description: "Download data peserta didik dari Dapodik Web Service ke Excel secara otomatis"
license: MIT
compatibility: opencode
metadata:
  audience: sd-operator
  workflow: data-extraction
  source: custom
---

# Dapodik Scraper Skill

Download data peserta didik dari aplikasi Dapodik Web Service secara otomatis dan simpan ke file Excel.

## Trigger Phrases
- "download data peserta didik"
- "unduh data PD dari dapodik"
- "ambil data siswa dari dapodik"
- "scraping data dapodik"
- "ekstrak data peserta didik"
- "download daftar PD"
- "dapodik download"
- "ambil data dari dapodik"
- "tarik data siswa"
- "export data peserta didik ke excel"

## Prerequisites
- Aplikasi Dapodik harus berjalan di `http://localhost:5774`
- Token Web Service dan NPSN harus tersedia
- Package `requests`, `pandas`, `openpyxl` harus terinstall

## Token & NPSN (SDN Pasirhalang)
- **Token**: `AlAiyPRTaYFDKLE`
- **NPSN**: `20205293`
- **URL**: `http://localhost:5774`

## Workflow

### 1. Pastikan Dapodik Berjalan
Pastikan aplikasi Dapodik sudah running di `http://localhost:5774`. Jika belum, minta user membuka aplikasi Dapodik desktop terlebih dahulu.

### 2. Jalankan Script
Script sudah tersedia di: `C:\Users\USER\Documents\dapodik_download.py`

```bash
python C:\Users\USER\Documents\dapodik_download.py
```

### 3. Verifikasi Output
Script akan menghasilkan file Excel di: `C:\Users\USER\Documents\daftar_pd.xlsx`

Pastikan output menampilkan:
- Total peserta didik berhasil didownload
- File Excel tersimpan
- Contoh data ditampilkan

## Script Content

```python
#!/usr/bin/env python3
"""
Script untuk download SEMUA data peserta didik dari Dapodik Web Service
Menggunakan direct API call (bypass library yang bermasalah)
"""
import requests
import pandas as pd
from datetime import datetime

TOKEN = "AlAiyPRTaYFDKLE"
NPSN = "20205293"
BASE_URL = "http://localhost:5774"
OUTPUT_FILE = r"C:\Users\USER\Documents\daftar_pd.xlsx"

def get_all_peserta_didik():
    """Get ALL peserta didik data with pagination"""
    headers = {
        "Accept": "*/*",
        "Authorization": f"Bearer {TOKEN}",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "User-Agent": "dapodik-webservice"
    }
    
    all_data = []
    start = 0
    limit = 200  # Get 200 per request
    
    print("=" * 60)
    print("  DOWNLOAD DATA PESERTA DIDIK - Dapodik Web Service")
    print("=" * 60)
    
    while True:
        params = {"npsn": NPSN, "start": start, "limit": limit}
        
        try:
            r = requests.get(
                f"{BASE_URL}/WebService/getPesertaDidik",
                headers=headers,
                params=params,
                timeout=30
            )
            
            if r.status_code != 200:
                print(f"Error: HTTP {r.status_code}")
                break
            
            data = r.json()
            rows = data.get("rows", [])
            total = data.get("results", 0)
            
            if not rows:
                break
            
            all_data.extend(rows)
            print(f"  Mengambil data {start + 1}-{start + len(rows)} dari {total}...")
            
            start += limit
            if start >= total:
                break
                
        except Exception as e:
            print(f"Error: {e}")
            break
    
    return all_data

def save_to_excel(data):
    """Save data to Excel file"""
    if not data:
        print("Tidak ada data untuk disimpan")
        return
    
    df = pd.DataFrame(data)
    
    # Reorder columns - put important ones first
    important_cols = [
        "nama", "nisn", "nik", "jenis_kelamin", "tempat_lahir", 
        "tanggal_lahir", "agama_id_str", "nama_ayah", "pekerjaan_ayah_id_str",
        "nama_ibu", "pekerjaan_ibu_id_str", "nama_wali", "pekerjaan_wali_id_str",
        "anak_keberapa", "alamat_jalan", "rt", "rw", "nama_dusun",
        "desa_kelurahan", "kode_pos", "lintang", "bujur",
        "nomor_telepon_rumah", "nomor_telepon_seluler", "email",
        "sekolah_asal", "nipd", "jenis_pendaftaran_id_str",
        "tanggal_masuk_sekolah", "rombongan_belajar_id",
        "nama_rombel", "tingkat_pendidikan_id",
        "kurikulum_id_str", "semester_id", "kebutuhan_khusus",
        "tinggi_badan", "berat_badan",
        "peserta_didik_id", "registrasi_id", "anggota_rombel_id"
    ]
    
    # Only keep columns that exist
    existing_cols = [c for c in important_cols if c in df.columns]
    # Add any extra columns not in our list
    extra_cols = [c for c in df.columns if c not in important_cols]
    final_cols = existing_cols + extra_cols
    
    df = df[final_cols]
    
    # Save to Excel
    df.to_excel(OUTPUT_FILE, index=False)
    
    print(f"\n{'=' * 60}")
    print(f"  DATA BERHASIL DISIMPAN!")
    print(f"{'=' * 60}")
    print(f"  File: {OUTPUT_FILE}")
    print(f"  Total: {len(df)} peserta didik")
    print(f"  Kolom: {len(df.columns)} field")
    print(f"  Waktu: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"{'=' * 60}")
    
    # Show sample
    print(f"\n  CONTOH DATA (3 baris pertama):")
    print(f"  {'-' * 60}")
    for _, row in df.head(3).iterrows():
        print(f"  Nama: {row.get('nama', '-')}")
        print(f"  NISN: {row.get('nisn', '-')}")
        print(f"  Kelas: {row.get('nama_rombel', '-')}")
        print(f"  {'-' * 60}")

if __name__ == "__main__":
    data = get_all_peserta_didik()
    save_to_excel(data)
```

## API Endpoint Reference
- **URL**: `http://localhost:5774/WebService/{function}`
- **Auth**: `Authorization: Bearer {TOKEN}`
- **Params**: `npsn={NPSN}&start={offset}&limit={count}`

### Available Functions
| Function | Deskripsi |
|----------|-----------|
| `getPesertaDidik` | Data peserta didik |
| `getGtk` | Data GTK (Guru & Tenaga Kependidikan) |
| `getRombonganBelajar` | Data Rombel/Kelas |
| `getSekolah` | Data profil sekolah |
| `getPengguna` | Data pengguna |

## Error Handling
- Jika Dapodik tidak running: minta user membuka aplikasi Dapodik
- Jika token salah: minta user cek token di Pengaturan → Web Service
- Jika koneksi gagal: cek apakah Dapodik berjalan di port 5774

## Output Format
File Excel dengan kolom terurut:
1. Nama
2. NISN
3. NIK
4. Jenis Kelamin
5. Tempat/Tanggal Lahir
6. Agama
7. Data Orang Tua (Ayah, Ibu, Wali)
8. Alamat Lengkap
9. Kontak (Telepon, Email)
10. Data Akademik (Kelas, Kurikulum, Semester)
11. Data Lainnya
