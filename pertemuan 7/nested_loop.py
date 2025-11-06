tabel = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

text_angka = ["Pertama", "Kedua", "Ketiga", "Keempat"]

for baris in range(len(tabel)):
    for kolom in range (len(tabel[baris])):
        print(f"baris {text_angka[baris]}, kolom {text_angka[kolom]} adalah: {tabel[baris][kolom]}")    