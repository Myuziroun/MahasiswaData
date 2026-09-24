"""
Module: main.py
Deskripsi: Entry point aplikasi CLI Sistem Manajemen Data Mahasiswa & Nilai
Unit Kompetensi: Pemrograman Terstruktur, Clean Code, OOP, CRUD & Debugging
"""

import sys
import os

# Memastikan modul lokal dapat diimpor dengan benar
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import Mahasiswa
from database import (
    init_db,
    seed_contoh_data,
    tambah_mahasiswa,
    ambil_semua_mahasiswa,
    cari_mahasiswa_by_nim,
    cari_mahasiswa,
    ubah_mahasiswa,
    hapus_mahasiswa
)
from utils import (
    validasi_nim,
    validasi_teks,
    input_float,
    format_tabel
)


def header_aplikasi():
    """Menampilkan header aplikasi."""
    print("=" * 65)
    print("   SISTEM MANAJEMEN DATA MAHASISWA & TRANSKRIP NILAI (SIMAMA)   ")
    print("       Aplikasi Sertifikasi Kompetensi Software Development      ")
    print("=" * 65)


def tampilkan_daftar_tabel(daftar_mhs: list):
    """Membantu menampilkan daftar objek Mahasiswa ke dalam format tabel."""
    headers = ["NIM", "Nama Mahasiswa", "Jurusan", "Tugas", "UTS", "UAS", "Akhir", "Grade", "Status"]
    rows = []
    for m in daftar_mhs:
        rows.append([
            m.nim,
            m.nama,
            m.jurusan,
            f"{m.nilai_tugas:.1f}",
            f"{m.nilai_uts:.1f}",
            f"{m.nilai_uas:.1f}",
            f"{m.hitung_nilai_akhir():.2f}",
            m.get_grade(),
            m.get_status()
        ])
    print(format_tabel(headers, rows))


def menu_tampilkan():
    """Fitur 1: Menampilkan seluruh data mahasiswa."""
    print("\n--- [1] DAFTAR SELURUH MAHASISWA ---")
    daftar = ambil_semua_mahasiswa()
    tampilkan_daftar_tabel(daftar)
    print(f"Total data mahasiswa: {len(daftar)} orang.\n")


def menu_tambah():
    """Fitur 2: Menambahkan data mahasiswa baru."""
    print("\n--- [2] TAMBAH DATA MAHASISWA BARU ---")
    
    # Validasi input NIM
    while True:
        nim = input("Masukkan NIM (5-20 karakter alfanumerik) : ").strip()
        if not validasi_nim(nim):
            print("[!] Format NIM tidak valid! Minimal 5 karakter alfanumerik.")
            continue
        # Cek apakah NIM sudah ada
        ada = cari_mahasiswa_by_nim(nim)
        if ada:
            print(f"[!] NIM '{nim}' sudah digunakan oleh '{ada.nama}'. Gunakan NIM lain.")
            continue
        break

    # Validasi input Nama
    while True:
        nama = input("Masukkan Nama Lengkap                    : ").strip()
        if validasi_teks(nama, min_len=2):
            break
        print("[!] Nama tidak boleh kosong (minimal 2 karakter).")

    # Validasi input Jurusan
    while True:
        jurusan = input("Masukkan Program Studi / Jurusan         : ").strip()
        if validasi_teks(jurusan, min_len=2):
            break
        print("[!] Jurusan tidak boleh kosong.")

    # Input Nilai menggunakan input_float aman
    print("--- Input Nilai Akademik (0.0 - 100.0) ---")
    tugas = input_float("Nilai Tugas (30%) : ")
    uts = input_float("Nilai UTS   (30%) : ")
    uas = input_float("Nilai UAS   (40%) : ")

    # Buat objek Mahasiswa (OOP)
    mhs_baru = Mahasiswa(
        nim=nim,
        nama=nama,
        jurusan=jurusan,
        nilai_tugas=tugas,
        nilai_uts=uts,
        nilai_uas=uas
    )

    # Simpan ke Database
    sukses, pesan = tambah_mahasiswa(mhs_baru)
    if sukses:
        print(f"\n[SUKSES] {pesan}")
        print("Detail: " + mhs_baru.info())
    else:
        print(f"\n[GAGAL] {pesan}")


def menu_cari():
    """Fitur 3: Mencari mahasiswa berdasarkan kata kunci (NIM, Nama, Jurusan)."""
    print("\n--- [3] CARI MAHASISWA ---")
    keyword = input("Masukkan kata kunci pencarian (NIM / Nama / Jurusan): ").strip()
    if not keyword:
        print("[!] Kata kunci tidak boleh kosong.")
        return

    hasil = cari_mahasiswa(keyword)
    print(f"\nHasil pencarian untuk '{keyword}':")
    tampilkan_daftar_tabel(hasil)
    print(f"Ditemukan {len(hasil)} data yang cocok.\n")


