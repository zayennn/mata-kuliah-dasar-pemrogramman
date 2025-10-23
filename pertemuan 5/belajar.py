mapel = [ 'matematika', 'fisika', 'kimia']
# iterasi list menggunakan indeks
for i in range(len(mapel)):
    print("Saya suka", mapel[i])
    
    
    
# ======================================


count = 0

while ( count < 5 ) :
    print('count is : ', count + 1)
    count += 1
print('good bye!')



# ======================================


text = "PemrogrammanPython"

for tulisan in text :
    print(tulisan)
    
    
    
# ======================================

ulang = int(input("Masukkan jumlah data yang ingin diinput: "))

for i in range(ulang):
    print("Data Ke - " + str(i + 1))
    nama = input("Masukkan Nim anda : ")
    uts = int(input("Masukkan Nilai UTS anda : "))
    uas = int(input("Masukkan Nilai UAS anda : "))
    print("NIM anda adalah %s nilai UTS anda %i nilai UAS anda %i" % (nama, uts, uas))
    print("----------------------------------------\n")
