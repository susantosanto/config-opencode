# 📚 HARI 2 — Perulangan (Looping) dalam Python

> **Tujuan:** Memahami konsep perulangan dengan sangat detail, agar bisa digunakan untuk memproses data siswa, nilai, dan tugas-tugas administratif sekolah.

---

## 🔑 KONSEP DASAR: APA ITU PERULANGAN?

### Bayangkan Anda Seorang Guru

Setiap hari Anda harus:
1. Mengisi daftar hadir untuk 30 siswa
2. Menghitung nilai rata-rata kelas
3. Menyampaikan pesan yang sama ke 6 kelas berbeda

**Tanpa perulangan:** Anda menulis nama satu per satu, 30 kali.
**Dengan perulangan:** Anda tulis sekali, komputer mengulang 30 kali.

> **Perulangan = melakukan sesuatu secara berulang tanpa menulis ulang kode.**

---

## 1. FOR LOOP — Mengulang Sesuatu yang Sudah Diketahui Jumlahnya

### 📌 Kapan Pakai for loop?
- Ketika Anda **tahu berapa kali** ingin mengulang
- Ketika mengulang **isi list/array/kumpulan data**

### 🔤 Struktur Dasar For Loop

```python
for variabel in urutan:
    # lakukan sesuatu
```

**Penjelasan:**
- `for` = kata kunci untuk memulai perulangan
- `variabel` = nama sementara untuk setiap item (bisa nama apa saja)
- `in` = kata kunci yang berarti "di dalam"
- `urutan` = kumpulan data yang akan diulang

---

### Contoh 1: Mengulang Angka (range)

```python
for i in range(5):
    print(i)
```

**Penjelasan:**
- `range(5)` menghasilkan angka: 0, 1, 2, 3, 4 (5 angka)
- `i` adalah variabel sementara yang menyimpan angka saat ini
- `print(i)` menampilkan angka tersebut

**Hasil:**
```
0
1
2
3
4
```

---

### Contoh 2: Mengulang dengan Batas Awal dan Akhir

```python
for i in range(1, 6):
    print(i)
```

- `range(1, 6)` menghasilkan: 1, 2, 3, 4, 5
- Dimulai dari 1, berakhir sebelum 6

**Hasil:**
```
1
2
3
4
5
```

---

### Contoh 3: Mengulang dengan Langkah (Step)

```python
for i in range(0, 10, 2):
    print(i)
```

- `range(0, 10, 2)` = mulai dari 0, sampai sebelum 10, naik 2 setiap langkah
- Menghasilkan: 0, 2, 4, 6, 8

**Hasil:**
```
0
2
4
6
8
```

---

### Contoh 4: Mengulang List (Kumpulan Data)

```python
nama_siswa = ["Budi", "Ani", "Citra", "Dedi", "Eka"]

for nama in nama_siswa:
    print(nama)
```

**Penjelasan:**
- `nama_siswa` adalah list (kumpulan nama)
- `for nama in nama_siswa` = untuk setiap item dalam list, simpan ke variabel `nama`
- `print(nama)` = tampilkan nama tersebut

**Hasil:**
```
Budi
Ani
Citra
Dedi
Eka
```

---

### Contoh 5: Menggunakan enumerate (Index + Value)

Kadang kita butuh tahu **posisi** (index) juga, bukan hanya nilainya.

```python
nama_siswa = ["Budi", "Ani", "Citra"]

for index, nama in enumerate(nama_siswa):
    print(f"Posisi {index}: {nama}")
```

**Hasil:**
```
Posisi 0: Budi
Posisi 1: Ani
Posisi 2: Citra
```

> **Catatan:** Index dimulai dari 0, bukan 1!

---

### Contoh 6: For Loop untuk Hitung Nilai Rata-rata