def menu_ubah():
    """Fitur 4: Mengubah data mahasiswa yang ada."""
    print("\n--- [4] UBAH DATA MAHASISWA ---")
    nim = input("Masukkan NIM mahasiswa yang ingin diubah: ").strip()
    mhs = cari_mahasiswa_by_nim(nim)
    if not mhs:
        print(f"[!] Mahasiswa dengan NIM '{nim}' tidak ditemukan.")
        return

    print("\nData saat ini:")
    print(f"1. Nama        : {mhs.nama}")
    print(f"2. Jurusan     : {mhs.jurusan}")
    print(f"3. Nilai Tugas : {mhs.nilai_tugas}")
    print(f"4. Nilai UTS   : {mhs.nilai_uts}")
    print(f"5. Nilai UAS   : {mhs.nilai_uas}")
    print("(Tekan ENTER langsung jika tidak ingin mengubah kolom tertentu)")

    nama_baru = input(f"Nama baru [{mhs.nama}]: ").strip()
    if nama_baru:
        mhs.nama = nama_baru

    jurusan_baru = input(f"Jurusan baru [{mhs.jurusan}]: ").strip()
    if jurusan_baru:
        mhs.jurusan = jurusan_baru

    tugas_raw = input(f"Nilai Tugas baru [{mhs.nilai_tugas}]: ").strip()
    if tugas_raw:
        try:
            val = float(tugas_raw)
            if 0 <= val <= 100:
                mhs.nilai_tugas = val
            else:
                print("[!] Nilai harus 0-100. Nilai lama dipertahankan.")
        except ValueError:
            print("[!] Format salah. Nilai lama dipertahankan.")

    uts_raw = input(f"Nilai UTS baru [{mhs.nilai_uts}]: ").strip()
    if uts_raw:
        try:
            val = float(uts_raw)
            if 0 <= val <= 100:
                mhs.nilai_uts = val
            else:
                print("[!] Nilai harus 0-100. Nilai lama dipertahankan.")
        except ValueError:
            print("[!] Format salah. Nilai lama dipertahankan.")

    uas_raw = input(f"Nilai UAS baru [{mhs.nilai_uas}]: ").strip()
    if uas_raw:
        try:
            val = float(uas_raw)
            if 0 <= val <= 100:
                mhs.nilai_uas = val
            else:
                print("[!] Nilai harus 0-100. Nilai lama dipertahankan.")
        except ValueError:
            print("[!] Format salah. Nilai lama dipertahankan.")

    sukses, pesan = ubah_mahasiswa(mhs)
    if sukses:
        print(f"\n[SUKSES] {pesan}")
        print("Data terbaru: " + mhs.info())
    else:
        print(f"\n[GAGAL] {pesan}")


def menu_hapus():
    """Fitur 5: Menghapus data mahasiswa berdasarkan NIM."""
    print("\n--- [5] HAPUS DATA MAHASISWA ---")
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ").strip()
    mhs = cari_mahasiswa_by_nim(nim)
    if not mhs:
        print(f"[!] Mahasiswa dengan NIM '{nim}' tidak ditemukan.")
        return

    print(f"Data yang akan dihapus: {mhs.nim} - {mhs.nama} ({mhs.jurusan})")
    konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/N): ").strip().lower()
    if konfirmasi == "y":
        sukses, pesan = hapus_mahasiswa(nim)
        if sukses:
            print(f"[SUKSES] {pesan}")
        else:
            print(f"[GAGAL] {pesan}")
    else:
        print("[BATAL] Penghapusan data dibatalkan.")


def menu_statistik():
    """Fitur 6: Menghitung statistik dan ringkasan nilai kelas."""
    print("\n--- [6] STATISTIK & RINGKASAN KELAS ---")
    daftar = ambil_semua_mahasiswa()
    if not daftar:
        print("[!] Belum ada data mahasiswa untuk dihitung.")
        return

    nilai_akhir_list = [m.hitung_nilai_akhir() for m in daftar]
    lulus_count = sum(1 for m in daftar if m.get_status() == "LULUS")
    tidak_lulus_count = len(daftar) - lulus_count
    
    rata_rata = sum(nilai_akhir_list) / len(nilai_akhir_list)
    nilai_tertinggi = max(nilai_akhir_list)
    nilai_terendah = min(nilai_akhir_list)

    print("=" * 45)
    print(f" Total Mahasiswa Terdaftar : {len(daftar)} orang")
    print(f" Rata-rata Nilai Akhir     : {rata_rata:.2f}")
    print(f" Nilai Akhir Tertinggi     : {nilai_tertinggi:.2f}")
    print(f" Nilai Akhir Terendah      : {nilai_terendah:.2f}")
    print(f" Jumlah Mahasiswa Lulus    : {lulus_count} orang ({(lulus_count/len(daftar)*100):.1f}%)")
    print(f" Jumlah Tidak Lulus        : {tidak_lulus_count} orang ({(tidak_lulus_count/len(daftar)*100):.1f}%)")
    print("=" * 45)


def main():
    """Fungsi utama program - loop menu interaktif terstruktur."""
    # Inisialisasi basis data dan data contoh
    init_db()
    seed_contoh_data()

    while True:
        header_aplikasi()
        print("[1] Tampilkan Semua Mahasiswa")
        print("[2] Tambah Mahasiswa Baru")
        print("[3] Cari Mahasiswa (NIM / Nama / Jurusan)")
        print("[4] Ubah Data Mahasiswa")
        print("[5] Hapus Data Mahasiswa")
        print("[6] Statistik Nilai Kelas")
        print("[0] Keluar Aplikasi")
        print("=" * 65)

        pilihan = input("Pilih menu [0-6]: ").strip()

        if pilihan == "1":
            menu_tampilkan()
        elif pilihan == "2":
            menu_tambah()
        elif pilihan == "3":
            menu_cari()
        elif pilihan == "4":
            menu_ubah()
        elif pilihan == "5":
            menu_hapus()
        elif pilihan == "6":
            menu_statistik()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan sistem ini. Sampai jumpa!")
            sys.exit(0)
        else:
            print("\n[!] Pilihan tidak valid! Masukkan angka antara 0 sampai 6.\n")

        input("Tekan ENTER untuk kembali ke menu utama...")
        print("\n" * 2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh pengguna. Sampai jumpa!")
        sys.exit(0)
