"""
Kalkulator Koordinat
Algoritma dan Pemrograman | S1 Pendidikan Matematika FKIP Untirta | 2026/2027 Ganjil
Nama  : Van
NIM   : (isi dengan NIM kamu)
Tugas : Kuis 1 - Praktik
"""

# Input koordinat titik A dan B
x1 = float(input("Masukkan koordinat x1 (titik A): "))
y1 = float(input("Masukkan koordinat y1 (titik A): "))
x2 = float(input("Masukkan koordinat x2 (titik B): "))
y2 = float(input("Masukkan koordinat y2 (titik B): "))

# Perhitungan dx dan dy
dx = x2 - x1
dy = y2 - y1

# Jarak Euclidean
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

# Titik tengah
titik_tengah_x = (x1 + x2) / 2
titik_tengah_y = (y1 + y2) / 2

# Output dengan dua angka desimal
print(f"Titik A = ({x1:.2f}, {y1:.2f})")
print(f"Titik B = ({x2:.2f}, {y2:.2f})")
print(f"Perubahan dx = {dx:.2f}")
print(f"Perubahan dy = {dy:.2f}")
print(f"Jarak Euclidean = {jarak:.2f}")
print(f"Titik tengah = ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")
