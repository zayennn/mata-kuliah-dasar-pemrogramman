# =================== Studi Kasus ===================
pembeli=input("Input Nama Pembeli : ")
no_hp=input("Input No. Handphone : ")
jurusan=input("Input Jurusan [SBY/BL/LMP] : ")

if jurusan=="SBY":
	namajurusan="Surabaya"
	harga=300000
elif jurusan=="BL":
	namajurusan="Bali"
	harga=350000
else:
	namajurusan="Lampung"
	harga=500000

jumlah=int(input("Masukkan Jumlah Beli : "))

if jumlah>=3 :
	potongan=(jumlah*harga)*0.1
else:
	potongan=0
total=(jumlah*harga)-potongan

print("------------------------------------")
print(" PENJUALAN TIKET BUS")
print(" XYZ")
print("------------------------------------")
print("Nama Pembeli : "+str(pembeli))
print("No. Handphone : "+str(no_hp))
print("Kode Jurusan yang dipilih : "+str(jurusan))
print("Nama Kota Tujuan : "+str(namajurusan))
print("Harga : ",+(harga))
print("Jumlah Beli : ",+(jumlah))
print("------------------------------------")
print("potongan yang didapat : ",+(potongan))
print("Total Bayar : ",+(total))
ubay=int(input("Masukkan Uang Bayar : "))
uangkembali=ubay-total
print("Uang Kembali : ",+uangkembali)