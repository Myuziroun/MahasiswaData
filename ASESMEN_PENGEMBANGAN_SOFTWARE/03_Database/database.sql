-- =====================================================================
-- SKRIP BASIS DATA: SISTEM MANAJEMEN DATA MAHASISWA & NILAI (SIMAMA)
-- Unit Kompetensi : Akses Basis Data (CRUD) & Pemrograman Terstruktur
-- Engine          : SQLite 3 / ANSI SQL Compliant
-- =====================================================================

-- 1. Pembuatan Tabel Mahasiswa (DDL)
CREATE TABLE IF NOT EXISTS mahasiswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nim TEXT NOT NULL UNIQUE,
    nama TEXT NOT NULL,
    jurusan TEXT NOT NULL,
    nilai_tugas REAL NOT NULL DEFAULT 0.0 CHECK(nilai_tugas >= 0.0 AND nilai_tugas <= 100.0),
    nilai_uts REAL NOT NULL DEFAULT 0.0 CHECK(nilai_uts >= 0.0 AND nilai_uts <= 100.0),
    nilai_uas REAL NOT NULL DEFAULT 0.0 CHECK(nilai_uas >= 0.0 AND nilai_uas <= 100.0),
    nilai_akhir REAL NOT NULL DEFAULT 0.0,
    grade TEXT NOT NULL DEFAULT 'E',
    status TEXT NOT NULL DEFAULT 'TIDAK LULUS'
);

-- 2. Pembuatan Index untuk Optimasi Pencarian
CREATE INDEX IF NOT EXISTS idx_mahasiswa_nim ON mahasiswa(nim);
CREATE INDEX IF NOT EXISTS idx_mahasiswa_nama ON mahasiswa(nama);

-- 3. Data Awal / Seeding (DML)
INSERT OR IGNORE INTO mahasiswa (nim, nama, jurusan, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir, grade, status)
VALUES 
    ('2024001', 'Budi Santoso', 'Teknik Informatika', 85.0, 90.0, 88.0, 87.70, 'A', 'LULUS'),
    ('2024002', 'Siti Aminah', 'Sistem Informasi', 78.0, 82.0, 80.0, 80.00, 'B', 'LULUS'),
    ('2024003', 'Rian Pratama', 'Teknik Komputer', 60.0, 65.0, 70.0, 65.50, 'C', 'LULUS'),
    ('2024004', 'Dewi Lestari', 'Teknik Informatika', 95.0, 92.0, 98.0, 95.30, 'A', 'LULUS'),
    ('2024005', 'Ahmad Fauzi', 'Manajemen Informatika', 45.0, 50.0, 40.0, 44.50, 'D', 'TIDAK LULUS');

-- =====================================================================
-- CONTOH KUERI CRUD UNTUK PENGUJIAN:
-- =====================================================================

-- [C] Create / Insert Data:
-- INSERT INTO mahasiswa (nim, nama, jurusan, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir, grade, status)
-- VALUES ('2024006', 'Rina Wulandari', 'Sistem Informasi', 80, 85, 90, 85.5, 'A', 'LULUS');

-- [R] Read / Select All:
-- SELECT * FROM mahasiswa ORDER BY nim ASC;

-- [R] Read / Cari Berdasarkan NIM atau Nama:
-- SELECT * FROM mahasiswa WHERE nim = '2024001' OR nama LIKE '%Budi%';

-- [U] Update Data:
-- UPDATE mahasiswa 
-- SET nilai_tugas = 90.0, nilai_akhir = 89.20, grade = 'A', status = 'LULUS'
-- WHERE nim = '2024001';

-- [D] Delete Data:
-- DELETE FROM mahasiswa WHERE nim = '2024005';
