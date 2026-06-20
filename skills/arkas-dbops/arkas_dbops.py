#!/usr/bin/env python3
"""
ARKAS DB Ops - ARKAS Database Operations Tool
Koneksi, eksplorasi, query, dan export database ARKAS SQLCipher.

Usage:
  python arkas_dbops.py tables                    # List semua tabel
  python arkas_dbops.py schema [tabel]            # Lihat struktur tabel
  python arkas_dbops.py query "SQL_QUERY"         # Jalankan SQL query
  python arkas_dbops.py query "SQL" --export      # Query + export ke Excel
  python arkas_dbops.py query "SQL" --export output.xlsx
  python arkas_dbops.py tables --export           # List tabel ke Excel
  python arkas_dbops.py sekolah                   # Info sekolah
  python arkas_dbops.py anggaran [tahun]          # Ringkasan anggaran
  python arkas_dbops.py triggers                  # Daftar triggers
  python arkas_dbops.py --help                    # Panduan lengkap
"""

import json
import os
import sys
import argparse
from datetime import datetime

# ─── Konfigurasi ──────────────────────────────────────
CONFIG_PATH = os.path.expanduser(r"~\.config\opencode\arkas_config.json")
EXPORT_DIR = os.path.expanduser(r"~\Documents\arkas_analysis\exports")

# Default jika config tidak ditemukan (fallback)
DEFAULT_DB = os.path.expanduser(r"~\AppData\Roaming\Arkas\arkas.db")


# ─── Koneksi Database ─────────────────────────────────
def load_config():
    """Load konfigurasi ARKAS dari file JSON."""
    if not os.path.exists(CONFIG_PATH):
        print(f"❌ Config tidak ditemukan: {CONFIG_PATH}")
        print("   Buat file dengan format:")
        print('   {"arkas": {"db_path": "...", "key": "...", "cipher_compatibility": 4}}')
        sys.exit(1)

    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

    arkas = config.get("arkas", {})
    return {
        "db_path": arkas.get("db_path", DEFAULT_DB),
        "key": arkas.get("key"),
        "cipher_compatibility": arkas.get("cipher_compatibility", 4),
        "sekolah": arkas.get("sekolah", "Unknown"),
        "npsn": arkas.get("npsn", "Unknown"),
    }


def connect_db(cfg):
    """Koneksi ke database ARKAS SQLCipher."""
    try:
        import sqlcipher3 as sqlite
    except ImportError:
        print("❌ sqlcipher3 tidak terinstall.")
        print("   Install: pip install sqlcipher3-binary")
        sys.exit(1)

    if not os.path.exists(cfg["db_path"]):
        print(f"❌ Database tidak ditemukan: {cfg['db_path']}")
        sys.exit(1)

    db = sqlite.connect(cfg["db_path"])
    db.execute(f"PRAGMA key = '{cfg['key']}'")
    db.execute(f"PRAGMA cipher_compatibility = {cfg['cipher_compatibility']}")
    db.execute("PRAGMA foreign_keys = ON")
    return db


# ─── Fungsi Operasi ───────────────────────────────────
def list_tables(db, cfg):
    """Daftar semua tabel dalam database."""
    cursor = db.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = cursor.fetchall()

    print(f"\n{'='*60}")
    print(f"  📋 DAFTAR TABEL - {cfg['sekolah']} ({cfg['npsn']})")
    print(f"{'='*60}")

    if not tables:
        print("  (tidak ada tabel ditemukan)")
        return []

    for i, t in enumerate(tables, 1):
        # Hitung jumlah baris
        try:
            row_count = db.execute(f"SELECT COUNT(*) FROM {t[0]}").fetchone()[0]
        except Exception:
            row_count = "?"
        print(f"  {i:2d}. {t[0]:30s} ({row_count} rows)")

    print(f"{'='*60}")
    return tables


