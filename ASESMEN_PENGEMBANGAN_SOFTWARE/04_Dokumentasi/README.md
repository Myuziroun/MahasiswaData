# SISTEM MANAJEMEN DATA MAHASISWA & TRANSKRIP NILAI (SIMAMA)
**Proyek Asesmen Sertifikasi Kompetensi Software Development (BNSP)**

Sistem aplikasi berbasis Console/CLI untuk pengelolaan data induk mahasiswa, pencatatan nilai akademik (Tugas, UTS, UAS), penghitungan nilai akhir berbobot, penentuan grade huruf, penentuan kelulusan, dan statistik kelas yang terintegrasi dengan basis data SQLite.

---

## 1. Pemetaan 9 Unit Kompetensi BNSP

Aplikasi ini dirancang khusus untuk memenuhi **100% dari 9 Unit Kompetensi** skema Software Development:

| No | Unit Kompetensi | Bukti Implementasi & Lokasi Berkas |
|:---:|:---|:---|
| **1** | **Spesifikasi Program** | Dokumen spesifikasi lengkap berisi Functional & Non-Functional Requirements, Use Case Diagram, Flowchart, dan Kamus Data.<br>📁 [`01_Spesifikasi/Requirement.pdf`](../01_Spesifikasi/Requirement.pdf)<br>📁 [`01_Spesifikasi/Flowchart_UseCase.pdf`](../01_Spesifikasi/Flowchart_UseCase.pdf) |
| **2** | **Code Guidelines & Clean Code** | Kode program mematuhi standar PEP 8, struktur modular terorganisir, penamaan variabel & fungsi deskriptif (*snake_case*, *PascalCase*), dan bebas dari *over-engineering*.<br>📁 [`02_SourceCode/project/`](../02_SourceCode/project/) |
| **3** | **Pemrograman Terstruktur** | Alur logika menu menggunakan perulangan (`while True`), percabangan terstruktur (`if-elif-else`) untuk evaluasi grade A-E, dan fungsi matematika modular.<br>📁 [`02_SourceCode/project/utils.py`](../02_SourceCode/project/utils.py) |
| **4** | **Pemrograman Berorientasi Objek (OOP)** | Penerapan pilar OOP: **Inheritance** (`Person` diwarisi oleh `Mahasiswa`), **Encapsulation** (atribut privat dengan `@property` & `@setter` validasi), dan **Polymorphism** (override method `info()`).<br>📁 [`02_SourceCode/project/models.py`](../02_SourceCode/project/models.py) |
| **5** | **Library / Pre-Existing** | Menggunakan modul bawaan Python (*standard library*) untuk portabilitas maksimal: `sqlite3` (database), `unittest` (testing), `re` (regex validasi), serta utilitas tabel konsol mandiri.<br>📁 [`02_SourceCode/project/utils.py`](../02_SourceCode/project/utils.py) |
| **6** | **Akses Basis Data (CRUD)** | Menggunakan SQLite lokal (`mahasiswa.db`) dengan query berparameter (`?`) untuk mencegah SQL Injection. Mencakup operasi Create, Read, Update, Delete, dan Search.<br>📁 [`02_SourceCode/project/database.py`](../02_SourceCode/project/database.py)<br>📁 [`03_Database/database.sql`](../03_Database/database.sql) |
| **7** | **Dokumentasi Kode** | Dilengkapi *Docstring* pada seluruh class dan fungsi, panduan instalasi dan penggunaan (`README.md`), serta tangkapan layar eksekusi fitur.<br>📁 [`04_Dokumentasi/README.md`](README.md)<br>📁 [`04_Dokumentasi/Screenshot_Program/`](Screenshot_Program/) |
| **8** | **Debugging** | Catatan analisis galat runtime error (`ValueError`, `IntegrityError`, `ZeroDivisionError`), mitigasi penanganan `try-except`, serta prosedur debugging menggunakan breakpoint di IDE.<br>📁 [`05_Debugging/Catatan_Debugging.pdf`](../05_Debugging/Catatan_Debugging.pdf) |
| **9** | **Pengujian Unit (Unit Test)** | Pengujian unit otomatis sebanyak 10 skenario uji mencakup kalkulasi nilai, grade, validasi, dan OOP (100% PASS), beserta matriks pengujian format Excel.<br>📁 [`06_Testing/test_kalkulasi.py`](../06_Testing/test_kalkulasi.py)<br>📁 [`06_Testing/TestCase_Hasil.xlsx`](../06_Testing/TestCase_Hasil.xlsx) |

---

## 2. Struktur Direktori Proyek

