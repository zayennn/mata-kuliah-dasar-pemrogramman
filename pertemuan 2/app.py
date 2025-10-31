print("========= latihan 1 =========\n")
product = input("masukin nama product: ")
harga_per_item = int(input("masukin harga per item: "))
jumlah_terjual = int(input("jumlah terjual:"))

total_harga = harga_per_item * jumlah_terjual

print(
    f"""
nama product         : {product}
harga per item       : {harga_per_item}
jumlah terjual       : {jumlah_terjual}
total harga          : {total_harga}
"""
)

print("========= latihan 2 =========\n")

nim = int(input("masukin nim: "))
nama = input("masukin nama: ")
jurusan = input("masukin jurusan: ")
alamat = input("masukin alamat: ")

print(
    f"""
nim kamu adalah      : {nim} 
nama kamu adalah     : {nama}
jurusan kamu adalah  : {jurusan}
alamat kamu di       : {alamat}
"""
)
