#!/usr/bin/env python3
"""
Dapodik GTK Lookup - Cari data lengkap Guru dan Tenaga Kependidikan
、支持 Riwayat Pendidikan, Kepangkatan, dan Semua Field dari API Dapodik

Usage:
    python lookup.py "<nama>"              # Cari GTK
    python lookup.py "<nama>" "Guru"      # Cari dengan filter jenis
    python lookup.py ""                  # Tampilkan semua GTK
    python lookup.py "<nama>" "--all"     # Tampilkan semua field termasuk array
"""

import requests
import json
import sys
import io
from datetime import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE_URL = "http://localhost:5774"
TOKEN = "AlAiyPRTaYFDKLE"
NPSN = "20205293"
SEKOLAH = "SD NEGERI PASIRHALANG"

headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "*/*"}


def get_all_gtk():
    """Get ALL GTK data with pagination"""
    all_data = []
    start = 0
    limit = 200

    print("Mengambil data GTK dari Dapodik...")

    while True:
        try:
            params = {"npsn": NPSN, "start": start, "limit": limit}
            r = requests.get(
                f"{BASE_URL}/WebService/getGtk",
                headers=headers,
                params=params,
                timeout=15,
            )

            if r.status_code != 200:
                print(f"Error: HTTP {r.status_code}")
                break

            data = r.json()
            rows = data.get("rows", [])
            if not rows:
                break

            all_data.extend(rows)
            total = data.get("results", 0)
            print(f"  Mendapat {len(rows)} data dari total {total}...")
            start += limit
            if start >= total:
                break
        except Exception as e:
            print(f"Error: {e}")
            break

    return all_data


def lookup_gtk(nama_cari, jenis_gtk_cari=None):
    """Cari GTK berdasarkan nama dan/atau jenis"""
    semua_data = get_all_gtk()

    if not semua_data:
        print("Gagal mengambil data dari Dapodik. Pastikan Dapodik berjalan.")
        return []

    hasil = []
    nama_cari_lower = nama_cari.lower()

    for gtk in semua_data:
        nama_gtk = gtk.get("nama", "").lower()
        jenis_gtk = gtk.get("jenis_ptk_id_str", "").lower()

        if nama_cari_lower in nama_gtk or nama_gtk in nama_cari_lower:
            if jenis_gtk_cari:
                jenis_cari_lower = jenis_gtk_cari.lower()
                if jenis_cari_lower in jenis_gtk or jenis_gtk in jenis_cari_lower:
                    hasil.append(gtk)
            else:
                hasil.append(gtk)

    return hasil


def format_tgl(tgl_str):
    """Format tanggal dari YYYY-MM-DD ke DD Month YYYY"""
    if not tgl_str or tgl_str == "-":
        return "-"
    try:
        return datetime.strptime(tgl_str, "%Y-%m-%d").strftime("%d %B %Y")
    except:
        return tgl_str