def show_schema(db, cfg, table_name=None):
    """Lihat struktur satu atau semua tabel."""
    if table_name:
        tables = [table_name]
    else:
        cursor = db.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        tables = [t[0] for t in cursor.fetchall()]

    for table in tables:
        try:
            cursor = db.execute(f"PRAGMA table_info({table})")
            cols = cursor.fetchall()
            print(f"\n--- STRUKTUR: {table} ---")
            print(f"{'Kolom':25s} {'Tipe':15s} {'PK':3s} {'NotNull':8s} {'Default'}")
            print("-"*65)
            for c in cols:
                pk = "✓" if c[5] else ""
                nn = "✓" if c[3] else ""
                default = str(c[4]) if c[4] else "-"
                print(f"{c[1]:25s} {str(c[2]):15s} {pk:3s} {nn:8s} {default}")

            # Foreign keys
            cursor = db.execute(f"PRAGMA foreign_key_list({table})")
            fks = cursor.fetchall()
            if fks:
                print(f"\n  Foreign Keys:")
                for fk in fks:
                    print(f"    {fk[3]} → {fk[2]}({fk[4]})")

            # Indexes
            cursor = db.execute(f"PRAGMA index_list({table})")
            idxs = cursor.fetchall()
            if idxs:
                print(f"\n  Indexes:")
                for idx in idxs:
                    print(f"    {idx[1]} ({'UNIQUE' if idx[2] else ''})")

        except Exception as e:
            print(f"  ❌ Error membaca {table}: {e}")


def list_triggers(db, cfg):
    """Daftar semua trigger dalam database."""
    cursor = db.execute(
        "SELECT name, tbl_name, sql FROM sqlite_master WHERE type='trigger'"
    )
    triggers = cursor.fetchall()

    print(f"\n{'='*60}")
    print(f"  ⚡ DAFTAR TRIGGERS")
    print(f"{'='*60}")

    if not triggers:
        print("  (tidak ada trigger ditemukan)")
        return

    for t in triggers:
        print(f"\n  Trigger: {t[0]} → Table: {t[1]}")
        print(f"  SQL: {t[2][:200]}...")


def show_sekolah(db, cfg):
    """Tampilkan informasi sekolah."""
    try:
        cursor = db.execute("SELECT nama, npsn, alamat, kepsek, nip_kepsek, jumlah_siswa FROM mst_sekolah")
        school = cursor.fetchone()
        if school:
            print(f"\n{'='*60}")
            print(f"  🏫 INFO SEKOLAH")
            print(f"{'='*60}")
            print(f"  Nama        : {school[0]}")
            print(f"  NPSN        : {school[1]}")
            print(f"  Alamat      : {school[2]}")
            print(f"  Kepsek      : {school[3]}")
            print(f"  NIP Kepsek  : {school[4]}")
            print(f"  Jml Siswa   : {school[5]}")
            print(f"{'='*60}")
    except Exception as e:
        print(f"  ❌ Error: {e}")


def show_anggaran(db, cfg, tahun=None):
    """Ringkasan anggaran per tahun."""
    if tahun:
        where = f"WHERE tahun_anggaran = {tahun} AND soft_delete = 0"
    else:
        where = "WHERE soft_delete = 0"

    try:
        sql = f"""
            SELECT tahun_anggaran, COUNT(*) as jumlah, SUM(jumlah) as total
            FROM anggaran
            {where}
            GROUP BY tahun_anggaran
            ORDER BY tahun_anggaran DESC
        """
        cursor = db.execute(sql)
        rows = cursor.fetchall()

        print(f"\n{'='*60}")
        print(f"  💰 RINGKASAN ANGGARAN")
        print(f"{'='*60}")
        total_all = 0
        for r in rows:
            total = r[2] if r[2] else 0
            total_all += total
            print(f"  Tahun {r[0]}: {r[1]} item | Rp {total:,.0f}")
        print(f"{'='*60}")
        if len(rows) > 1:
            print(f"  TOTAL: Rp {total_all:,.0f}")
            print(f"{'='*60}")
    except Exception as e:
        print(f"  ❌ Error: {e}")


