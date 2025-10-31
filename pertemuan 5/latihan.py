print(
    """
       GEROBAK FRIED CHICKEN
=====================================
Kode | Potongan | Harga 
 D   | Dada      | Rp. 2500
 P   | Paha      | Rp. 2000
 S   | Sayap     | Rp. 1500
=====================================
"""
)

menu = {"D": ("Dada", 2500), "P": ("Paha", 2000), "S": ("Sayap", 1500)}

tax = 0.10

while True:
    jenis_beli = int(input("Masukkan berapa jenis potongan yang dibeli: "))
    if 0 < jenis_beli <= 3:
        break
    print("Jumlah tidak valid! Maksimal 3 jenis potongan (D/P/S)")

data_pesanan = []

for i in range(jenis_beli):
    print(f"\nJenis ke-{i+1}")
    while True:
        kode = input("Masukkan kode potongan (D/P/S): ").strip().upper()
        if kode in menu:
            break
        print("Kode tidak dikenali! Coba lagi.")
    qty = int(input("Masukkan jumlah potongan: "))
    nama, harga = menu[kode]
    total_harga = harga * qty
    data_pesanan.append((nama, harga, qty, total_harga))

print(
    """
                 DETAIL PESANAN ANDA
============================================================
 No | Potongan | Harga Satuan | Jumlah | Total Harga
============================================================
"""
)

total_semua = 0

for i, (nama, harga, qty, total_harga) in enumerate(data_pesanan, start=1):
    print(f"{i:^3}| {nama:^9}| {harga:^13}| {qty:^8}| {total_harga:^12}")
    total_semua += total_harga

ppn = total_semua * tax
grand_total = total_semua + ppn

print("============================================================")
print(f"Total Harga : Rp. {total_semua}")
print(f"PPN (10%)   : Rp. {int(ppn)}")
print(f"Total Bayar : Rp. {int(grand_total)}")