```python
nilai_siswa = [80, 85, 90, 75, 88]
total = 0

for nilai in nilai_siswa:
    total = total + nilai
    print(f"Nilai: {nilai}, Total sementara: {total}")

rata_rata = total / len(nilai_siswa)
print(f"\nRata-rata: {rata_rata}")
```

**Hasil:**
```
Nilai: 80, Total sementara: 80
Nilai: 85, Total sementara: 165
Nilai: 90, Total sementara: 255
Nilai: 75, Total sementara: 330
Nilai: 88, Total sementara: 418
Rata-rata: 83.6
```

---

## 2. WHILE LOOP — Mengulang Sesuatu dengan Kondisi

### 📌 Kapan Pakai while loop?
- Ketika Anda **tidak tahu** berapa kali harus mengulang
- Ketika pengulangan bergantung pada **kondisi tertentu**

### 🔤 Struktur Dasar While Loop

```python
while kondisi:
    # lakukan sesuatu
```

**Penjelasan:**
- `while` = kata kunci untuk memulai perulangan
- `kondisi` = pernyataan yang bernilai True/False
- Selama kondisi **True**, loop akan terus berjalan
- Jika kondisi menjadi **False**, loop berhenti

---

### Contoh 1: Hitung Mundur

```python
print("Persiapan peluncuran...")
countdown = 5

while countdown > 0:
    print(countdown)
    countdown = countdown - 1

print("GO! Roket meluncur!")
```

**Penjelasan:**
1. `countdown = 5` → kondisi `5 > 0` = True → jalankan loop
2. Tampilkan 5, kurangi menjadi 4
3. `4 > 0` = True → jalankan loop
4. Tampilkan 4, kurangi menjadi 3
5. ...sampai `0 > 0` = False → keluar dari loop

**Hasil:**
```
Persiapan peluncuran...
5
4
3
2
1
GO! Roket meluncur!
```

---

### Contoh 2: Menu Login Sederhana

```python
kesempatan = 3

while kesempatan > 0:
    password = input("Masukkan password: ")
    
    if password == "sekolah123":
        print("✅ Login berhasil!")
        break  # keluar dari loop
    else:
        kesempatan = kesempatan - 1
        print(f"❌ Password salah. Sisa kesempatan: {kesempatan}")

if kesempatan == 0:
    print("🚫 Akun terkunci!")
```

---

### Contoh 3: Menghitung Total dengan While

```python
nilai = [80, 85, 90]
index = 0
total = 0

while index < len(nilai):
    total = total + nilai[index]
    index = index + 1

print(f"Total: {total}")
```

---

## 3. BREAK — Keluar dari Loop Sekarang

`break` = langsung keluar dari loop, tidak peduli ada lagi atau tidak.

```python
for i in range(10):
    if i == 5:
        print("Ketemu angka 5! Keluar sekarang.")
        break
    print(f"Angka: {i}")

print("Selesai!")
```

**Hasil:**
```
Angka: 0
Angka: 1
Angka: 2
Angka: 3
Angka: 4
Ketemu angka 5! Keluar sekarang.
Selesai!
```

---

## 4. CONTINUE — Lewati Iterasi Ini, Lanjutkan yang Berikutnya

`continue` = skip (lewati) kode di bawahnya, langsung ke iterasi berikutnya.

```python
for i in range(5):
    if i == 2:
        print("Angka 2 dilewati!")
        continue
    print(f"Proses angka: {i}")

print("Selesai!")
```

**Hasil:**
```
Proses angka: 0
Proses angka: 1
Angka 2 dilewati!
Proses angka: 3
Proses angka: 4
Selesai!
```

---

## 5. PASS — Tempat Kosong (Placeholder)

`pass` = tidak melakukan apa-apa, hanya placeholder.

```python
for i in range(5):
    if i == 2:
        pass  # TODO: nanti isi kode di sini
    else:
        print(f"Angka: {i}")
```

---

## 6. LIST COMPREHENSION — Cara Pendek Membuat List

