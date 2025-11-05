jumlah_data = int(input("Masukkan Jumlah Data Mahasiswa : "))

nim = []
uts = []
uas = []
rata_rata = []

for i in range (1, jumlah_data + 1):
    print (f"Data ke - {i}")

    nim.append(int(input("Masukkan NIM Anda : ")))
    uts.append (int(input("Masukkan UTS Anda : ")))
    uas.append (int(input("Masukkan UAS Anda : ")))

for z in range (jumlah_data):
    rata = (uas[z] + uts[z]) / 2
    rata_rata.append(rata)


print("===============================================")
print("NIM\t\t| UTS\t| UAS\t| Rata-Rata")
print("===============================================")

for i in range(jumlah_data):
    print(f"{nim[i]}\t| {uts[i]}\t| {uas[i]}\t| {rata_rata[i]}")