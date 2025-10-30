my_alamat = []

while True :
    
    print(f"""
    ============ daftar menu ============
    1. lihat akun
    2. bikin akun
    3. tambah alamat
    4. keluar
    """)
    
    
    user_choice = int(input('masukan angka daftar menu : '))
    
    if user_choice == 1 :
        if my_alamat :
            for i,akun in enumerate(my_alamat, start=1) :
                print(f"{i}. Nama: {akun[0]} | Alamat: {akun[1]}")
        else :
            print('data kosong, isi datamu terlebih dahulu')
            
        
    elif user_choice == 2 :
        username = input('masukan nama anda : ').capitalize()
        alamat = input('masukan alamat anda : ')
        
        user_account = [username, alamat]
        my_alamat.append(user_account)
        print('data berhasil di tambahkan!')
        
    elif user_choice == 3 :
       if my_alamat:
        print("\nPilih akun yang mau ditambah alamat:")
        for i, akun in enumerate(my_alamat, start=1):
            print(f"{i}. {akun[0]} (alamat: {akun[1]})")
        
        pilih = int(input("Masukkan nomor akun: ")) - 1
        if 0 <= pilih < len(my_alamat):
            alamat_baru = input("Tambahkan alamat baru: ")
            my_alamat[pilih][1] += f", {alamat_baru}"
            print("Alamat berhasil ditambahkan!")
        else:
            print("Nomor akun tidak valid.")
    
    elif user_choice == 4 :
        print('program telah berhenti')
        break
    
    else :
        print('masukan input yang valid')