class Mahasiswa() :
    def __init__(self, name, nis, code_major, price):
        self.name = name
        self.nis = nis
        self.code_major = code_major
        self.price = price
        
    def info(self):
        print(f"""name : {self.name}
nis : {self.nis}
major : {self.code_major}
price : {self.price}""")

mahasiswa = input("Masukkan nama mahasiswa : ").capitalize()
nis = input("Masukkan NIS mahasiswa : ")
code_major = input("Masukkan jurusan mahasiswa (SI/SIA) : ").upper()

if code_major == "SI" :
    price = 2400000
    data_mahasiswa = Mahasiswa(mahasiswa, nis, code_major, price)
    data_mahasiswa.info()
elif code_major == "SIA" :
    price = 2000000
    data_mahasiswa = Mahasiswa(mahasiswa, nis, code_major, price)
    data_mahasiswa.info()
else :
    print('Jurusan tidak ditemukan')