"""
Module: utils.py
Deskripsi: Berisi fungsi validasi input, kalkulasi nilai/grade, dan utilitas tampilan
Unit Kompetensi: Pemrograman Terstruktur, Library / Pre-Existing, Clean Code & Debugging
"""

import os
import re

def hitung_nilai_akhir(tugas: float, uts: float, uas: float) -> float:
    """
    Menghitung nilai akhir berbasis bobot:
    30% Tugas + 30% UTS + 40% UAS.
    """
    hasil = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)
    return round(hasil, 2)


def tentukan_grade(nilai_akhir: float) -> str:
    """
    Menentukan predikat grade huruf (A, B, C, D, E) berdasarkan nilai akhir.
    Menggunakan percabangan terstruktur (if-elif-else).
    """
    if nilai_akhir >= 85.0:
        return "A"
    elif nilai_akhir >= 70.0:
        return "B"
    elif nilai_akhir >= 55.0:
        return "C"
    elif nilai_akhir >= 40.0:
        return "D"
    else:
        return "E"


def tentukan_status(grade: str) -> str:
    """
    Menentukan status kelulusan berdasarkan grade:
    - A, B, C = LULUS
    - D, E    = TIDAK LULUS
    """
    if grade.upper() in ["A", "B", "C"]:
        return "LULUS"
    return "TIDAK LULUS"


def validasi_nim(nim: str) -> bool:
    """
    Validasi format NIM:
    - Tidak boleh kosong
    - Terdiri dari 5 hingga 20 karakter alfanumerik (umumnya digit/angka)
    """
    if not nim or not isinstance(nim, str):
        return False
    nim_clean = nim.strip()
    return bool(re.match(r"^[A-Za-z0-9]{5,20}$", nim_clean))


def validasi_nilai(nilai: float) -> bool:
    """
    Validasi rentang nilai:
    - Harus bernilai antara 0.0 sampai dengan 100.0
    """
    try:
        val = float(nilai)
        return 0.0 <= val <= 100.0
    except (ValueError, TypeError):
        return False


def validasi_teks(teks: str, min_len: int = 1) -> bool:
    """Memvalidasi bahwa string tidak kosong dan memenuhi panjang minimum."""
    if not teks or not isinstance(teks, str):
        return False
    return len(teks.strip()) >= min_len


def input_float(prompt: str, min_val: float = 0.0, max_val: float = 100.0) -> float:
    """
    Membaca input float dari user secara aman dengan penanganan kesalahan (try-except).
    Mencegah crash aplikasi saat user salah mengetikkan huruf/simbol.
    """
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if min_val <= val <= max_val:
                return round(val, 2)
            print(f"[!] Nilai harus berada dalam rentang {min_val} sampai {max_val}. Coba lagi.")
        except ValueError:
            print("[!] Input tidak valid! Harap masukkan angka desimal/bulat (contoh: 85 atau 78.5).")


def format_tabel(headers: list, data: list) -> str:
    """
    Menghasilkan tampilan tabel ASCII yang rapi tanpa memerlukan library eksternal.
    Menjamin program dapat berjalan 100% di semua lingkungan Python.
    """
    if not headers:
        return ""

    str_data = [[str(cell) for cell in row] for row in data]
    col_widths = [len(h) for h in headers]

    for row in str_data:
        for idx, cell in enumerate(row):
            if idx < len(col_widths):
                col_widths[idx] = max(col_widths[idx], len(cell))
            else:
                col_widths.append(len(cell))

    # Garis pemisah horizontal
    def separator(sep_char="-", cross_char="+"):
        parts = [sep_char * (w + 2) for w in col_widths]
        return cross_char + cross_char.join(parts) + cross_char

    # Format baris
    def format_row(row_cells):
        padded = [f" {str(cell).ljust(col_widths[i])} " for i, cell in enumerate(row_cells)]
        return "|" + "|".join(padded) + "|"

    lines = [
        separator("=", "+"),
        format_row(headers),
        separator("=", "+")
    ]

    if not str_data:
        empty_msg = "(Tidak ada data untuk ditampilkan)"
        total_width = sum(col_widths) + (3 * len(col_widths)) - 1
        lines.append(f"| {empty_msg.center(total_width - 2)} |")
    else:
        for row in str_data:
            lines.append(format_row(row))

    lines.append(separator("-", "+"))
    return "\n".join(lines)


def bersihkan_layar():
    """Membersihkan tampilan terminal console."""
    os.system("cls" if os.name == "nt" else "clear")
