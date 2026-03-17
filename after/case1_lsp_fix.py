class Mahasiswa:
    pass

class MahasiswaAktif(Mahasiswa):
    def presentasi(self):
        print("Mahasiswa aktif sedang presentasi di kelas")

class MahasiswaCuti(Mahasiswa):
    def status(self):
        print("Mahasiswa sedang cuti, tidak mengikuti kegiatan akademik")