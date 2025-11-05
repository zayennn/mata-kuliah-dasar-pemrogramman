class Mahasiswa :
    def __init__( self, nama, nim, uts, uas ):
        self.nama = nama
        self.nim = nim
        self.uts = uts
        self.uas = uas
        
    def rata_nilai( self ) :
        print(f"""
================ data mahasiswa ================

nama mahasiswa       : { self.nama }
nim mahasiswa        : { self.nim }
nilai uts mahasiswa  : { self.uts }
nilai uas mahasiswa  : { self.uas }
nilai rata"          : { ( self.uts + self.uas ) / 2}
""""")
        
        
class Jumlah(Mahasiswa) :
    def __init__(self, nama, nim, uts, uas, total):
        super().__init__(nama, nim, uts, uas)
        self.total = total
    
    def info(self) :
        
        # self.jumlah = 0
        
        for i in range(1, self.total + 1) :
            print(f"""
================ data mahasiswa {i} ================

nama mahasiswa       : { self.nama }
nim mahasiswa        : { self.nim }
nilai uts mahasiswa  : { self.uts }
nilai uas mahasiswa  : { self.uas }
nilai rata"          : { ( self.uts + self.uas ) / 2 }
""""")
        
jumlah_data = input('masukan jumlah data mahasiswa : ')

try :
    jumlah_data = int(jumlah_data)
    
    for i in range( 1, jumlah_data + 1 ) :
        print(f"\n================ input data maha siswa ke - {i} ================\n")
        nama = input('nama mahasiswa : ').capitalize()
        nim = int(input('nim mahasiswa : '))
        nilai_uts = float(input('nilai uts mahasiswa : '))
        nilai_uas = float(input('nilai uas mahasiswa : '))
            
        data_mahasiswa = Jumlah(nama, nim, nilai_uts, nilai_uas, jumlah_data)
        data_mahasiswa.info()
    
except ValueError :
    print('value bukan angka, silahkan isi value dengan angka!')