```text
ASESMEN_PENGEMBANGAN_SOFTWARE/
│
├── 01_Spesifikasi/
│   ├── Requirement.pdf             # Dokumen kebutuhan fungsional, non-fungsional, & kamus data
│   ├── Requirement.md              # Source markdown spesifikasi
│   ├── Flowchart_UseCase.pdf       # Diagram alur program, use case, & class diagram
│   └── Flowchart_UseCase.md        # Source markdown flowchart & use case
│
├── 02_SourceCode/
│   └── project/
│       ├── main.py                 # Entry point menu interaktif CLI
│       ├── models.py               # Implementasi OOP (Class Person & Mahasiswa)
│       ├── database.py             # Koneksi SQLite & operasi CRUD
│       └── utils.py                # Fungsi validasi, kalkulasi terstruktur, & tabel
│
├── 03_Database/
│   ├── database.sql                # DDL skrip CREATE TABLE & contoh INSERT
│   └── mahasiswa.db                # File basis data SQLite (siap pakai)
│
├── 04_Dokumentasi/
│   ├── README.md                   # Panduan teknis lengkap & pemetaan kompetensi
│   └── Screenshot_Program/         # Bukti hasil eksekusi fitur-fitur aplikasi
│       ├── 01_menu_utama.png
│       ├── 02_tampilkan_data.png
│       ├── 03_tambah_mahasiswa.png
│       ├── 04_pencarian_data.png
│       ├── 05_ubah_data.png
│       ├── 06_hapus_data.png
│       ├── 07_statistik_kelas.png
│       └── 08_hasil_unit_testing.png
│
├── 05_Debugging/
│   ├── Catatan_Debugging.pdf       # Laporan analisis error, try-except, & breakpoint
│   └── Catatan_Debugging.md        # Source markdown catatan debugging
│
└── 06_Testing/
    ├── test_kalkulasi.py           # Script unit test otomatis (10 test cases)
    ├── TestCase_Hasil.xlsx         # Matriks hasil uji spreadsheet Excel
    └── TestCase_Hasil.md           # Versi markdown matriks hasil uji
```

---

## 3. Persyaratan Sistem & Instalasi

* **Sistem Operasi:** Windows, macOS, atau Linux
* **Penerjemah Bahasa:** Python versi 3.8 atau lebih baru
* **Dependensi Eksternal:** **TIDAK ADA (Zero External Dependency)**  
  Aplikasi 100% menggunakan Python Standard Library (`sqlite3`, `unittest`, `re`, `os`, `sys`).

---

## 4. Cara Menjalankan Aplikasi

### 4.1 Menjalankan Program Utama (CLI)
Buka terminal / PowerShell pada folder project dan jalankan:
```bash
cd ASESMEN_PENGEMBANGAN_SOFTWARE/02_SourceCode/project
python main.py
```

### 4.2 Menjalankan Pengujian Unit (Unit Test)
Buka terminal pada folder testing dan jalankan:
```bash
cd ASESMEN_PENGEMBANGAN_SOFTWARE/06_Testing
python test_kalkulasi.py
```
Hasil eksekusi akan menampilkan 10 pengujian berstatus `ok` (100% PASS).

---

## 5. Fitur Utama Program

1. **[1] Tampilkan Semua Mahasiswa:**  
   Menampilkan tabel seluruh mahasiswa terdaftar lengkap dengan Nilai Tugas, UTS, UAS, Nilai Akhir hasil perhitungan, Grade mutu, dan Status kelulusan.
2. **[2] Tambah Mahasiswa Baru:**  
   Menambahkan data mahasiswa baru disertai validasi NIM (tidak boleh duplikat/format salah) dan nilai (rentang 0-100).
3. **[3] Cari Mahasiswa:**  
   Pencarian fleksibel berdasarkan kata kunci NIM, Nama Mahasiswa, atau Program Studi.
4. **[4] Ubah Data Mahasiswa:**  
   Memperbarui data identitas maupun komponen nilai berdasarkan NIM. Nilai akhir dan grade akan otomatis dihitung ulang.
5. **[5] Hapus Data Mahasiswa:**  
   Menghapus rekaman mahasiswa dari basis data dengan konfirmasi persetujuan pengguna (`y/N`).
6. **[6] Statistik Nilai Kelas:**  
   Menyajikan ringkasan nilai rata-rata kelas, nilai tertinggi, nilai terendah, dan rasio kelulusan.

---

## 6. Formula Bisnis & Grading

* **Perhitungan Nilai Akhir:**
  $$\text{Nilai Akhir} = (30\% \times \text{Tugas}) + (30\% \times \text{UTS}) + (40\% \times \text{UAS})$$

* **Konversi Grade:**
  * **A :** Nilai Akhir $\ge$ 85.00 $\rightarrow$ **LULUS**
  * **B :** 70.00 $\le$ Nilai Akhir < 85.00 $\rightarrow$ **LULUS**
  * **C :** 55.00 $\le$ Nilai Akhir < 70.00 $\rightarrow$ **LULUS**
  * **D :** 40.00 $\le$ Nilai Akhir < 55.00 $\rightarrow$ **TIDAK LULUS**
  * **E :** Nilai Akhir < 40.00 $\rightarrow$ **TIDAK LULUS**