def format_gtk_lengkap(gtk, show_all=False):
    """Format data GTK LENGKAP dengan semua field"""
    output = []

    # ===== HEADER =====
    output.append("=" * 75)
    output.append("  DATA LENGKAP GURU & TENAGA KEPENDIDIKAN (GTK)")
    output.append("  Dapodik Web Service")
    output.append("=" * 75)
    output.append(f"  Sekolah     : {SEKOLAH}")
    output.append(f"  NPSN         : {NPSN}")
    output.append(f"  Tanggal Cetak: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    output.append("")

    # ===== DATA PRIBADI =====
    output.append("-" * 75)
    output.append("  📋 DATA PRIBADI")
    output.append("-" * 75)
    output.append(f"  Nama Lengkap      : {gtk.get('nama', '-')}")
    output.append(f"  NIP              : {gtk.get('nip', '-')}")
    output.append(f"  NIPK             : {gtk.get('nipk', '-')}")
    output.append(f"  NUPTK            : {gtk.get('nuptk', '-')}")
    output.append(f"  NIK              : {gtk.get('nik', '-')}")
    output.append(
        f"  Jenis Kelamin     : {'Laki-laki' if gtk.get('jenis_kelamin') == 'L' else 'Perempuan' if gtk.get('jenis_kelamin') == 'P' else '-'}"
    )
    output.append(f"  Tempat Lahir     : {gtk.get('tempat_lahir', '-')}")
    output.append(f"  Tanggal Lahir    : {format_tgl(gtk.get('tanggal_lahir'))}")
    output.append(f"  Agama           : {gtk.get('agama_id_str', '-')}")
    output.append(f"  Status Kawin    : {gtk.get('status_kawin_id_str', '-')}")
    output.append("")

    # ===== DATA KEPEGAWAIAN =====
    output.append("-" * 75)
    output.append("  💼 DATA KEPEGAWAIAN")
    output.append("-" * 75)
    output.append(f"  Jenis GTK        : {gtk.get('jenis_ptk_id_str', '-')}")
    output.append(f"  Jabatan         : {gtk.get('jabatan_ptk_id_str', '-')}")
    output.append(f"  Status Kepegawai: {gtk.get('status_kepegawaian_id_str', '-')}")
    output.append(f"  Tmt Surat Tugas : {format_tgl(gtk.get('tanggal_surat_tugas'))}")
    output.append(
        f"  PTK Induk      : {'Ya' if gtk.get('ptk_induk') == '1' else 'Tidak'}"
    )
    output.append(f"  Tahun Ajaran   : {gtk.get('tahun_ajaran_id', '-')}")
    output.append(f"  Pangkat/Gol    : {gtk.get('pangkat_golongan_terakhir', '-')}")
    output.append("")

    # ===== PENDIDIKAN TERAKHIR =====
    output.append("-" * 75)
    output.append("  🎓 PENDIDIKAN TERAKHIR")
    output.append("-" * 75)
    output.append(f"  Pendidikan     : {gtk.get('pendidikan_terakhir', '-')}")
    output.append(f"  Bidang Studi  : {gtk.get('bidang_studi_terakhir', '-')}")
    output.append("")

    # ===== RIWAYAT PENDIDIKAN (Array) =====
    rwy_pend = gtk.get("rwy_pend_formal", [])
    if rwy_pend and show_all:
        output.append("-" * 75)
        output.append("  📚 RIWAYAT PENDIDIKAN FORMAL")
        output.append("-" * 75)
        for i, p in enumerate(rwy_pend, 1):
            output.append(f"  #{i}. {p.get('jenjang_pendidikan_id_str', '-')}")
            output.append(f"      Sekolah: {p.get('satuan_pendidikan_formal', '-')}")
            output.append(f"      Fakultas: {p.get('fakultas', '-')}")
            output.append(f"      Prodi    : {p.get('bidang_studi_id_str', '-')}")
            output.append(
                f"      Tahun   : {p.get('tahun_masuk', '-')} - {p.get('tahun_lulus', '-')}"
            )
            output.append(f"      NIM     : {p.get('nim', '-')}")
            output.append(f"      IPK     : {p.get('ipk', '-')}")
            output.append(f"      Gelar   : {p.get('gelar_akademik_id_str', '-')}")
            output.append("")
    elif rwy_pend:
        output.append("-" * 75)
        output.append("  📚 RIWAYAT PENDIDIKAN")
        output.append("-" * 75)
        for i, p in enumerate(rwy_pend, 1):
            tahun = f"{p.get('tahun_masuk', '')}-{p.get('tahun_lulus', '')}"
            output.append(
                f"  {i}. {p.get('jenjang_pendidikan_id_str', '-'):<12} | {p.get('satuan_pendidikan_formal', '-'):<30} | {tahun}"
            )
        output.append("")

    # ===== RIWAYAT KEPANGKATAN/GAJI BERKALA (Array) =====
    rwy_pangkat = gtk.get("rwy_kepangkatan", [])
    if rwy_pangkat and show_all:
        output.append("-" * 75)
        output.append("  💰 RIWAYAT KEPANGKATAN (GAJI BERKALA)")
        output.append("-" * 75)
        for i, p in enumerate(rwy_pangkat, 1):
            output.append(f"  #{i}. {p.get('pangkat_gol_id_str', '-')}")
            output.append(f"      No SK    : {p.get('nomor_sk', '-')}")
            output.append(f"      Tgl SK : {format_tgl(p.get('tanggal_sk'))}")
            output.append(f"      Tmt    : {format_tgl(p.get('tmt_pangkat'))}")
            output.append(
                f"      Masa Kerja: {p.get('masa_kerja_gol_tahun', '0')} th {p.get('masa_kerja_gol_bulan', '0')} bln"
            )
            output.append("")
    elif rwy_pangkat:
        output.append("-" * 75)
        output.append("  💰 RIWAYAT KEPANGKATAN")
        output.append("-" * 75)
        output.append(f"  {'No':<4} {'Pangkat':<8} {'No SK':<30} {'Tmt Pangkat':<15}")
        output.append("-" * 75)
        for i, p in enumerate(rwy_pangkat, 1):
            tmt = format_tgl(p.get("tmt_pangkat"))[:15]
            output.append(
                f"  {i:<4} {p.get('pangkat_gol_id_str', '-'):<8} {p.get('nomor_sk', '-')[:30]:<30} {tmt}"
            )
        output.append("")

    # ===== RIWAYAT SERTIFIKASI (Jika ada di array lain) =====
    # Cek semua key yang ada di data
    if show_all:
        output.append("-" * 75)
        output.append("  📜 SEMUA FIELD DARI API")
        output.append("-" * 75)
        for key, value in gtk.items():
            if isinstance(value, list):
                if value:
                    output.append(f"  {key}: [{len(value)} item]")
                else:
                    output.append(f"  {key}: []")
            elif isinstance(value, dict):
                output.append(f"  {key}: {{...}}")
            else:
                output.append(f"  {key}: {value}")
        output.append("")

    # ===== DATA KONTAK =====
    output.append("-" * 75)
    output.append("  📞 DATA KONTAK")
    output.append("-" * 75)
    output.append(f"  Alamat       : {gtk.get('alamat_jalan', '-')}")
    output.append(f"  RT/RW       : {gtk.get('rt', '-')}/{gtk.get('rw', '-')}")
    output.append(f"  Desa        : {gtk.get('desa_kelurahan', '-')}")
    output.append(f"  Kode Pos    : {gtk.get('kode_pos', '-')}")
    output.append(f"  Telepon    : {gtk.get('nomor_telepon_rumah', '-')}")
    output.append(f"  HP          : {gtk.get('nomor_telepon_seluler', '-')}")
    output.append(f"  Email       : {gtk.get('email', '-')}")
    output.append("")

    # ===== DATA IDREFERENSI =====
    output.append("-" * 75)
    output.append("  🔑 DATA ID (REFERENSI)")
    output.append("-" * 75)
    output.append(f"  PTK ID           : {gtk.get('ptk_id', '-')}")
    output.append(f"  PTK Terdaftar ID  : {gtk.get('ptk_terdaftar_id', '-')}")
    output.append("=" * 75)

    return "\n".join(output)


def format_ringkasan(gtk):
    """Format ringkasan 1 baris"""
    pangkat = gtk.get("pangkat_golongan_terakhir", "-")
    rwy_pend = len(gtk.get("rwy_pend_formal", []))
    rwy_pangkat = len(gtk.get("rwy_kepangkatan", []))
    return {
        "Nama": gtk.get("nama", "-"),
        "NIP": gtk.get("nip", "-") or gtk.get("nuptk", "-")[:15]
        if gtk.get("nuptk")
        else "-",
        "Jenis": gtk.get("jenis_ptk_id_str", "-"),
        "Jabatan": gtk.get("jabatan_ptk_id_str", "-"),
        "Pendidikan": gtk.get("pendidikan_terakhir", "-"),
        "Pangkat": pangkat if pangkat else "-",
        "Riwayat Pend": rwy_pend,
        "Riwayat Kenaikan": rwy_pangkat,
    }


def print_tabel(gtk_list):
    """Cetak tabel ringkasan"""
    print("\n" + "=" * 90)
    print("  DAFTAR GTK SDN PASIRHALANG")
    print("=" * 90)
    print(
        f"{'No':<4} {'Nama':<25} {'NIP/NUPTK':<18} {'Jenis':<10} {'Pangkat':<8} {'Rwy Pend':<10} {'Rwy Kenaikan'}"
    )
    print("-" * 90)
    for i, gtk in enumerate(gtk_list, 1):
        pangkat = gtk.get("pangkat_golongan_terakhir", "-") or "-"
        if pangkat and pangkat != "-":
            pangkat = pangkat[:8]
        rwy_pend = len(gtk.get("rwy_pend_formal", []))
        rwy_pangkat = len(gtk.get("rwy_kepangkatan", []))
        nip = gtk.get("nip", "") or (
            gtk.get("nuptk", "")[:15] if gtk.get("nuptk") else "-"
        )
        nama = gtk.get("nama", "-")[:24]
        jenis = gtk.get("jenis_ptk_id_str", "-")[:10]

        print(
            f"{i:<4} {nama:<25} {nip:<18} {jenis:<10} {pangkat:<8} {rwy_pend:<10} {rwy_pangkat}"
        )
    print("-" * 90)
    print(f"  Total GTK: {len(gtk_list)}")


if __name__ == "__main__":
    # Parse argument
    nama = ""
    show_all = False
    jenis_gtk = None

    if len(sys.argv) >= 2:
        nama = sys.argv[1]

    if len(sys.argv) >= 3:
        if sys.argv[2] == "--all":
            show_all = True
        else:
            jenis_gtk = sys.argv[2]

    if len(sys.argv) >= 4:
        if sys.argv[3] == "--all":
            show_all = True

    # Jalankan pencarian
    if not nama.strip():
        # Tampilkan semua
        semua_data = get_all_gtk()
        print_tabel(semua_data)
        sys.exit(0)

    print(f"\n🔍 Mencari GTK dengan nama: '{nama}'")
    if jenis_gtk:
        print(f"   Filter Jenis GTK: '{jenis_gtk}'")
    print()

    hasil = lookup_gtk(nama, jenis_gtk)

    if not hasil:
        print(f"❌ Tidak ditemukan GTK dengan nama '{nama}'")
        print("\n💡 Tips:")
        print("  - Coba gunakan nama depan saja")
        print("  - Pastikan ejaan nama benar")
        print("  - python lookup.py '' untuk lihat semua GTK")
        sys.exit(0)

    print(f"✅ Ditemukan {len(hasil)} GTK:\n")

    for i, gtk in enumerate(hasil):
        print(format_gtk_lengkap(gtk, show_all=show_all))

        # Simpan JSON (hasil pertama)
        if i == 0:
            with open(
                r"C:\Users\USER\Documents\dapodik_gtk_lookup_result.json",
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(
                    {
                        "search_name": nama,
                        "search_type": jenis_gtk,
                        "show_all": show_all,
                        "found": len(hasil),
                        "timestamp": datetime.now().isoformat(),
                        "gtk_list": hasil,
                    },
                    f,
                    ensure_ascii=False,
                    indent=2,
                )
            print(
                f"📁 Data JSON disimpan ke: C:\\Users\\USER\\Documents\\dapodik_gtk_lookup_result.json"
            )
        print()