Ini adalah **cara singkat** menulis for loop dalam satu baris.

### Format Dasar:
```python
[ekspresi for item in iterable]
```

### Contoh 1: Kuadrat Semua Angka

```python
# Cara biasa
angka = [1, 2, 3, 4, 5]
kuadrat = []
for n in angka:
    kuadrat.append(n ** 2)

# Cara List Comprehension
kuadrat = [n ** 2 for n in angka]
print(kuadrat)  # [1, 4, 9, 16, 25]
```

### Contoh 2: Hanya Angka Genap

```python
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
genap = [n for n in angka if n % 2 == 0]
print(genap)  # [2, 4, 6, 8, 10]
```

### Contoh 3: Ubah Nama Jadi Kapital

```python
nama = ["budi", "ani", "citra"]
nama_besar = [n.upper() for n in nama]
print(nama_besar)  # ['BUDI', 'ANI', 'CITRA']
```

---

## 📝 LATIHAN — Game Tebak Angka (Versi Detail)

Sekarang dengan pemahaman yang lebih baik, mari buat game tebak angka:

```python
import random

print("=" * 40)
print("       GAME TEBAK ANGKA")
print("=" * 40)
print("Komputer memilih angka 1-10")
print("Anda punya 3 kesempatan!\n")

# Komputer memilih angka secara acak
angka_rahasia = random.randint(1, 10)

# Inisialisasi variabel
max_tebakan = 3
tebakan_ke = 0
berhasil = False

# Loop utama - selama masih ada kesempatan
while tebakan_ke < max_tebakan:
    # Minta input dari user
    tebakan_str = input(f"Tebakan ke-{tebakan_ke + 1}: ")
    
    # Cek apakah input adalah angka
    if not tebakan_str.isdigit():
        print("⚠️ Mohon masukkan angka!\n")
        continue
    
    # Konversi ke integer
    tebakan = int(tebakan_str)
    
    # Cek tebakan
    if tebakan == angka_rahasia:
        print(f"\n✅ BENAR! Angka rahasia adalah {angka_rahasia}")
        print(f"Anda menebak dalam {tebakan_ke + 1} kali percobaan.")
        berhasil = True
        break  # Keluar dari loop karena sudah benar
    elif tebakan < angka_rahasia:
        print("⬆️ Terlalu kecil! Coba lebih besar.")
    else:
        print("⬇️ Terlalu besar! Coba lebih kecil.")
    
    # Tingkatkan counter
    tebakan_ke = tebakan_ke + 1
    print(f"Sisa kesempatan: {max_tebakan - tebakan_ke}\n")

# Cek jika gagal
if not berhasil:
    print(f"\n❌ GAGAL! Angka rahasia adalah {angka_rahasia}")
    print("Silakan coba lagi nanti.")
```

---

## ✅ KESIMPULAN — Kapan Pakai Yang Mana?

| Situasi | Gunakan |
|---------|---------|
| Tahu jumlah pengulangan | `for` |
| Mengulang isi list/array | `for` |
| Tidak tahu kapan berhenti | `while` |
| Bergantung pada kondisi | `while` |
| Ingin keluar sekarang | `break` |
| Ingin skip iterasi ini | `continue` |
| Tempat kosong sementara | `pass` |
| Buat list dengan for dalam 1 baris | List Comprehension |

---

## 📋 TUGAS

1. **Jalankan kode latihan** di atas
2. **Modifikasi:** Ubah batas tebakan dari 3 menjadi 5
3. **Modifikasi:** Ubah range angka dari 1-10 menjadi 1-100
4. **Pahami:** Coba jelaskan ke diri sendiri mengapa while loop bisa infinite jika kondisinya tidak pernah berubah!

---

**Kalau sudah paham dan mau lanjut, ketik "lanjut Hari 3"** — kita akan belajar **Data Structures (List, Dict, Set, Tuple)** yang paling penting untuk mengelola data siswa di sekolah.