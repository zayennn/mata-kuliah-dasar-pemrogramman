while True :
    
    print(f"""
    ============ daftar menu ============
    1. lihat akun
    2. bikin akun
    3. tambah alamat
    4. keluar
    """)
    
    my_alamat = []
    
    user_choice = int(input('masukan angka daftar menu : '))
    
    if user_choice == 1 :
        if my_alamat :
            for i in range(my_alamat) :
                print()
        else :
            print('data kosong, isi datamu terlebih dahulu')
            
        
    elif user_choice == 2 :
        username = input('masukan nama anda : ').capitalize()
        alamat = input('masukan alamat anda : ')
        
        user_account = [username, alamat]
        my_alamat.append(user_account)
        print('data berhasil di tambahkan!')
        
    elif user_choice == 3 :
        alamat = input('tambahkan alamat anda : ')
        my_alamat[1].append(alamat)
        print('alamat berhasil di tambahkan!')
    
    elif user_choice == 4 :
        print('program telah berhenti')
        break
    
    else :
        print('masukan input yang valid')