# Program konversi suhu Celsius ke Fahrenheit dan Kelvin
# Algoritma dan Pemrograman | S1 Pendidikan Matematika FKIP Untirta | 2026/2027 Ganjil

KELVIN_OFFSET = 273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + KELVIN_OFFSET

# Input dari pengguna
celsius = float(input("Masukkan suhu dalam Celsius: "))

# Proses konversi
fahrenheit = celsius_to_fahrenheit(celsius)
kelvin = celsius_to_kelvin(celsius)

# Output dengan format 2 angka desimal
print(f"Suhu dalam Fahrenheit = {fahrenheit:.2f} °F")
print(f"Suhu dalam Kelvin = {kelvin:.2f} K")
