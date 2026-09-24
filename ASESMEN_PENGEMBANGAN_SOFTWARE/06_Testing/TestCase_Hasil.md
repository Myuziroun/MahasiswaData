# TABEL HASIL PENGUJIAN UNIT (UNIT TEST CASE MATRIX)
**Sistem Manajemen Data Mahasiswa & Nilai (SIMAMA)**  
*Skema Sertifikasi: Software Development (BNSP)*

| ID Test Case | Modul / Fitur | Deskripsi Skenario | Data Masukan (Input) | Hasil yang Diharapkan | Hasil Pengamatan | Status |
|:---:|:---|:---|:---|:---|:---|:---:|
| **TC-01** | Kalkulasi Nilai | Hitung bobot 30% Tugas, 30% UTS, 40% UAS | Tugas: 85, UTS: 90, UAS: 88 | Nilai Akhir = 87.70 | Nilai Akhir = 87.70 | **PASS** |
| **TC-02** | Logika Grade A | Verifikasi nilai batas atas $\ge$ 85 | Nilai Akhir = 85.0, 92.5, 100.0 | Grade = 'A' | Grade = 'A' | **PASS** |
| **TC-03** | Logika Grade B | Verifikasi rentang 70.0 $\le$ Nilai < 85.0 | Nilai Akhir = 70.0, 79.9, 84.99 | Grade = 'B' | Grade = 'B' | **PASS** |
| **TC-04** | Logika Grade C | Verifikasi rentang 55.0 $\le$ Nilai < 70.0 | Nilai Akhir = 55.0, 65.0, 69.9 | Grade = 'C' | Grade = 'C' | **PASS** |
| **TC-05** | Logika Grade D | Verifikasi rentang 40.0 $\le$ Nilai < 55.0 | Nilai Akhir = 40.0, 48.5, 54.9 | Grade = 'D' | Grade = 'D' | **PASS** |
| **TC-06** | Logika Grade E | Verifikasi nilai di bawah 40.0 | Nilai Akhir = 39.9, 20.0, 0.0 | Grade = 'E' | Grade = 'E' | **PASS** |
| **TC-07** | Status Kelulusan | Evaluasi status LULUS / TIDAK LULUS | Grade A, B, C $\to$ Lulus; D, E $\to$ Tidak | Lulus untuk A/B/C, Tidak untuk D/E | Sesuai ekspektasi | **PASS** |
| **TC-08** | Validasi NIM | Cek format NIM alfanumerik panjang 5-20 | Valid: '2024001', Invalid: '123', '' | True untuk valid, False untuk invalid | Sesuai ekspektasi | **PASS** |
| **TC-09** | Validasi Nilai | Rentang angka valid harus [0.0 - 100.0] | Input: -5.0 (negatif), 105.0 (overflow) | False (Ditolak) | False (Ditolak) | **PASS** |
| **TC-10** | OOP Enkapsulasi | Pencegahan input atribut invalid via setter | mhs.nilai_tugas = 150.0 / -10.0 | Memunculkan ValueError | ValueError dimunculkan | **PASS** |

### Ringkasan Eksekusi Unit Test:
- Total Uji: 10
- Sukses (Passed): 10 (100%)
- Gagal (Failed): 0 (0%)
- Waktu Eksekusi: 0.001 detik
- Alat Pengujian: `unittest` (Python Standard Library)
