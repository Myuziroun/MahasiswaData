# DOKUMEN SPESIFIKASI KEBUTUHAN SISTEM (REQUIREMENTS SPECIFICATION)
## Sistem Manajemen Data Mahasiswa & Transkrip Nilai (SIMAMA)
**Skema Sertifikasi:** Pemrograman / Software Development (BNSP)  
**Unit Kompetensi:** Mengimplementasikan Spesifikasi Program

---

## 1. Deskripsi Umum Sistem
Sistem Manajemen Data Mahasiswa & Transkrip Nilai (SIMAMA) adalah aplikasi berbasis Console/CLI yang dirancang untuk mengelola data induk mahasiswa, pencatatan nilai akademik (Tugas, UTS, UAS), penghitungan otomatis Nilai Akhir berbasis bobot persentase, penentuan grade huruf, penentuan status kelulusan, serta penyajian statistik kelas.

Sistem ini dikembangkan secara modular, menerapkan konsep Pemrograman Terstruktur, Pemrograman Berorientasi Objek (OOP), basis data relasional SQLite, dan dilengkapi dengan pengujian unit otomatis (*unit testing*).

---

## 2. Kebutuhan Fungsional (Functional Requirements)

| Kode | Nama Fitur | Deskripsi Kebutuhan |
|:---:|:---|:---|
| **FR-01** | Input Data Mahasiswa & Nilai | Pengguna dapat menambahkan data mahasiswa baru meliputi NIM, Nama Lengkap, Jurusan, Nilai Tugas, Nilai UTS, dan Nilai UAS. |
| **FR-02** | Tampilkan Seluruh Data | Sistem dapat menampilkan seluruh daftar mahasiswa dalam bentuk tabel yang memuat data identitas, nilai komponen, nilai akhir terhitung, grade, dan status kelulusan. |
| **FR-03** | Pencarian Mahasiswa | Pengguna dapat melakukan pencarian data mahasiswa berdasarkan kata kunci NIM, Nama, maupun Program Studi. |
| **FR-04** | Perbaruan Data (Update) | Pengguna dapat memperbarui identitas mahasiswa maupun nilai komponen akademik berdasarkan NIM unik. |
| **FR-05** | Penghapusan Data (Delete) | Pengguna dapat menghapus data mahasiswa tertentu dengan konfirmasi keamanan (*safety confirmation*). |
| **FR-06** | Ringkasan Statistik Kelas | Sistem mampu menghitung dan menampilkan statistik agregat: rata-rata nilai akhir, nilai tertinggi, nilai terendah, serta persentase kelulusan kelas. |
| **FR-07** | Validasi Input & Enkapsulasi | Sistem memvalidasi NIM (alfanumerik 5-20 karakter), nama tidak boleh kosong, dan nilai akademik wajib berada dalam rentang numerik 0.0 s/d 100.0. |

---

## 3. Kebutuhan Non-Fungsional (Non-Functional Requirements)

| Kode | Kategori | Deskripsi Kebutuhan |
|:---:|:---|:---|
| **NFR-01** | Usability | Antarmuka CLI interaktif dengan tata letak menu yang intuitif, nomor navigasi jelas, dan format tabel data yang mudah dibaca. |
| **NFR-02** | Reliability | Sistem tahan terhadap kesalahan input pengguna (*graceful error handling*) menggunakan blok `try-except` sehingga aplikasi tidak mengalami *crash* mendadak. |
| **NFR-03** | Portability | Menggunakan SQLite 3 dan modul bawaan Python (*standard library*) sehingga aplikasi dapat langsung dijalankan pada berbagai OS (Windows, Linux, macOS) tanpa perlu instalasi DBMS server pihak ketiga. |
| **NFR-04** | Maintainability | Kode program ditulis dengan prinsip *Clean Code* (PEP 8), modular terpisah (`models.py`, `database.py`, `utils.py`, `main.py`), dan dilengkapi dokumentasi *docstring*. |
| **NFR-05** | Performance | Eksekusi kueri lokal SQLite berlangsung instan (< 100 ms) untuk operasi CRUD ratusan data. |

---

## 4. Kamus Data (Data Dictionary)

### Entitas: `mahasiswa` (Tabel SQLite)
| Nama Atribut | Tipe Data | Constraint | Deskripsi |
|:---|:---|:---|:---|
| `id` | INTEGER | PRIMARY KEY, AUTOINCREMENT | Identifier unik internal sistem |
| `nim` | TEXT / VARCHAR(20) | NOT NULL, UNIQUE | Nomor Induk Mahasiswa (kunci bisnis) |
| `nama` | TEXT / VARCHAR(100) | NOT NULL | Nama lengkap mahasiswa |
| `jurusan` | TEXT / VARCHAR(50) | NOT NULL | Program studi / Jurusan |
| `nilai_tugas` | REAL / FLOAT | NOT NULL, DEFAULT 0.0, CHECK (0-100) | Nilai komponen Tugas mandiri/kelompok |
| `nilai_uts` | REAL / FLOAT | NOT NULL, DEFAULT 0.0, CHECK (0-100) | Nilai Ujian Tengah Semester |
| `nilai_uas` | REAL / FLOAT | NOT NULL, DEFAULT 0.0, CHECK (0-100) | Nilai Ujian Akhir Semester |
| `nilai_akhir` | REAL / FLOAT | NOT NULL, DEFAULT 0.0 | Nilai hasil kalkulasi berbobot |
| `grade` | TEXT / VARCHAR(2) | NOT NULL, DEFAULT 'E' | Predikat huruf mutu: A, B, C, D, E |
| `status` | TEXT / VARCHAR(20) | NOT NULL, DEFAULT 'TIDAK LULUS' | Status kelulusan: LULUS / TIDAK LULUS |

---

## 5. Aturan Bisnis (Business Rules)

### 5.1 Formula Nilai Akhir
$$\text{Nilai Akhir} = (0.30 \times \text{Nilai Tugas}) + (0.30 \times \text{Nilai UTS}) + (0.40 \times \text{Nilai UAS})$$

### 5.2 Skala Penentuan Grade & Kelulusan
| Rentang Nilai Akhir | Grade | Bobot Mutu | Status Kelulusan |
|:---:|:---:|:---:|:---:|
| 85.00 - 100.00 | **A** | 4.00 | **LULUS** |
| 70.00 - 84.99 | **B** | 3.00 | **LULUS** |
| 55.00 - 69.99 | **C** | 2.00 | **LULUS** |
| 40.00 - 54.99 | **D** | 1.00 | **TIDAK LULUS** (Remedial) |
| 0.00 - 39.99 | **E** | 0.00 | **TIDAK LULUS** |
