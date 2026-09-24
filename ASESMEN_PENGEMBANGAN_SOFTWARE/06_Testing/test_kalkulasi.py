"""
Module: test_kalkulasi.py
Deskripsi: Pengujian Unit Otomatis (Unit Testing) menggunakan library standard unittest
Unit Kompetensi: Pengujian Unit (Unit Test), Pemrograman Terstruktur, OOP & Debugging
"""

import sys
import os
import unittest

# Menambahkan folder project ke sys.path
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "02_SourceCode", "project"))
sys.path.insert(0, PROJECT_DIR)

from utils import (
    hitung_nilai_akhir,
    tentukan_grade,
    tentukan_status,
    validasi_nim,
    validasi_nilai
)
from models import Person, Mahasiswa


class TestUnitSIMAMA(unittest.TestCase):
    """Kumpulan test case untuk menguji logika bisnis, kalkulasi, dan validasi."""

    def test_tc01_hitung_nilai_akhir(self):
        """TC-01: Memastikan formula bobot (30% tugas + 30% uts + 40% uas) akurat."""
        # Kasus 1: 80, 80, 80 -> 80.0
        self.assertEqual(hitung_nilai_akhir(80.0, 80.0, 80.0), 80.0)
        # Kasus 2: 100, 100, 100 -> 100.0
        self.assertEqual(hitung_nilai_akhir(100.0, 100.0, 100.0), 100.0)
        # Kasus 3: 0, 0, 0 -> 0.0
        self.assertEqual(hitung_nilai_akhir(0.0, 0.0, 0.0), 0.0)
        # Kasus 4: 85, 90, 88 -> 0.3*85 + 0.3*90 + 0.4*88 = 25.5 + 27.0 + 35.2 = 87.7
        self.assertEqual(hitung_nilai_akhir(85.0, 90.0, 88.0), 87.7)

    def test_tc02_penentuan_grade_A(self):
        """TC-02: Memastikan nilai >= 85 menghasilkan grade A."""
        self.assertEqual(tentukan_grade(85.0), "A")
        self.assertEqual(tentukan_grade(92.5), "A")
        self.assertEqual(tentukan_grade(100.0), "A")

    def test_tc03_penentuan_grade_B(self):
        """TC-03: Memastikan rentang nilai 70 <= nilai < 85 menghasilkan grade B."""
        self.assertEqual(tentukan_grade(70.0), "B")
        self.assertEqual(tentukan_grade(79.9), "B")
        self.assertEqual(tentukan_grade(84.99), "B")

    def test_tc04_penentuan_grade_C(self):
        """TC-04: Memastikan rentang nilai 55 <= nilai < 70 menghasilkan grade C."""
        self.assertEqual(tentukan_grade(55.0), "C")
        self.assertEqual(tentukan_grade(65.0), "C")
        self.assertEqual(tentukan_grade(69.9), "C")

    def test_tc05_penentuan_grade_D(self):
        """TC-05: Memastikan rentang nilai 40 <= nilai < 55 menghasilkan grade D."""
        self.assertEqual(tentukan_grade(40.0), "D")
        self.assertEqual(tentukan_grade(48.5), "D")
        self.assertEqual(tentukan_grade(54.9), "D")

    def test_tc06_penentuan_grade_E(self):
        """TC-06: Memastikan nilai < 40 menghasilkan grade E."""
        self.assertEqual(tentukan_grade(39.9), "E")
        self.assertEqual(tentukan_grade(20.0), "E")
        self.assertEqual(tentukan_grade(0.0), "E")

    def test_tc07_status_kelulusan(self):
        """TC-07: Memastikan penentuan status kelulusan (A,B,C Lulus; D,E Tidak Lulus)."""
        self.assertEqual(tentukan_status("A"), "LULUS")
        self.assertEqual(tentukan_status("B"), "LULUS")
        self.assertEqual(tentukan_status("C"), "LULUS")
        self.assertEqual(tentukan_status("D"), "TIDAK LULUS")
        self.assertEqual(tentukan_status("E"), "TIDAK LULUS")

    def test_tc08_validasi_nim(self):
        """TC-08: Menguji validasi format NIM (panjang dan karakter alfanumerik)."""
        # Valid
        self.assertTrue(validasi_nim("2024001"))
        self.assertTrue(validasi_nim("IF20241001"))
        # Invalid: kurang dari 5 karakter
        self.assertFalse(validasi_nim("123"))
        # Invalid: kosong
        self.assertFalse(validasi_nim(""))
        # Invalid: karakter khusus
        self.assertFalse(validasi_nim("2024@001#"))

    def test_tc09_validasi_nilai_rentang(self):
        """TC-09: Menguji validasi rentang nilai harus berada di [0.0 - 100.0]."""
        self.assertTrue(validasi_nilai(0.0))
        self.assertTrue(validasi_nilai(50.5))
        self.assertTrue(validasi_nilai(100.0))
        # Nilai negatif
        self.assertFalse(validasi_nilai(-5.0))
        # Melebihi 100
        self.assertFalse(validasi_nilai(105.0))
        # Tipe data tidak valid
        self.assertFalse(validasi_nilai("bukan_angka"))

    def test_tc10_oop_inheritance_dan_enkapsulasi(self):
        """TC-10: Menguji prinsip OOP Pewarisan, Enkapsulasi, dan Polimorfisme."""
        # Instansiasi objek Mahasiswa
        mhs = Mahasiswa(
            nim="2024999",
            nama="Test User",
            jurusan="Informatika",
            nilai_tugas=80,
            nilai_uts=85,
            nilai_uas=90
        )
        # Memastikan inheritance dari Person
        self.assertIsInstance(mhs, Person)
        self.assertIsInstance(mhs, Mahasiswa)
        self.assertEqual(mhs.nama, "Test User")

        # Menguji enkapsulasi dan setter validation
        with self.assertRaises(ValueError):
            mhs.nilai_tugas = 150.0  # Melebihi batas

        with self.assertRaises(ValueError):
            mhs.nilai_uts = -10.0    # Nilai negatif

        # Menguji perhitungan nilai pada objek
        # 0.3*80 + 0.3*85 + 0.4*90 = 24 + 25.5 + 36 = 85.5
        self.assertEqual(mhs.hitung_nilai_akhir(), 85.5)
        self.assertEqual(mhs.get_grade(), "A")
        self.assertEqual(mhs.get_status(), "LULUS")


if __name__ == "__main__":
    unittest.main(verbosity=2)
