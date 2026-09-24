# DOKUMEN DIAGRAM ALUR (FLOWCHART) & USE CASE
## Sistem Manajemen Data Mahasiswa & Transkrip Nilai (SIMAMA)
**Skema Sertifikasi:** Pemrograman / Software Development (BNSP)  
**Unit Kompetensi:** Mengimplementasikan Spesifikasi Program & Pemrograman Terstruktur

---

## 1. Use Case Diagram

Diagram Use Case memodelkan interaksi antara Aktor (Admin Akademik / Dosen) dengan fungsi-fungsi utama yang disediakan oleh sistem SIMAMA.

```mermaid
flowchart LR
    Actor((Admin / User Akademik))
    
    subgraph Sistem_SIMAMA ["Sistem SIMAMA"]
        UC1(["Tampilkan Seluruh Mahasiswa"])
        UC2(["Tambah Mahasiswa & Nilai"])
        UC3(["Pencarian Mahasiswa"])
        UC4(["Ubah Data Mahasiswa"])
        UC5(["Hapus Data Mahasiswa"])
        UC6(["Statistik & Ringkasan Kelas"])
        UC7(["Validasi Input & Kalkulasi Grade"])
    end

    Actor --> UC1
    Actor --> UC2
    Actor --> UC3
    Actor --> UC4
    Actor --> UC5
    Actor --> UC6

    UC2 -.->|include| UC7
    UC4 -.->|include| UC7
```

### Deskripsi Use Case:
1. **Tampilkan Seluruh Mahasiswa**: Membaca basis data dan menyajikan tabel lengkap mahasiswa beserta nilai akhir dan predikat grade.
2. **Tambah Mahasiswa**: Menerima input data baru, memvalidasi format, melakukan enkapsulasi objek `Mahasiswa`, dan menyimpannya ke database SQLite.
3. **Pencarian Mahasiswa**: Menyaring data berdasarkan kata kunci NIM, Nama, atau Jurusan dengan klausa SQL `LIKE`.
4. **Ubah Data**: Mengambil rekaman data lama, memungkinkan pengguna memperbarui nama, jurusan, atau nilai, serta menghitung ulang nilai akhir dan grade.
5. **Hapus Data**: Menghapus rekaman berdasarkan NIM dengan dialog konfirmasi keselamatan.
6. **Statistik Kelas**: Mengagregasi data kelas (rata-rata, tertinggi, terendah, persentase kelulusan).

---

## 2. Flowchart Alur Program Utama (Interactive CLI)

Diagram alur berikut menggambarkan jalannya aplikasi sejak dijalankan hingga pengguna keluar.

```mermaid
flowchart TD
    Start([Mulai]) --> InitDB[Inisialisasi Database & Seeding Data Awal]
    InitDB --> ShowMenu[Tampilkan Menu Pilihan 0 - 6]
    ShowMenu --> InputChoice[/Input Pilihan Pengguna/]
    
    InputChoice --> CheckChoice{Pilihan Menu?}

    CheckChoice -->|1| Menu1[Ambil Seluruh Data dari SQLite<br/>Format Tabel ASCII & Cetak]
    CheckChoice -->|2| Menu2[Input NIM, Nama, Jurusan & Nilai<br/>Validasi Format & Rentang<br/>Simpan ke Database SQLite]
    CheckChoice -->|3| Menu3[Input Keyword Pencarian<br/>Filter NIM/Nama/Jurusan via SQL<br/>Tampilkan Hasil]
    CheckChoice -->|4| Menu4[Input NIM Target<br/>Ambil Data Lama & Form Ubah<br/>Update ke Database SQLite]
    CheckChoice -->|5| Menu5[Input NIM Target<br/>Konfirmasi Penghapusan y/n<br/>Hapus Rekaman dari SQLite]
    CheckChoice -->|6| Menu6[Hitung Rata-rata, Max, Min<br/>Persentase Kelulusan Kelas<br/>Tampilkan Ringkasan]
    CheckChoice -->|0| ExitProgram([Keluar Aplikasi])
    CheckChoice -->|Lainnya| Invalid[Tampilkan Pesan Pilihan Tidak Valid]

    Menu1 --> PressEnter[/Tekan Enter untuk Kembali/]
    Menu2 --> PressEnter
    Menu3 --> PressEnter
    Menu4 --> PressEnter
    Menu5 --> PressEnter
    Menu6 --> PressEnter
    Invalid --> PressEnter

    PressEnter --> ShowMenu
```

---

## 3. Flowchart Logika Validasi & Kalkulasi Nilai (Subprogram)

Diagram alur berikut menggambarkan alur logika terstruktur pada fungsi penentuan Grade dan Kelulusan:

```mermaid
flowchart TD
    InVal[/Input: Tugas, UTS, UAS/] --> Hitung["Nilai Akhir = 0.3*Tugas + 0.3*UTS + 0.4*UAS"]
    Hitung --> CekA{"Nilai Akhir >= 85.0?"}
    CekA -->|Ya| GradeA["Grade = 'A'<br/>Status = 'LULUS'"]
    CekA -->|Tidak| CekB{"Nilai Akhir >= 70.0?"}
    
    CekB -->|Ya| GradeB["Grade = 'B'<br/>Status = 'LULUS'"]
    CekB -->|Tidak| CekC{"Nilai Akhir >= 55.0?"}
    
    CekC -->|Ya| GradeC["Grade = 'C'<br/>Status = 'LULUS'"]
    CekC -->|Tidak| CekD{"Nilai Akhir >= 40.0?"}
    
    CekD -->|Ya| GradeD["Grade = 'D'<br/>Status = 'TIDAK LULUS'"]
    CekD -->|Tidak| GradeE["Grade = 'E'<br/>Status = 'TIDAK LULUS'"]

    GradeA --> ReturnOut[/Output: Nilai Akhir, Grade, Status/]
    GradeB --> ReturnOut
    GradeC --> ReturnOut
    GradeD --> ReturnOut
    GradeE --> ReturnOut
```

---

## 4. Class Diagram (Pemrograman Berorientasi Objek - OOP)

Menerapkan pilar OOP: **Inheritance**, **Encapsulation**, dan **Polymorphism**.

```mermaid
classDiagram
    class Person {
        -str _nama
        +nama() str
        +nama(str) void
        +info() str
    }

    class Mahasiswa {
        -str _nim
        -str _jurusan
        -float _nilai_tugas
        -float _nilai_uts
        -float _nilai_uas
        +nim() str
        +jurusan() str
        +nilai_tugas() float
        +nilai_uts() float
        +nilai_uas() float
        +hitung_nilai_akhir() float
        +get_grade() str
        +get_status() str
        +info() str
        +to_dict() dict
    }

    Person <|-- Mahasiswa : Inheritance
```
