"""
Module: models.py
Deskripsi: Berisi implementasi class Berorientasi Objek (OOP)
Unit Kompetensi: Pemrograman Berorientasi Objek (OOP) & Clean Code
"""

class Person:
    """
    Class induk (Parent Class) yang merepresentasikan entitas dasar seseorang.
    Menerapkan prinsip Enkapsulasi (Encapsulation).
    """

    def __init__(self, nama: str):
        self._nama = nama.strip()

    @property
    def nama(self) -> str:
        """Getter untuk atribut nama."""
        return self._nama

    @nama.setter
    def nama(self, nilai: str):
        """Setter untuk atribut nama dengan validasi sederhana."""
        if not nilai or not nilai.strip():
            raise ValueError("Nama tidak boleh kosong.")
        self._nama = nilai.strip()

    def info(self) -> str:
        """
        Method polimorfik untuk menampilkan informasi dasar entitas.
        Akan di-override oleh class turunan (Polymorphism).
        """
        return f"Nama: {self._nama}"


class Mahasiswa(Person):
    """
    Class anak (Child Class) yang mewarisi class Person.
    Menyimpan data akademik mahasiswa beserta nilai dan hasil evaluasi.
    """

    def __init__(
        self,
        nim: str,
        nama: str,
        jurusan: str,
        nilai_tugas: float = 0.0,
        nilai_uts: float = 0.0,
        nilai_uas: float = 0.0,
        id_db: int = None
    ):
        # Memanggil konstruktor class induk (Inheritance)
        super().__init__(nama)
        
        self.id_db = id_db
        self._nim = nim.strip()
        self._jurusan = jurusan.strip()
        self._nilai_tugas = float(nilai_tugas)
        self._nilai_uts = float(nilai_uts)
        self._nilai_uas = float(nilai_uas)

    # --- Property Getter & Setter (Encapsulation) ---

    @property
    def nim(self) -> str:
        return self._nim

    @nim.setter
    def nim(self, value: str):
        if not value or not value.strip():
            raise ValueError("NIM tidak boleh kosong.")
        self._nim = value.strip()

    @property
    def jurusan(self) -> str:
        return self._jurusan

    @jurusan.setter
    def jurusan(self, value: str):
        if not value or not value.strip():
            raise ValueError("Jurusan tidak boleh kosong.")
        self._jurusan = value.strip()

    @property
    def nilai_tugas(self) -> float:
        return self._nilai_tugas

    @nilai_tugas.setter
    def nilai_tugas(self, value: float):
        if not (0.0 <= value <= 100.0):
            raise ValueError("Nilai Tugas harus berada di antara 0 dan 100.")
        self._nilai_tugas = float(value)

    @property
    def nilai_uts(self) -> float:
        return self._nilai_uts

    @nilai_uts.setter
    def nilai_uts(self, value: float):
        if not (0.0 <= value <= 100.0):
            raise ValueError("Nilai UTS harus berada di antara 0 dan 100.")
        self._nilai_uts = float(value)

    @property
    def nilai_uas(self) -> float:
        return self._nilai_uas

    @nilai_uas.setter
    def nilai_uas(self, value: float):
        if not (0.0 <= value <= 100.0):
            raise ValueError("Nilai UAS harus berada di antara 0 dan 100.")
        self._nilai_uas = float(value)

    # --- Logika Perhitungan Nilai & Status ---

    def hitung_nilai_akhir(self) -> float:
        """
        Menghitung nilai akhir dengan bobot:
        - Tugas : 30% (0.30)
        - UTS   : 30% (0.30)
        - UAS   : 40% (0.40)
        """
        akhir = (0.30 * self._nilai_tugas) + (0.30 * self._nilai_uts) + (0.40 * self._nilai_uas)
        return round(akhir, 2)

    def get_grade(self) -> str:
        """
        Menentukan predikat grade huruf berdasarkan nilai akhir:
        - A: 85 - 100
        - B: 70 - 84.99
        - C: 55 - 69.99
        - D: 40 - 54.99
        - E: < 40
        """
        akhir = self.hitung_nilai_akhir()
        if akhir >= 85.0:
            return "A"
        elif akhir >= 70.0:
            return "B"
        elif akhir >= 55.0:
            return "C"
        elif akhir >= 40.0:
            return "D"
        else:
            return "E"

    def get_status(self) -> str:
        """
        Menentukan status kelulusan mahasiswa:
        - Grade A, B, C dinyatakan LULUS
        - Grade D, E dinyatakan TIDAK LULUS
        """
        return "LULUS" if self.get_grade() in ["A", "B", "C"] else "TIDAK LULUS"

    # --- Polymorphism ---

    def info(self) -> str:
        """Override method info dari class induk Person (Polymorphism)."""
        return (
            f"NIM: {self._nim} | Nama: {self._nama} | Jurusan: {self._jurusan} | "
            f"Nilai Akhir: {self.hitung_nilai_akhir()} ({self.get_grade()}) - {self.get_status()}"
        )

    def to_dict(self) -> dict:
        """Mengonversi data mahasiswa menjadi dictionary."""
        return {
            "nim": self._nim,
            "nama": self._nama,
            "jurusan": self._jurusan,
            "nilai_tugas": self._nilai_tugas,
            "nilai_uts": self._nilai_uts,
            "nilai_uas": self._nilai_uas,
            "nilai_akhir": self.hitung_nilai_akhir(),
            "grade": self.get_grade(),
            "status": self.get_status()
        }
