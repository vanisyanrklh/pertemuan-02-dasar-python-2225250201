# Program menghitung luas dan keliling persegi panjang
# Algoritma dan Pemrograman | S1 Pendidikan Matematika FKIP Untirta | 2026/2027 Ganjil

def hitung_luas(panjang, lebar):
    return panjang * lebar

def hitung_keliling(panjang, lebar):
    return 2 * (panjang + lebar)

# Input dari pengguna
panjang = float(input("Masukkan panjang (cm): "))
lebar = float(input("Masukkan lebar (cm): "))

# Proses
luas = hitung_luas(panjang, lebar)
keliling = hitung_keliling(panjang, lebar)
print(f"Keliling persegi panjang = {keliling:.2f} cm")

# Output dengan format 2 angka desimal
print(f"Luas persegi panjang = {luas:.2f} cm²")
print(f"Keliling persegi panjang = {keliling:.2f} cm")
