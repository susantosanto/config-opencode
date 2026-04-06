#!/usr/bin/env python3
"""
Dapodik Student Lookup - Cari data lengkap siswa berdasarkan nama dan kelas
Digunakan untuk keperluan surat-menyurat dan dokumen sekolah
"""

import requests
import json
import sys
from datetime import datetime

BASE_URL = "http://localhost:5774"
TOKEN = "AlAiyPRTaYFDKLE"
NPSN = "20205293"
SEKOLAH = "SD NEGERI PASIRHALANG"

headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "*/*"}


def get_all_peserta_didik():
    """Get ALL peserta didik data with pagination"""
    all_data = []
    start = 0
    limit = 200

    while True:
        try:
            params = {"npsn": NPSN, "start": start, "limit": limit}
            r = requests.get(
                f"{BASE_URL}/WebService/getPesertaDidik",
                headers=headers,
                params=params,
                timeout=15,
            )

            if r.status_code != 200:
                break

            data = r.json()
            rows = data.get("rows", [])
            if not rows:
                break

            all_data.extend(rows)
            total = data.get("results", 0)
            start += limit
            if start >= total:
                break
        except Exception as e:
            print(f"Error: {e}")
            break

    return all_data


def lookup_siswa(nama_cari, kelas_cari=None):
    """Cari siswa berdasarkan nama dan/atau kelas"""
    semua_data = get_all_peserta_didik()

    if not semua_data:
        print("Gagal mengambil data dari Dapodik. Pastikan Dapodik berjalan.")
        return []

    hasil = []
    nama_cari_lower = nama_cari.lower()

    for siswa in semua_data:
        nama_siswa = siswa.get("nama", "").lower()
        rombel = siswa.get("nama_rombel", "").lower()

        # Match nama (partial match)
        if nama_cari_lower in nama_siswa or nama_siswa in nama_cari_lower:
            # Jika kelas dicari, filter juga berdasarkan kelas
            if kelas_cari:
                kelas_cari_lower = kelas_cari.lower()
                if kelas_cari_lower in rombel or rombel in kelas_cari_lower:
                    hasil.append(siswa)
            else:
                hasil.append(siswa)

    return hasil


