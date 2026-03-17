from abc import ABC, abstractmethod

class Proyektor(ABC):
    @abstractmethod
    def gunakan_proyektor(self):
        pass

class LabKomputer(ABC):
    @abstractmethod
    def gunakan_lab(self):
        pass


class RuangDiskusi(ABC):
    @abstractmethod
    def gunakan_ruang_diskusi(self):
        pass

class KelasBiasa(Proyektor):
    def gunakan_proyektor(self):
        print("Menggunakan proyektor di kelas biasa")

class LabLengkap(Proyektor, LabKomputer, RuangDiskusi):
    def gunakan_proyektor(self):
        print("Menggunakan proyektor di lab")

    def gunakan_lab(self):
        print("Menggunakan komputer di lab")

    def gunakan_ruang_diskusi(self):
        print("Menggunakan ruang diskusi untuk kelompok")