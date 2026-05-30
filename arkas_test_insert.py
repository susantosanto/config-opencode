import sqlcipher3
import json
import os
import uuid
import base64
from datetime import datetime

# Konfigurasi
config_path = r'C:\Users\USER\.config\opencode\arkas_config.json'
db_copy_path = r'C:\Users\USER\Documents\arkas_analysis\arkas_copy.db'

with open(config_path, 'r') as f:
    config = json.load(f)

key = config['arkas']['key']
cipher_comp = config['arkas']['cipher_compatibility']

def generate_id():
    # Menghasilkan ID 22 karakter ala ARKAS (Base64 URL-safe UUID)
    u = uuid.uuid4()
    return base64.urlsafe_b64encode(u.bytes).decode('utf-8').rstrip('=')

def connect_db(path):
    conn = sqlcipher3.connect(path)
    conn.execute(f"PRAGMA key = '{key}'")
    conn.execute(f"PRAGMA cipher_compatibility = {cipher_comp}")
    return conn

def test_insert_and_cleanup():
    conn = connect_db(db_copy_path)
    cursor = conn.cursor()
    
    # 1. Ambil info penting dari anggaran terbaru (2026)
    cursor.execute("SELECT id_anggaran, sekolah_id FROM anggaran WHERE tahun_anggaran = 2026 AND soft_delete = 0 LIMIT 1")
    res = cursor.fetchone()
    if not res:
        print("Gagal menemukan anggaran 2026!")
        return
    id_anggaran, sekolah_id = res
    print(f"Target Anggaran: {id_anggaran} | Sekolah: {sekolah_id}")

    # 2. Persiapkan data dummy
    new_id_rapbs = generate_id()
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"Memasukkan data dummy ke RAPBS dengan ID: {new_id_rapbs}")
    
    try:
        # Insert ke rapbs
        cursor.execute("""
            INSERT INTO rapbs (
                id_rapbs, sekolah_id, id_anggaran, id_ref_kode, id_ref_tahun_anggaran,
                kode_rekening, id_barang, urutan, uraian, volume, satuan, harga_satuan, 
                jumlah, soft_delete, create_date, last_update
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            new_id_rapbs, sekolah_id, id_anggaran, 'dummy_code', 2026,
            '5.1.02.02.01.0063', 'dummy_barang', '999', 'TEST INPUT DIRECT - GEMINI CLI', 
            1, 'Paket', 100000, 100000, 0, now_str, now_str
        ))
        
        # 3. Verifikasi apakah data masuk
        cursor.execute("SELECT uraian, jumlah FROM rapbs WHERE id_rapbs = ?", (new_id_rapbs,))
        row = cursor.fetchone()
        if row:
            print(f"SUKSES! Data ditemukan: {row}")
        else:
            print("GAGAL! Data tidak ditemukan.")

        # 4. Cleanup (Hapus data dummy agar tidak mengotori copy database secara permanen)
        cursor.execute("DELETE FROM rapbs WHERE id_rapbs = ?", (new_id_rapbs,))
        conn.commit()
        print("Cleanup selesai.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    test_insert_and_cleanup()
