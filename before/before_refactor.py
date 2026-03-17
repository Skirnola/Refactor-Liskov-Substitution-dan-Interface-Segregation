# CASE 1 - LSP
class Mahasiswa:
    def presentasi(self):
        print("Mahasiswa sedang presentasi di kelas")

class MahasiswaAktif(Mahasiswa):
    def presentasi(self):
        print("Mahasiswa aktif sedang presentasi dengan baik")

class MahasiswaCuti(Mahasiswa):
    def presentasi(self):
        raise Exception("Mahasiswa cuti tidak mengikuti presentasi")

    
class AktivitasMahasiswa:
    def kuliah(self):
        pass

    def makan_kantin(self):
        pass

    def ikut_organisasi(self):
        pass

# CASE 2 - ISP
class MahasiswaBiasa(AktivitasMahasiswa):
    def kuliah(self):
        print("Mahasiswa mengikuti perkuliahan")

    def makan_kantin(self):
        print("Mahasiswa makan di kantin")

    def ikut_organisasi(self):
        print("Mahasiswa ikut organisasi kampus")


class MahasiswaOnline(AktivitasMahasiswa):
    def kuliah(self):
        print("Mahasiswa mengikuti kuliah online")

    def makan_kantin(self):
        raise Exception("Mahasiswa online tidak ke kantin")

    def ikut_organisasi(self):
        raise Exception("Mahasiswa online tidak ikut organisasi offline")
    
# CASE 3 - ISP + LSP
class FasilitasKampus:
    def proyektor(self):
        pass

    def lab_komputer(self):
        pass

    def ruang_diskusi(self):
        pass


class KelasBiasa(FasilitasKampus):
    def proyektor(self):
        print("Menggunakan proyektor di kelas")

    def lab_komputer(self):
        raise Exception("Tidak ada lab komputer di kelas biasa")

    def ruang_diskusi(self):
        raise Exception("Tidak ada ruang diskusi khusus")