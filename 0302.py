print("Kode Tugas: P0302")
print("NIM: 251080200005")
print("Nama: Najwa Karimah N")

print()
print("Algoritma:")
print("1. Mulai program")
print("2. Masukkan angka yang akan dicari faktornya")
print("3. Siapkan list kosong untuk menyimpan faktor")
print("4. Lakukan perulangan dari 1 sampai angka tersebut")
print("5. Jika angka habis dibagi i, maka simpan i ke dalam list faktor")
print("6. Tampilkan semua faktor")
print("7. Selesai")

print()
print("Pseudocode:")
print("Start")
print("  input number")
print("  factors = []")
print("  for i = 1 to number")
print("      if number mod i = 0 then")
print("          add i to factors")
print("  print factors")
print("Stop")

def faktor(angka):
    hasil = []
    for i in range(1, angka + 1):
        if angka % i == 0:
            hasil.append(i)
    return hasil

print()
print("Hasil:")

angka = int(input("Masukkan angka: "))
print("Faktor dari", angka, "adalah:", faktor(angka))
