# PROYEK ASESMEN SERTIFIKASI KOMPETENSI SOFTWARE DEVELOPMENT (BNSP)
## SISTEM MANAJEMEN DATA MAHASISWA & TRANSKRIP NILAI (SIMAMA)

Selamat datang di repositori proyek asesmen sertifikasi kompetensi skema **Software Development / Pemrograman**.  
Seluruh berkas persyaratan dan bukti kompetensi telah disusun secara rapi pada folder utama:

📂 **[`ASESMEN_PENGEMBANGAN_SOFTWARE/`](ASESMEN_PENGEMBANGAN_SOFTWARE/)**

---

## 📌 Ringkasan Cepat & Lokasi Bukti 9 Unit Kompetensi

| No | Unit Kompetensi | File Bukti Konkret |
|:---:|:---|:---|
| **1** | **Mengimplementasikan Spesifikasi Program** | [Requirement.pdf](ASESMEN_PENGEMBANGAN_SOFTWARE/01_Spesifikasi/Requirement.pdf) & [Flowchart_UseCase.pdf](ASESMEN_PENGEMBANGAN_SOFTWARE/01_Spesifikasi/Flowchart_UseCase.pdf) |
| **2** | **Menerapkan Perintah Bermakna & Clean Code** | Kode terstruktur modular PEP 8 pada [02_SourceCode/project/](ASESMEN_PENGEMBANGAN_SOFTWARE/02_SourceCode/project/) |
| **3** | **Menerapkan Pemrograman Terstruktur** | Looping menu interaktif, percabangan grade pada [utils.py](ASESMEN_PENGEMBANGAN_SOFTWARE/02_SourceCode/project/utils.py) |
| **4** | **Menerapkan Pemrograman Berorientasi Objek (OOP)** | Class `Person` & `Mahasiswa` (Inheritance, Encapsulation, Polymorphism) pada [models.py](ASESMEN_PENGEMBANGAN_SOFTWARE/02_SourceCode/project/models.py) |
| **5** | **Menggunakan Library / Komponen Pre-Existing** | SQLite3, Unittest, RegEx, dan formatting tabel pada [database.py](ASESMEN_PENGEMBANGAN_SOFTWARE/02_SourceCode/project/database.py) |
| **6** | **Mengakses Basis Data (CRUD)** | Basis data SQLite [mahasiswa.db](ASESMEN_PENGEMBANGAN_SOFTWARE/03_Database/mahasiswa.db) & query [database.sql](ASESMEN_PENGEMBANGAN_SOFTWARE/03_Database/database.sql) |
| **7** | **Membuat Dokumentasi Kode Program** | [README.md](ASESMEN_PENGEMBANGAN_SOFTWARE/04_Dokumentasi/README.md) & [Screenshot_Program/](ASESMEN_PENGEMBANGAN_SOFTWARE/04_Dokumentasi/Screenshot_Program/) |
| **8** | **Melakukan Debugging** | Laporan analisis error & breakpoint pada [Catatan_Debugging.pdf](ASESMEN_PENGEMBANGAN_SOFTWARE/05_Debugging/Catatan_Debugging.pdf) |
| **9** | **Melakukan Pengujian Unit (Unit Test)** | 10 skenario uji otomatis pada [test_kalkulasi.py](ASESMEN_PENGEMBANGAN_SOFTWARE/06_Testing/test_kalkulasi.py) & [TestCase_Hasil.xlsx](ASESMEN_PENGEMBANGAN_SOFTWARE/06_Testing/TestCase_Hasil.xlsx) |

---

## 🚀 Cara Menjalankan Aplikasi

### 1. Menjalankan Menu Program (CLI):
```bash
python ASESMEN_PENGEMBANGAN_SOFTWARE/02_SourceCode/project/main.py
```

### 2. Menjalankan Pengujian Unit Otomatis:
```bash
python ASESMEN_PENGEMBANGAN_SOFTWARE/06_Testing/test_kalkulasi.py
```

> **Catatan:** Aplikasi ini memiliki **Zero External Dependencies** (hanya memerlukan Python 3.8+ bawaan) sehingga dapat langsung dijalankan oleh Asesor tanpa instalasi paket pip tambahan.