def format_data_siswa(siswa):
    """Format data siswa untuk ditampilkan"""
    output = []
    output.append("=" * 60)
    output.append("  DATA LENGKAP PESERTA DIDIK")
    output.append("=" * 60)
    output.append(f"  Sekolah: {SEKOLAH}")
    output.append(f"  NPSN: {NPSN}")
    output.append(f"  Tanggal Cetak: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    output.append("")
    output.append("  --- DATA PRIBADI ---")
    output.append(f"  Nama Lengkap    : {siswa.get('nama', '-')}")
    output.append(f"  NISN            : {siswa.get('nisn', '-')}")
    output.append(f"  NIK             : {siswa.get('nik', '-')}")
    output.append(f"  NIPD            : {siswa.get('nipd', '-')}")
    output.append(
        f"  Jenis Kelamin   : {'Laki-laki' if siswa.get('jenis_kelamin') == 'L' else 'Perempuan' if siswa.get('jenis_kelamin') == 'P' else '-'}"
    )
    output.append(f"  Tempat Lahir    : {siswa.get('tempat_lahir', '-')}")
    output.append(f"  Tanggal Lahir   : {siswa.get('tanggal_lahir', '-')}")
    output.append(f"  Agama           : {siswa.get('agama_id_str', '-')}")
    output.append(f"  Anak Ke         : {siswa.get('anak_keberapa', '-')}")
    output.append(f"  Kebutuhan Khusus: {siswa.get('kebutuhan_khusus', '-')}")
    output.append(f"  Tinggi Badan    : {siswa.get('tinggi_badan', '-')} cm")
    output.append(f"  Berat Badan     : {siswa.get('berat_badan', '-')} kg")
    output.append("")
    output.append("  --- DATA AKADEMIK ---")
    output.append(f"  Kelas/Rombel    : {siswa.get('nama_rombel', '-')}")
    output.append(f"  Kurikulum       : {siswa.get('kurikulum_id_str', '-')}")
    output.append(f"  Jenis Pendaftaran: {siswa.get('jenis_pendaftaran_id_str', '-')}")
    output.append(f"  Tanggal Masuk   : {siswa.get('tanggal_masuk_sekolah', '-')}")
    output.append(f"  Sekolah Asal    : {siswa.get('sekolah_asal', '-')}")
    output.append(f"  Tingkat         : {siswa.get('tingkat_pendidikan_id', '-')}")
    output.append(f"  Semester        : {siswa.get('semester_id', '-')}")
    output.append("")
    output.append("  --- DATA ORANG TUA ---")
    output.append(f"  Nama Ayah       : {siswa.get('nama_ayah', '-')}")
    output.append(f"  Pekerjaan Ayah  : {siswa.get('pekerjaan_ayah_id_str', '-')}")
    output.append(f"  Nama Ibu        : {siswa.get('nama_ibu', '-')}")
    output.append(f"  Pekerjaan Ibu   : {siswa.get('pekerjaan_ibu_id_str', '-')}")
    output.append(f"  Nama Wali       : {siswa.get('nama_wali', '-')}")
    output.append(f"  Pekerjaan Wali  : {siswa.get('pekerjaan_wali_id_str', '-')}")
    output.append("")
    output.append("  --- DATA ALAMAT ---")
    output.append(f"  Alamat          : {siswa.get('alamat_jalan', '-')}")
    output.append(f"  RT/RW           : {siswa.get('rt', '-')}/{siswa.get('rw', '-')}")
    output.append(f"  Dusun           : {siswa.get('nama_dusun', '-')}")
    output.append(f"  Desa/Kelurahan  : {siswa.get('desa_kelurahan', '-')}")
    output.append(f"  Kode Pos        : {siswa.get('kode_pos', '-')}")
    output.append(
        f"  Lintang/Bujur   : {siswa.get('lintang', '-')}/{siswa.get('bujur', '-')}"
    )
    output.append("")
    output.append("  --- DATA KONTAK ---")
    output.append(f"  Telepon Rumah   : {siswa.get('nomor_telepon_rumah', '-')}")
    output.append(f"  Telepon Seluler : {siswa.get('nomor_telepon_seluler', '-')}")
    output.append(f"  Email           : {siswa.get('email', '-')}")
    output.append("")
    output.append("  --- DATA ID (untuk referensi) ---")
    output.append(f"  peserta_didik_id: {siswa.get('peserta_didik_id', '-')}")
    output.append(f"  registrasi_id   : {siswa.get('registrasi_id', '-')}")
    output.append(f"  anggota_rombel  : {siswa.get('anggota_rombel_id', '-')}")
    output.append(f"  rombel_id       : {siswa.get('rombongan_belajar_id', '-')}")
    output.append("=" * 60)

    return "\n".join(output)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lookup.py <nama_siswa> [kelas]")
        print("Example: python lookup.py 'Muhammad Iqbal' 'Kelas 3'")
        print("Example: python lookup.py 'Iqbal'")
        sys.exit(1)

    nama = sys.argv[1]
    kelas = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"\nMencari siswa dengan nama: '{nama}'")
    if kelas:
        print(f"Filter kelas: '{kelas}'")
    print()

    hasil = lookup_siswa(nama, kelas)

    if not hasil:
        print(f"Tidak ditemukan siswa dengan nama '{nama}'")
        if kelas:
            print(f"Filter kelas: '{kelas}'")
        print("\nTips:")
        print("  - Coba gunakan nama depan saja")
        print("  - Pastikan ejaan nama benar")
        print("  - Cek apakah Dapodik sudah berjalan")
        sys.exit(0)

    print(f"Ditemukan {len(hasil)} siswa:\n")

    for i, siswa in enumerate(hasil):
        print(format_data_siswa(siswa))
        print()

        # Save to JSON for programmatic use (first result)
        if i == 0:
            with open(
                r"C:\Users\USER\Documents\dapodik_student_lookup_result.json",
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(
                    {
                        "search_name": nama,
                        "search_class": kelas,
                        "found": len(hasil),
                        "timestamp": datetime.now().isoformat(),
                        "students": hasil,
                    },
                    f,
                    ensure_ascii=False,
                    indent=2,
                )
            print(
                f"Data JSON disimpan ke: C:\\Users\\USER\\Documents\\dapodik_student_lookup_result.json"
            )
