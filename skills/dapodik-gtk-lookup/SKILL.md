---
name: dapodik-gtk-lookup
description: "Cari data lengkap Guru dan Tenaga Kependidikan (GTK) berdasarkan nama dan/atau jenis dari Dapodik Web Service untuk slip gaji, surat keterangan, dan dokumen GTK"
license: MIT
compatibility: opencode
metadata:
  audience: sd-operator
  workflow: data-lookup
  source: custom
---

# Dapodik GTK Lookup Skill

Cari data lengkap Guru dan Tenaga Kependidikan (GTK) berdasarkan nama dan/atau jenis GTK dari Dapodik Web Service. Data yang diambil bisa digunakan untuk:
- Slip gaji GTK
- Surat keterangan GTK
- Daftar nominatif GTK
- Dokumen administrasi sekolah

## Trigger Phrases
- "cari data gtk [nama]"
- "lookup guru [nama]"
- "data lengkap tendik [nama]"
- "cari gtk [nama] Jenis gtk [jenis]"
- "ambil data guru dari dapodik"
- "cari tendik [nama]"
- "data gtk untuk slip gaji"

## Prerequisites
- Aplikasi Dapodik harus berjalan di `http://localhost:5774`
- Token Web Service dan NPSN harus tersedia
- Package `requests` harus terinstall

## Token & NPSN (SDN Pasirhalang)
- **Token**: `AlAiyPRTaYFDKLE`
- **NPSN**: `20205293`
- **URL**: `http://localhost:5774`
- **Sekolah**: SD NEGERI PASIRHALANG

## Workflow

### 1. Pastikan Dapodik Berjalan
Pastikan aplikasi Dapodik sudah running di `http://localhost:5774`.

### 2. Jalankan Script Lookup
Script tersedia di: `C:\Users\USER\.config\opencode\skills\dapodik-gtk-lookup\lookup.py`

```bash
python C:\Users\USER\.config\opencode\skills\dapodik-gtk-lookup\lookup.py "[nama_gtk]" "[jenis_gtk_opsional]"
```

### 3. Output
Script akan menampilkan data lengkap GTK dalam format terstruktur.

## Contoh Penggunaan

### Contoh 1: Cari GTK berdasarkan nama
```bash
python lookup.py "Ahmad"
```

### Contoh 2: Cari GTK dengan filter jenis
```bash
python lookup.py "Ahmad" "Guru"
python lookup.py "Hartono" "Tendik"
```

### Contoh 3: Tampilkan semua GTK (tanpa filter)
```bash
python lookup.py ""
```
Atau cukup jalankan tanpa argument (nama kosong = tampilkan semua)

## Output Format

Data ditampilkan dalam format terstruktur dengan section:

1. **Data Pribadi** 
   - Nama, NIP, NIPK, NUPTK, NIK
   - Jenis Kelamin, TTL, Agama, Status Kawin

2. **Data Kepegawaian**
   - Jenis GTK, Jabatan
   - TMT Jabatan, TMT CPNS, TMT PNS
   - Semester join

3. **Pendidikan & Sertifikasi**
   - Tanggal Ijază, Universitas, Prodi
   - Status Sertifikasi, No Sertifikasi
   - Mapel Sertifikasi

4. **Data Mengajar**
   - Rombel diampu, Mapel diampu
   - Jam mengajar

5. **Alamat & Kontak**
   - Alamat lengkap, RT/RW, Desa
   - Telepon, Email

6. **Data Lainnya**
   - Tinggi/Berat badan, Golongan darah
   - SK CPNS, SK PNS

7. **Data ID (Referensi)**
   - gtk_id, PTK_ID, registrasi_id

## Integration
Hasil pencarian juga disimpan sebagai JSON di:
`C:\Users\USER\Documents\dapodik_gtk_lookup_result.json`

File ini bisa digunakan untuk:
- Generate slip gaji otomatis
- Daftar GTK untuk Bos
- Export ke Excel/PDF
- Integrasi dengan sistem lain

## API Endpoint Reference
- **URL**: `http://localhost:5774/WebService/getGtk`
- **Auth**: `Authorization: Bearer {TOKEN}`
- **Params**: `npsn={NPSN}&start={offset}&limit={count}`

Available Functions:
| Function | Deskripsi |
|----------|-----------|
| `getGtk` | Data GTK (Guru & Tenaga Kependidikan) |
| `getPesertaDidik` | Data peserta didik |
| `getRombonganBelajar` | Data Rombel/Kelas |
| `getSekolah` | Data profil sekolah |

## Error Handling
- Jika Dapodik tidak running: minta user membuka aplikasi Dapodik
- Jika token salah: minta user cek token di Pengaturan → Web Service
- Jika tidak ditemukan: sarankan coba nama depan saja

## Tips Pencarian
1. Gunakan nama depan untuk hasil lebih lengkap
2. Filter jenis GTK (Guru/Tendik) untuk hasil spesifik
3. Untuk lihat semua GTK, gunakan nama kosong atau nama "*"