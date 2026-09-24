"""
Module: database.py
Deskripsi: Mengelola koneksi basis data SQLite dan operasi CRUD (Create, Read, Update, Delete)
Unit Kompetensi: Akses Basis Data (CRUD), Library / Pre-Existing, Debugging & Clean Code
"""

import os
import sqlite3
from typing import List, Optional, Tuple
from models import Mahasiswa

# Lokasi default file database di folder 03_Database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "03_Database", "mahasiswa.db"))


def get_connection(db_path: str = None) -> sqlite3.Connection:
    """
    Membuka dan mengembalikan objek koneksi database SQLite.
    Mengaktifkan row_factory agar baris hasil query dapat diakses berdasarkan nama kolom.
    """
    path = db_path or DEFAULT_DB_PATH
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: str = None):
    """
    Inisialisasi tabel 'mahasiswa' jika belum ada di database.
    Menerapkan constraint PRIMARY KEY pada id dan UNIQUE pada nim.
    """
    conn = get_connection(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mahasiswa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nim TEXT NOT NULL UNIQUE,
                nama TEXT NOT NULL,
                jurusan TEXT NOT NULL,
                nilai_tugas REAL NOT NULL DEFAULT 0.0,
                nilai_uts REAL NOT NULL DEFAULT 0.0,
                nilai_uas REAL NOT NULL DEFAULT 0.0,
                nilai_akhir REAL NOT NULL DEFAULT 0.0,
                grade TEXT NOT NULL DEFAULT 'E',
                status TEXT NOT NULL DEFAULT 'TIDAK LULUS'
            );
        """)
        conn.commit()
    finally:
        conn.close()


def row_to_mahasiswa(row: sqlite3.Row) -> Mahasiswa:
    """Helper fungsi untuk mengonversi row database menjadi objek Mahasiswa (OOP)."""
    return Mahasiswa(
        nim=row["nim"],
        nama=row["nama"],
        jurusan=row["jurusan"],
        nilai_tugas=row["nilai_tugas"],
        nilai_uts=row["nilai_uts"],
        nilai_uas=row["nilai_uas"],
        id_db=row["id"]
    )


def tambah_mahasiswa(mhs: Mahasiswa, db_path: str = None) -> Tuple[bool, str]:
    """
    Menyimpan data mahasiswa baru ke basis data (CREATE).
    Menerapkan penanganan sqlite3.IntegrityError jika NIM sudah terdaftar.
    """
    conn = get_connection(db_path)
    cursor = conn.cursor()
    try:
        nilai_akhir = mhs.hitung_nilai_akhir()
        grade = mhs.get_grade()
        status = mhs.get_status()

        cursor.execute("""
            INSERT INTO mahasiswa (nim, nama, jurusan, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir, grade, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            mhs.nim,
            mhs.nama,
            mhs.jurusan,
            mhs.nilai_tugas,
            mhs.nilai_uts,
            mhs.nilai_uas,
            nilai_akhir,
            grade,
            status
        ))
        conn.commit()
        return True, "Data mahasiswa berhasil disimpan ke database."
    except sqlite3.IntegrityError:
        return False, f"Gagal: Mahasiswa dengan NIM '{mhs.nim}' sudah terdaftar!"
    except sqlite3.Error as e:
        return False, f"Kesalahan Database: {e}"
    finally:
        conn.close()


