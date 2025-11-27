class Perhitungan :
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def Jumlah(self) :
        print(f"hasil dari {self.a} ditambah {self.b} adalah : {self.a + self.b}")

    def Pengurangan(self) :
        print(f"hasil dari {self.a} ditambah {self.b} adalah : {self.a - self.b}")

    def Perkalian(self) :
        print(f"hasil dari {self.a} ditambah {self.b} adalah : {self.a * self.b}")

    def Pembagian(self) :
        print(f"hasil dari {self.a} ditambah {self.b} adalah : {self.a / self.b}")

    def Pangkat(self) :
        print(f"hasil dari {self.a} ditambah {self.b} adalah : {self.a ** self.b}")
        
penjumlahan_pertama = Perhitungan(10, 10)
penjumlahan_pertama.Jumlah()
penjumlahan_pertama.Pengurangan()
penjumlahan_pertama.Perkalian()
penjumlahan_pertama.Pangkat()