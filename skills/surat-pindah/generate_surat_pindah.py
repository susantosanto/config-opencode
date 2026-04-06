#!/usr/bin/env python3
"""
Generate Surat Pindah Sekolah - Menggunakan template sebagai base
Copy template lalu replace data siswa dari Dapodik
"""

import requests
import json
import sys
import os
import re
import shutil
from datetime import datetime
from docx import Document

BASE_URL = "http://localhost:5774"
TOKEN = "AlAiyPRTaYFDKLE"
NPSN = "20205293"
SEKOLAH = "SD NEGERI PASIRHALANG"
DESA = "Mandalamukti"
KECAMATAN = "Cikalongwetan"
KABUPATEN = "Bandung Barat"
PROVINSI = "Jawa Barat"

TEMPLATE_PATH = r"C:\Users\USER\Documents\SK Pindah Sekolah.docx"
OUTPUT_FOLDER = r"C:\Users\USER\Documents\SK_Pindah"

headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/json"}


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
            print(f"Error fetching data: {e}")
            break

    return all_data


def search_students(nama_cari):
    """Cari siswa berdasarkan nama"""
    semua_data = get_all_peserta_didik()

    if not semua_data:
        print("Gagal mengambil data dari Dapodik. Pastikan Dapodik berjalan.")
        return []

    hasil = []
    nama_cari_lower = nama_cari.lower()

    for siswa in semua_data:
        nama_siswa = siswa.get("nama", "").lower()
        if nama_cari_lower in nama_siswa or nama_siswa in nama_cari_lower:
            hasil.append(siswa)

    return hasil


def display_student_options(students):
    """Tampilkan daftar siswa untuk dipilih"""
    print("\n" + "=" * 70)
    print("DITEMUKAN BEBERAPA SISWA:")
    print("=" * 70)

    for i, siswa in enumerate(students, 1):
        print(f"\n{i}. {siswa.get('nama', '-')}")
        print(f"   NISN: {siswa.get('nisn', '-')}")
        print(f"   Kelas: {siswa.get('nama_rombel', '-')}")
        print(
            f"   TTL: {siswa.get('tempat_lahir', '-')}, {siswa.get('tanggal_lahir', '-')}"
        )
        print(f"   Nama Ayah: {siswa.get('nama_ayah', '-')}")
        print(f"   Nama Ibu: {siswa.get('nama_ibu', '-')}")

    print("\n" + "-" * 70)
    print("0. BATALKAN")
    print("-" * 70)


def select_student(students, non_interactive=False, choice_idx=None):
    """Minta user memilih siswa, atau pilih otomatis jika non-interactive"""
    if non_interactive:
        if choice_idx is not None and 0 <= choice_idx < len(students):
            return students[choice_idx]
        return students[0]

    while True:
        try:
            choice = input("\nPilih nomor siswa (1-{}): ".format(len(students)))
            if choice.strip() == "0":
                print("Operasi dibatalkan.")
                return None

            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(students):
                return students[choice_idx]
            else:
                print(f"Nomor tidak valid. Pilih 1-{len(students)} atau 0 untuk batal.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")


def get_kelas_tingkat(nama_rombel):
    """Konversi nama rombel ke format kelas seperti template: 'II (Dua)'"""
    if not nama_rombel:
        return "-", "-"

    rombel_lower = nama_rombel.lower()
    match = re.search(r"(\d+)", rombel_lower)
    if match:
        angka = match.group(1)
        tingkat_map = {
            "1": ("I", "Satu"),
            "2": ("II", "Dua"),
            "3": ("III", "Tiga"),
            "4": ("IV", "Empat"),
            "5": ("V", "Lima"),
            "6": ("VI", "Enam"),
        }
        if angka in tingkat_map:
            romawi, kata = tingkat_map[angka]
            return f"{romawi} ({kata})", romawi

    return nama_rombel, nama_rombel


def replace_paragraph_text(p, new_text):
    """Replace all runs in a paragraph with new text, keeping first run's formatting"""
    for run in p.runs:
        run.text = ""
    if p.runs:
        p.runs[0].text = new_text
    else:
        p.add_run(new_text)