def run_query(db, cfg, sql, export=False, export_path=None):
    """Jalankan SQL query dan tampilkan hasilnya."""
    try:
        cursor = db.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        print(f"\n{'='*70}")
        print(f"  📊 HASIL QUERY ({len(rows)} baris, {len(columns)} kolom)")
        print(f"{'='*70}")
        print(f"  SQL: {sql[:100]}{'...' if len(sql) > 100 else ''}")
        print(f"{'='*70}")

        if not rows:
            print("  (tidak ada data)")
            return

        # Tampilkan header
        header = " | ".join(f"{c:20s}" for c in columns[:5])
        if len(columns) > 5:
            header += " | ..."
        print(f"  {header}")
        print(f"  {'-'*70}")

        # Tampilkan data (max 20 baris)
        for i, row in enumerate(rows):
            if i >= 20:
                print(f"  ... dan {len(rows) - 20} baris lainnya")
                break
            vals = " | ".join(f"{str(v)[:20]:20s}" for v in row[:5])
            if len(row) > 5:
                vals += " | ..."
            print(f"  {vals}")

        print(f"{'='*70}")

        # Export ke Excel
        if export:
            try:
                import pandas as pd
                df = pd.DataFrame(rows, columns=columns)
                if not export_path:
                    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                    export_path = os.path.join(EXPORT_DIR, f"arkas_query_{ts}.xlsx")
                os.makedirs(os.path.dirname(export_path), exist_ok=True)
                df.to_excel(export_path, index=False)
                print(f"\n  ✅ Diexport ke: {export_path}")
                print(f"  Total baris: {len(df)}")
            except ImportError:
                print("\n  ⚠️  pandas tidak terinstall. Export dibatalkan.")
                print("     Install: pip install pandas openpyxl")

    except Exception as e:
        print(f"\n  ❌ Error query: {e}")


def export_tables_to_excel(db, cfg):
    """Export daftar tabel ke Excel."""
    try:
        import pandas as pd
        cursor = db.execute("SELECT name, type, sql FROM sqlite_master WHERE type='table' ORDER BY name")
        rows = []
        for r in cursor.fetchall():
            try:
                count = db.execute(f"SELECT COUNT(*) FROM {r[0]}").fetchone()[0]
            except Exception:
                count = 0
            rows.append({"table_name": r[0], "row_count": count, "sql": r[2][:100] if r[2] else ""})

        df = pd.DataFrame(rows)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(EXPORT_DIR, f"arkas_tables_{ts}.xlsx")
        os.makedirs(EXPORT_DIR, exist_ok=True)
        df.to_excel(path, index=False)
        print(f"\n  ✅ Daftar tabel diexport ke: {path}")
    except ImportError:
        print("\n  ⚠️  pandas tidak terinstall.")


# ─── CLI Main ─────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="ARKAS DB Ops - Database Operations Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Contoh:
  python arkas_dbops.py tables                         # List tabel
  python arkas_dbops.py tables --export                # Export ke Excel
  python arkas_dbops.py schema kas_umum                # Struktur tabel
  python arkas_dbops.py query "SELECT * FROM kas_umum LIMIT 5"  # SQL
  python arkas_dbops.py query "SELECT * FROM kas_umum" --export  # +Excel
  python arkas_dbops.py sekolah                        # Info sekolah
  python arkas_dbops.py anggaran                       # Ringkasan anggaran
  python arkas_dbops.py anggaran 2026                  # Anggaran 2026
  python arkas_dbops.py triggers                       # Daftar triggers
        """
    )

    parser.add_argument("command", nargs="?", help="Perintah: tables, schema, query, sekolah, anggaran, triggers")
    parser.add_argument("args", nargs="*", help="Argumen tambahan")
    parser.add_argument("--export", action="store_true", help="Export hasil ke Excel")
    parser.add_argument("--output", help="Path file Excel output")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    cfg = load_config()
    db = connect_db(cfg)

    print(f"\n  🔗 ARKAS: {cfg['sekolah']} (NPSN: {cfg['npsn']})")
    print(f"  📁 DB: {cfg['db_path']}")

    if args.command == "tables":
        tables = list_tables(db, cfg)
        if args.export:
            export_tables_to_excel(db, cfg)

    elif args.command == "schema":
        table_name = args.args[0] if args.args else None
        show_schema(db, cfg, table_name)

    elif args.command == "query":
        sql = " ".join(args.args) if args.args else None
        if not sql:
            print("❌ Masukkan SQL query. Contoh: query \"SELECT * FROM kas_umum LIMIT 5\"")
            return
        run_query(db, cfg, sql, export=args.export, export_path=args.output)

    elif args.command == "sekolah":
        show_sekolah(db, cfg)

    elif args.command == "anggaran":
        tahun = int(args.args[0]) if args.args else None
        show_anggaran(db, cfg, tahun)

    elif args.command == "triggers":
        list_triggers(db, cfg)

    else:
        print(f"❌ Perintah tidak dikenal: {args.command}")
        parser.print_help()

    db.close()


if __name__ == "__main__":
    main()
