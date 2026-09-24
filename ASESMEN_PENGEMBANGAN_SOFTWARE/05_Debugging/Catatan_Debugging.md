# CATATAN & LAPORAN PROSES DEBUGGING
## Sistem Manajemen Data Mahasiswa & Transkrip Nilai (SIMAMA)
**Skema Sertifikasi:** Pemrograman / Software Development (BNSP)  
**Unit Kompetensi:** Melakukan Debugging (Kode Unit: J.620100.016.01)

---

## 1. Tujuan Debugging
Tujuan dari proses debugging ini adalah:
1. Mengidentifikasi potensi galat (*error*) baik berupa kesalahan sintaks, runtime error, maupun kesalahan logika bisnis.
2. Memastikan aplikasi memiliki ketahanan (*resilience*) dengan menerapkan teknik penanganan pengecualian (*exception handling* `try-except`).
3. Mendokumentasikan langkah pemeriksaan variabel menggunakan fasilitas debugging (IDE / Breakpoint).

---

## 2. Skenario Analisis Error dan Solusi Penanganannya

### Skenario 1: Runtime Error `ValueError` pada Input Nilai Numerik
* **Deskripsi Masalah:**  
  Pengguna secara tidak sengaja memasukkan karakter string non-numerik (misalnya mengetik `"delapan puluh"` atau simbol `"abc"`) pada saat diminta menginput Nilai Tugas, UTS, atau UAS.
* **Gejala / Traceback Asli (Sebelum Diperbaiki):**
  ```text
  Traceback (most recent call last):
    File "main.py", line 68, in menu_tambah
      tugas = float(input("Nilai Tugas: "))
  ValueError: could not convert string to float: 'delapan puluh'
  ```
* **Dampak:** Aplikasi langsung berhenti mendadak (*crash*), data yang belum tersimpan hilang.
* **Solusi Penanganan (Exception Handling):**  
  Membuat fungsi utilitas pembungkus `input_float()` di `utils.py` yang menggunakan perulangan `while True` dan blok `try-except ValueError`:
  ```python
  def input_float(prompt: str, min_val: float = 0.0, max_val: float = 100.0) -> float:
      while True:
          raw = input(prompt).strip()
          try:
              val = float(raw)
              if min_val <= val <= max_val:
                  return round(val, 2)
              print(f"[!] Nilai harus berada dalam rentang {min_val} sampai {max_val}.")
          except ValueError:
              print("[!] Input tidak valid! Harap masukkan angka desimal/bulat.")
  ```
* **Hasil Pengujian Debugging:**  
  Saat user memasukkan huruf `"tujuh"`, aplikasi tidak crash, melainkan menampilkan pesan peringatan ramah dan kembali meminta input yang benar.

---

### Skenario 2: Basis Data Error `sqlite3.IntegrityError` (Duplikasi NIM)
* **Deskripsi Masalah:**  
  Pengguna mendaftarkan mahasiswa baru menggunakan NIM yang sudah tersimpan di basis data SQLite (pelanggaran `UNIQUE constraint` pada kolom `nim`).
* **Gejala / Traceback Asli:**
  ```text
  sqlite3.IntegrityError: UNIQUE constraint failed: mahasiswa.nim
  ```
* **Solusi Penanganan:**  
  1. Melakukan pengecekan pra-input (`defensive check`) di `main.py` menggunakan `cari_mahasiswa_by_nim()`.
  2. Menangkap `sqlite3.IntegrityError` secara spesifik di `database.py`:
  ```python
  try:
      cursor.execute("INSERT INTO mahasiswa ... VALUES (?, ...)", (...))
      conn.commit()
      return True, "Data berhasil disimpan."
  except sqlite3.IntegrityError:
      return False, f"Gagal: Mahasiswa dengan NIM '{mhs.nim}' sudah terdaftar!"
  except sqlite3.Error as e:
      return False, f"Kesalahan Database: {e}"
  ```
* **Hasil Pengujian Debugging:**  
  Sistem berhasil menolak duplikasi data dengan pesan jelas tanpa membuat koneksi database *corrupt*.

---

### Skenario 3: Penanganan Enkapsulasi Nilai Tak Wajar (< 0 atau > 100)
* **Deskripsi Masalah:**  
  Nilai akademik tidak boleh berupa angka negatif (misal `-15`) atau melebihi 100 (misal `150`).
* **Solusi Penanganan:**  
  Penerapan validasi pada level setter di class `Mahasiswa` (`models.py`):
  ```python
  @nilai_tugas.setter
  def nilai_tugas(self, value: float):
      if not (0.0 <= value <= 100.0):
          raise ValueError("Nilai Tugas harus berada di antara 0 dan 100.")
      self._nilai_tugas = float(value)
  ```
* **Hasil Pengujian Debugging:**  
  Percobaan modifikasi atribut dengan angka abnormal otomatis ditolak dan divalidasi lewat unit test `TC-10`.

---

### Skenario 4: Pembagian dengan Nol (`ZeroDivisionError`) pada Statistik
* **Deskripsi Masalah:**  
  Jika menu statistik diakses saat basis data masih kosong (0 baris), operasi `rata_rata = sum(nilai) / len(daftar)` memicu `ZeroDivisionError: division by zero`.
* **Solusi Penanganan:**  
  Pemeriksaan awal di `menu_statistik()`:
  ```python
  daftar = ambil_semua_mahasiswa()
  if not daftar:
      print("[!] Belum ada data mahasiswa untuk dihitung.")
      return
  ```
* **Hasil Pengujian Debugging:**  
  Aplikasi menampilkan notifikasi informatif alih-alih melempar error.

---

## 3. Langkah-Langkah Debugging Menggunakan Breakpoint (Visual Studio Code / IDE)

Berikut adalah prosedur standar pengujian kode menggunakan fitur breakpoint:
1. **Memasang Breakpoint:**  
   Buka file `02_SourceCode/project/utils.py`. Klik pada nomor baris di samping baris `hasil = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)` hingga muncul titik merah (*red dot* / F9).
2. **Menjalankan Sesi Debug:**  
   Tekan **F5** pada VS Code (atau jalankan script test via debugger).
3. **Pemeriksaan Nilai Variabel (*Watch & Variables Window*):**  
   Saat eksekusi berhenti pada breakpoint, periksa panel **Variables**:
   - `tugas` = `85.0`
   - `uts` = `90.0`
   - `uas` = `88.0`
4. **Navigasi Langkah (*Step Over & Step Into*):**  
   - Tekan **F10** (*Step Over*) untuk mengeksekusi satu baris dan melihat nilai variabel `hasil` yang terhitung `87.7`.
   - Tekan **F5** (*Continue*) untuk melanjutkan program hingga selesai.

---

## 4. Kesimpulan Hasil Debugging
Seluruh skenario kegagalan (*failure modes*) telah diidentifikasi dan ditangani dengan mekanisme pencegahan yang tepat. Program teruji stabil dan siap untuk proses asesmen kompetensi.
