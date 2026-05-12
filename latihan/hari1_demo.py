# ============================================
# HARI 1 - Demo: Program Biodata (Auto Input)
# ============================================
# Versi ini tidak pakai input() — data langsung
# di-set di kode, agar bisa langsung dijalankan.
# ============================================

print("=" * 40)
print("       PROGRAM BIODATA SISWA")
print("=" * 40)

# Data langsung di-set (tanpa input)
nama = "Ahmad Fauzi"
nisn = "0012345678"
kelas = "6A"
umur = 12
tinggi = 145.5
siswa_baru = True

# Tampilkan hasil
print(f"\nNama        : {nama}")
print(f"NISN        : {nisn}")
print(f"Kelas       : {kelas}")
print(f"Umur        : {umur} tahun")
print(f"Tinggi      : {tinggi} cm")
print(f"Siswa Baru  : {'Ya' if siswa_baru else 'Bukan'}")
print("=" * 40)

# Cek tipe data
print("\n--- Tipe Data ---")
print(f"nama        -> {type(nama).__name__}")
print(f"nisn        -> {type(nisn).__name__}")
print(f"kelas       -> {type(kelas).__name__}")
print(f"umur        -> {type(umur).__name__}")
print(f"tinggi      -> {type(tinggi).__name__}")
print(f"siswa_baru  -> {type(siswa_baru).__name__}")
