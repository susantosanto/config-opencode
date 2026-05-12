# ============================================
# HARI 1 - Latihan: Program Biodata Sederhana
# ============================================
# Program ini meminta data biodata user,
# lalu menampilkannya dengan format rapi.
# ============================================

print("=" * 40)
print("       PROGRAM BIODATA SISWA")
print("=" * 40)

# Input data
nama = input("Nama lengkap    : ")
nisn = input("NISN            : ")
kelas = input("Kelas           : ")
umur = int(input("Umur (angka)    : "))
tinggi = float(input("Tinggi (cm)     : "))
siswa_baru = input("Siswa baru (y/n): ")

# Konversi jawaban siswa baru ke boolean
siswa_baru = siswa_baru.lower() == "y"

# Tampilkan hasil
print("\n" + "=" * 40)
print("       HASIL BIODATA")
print("=" * 40)
print(f"Nama        : {nama}")
print(f"NISN        : {nisn}")
print(f"Kelas       : {kelas}")
print(f"Umur        : {umur} tahun")
print(f"Tinggi      : {tinggi} cm")
print(f"Siswa Baru  : {'Ya' if siswa_baru else 'Bukan'}")
print("=" * 40)

# Cek tipe data
print("\n--- Tipe Data ---")
print(f"nama   -> {type(nama)}")
print(f"nisn   -> {type(nisn)}")
print(f"umur   -> {type(umur)}")
print(f"tinggi -> {type(tinggi)}")
print(f"siswa_baru -> {type(siswa_baru)}")
