# Program menghitung total gaji karyawan PT. Dingin Damai
gaji_pokok = 300000

golongan = int(input("Masukkan golongan (1/2/3): "))
pendidikan = input("Masukkan pendidikan (SMA/D1/D3/S1): ").upper()
jam_kerja = int(input("Masukkan jumlah jam kerja: "))

# Hitung tunjangan jabatan
if golongan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == 3:
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0
    
# Hitung tunjangan pendidikan
if pendidikan == "SMA":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "S1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0
    
# Hitung honor lembur
if jam_kerja > 8:
    lembur = (jam_kerja - 8) * 3500
else:
    lembur = 0

# Hitung total gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + lembur

# Tampilkan hasil
print("\n=== RINCIAN GAJI KARYAWAN ===")
print(f"Gaji Pokok           : Rp {gaji_pokok}")
print(f"Tunjangan Jabatan    : Rp {tunjangan_jabatan}")
print(f"Tunjangan Pendidikan : Rp {tunjangan_pendidikan}")
print(f"Honor Lembur         : Rp {lembur}")
print("--------------------------------")
print(f"Total Gaji           : Rp {total_gaji}")