def replace_value_in_paragraph(p, new_value):
    """Replace only the BOLD value runs in a paragraph, keeping label runs intact.
    Template has label split across multiple runs, then bold runs for the value.
    We find the first bold run and replace it with new_value, then clear remaining bold runs.
    """
    found_bold = False
    for run in p.runs:
        if run.bold:
            if not found_bold:
                run.text = new_value
                found_bold = True
            else:
                run.text = ""
        # Keep non-bold runs (label part) unchanged


def create_surat_pindah(siswa):
    """Buat surat pindah dengan copy template lalu replace data"""

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    nama_siswa = siswa.get("nama", "siswa")
    nama_file = f"surat_mutasi_{nama_siswa.lower().replace(' ', '_')}.docx"
    output_path = os.path.join(OUTPUT_FOLDER, nama_file)

    # Ambil data siswa
    nisn = siswa.get("nisn", "-")
    nama_ayah = siswa.get("nama_ayah", "-")
    nama_ibu = siswa.get("nama_ibu", "-")
    nama_rombel = siswa.get("nama_rombel", "-")
    jenis_kelamin = (
        "Laki-laki"
        if siswa.get("jenis_kelamin") == "L"
        else "Perempuan"
        if siswa.get("jenis_kelamin") == "P"
        else "-"
    )

    # Alamat
    dusun = siswa.get("nama_dusun", "")
    alamat_jalan = siswa.get("alamat_jalan", "")
    desa = siswa.get("desa_kelurahan", DESA)
    kecamatan = siswa.get("kecamatan", KECAMATAN)
    kabupaten = siswa.get("kabupaten_kota", KABUPATEN)

    # Format alamat line 1 (like template: "Kp. Cigondok Ds. Mandalamukti Kec. Cikalongwetan")
    addr_parts_1 = []
    if dusun and dusun != "-":
        addr_parts_1.append(f"Kp. {dusun}")
    elif alamat_jalan and alamat_jalan != "-":
        addr_parts_1.append(alamat_jalan)
    if desa and desa != "-":
        addr_parts_1.append(f"Ds. {desa}")
    if kecamatan and kecamatan != "-":
        addr_parts_1.append(f"Kec. {kecamatan}")
    alamat_line1 = " ".join(addr_parts_1)

    # Format alamat line 2 (like template: "Kab. Bandung Barat")
    addr_parts_2 = []
    if kabupaten and kabupaten != "-":
        addr_parts_2.append(f"Kab. {kabupaten}")
    alamat_line2 = " ".join(addr_parts_2)

    # Kelas
    kelas_str, _ = get_kelas_tingkat(nama_rombel)

    # Tanggal & nomor surat
    today = datetime.now()
    bulan_map = {
        1: "Januari",
        2: "Februari",
        3: "Maret",
        4: "April",
        5: "Mei",
        6: "Juni",
        7: "Juli",
        8: "Agustus",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Desember",
    }
    tgl_surat = f"{today.day} {bulan_map[today.month]} {today.year}"
    nomor_surat = f"421.2/{today.strftime('%Y')}/SD - 007/{today.strftime('%Y')}"

    # COPY template
    shutil.copy2(TEMPLATE_PATH, output_path)

    # Open and modify
    doc = Document(output_path)

    # P01: Update nomor surat
    replace_paragraph_text(doc.paragraphs[1], f"Nomor: {nomor_surat}")

    # P04: Nama siswa (bold value)
    replace_value_in_paragraph(doc.paragraphs[4], nama_siswa)

    # P05: NISN (bold value)
    replace_value_in_paragraph(doc.paragraphs[5], nisn)

    # P06: Jenis Kelamin (bold value)
    replace_value_in_paragraph(doc.paragraphs[6], jenis_kelamin)

    # P07: Murid Kelas (bold value)
    replace_value_in_paragraph(doc.paragraphs[7], kelas_str)

    # P09: Nama Ayah (bold value)
    nama_ayah_display = nama_ayah if nama_ayah and nama_ayah != "-" else "-"
    replace_value_in_paragraph(doc.paragraphs[9], nama_ayah_display)

    # P10: Nama Ibu (bold value)
    nama_ibu_display = nama_ibu if nama_ibu and nama_ibu != "-" else "-"
    replace_value_in_paragraph(doc.paragraphs[10], nama_ibu_display)

    # P11: Alamat line 1 (bold value)
    replace_value_in_paragraph(doc.paragraphs[11], alamat_line1)

    # P12: Alamat line 2 (bold value)
    if alamat_line2:
        replace_value_in_paragraph(doc.paragraphs[12], alamat_line2)
    else:
        # Clear the paragraph
        for run in doc.paragraphs[12].runs:
            run.text = ""

    doc.save(output_path)
    print(f"\n[OK] Surat pindah berhasil dibuat!")
    print(f"[OK] File: {output_path}")
    return output_path


