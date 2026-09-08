# Program menghitung nilai akhir mahasiswa
# Algoritma dan Pemrograman | S1 Pendidikan Matematika FKIP Untirta | 2026/2027 Ganjil

def hitung_nilai_akhir(tugas, uts, uas):
    return (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

# Input dari pengguna
nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# Proses
nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

# Output
print(f"Nama Mahasiswa: {nama}")
print(f"Nilai Akhir: {nilai_akhir:.2f}")