def ambil_semua_mahasiswa(db_path: str = None) -> List[Mahasiswa]:
    """Mengambil seluruh rekaman data mahasiswa dari basis data (READ)."""
    conn = get_connection(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM mahasiswa ORDER BY nim ASC")
        rows = cursor.fetchall()
        return [row_to_mahasiswa(r) for r in rows]
    finally:
        conn.close()


def cari_mahasiswa_by_nim(nim: str, db_path: str = None) -> Optional[Mahasiswa]:
    """Mencari satu mahasiswa berdasarkan Primary Key / Unique NIM."""
    conn = get_connection(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM mahasiswa WHERE nim = ?", (nim.strip(),))
        row = cursor.fetchone()
        return row_to_mahasiswa(row) if row else None
    finally:
        conn.close()


def cari_mahasiswa(keyword: str, db_path: str = None) -> List[Mahasiswa]:
    """Mencari mahasiswa berdasarkan kecocokan NIM, Nama, atau Jurusan."""
    conn = get_connection(db_path)
    cursor = conn.cursor()
    try:
        query_pattern = f"%{keyword.strip()}%"
        cursor.execute("""
            SELECT * FROM mahasiswa 
            WHERE nim LIKE ? OR nama LIKE ? OR jurusan LIKE ?
            ORDER BY nim ASC
        """, (query_pattern, query_pattern, query_pattern))
        rows = cursor.fetchall()
        return [row_to_mahasiswa(r) for r in rows]
    finally:
        conn.close()


def ubah_mahasiswa(mhs: Mahasiswa, db_path: str = None) -> Tuple[bool, str]:
    """Memperbarui informasi mahasiswa dan nilai di basis data (UPDATE)."""
    conn = get_connection(db_path)
    cursor = conn.cursor()
    try:
        nilai_akhir = mhs.hitung_nilai_akhir()
        grade = mhs.get_grade()
        status = mhs.get_status()

        cursor.execute("""
            UPDATE mahasiswa 
            SET nama = ?, jurusan = ?, nilai_tugas = ?, nilai_uts = ?, nilai_uas = ?,
                nilai_akhir = ?, grade = ?, status = ?
            WHERE nim = ?
        """, (
            mhs.nama,
            mhs.jurusan,
            mhs.nilai_tugas,
            mhs.nilai_uts,
            mhs.nilai_uas,
            nilai_akhir,
            grade,
            status,
            mhs.nim
        ))
        conn.commit()
        if cursor.rowcount > 0:
            return True, f"Data mahasiswa dengan NIM '{mhs.nim}' berhasil diperbarui."
        return False, f"Data dengan NIM '{mhs.nim}' tidak ditemukan."
    except sqlite3.Error as e:
        return False, f"Kesalahan Database: {e}"
    finally:
        conn.close()


def hapus_mahasiswa(nim: str, db_path: str = None) -> Tuple[bool, str]:
    """Menghapus data mahasiswa dari basis data berdasarkan NIM (DELETE)."""
    conn = get_connection(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM mahasiswa WHERE nim = ?", (nim.strip(),))
        conn.commit()
        if cursor.rowcount > 0:
            return True, f"Data mahasiswa dengan NIM '{nim}' berhasil dihapus."
        return False, f"Data dengan NIM '{nim}' tidak ditemukan."
    except sqlite3.Error as e:
        return False, f"Kesalahan Database: {e}"
    finally:
        conn.close()


def seed_contoh_data(db_path: str = None):
    """
    Mengisi data awal (seeding) 5 mahasiswa jika tabel masih kosong.
    Memudahkan penguji/asesor untuk langsung melihat dan menguji data.
    """
    init_db(db_path)
    conn = get_connection(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) AS total FROM mahasiswa")
        count = cursor.fetchone()["total"]
        if count == 0:
            contoh = [
                Mahasiswa("2024001", "Budi Santoso", "Teknik Informatika", 85, 90, 88),
                Mahasiswa("2024002", "Siti Aminah", "Sistem Informasi", 78, 82, 80),
                Mahasiswa("2024003", "Rian Pratama", "Teknik Komputer", 60, 65, 70),
                Mahasiswa("2024004", "Dewi Lestari", "Teknik Informatika", 95, 92, 98),
                Mahasiswa("2024005", "Ahmad Fauzi", "Manajemen Informatika", 45, 50, 40)
            ]
            for m in contoh:
                tambah_mahasiswa(m, db_path)
    finally:
        conn.close()
