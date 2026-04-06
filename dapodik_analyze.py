import requests
import re
import json

BASE_URL = "http://localhost:5774"
TOKEN = "AlAiyPRTaYFDKLE"
NPSN = "20205293"

headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "*/*"}

# Get all data from working endpoints and analyze structure
print("=== ANALYZING WORKING ENDPOINTS ===\n")

# 1. getSekolah
print("--- 1. getSekolah ---")
r = requests.get(
    f"{BASE_URL}/WebService/getSekolah",
    headers=headers,
    params={"npsn": NPSN, "start": 0, "limit": 1},
    timeout=10,
)
if r.status_code == 200:
    data = r.json()
    if data.get("rows"):
        row = data["rows"][0]
        print(f"Fields ({len(row)}):")
        for k, v in row.items():
            val_str = str(v)[:60]
            print(f"  {k}: {val_str}")

# 2. getGtk
print("\n--- 2. getGtk ---")
r = requests.get(
    f"{BASE_URL}/WebService/getGtk",
    headers=headers,
    params={"npsn": NPSN, "start": 0, "limit": 1},
    timeout=10,
)
if r.status_code == 200:
    data = r.json()
    total = data.get("results", 0)
    print(f"Total GTK: {total}")
    if data.get("rows"):
        row = data["rows"][0]
        print(f"Fields ({len(row)}):")
        for k, v in row.items():
            val_str = str(v)[:60]
            print(f"  {k}: {val_str}")

# 3. getRombonganBelajar
print("\n--- 3. getRombonganBelajar ---")
r = requests.get(
    f"{BASE_URL}/WebService/getRombonganBelajar",
    headers=headers,
    params={"npsn": NPSN, "start": 0, "limit": 10},
    timeout=10,
)
if r.status_code == 200:
    data = r.json()
    total = data.get("results", 0)
    print(f"Total Rombel: {total}")
    if data.get("rows"):
        for row in data["rows"]:
            nama = row.get("nama", "-")
            tingkat = row.get("tingkat", "-")
            print(f"  Kelas: {nama} (Tingkat: {tingkat})")

# 4. getPengguna
print("\n--- 4. getPengguna ---")
r = requests.get(
    f"{BASE_URL}/WebService/getPengguna",
    headers=headers,
    params={"npsn": NPSN, "start": 0, "limit": 1},
    timeout=10,
)
if r.status_code == 200:
    data = r.json()
    total = data.get("results", 0)
    print(f"Total Pengguna: {total}")
    if data.get("rows"):
        row = data["rows"][0]
        print(f"Fields ({len(row)}):")
        for k, v in row.items():
            val_str = str(v)[:60]
            print(f"  {k}: {val_str}")

# 5. Get sample peserta didik with rombel info
print("\n--- 5. Sample Peserta Didik ---")
r = requests.get(
    f"{BASE_URL}/WebService/getPesertaDidik",
    headers=headers,
    params={"npsn": NPSN, "start": 0, "limit": 3},
    timeout=10,
)
if r.status_code == 200:
    data = r.json()
    total = data.get("results", 0)
    print(f"Total PD: {total}")
    if data.get("rows"):
        for i, row in enumerate(data["rows"]):
            print(f"\n  Siswa {i + 1}:")
            print(f"    Nama: {row.get('nama', '-')}")
            print(f"    NISN: {row.get('nisn', '-')}")
            print(f"    JK: {row.get('jenis_kelamin', '-')}")
            print(f"    Rombel: {row.get('nama_rombel', '-')}")
            print(
                f"    Ayah: {row.get('nama_ayah', '-')} ({row.get('pekerjaan_ayah_id_str', '-')})"
            )
            print(
                f"    Ibu: {row.get('nama_ibu', '-')} ({row.get('pekerjaan_ibu_id_str', '-')})"
            )
