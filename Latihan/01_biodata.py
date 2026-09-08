# biodata.py

# Konstanta tahun sekarang
TAHUN_SEKARANG = 2026

# Input data biodata
nama = input("Masukkan Nama: ")
NIM = input("Masukkan NIM: ")
kelas = input("Masukkan Kelas: ")
tahun_lahir = int(input("Masukkan Tahun Lahir: "))

# Hitung umur
umur = TAHUN_SEKARANG - tahun_lahir

# Tampilkan kartu biodata dengan f-string
print(f"""
=============================
        KARTU BIODATA
=============================
Nama        : {nama}
NIM         : {NIM}
Kelas       : {kelas}
Tahun Lahir : {tahun_lahir}
Umur        : {umur} tahun
=============================
""")