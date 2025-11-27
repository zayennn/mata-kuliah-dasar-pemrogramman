def Penjumlahan(a, b) :
    print(f"hasil dari {a} ditambah {b} adalah : {a + b}")
    
def Pengurangan(a, b) :
    print(f"hasil dari {a} dikurang {b} adalah : {a - b}")

def Perkalian(a, b) :
    print(f"hasil dari {a} dikali {b} adalah : {a * b}")

def Pembagian(a, b) :
    print(f"hasil dari {a} dikali {b} adalah : {a + b}")

def Pangkat (a, b) :
    print(f"hasil dari {a} dipangkat {b} adalah : {a ** b}")
        
        
print()

num1 = int(input('masukan angka pertama : '))
num2 = int(input('masukan angka kedua : '))

print()

Penjumlahan(num1, num2)
Pengurangan(num1, num2)
Perkalian(num1, num2)
Pangkat(num1, num2)