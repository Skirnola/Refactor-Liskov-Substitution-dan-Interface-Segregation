from abc import ABC, abstractmethod


class Kuliah(ABC):
    @abstractmethod
    def kuliah(self):
        pass


class MakanKantin(ABC):
    @abstractmethod
    def makan_kantin(self):
        pass


class Organisasi(ABC):
    @abstractmethod
    def ikut_organisasi(self):
        pass


class MahasiswaBiasa(Kuliah, MakanKantin, Organisasi):
    def kuliah(self):
        print("Mahasiswa mengikuti perkuliahan di kampus")

    def makan_kantin(self):
        print("Mahasiswa makan di kantin kampus")

    def ikut_organisasi(self):
        print("Mahasiswa aktif dalam organisasi kampus")


class MahasiswaOnline(Kuliah):
    def kuliah(self):
        print("Mahasiswa mengikuti kuliah secara online dari rumah")