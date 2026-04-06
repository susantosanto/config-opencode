import requests
import json
from datetime import datetime
from collections import Counter

BASE_URL = "http://localhost:5774"
TOKEN = "AlAiyPRTaYFDKLE"
NPSN = "20205293"

headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "*/*"}


def get_all(endpoint, limit=200):
    all_data = []
    start = 0
    while True:
        try:
            r = requests.get(
                f"{BASE_URL}/WebService/{endpoint}",
                headers=headers,
                params={"npsn": NPSN, "start": start, "limit": limit},
                timeout=15,
            )
            if r.status_code != 200:
                break
            data = r.json()
            rows = data.get("rows", [])
            if not rows:
                break
            # rows bisa berupa dict (key-value) atau list
            if isinstance(rows, dict):
                all_data.append(rows)
                break
            elif isinstance(rows, list):
                all_data.extend(rows)
                total = data.get("results", 0)
                start += limit
                if start >= total:
                    break
        except Exception as e:
            break
    return all_data


def parse_item(item):
    if isinstance(item, str):
        try:
            return json.loads(item)
        except:
            return {}
    return item if isinstance(item, dict) else {}


print("=" * 80)
print("  EKSPLORASI MENDALAM DATA DAPODIK WEB SERVICE")
print(f"  Sekolah: SDN Pasirhalang | NPSN: {NPSN}")
print(f"  Waktu: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
print("=" * 80)

# ============================================================
# 1. DATA SEKOLAH
# ============================================================
print("\n" + "=" * 80)
print("  1. DATA SEKOLAH - PROFIL LENGKAP")
print("=" * 80)

r = requests.get(
    f"{BASE_URL}/WebService/getSekolah",
    headers=headers,
    params={"npsn": NPSN, "start": 0, "limit": 1},
    timeout=10,
)
raw_data = r.json()
rows_raw = raw_data.get("rows", {})

if isinstance(rows_raw, dict):
    sekolah_data = rows_raw
    print(f"Total fields: {len(sekolah_data)}")
    for k in sorted(sekolah_data.keys()):
        v = sekolah_data.get(k, "")
        print(f"  {k}: {str(v)[:100]}")
elif isinstance(rows_raw, list):
    sekolah_data = rows_raw[0] if rows_raw else {}
    if isinstance(sekolah_data, str):
        try:
            sekolah_data = json.loads(sekolah_data)
        except:
            pass
    if isinstance(sekolah_data, dict):
        print(f"Total fields: {len(sekolah_data)}")
        for k in sorted(sekolah_data.keys()):
            v = sekolah_data.get(k, "")
            print(f"  {k}: {str(v)[:100]}")

# ============================================================
# 2. GTK
# ============================================================
print("\n" + "=" * 80)
print("  2. DATA GTK (Guru & Tenaga Kependidikan)")
print("=" * 80)

gtk = get_all("getGtk")
print(f"Total GTK: {len(gtk)}")

gtk_parsed = [parse_item(g) for g in gtk]

jabatan_count = Counter()
status_count = Counter()
pendidikan_count = Counter()
gender_count = Counter()

for g in gtk_parsed:
    jabatan_count[g.get("jenis_ptk_id_str", "Unknown")] += 1
    status_count[g.get("status_kepegawaian_id_str", "Unknown")] += 1
    pendidikan_count[g.get("pendidikan_terakhir", "Unknown")] += 1
    gender_count[g.get("jenis_kelamin", "Unknown")] += 1

print("\n  Per Jabatan:")
for j, c in jabatan_count.most_common():
    print(f"    {j}: {c}")

print("\n  Per Status Kepegawaian:")
for s, c in status_count.most_common():
    print(f"    {s}: {c}")

print("\n  Per Pendidikan Terakhir:")
for p, c in pendidikan_count.most_common():
    print(f"    {p}: {c}")

print("\n  Per Jenis Kelamin:")
for g, c in gender_count.most_common():
    print(f"    {g}: {c}")

print("\n  Detail GTK:")
for i, g in enumerate(gtk_parsed):
    print(f"\n  --- GTK {i + 1} ---")
    print(f"    Nama        : {g.get('nama', '-')}")
    print(f"    NIK         : {g.get('nik', '-')}")
    print(f"    NIP         : {g.get('nip', '-')}")
    print(f"    NUPTK       : {g.get('nuptk', '-')}")
    print(f"    Jabatan     : {g.get('jenis_ptk_id_str', '-')}")
    print(f"    Status      : {g.get('status_kepegawaian_id_str', '-')}")
    print(f"    Pendidikan  : {g.get('pendidikan_terakhir', '-')}")
    print(f"    Bidang Studi: {g.get('bidang_studi_terakhir', '-')}")
    print(f"    Pangkat     : {g.get('pangkat_golongan_terakhir', '-')}")
    print(
        f"    TTL         : {g.get('tempat_lahir', '-')}, {g.get('tanggal_lahir', '-')}"
    )
    print(f"    Agama       : {g.get('agama_id_str', '-')}")
    print(f"    Tgl Tugas   : {g.get('tanggal_surat_tugas', '-')}")

    rwy_kep = g.get("rwy_kepangkatan", [])
    if rwy_kep:
        print(f"    Riwayat Kepangkatan: {len(rwy_kep)} record")
        for kp in rwy_kep[:2]:
            print(
                f"      - SK: {kp.get('nomor_sk', '-')} | TMT: {kp.get('tmt_kepangkatan', '-')}"
            )

    rwy_pend = g.get("rwy_pend_formal", [])
    if rwy_pend:
        print(f"    Riwayat Pendidikan: {len(rwy_pend)} record")
        for pd in rwy_pend[:2]:
            print(
                f"      - {pd.get('satuan_pendidikan', '-')} | {pd.get('tahun_lulus', '-')}"
            )

# ============================================================
# 3. PESERTA DIDIK
# ============================================================
print("\n" + "=" * 80)
print("  3. DATA PESERTA DIDIK")
print("=" * 80)

pd = get_all("getPesertaDidik")
print(f"Total Peserta Didik: {len(pd)}")

pd_parsed = [parse_item(p) for p in pd]

rombel_count = Counter()
jk_count = Counter()
agama_count = Counter()
pendaftaran_count = Counter()
pekerjaan_ayah = Counter()
pekerjaan_ibu = Counter()
tinggi_badan_stats = []
berat_badan_stats = []
sekolah_asal_count = Counter()

for p in pd_parsed:
    rombel_count[p.get("nama_rombel", "Tanpa Rombel")] += 1
    jk_count[p.get("jenis_kelamin", "L")] += 1
    agama_count[p.get("agama_id_str", "Unknown")] += 1
    pendaftaran_count[p.get("jenis_pendaftaran_id_str", "Unknown")] += 1
    pekerjaan_ayah[p.get("pekerjaan_ayah_id_str", "Unknown")] += 1
    pekerjaan_ibu[p.get("pekerjaan_ibu_id_str", "Unknown")] += 1

    tb = p.get("tinggi_badan")
    if tb and tb != "None":
        try:
            tinggi_badan_stats.append(int(tb))
        except:
            pass

    bb = p.get("berat_badan")
    if bb and bb != "None":
        try:
            berat_badan_stats.append(int(bb))
        except:
            pass

    sa = p.get("sekolah_asal")
    if sa and sa != "None":
        sekolah_asal_count[sa] += 1

print("\n  Per Rombel:")
for r, c in sorted(rombel_count.items()):
    print(f"    {r}: {c} siswa")

print(f"\n  Per Jenis Kelamin:")
for j, c in jk_count.most_common():
    print(f"    {j}: {c} siswa")

print(f"\n  Per Agama:")
for a, c in agama_count.most_common():
    print(f"    {a}: {c} siswa")

print(f"\n  Per Jenis Pendaftaran:")
for jp, c in pendaftaran_count.most_common():
    print(f"    {jp}: {c} siswa")

print(f"\n  Pekerjaan Ayah (Top 10):")
for pa, c in pekerjaan_ayah.most_common(10):
    print(f"    {pa}: {c}")

print(f"\n  Pekerjaan Ibu (Top 10):")
for pi, c in pekerjaan_ibu.most_common(10):
    print(f"    {pi}: {c}")

if tinggi_badan_stats:
    print(f"\n  Statistik Tinggi Badan:")
    print(f"    Min: {min(tinggi_badan_stats)} cm")
    print(f"    Max: {max(tinggi_badan_stats)} cm")
    print(f"    Avg: {sum(tinggi_badan_stats) / len(tinggi_badan_stats):.1f} cm")

if berat_badan_stats:
    print(f"\n  Statistik Berat Badan:")
    print(f"    Min: {min(berat_badan_stats)} kg")
    print(f"    Max: {max(berat_badan_stats)} kg")
    print(f"    Avg: {sum(berat_badan_stats) / len(berat_badan_stats):.1f} kg")

if sekolah_asal_count:
    print(f"\n  Sekolah Asal (Top 10):")
    for sa, c in sekolah_asal_count.most_common(10):
        print(f"    {sa}: {c} siswa")

print("\n  Detail Sample 5 Siswa:")
for i, p in enumerate(pd_parsed[:5]):
    print(f"\n  --- Siswa {i + 1} ---")
    print(f"    Nama     : {p.get('nama', '-')}")
    print(f"    NISN     : {p.get('nisn', '-')}")
    print(f"    NIK      : {p.get('nik', '-')}")
    print(f"    JK       : {p.get('jenis_kelamin', '-')}")
    print(f"    TTL      : {p.get('tempat_lahir', '-')}, {p.get('tanggal_lahir', '-')}")
    print(f"    Agama    : {p.get('agama_id_str', '-')}")
    print(f"    Rombel   : {p.get('nama_rombel', '-')}")
    print(f"    Kurikulum: {p.get('kurikulum_id_str', '-')}")
    print(
        f"    Ayah     : {p.get('nama_ayah', '-')} ({p.get('pekerjaan_ayah_id_str', '-')})"
    )
    print(
        f"    Ibu      : {p.get('nama_ibu', '-')} ({p.get('pekerjaan_ibu_id_str', '-')})"
    )
    print(f"    Wali     : {p.get('nama_wali', '-')}")
    print(f"    Anak ke  : {p.get('anak_keberapa', '-')}")
    print(f"    Tinggi   : {p.get('tinggi_badan', '-')} cm")
    print(f"    Berat    : {p.get('berat_badan', '-')} kg")
    print(f"    Kebutuhan: {p.get('kebutuhan_khusus', '-')}")
    print(f"    Tgl Masuk: {p.get('tanggal_masuk_sekolah', '-')}")
    print(f"    Asal     : {p.get('sekolah_asal', '-')}")

# ============================================================
# 4. ROMBONGAN BELAJAR
# ============================================================
print("\n" + "=" * 80)
print("  4. DATA ROMBONGAN BELAJAR")
print("=" * 80)

rombel = get_all("getRombonganBelajar")
print(f"Total Rombel: {len(rombel)}")

rombel_parsed = [parse_item(r) for r in rombel]

for i, r in enumerate(rombel_parsed):
    print(f"\n  --- Rombel {i + 1} ---")
    print(f"    Nama      : {r.get('nama', '-')}")
    print(f"    Jenis     : {r.get('jenis_rombel_str', '-')}")
    print(f"    Kurikulum : {r.get('kurikulum_id_str', '-')}")
    print(f"    Ruang     : {r.get('id_ruang_str', '-').strip()}")
    print(f"    Wali Kelas: {r.get('ptk_id_str', '-')}")
    print(f"    Moving    : {r.get('moving_class', '-')}")

    anggota = r.get("anggota_rombel", [])
    if isinstance(anggota, list):
        print(f"    Anggota   : {len(anggota)} siswa")

    pembelajaran = r.get("pembelajaran", [])
    if isinstance(pembelajaran, list):
        print(f"    Pembelajaran: {len(pembelajaran)} mapel")
        for pb in pembelajaran[:5]:
            if isinstance(pb, dict):
                print(f"      - {pb.get('mata_pelajaran_id_str', '-')}")

# ============================================================
# 5. PENGGUNA
# ============================================================
print("\n" + "=" * 80)
print("  5. DATA PENGGUNA")
print("=" * 80)

pengguna = get_all("getPengguna")
print(f"Total Pengguna: {len(pengguna)}")

pengguna_parsed = [parse_item(p) for p in pengguna]
peran_count = Counter()

for p in pengguna_parsed:
    peran = p.get("peran_id_str", "Unknown")
    peran_count[peran] += 1

print("\n  Per Peran:")
for peran, c in peran_count.most_common():
    print(f"    {peran}: {c}")

print("\n  Detail Pengguna:")
for i, p in enumerate(pengguna_parsed):
    print(
        f"  {i + 1}. {p.get('nama', '-')} | {p.get('peran_id_str', '-')} | {p.get('username', '-')} | HP: {p.get('no_hp', '-')}"
    )

# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "=" * 80)
print("  RINGKASAN AKHIR")
print("=" * 80)
print(f"  Sekolah          : 1 record")
print(f"  GTK              : {len(gtk_parsed)} record")
print(f"  Peserta Didik    : {len(pd_parsed)} record")
print(f"  Rombongan Belajar: {len(rombel_parsed)} record")
print(f"  Pengguna         : {len(pengguna_parsed)} record")
print("=" * 80)

# Save all data to JSON
output = {
    "timestamp": datetime.now().isoformat(),
    "sekolah": sekolah_data if isinstance(sekolah_data, dict) else {},
    "gtk": gtk_parsed,
    "peserta_didik": pd_parsed,
    "rombongan_belajar": rombel_parsed,
    "pengguna": pengguna_parsed,
}

with open(
    r"C:\Users\USER\Documents\dapodik_full_data.json", "w", encoding="utf-8"
) as f:
    json.dump(output, f, ensure_ascii=False, indent=2, default=str)

print(f"\n  Data disimpan ke: C:\\Users\\USER\\Documents\\dapodik_full_data.json")
print(f"  File size: {len(json.dumps(output, ensure_ascii=False))} bytes")