def main():
    print("=" * 70)
    print("GENERATE SURAT PINDAH SEKOLAH")
    print("=" * 70)

    # Check Dapodik
    try:
        r = requests.get(BASE_URL, timeout=5)
        if r.status_code != 200:
            print("[ERROR] Dapodik tidak merespons. Pastikan Dapodik berjalan.")
            sys.exit(1)
    except:
        print("[ERROR] Dapodik tidak dapat diakses di http://localhost:5774")
        sys.exit(1)

    # Parse arguments
    nama_input = None
    choice_idx = None
    non_interactive = False

    if len(sys.argv) > 1:
        nama_input = sys.argv[1]
    if len(sys.argv) > 2:
        arg2 = sys.argv[2]
        if arg2 == "--auto":
            non_interactive = True
        else:
            try:
                choice_idx = int(arg2) - 1
                non_interactive = True
            except ValueError:
                pass
    if len(sys.argv) > 3 and sys.argv[3] == "--auto":
        non_interactive = True

    if not nama_input:
        try:
            nama_input = input("\nMasukkan nama siswa: ").strip()
        except EOFError:
            print("[ERROR] Nama siswa harus diberikan sebagai argumen.")
            sys.exit(1)

    if not nama_input:
        print("[ERROR] Nama siswa harus diisi.")
        sys.exit(1)

    print(f"\nMencari siswa dengan nama: '{nama_input}'...")

    students = search_students(nama_input)

    if not students:
        print(f"\n[TIDAK DITEMUKAN] Tidak ada siswa dengan nama '{nama_input}'")
        print("\nTips:")
        print("  - Coba gunakan nama depan saja")
        print("  - Pastikan ejaan nama benar")
        sys.exit(1)

    if len(students) > 1:
        display_student_options(students)

        result_json = {
            "status": "multiple_found",
            "count": len(students),
            "students": [],
        }
        for i, s in enumerate(students, 1):
            result_json["students"].append(
                {
                    "number": i,
                    "nama": s.get("nama", "-"),
                    "nisn": s.get("nisn", "-"),
                    "kelas": s.get("nama_rombel", "-"),
                    "ttl": f"{s.get('tempat_lahir', '-')}, {s.get('tanggal_lahir', '-')}",
                }
            )

        print(
            f"\n[JSON_OUTPUT]{json.dumps(result_json, ensure_ascii=False)}[/JSON_OUTPUT]"
        )

        if non_interactive and choice_idx is not None:
            selected = select_student(
                students, non_interactive=True, choice_idx=choice_idx
            )
        elif non_interactive:
            selected = students[0]
            print(
                f"\n[INFO] Multiple students found. Auto-selected: {selected.get('nama')}"
            )
        else:
            try:
                selected = select_student(students, non_interactive=False)
            except EOFError:
                selected = students[0]
                print(
                    f"\n[INFO] Multiple students found. Auto-selected: {selected.get('nama')}"
                )

        if not selected:
            sys.exit(0)
        siswa = selected
    else:
        siswa = students[0]
        print(
            f"\nDitemukan: {siswa.get('nama')} (NISN: {siswa.get('nisn')}) - Kelas: {siswa.get('nama_rombel')}"
        )

        if not non_interactive:
            confirm = input("\nLanjutkan dengan siswa ini? (y/n): ").strip().lower()
            if confirm != "y":
                print("Operasi dibatalkan.")
                sys.exit(0)

    # Generate surat
    output_path = create_surat_pindah(siswa)

    result_json = {
        "status": "success",
        "student": {
            "nama": siswa.get("nama", "-"),
            "nisn": siswa.get("nisn", "-"),
            "kelas": siswa.get("nama_rombel", "-"),
        },
        "file": output_path,
    }
    print(f"\n[JSON_OUTPUT]{json.dumps(result_json, ensure_ascii=False)}[/JSON_OUTPUT]")


if __name__ == "__main__":
    main()
