print("Kode Tugas: P0301")
print("NIM: 251080200005")
print("NAMA: Najwa Karimah N")

print()
print("Algoritma:")
print("1. Mulai program")
print("2. Siapkan daftar angka: 13, 80, 8, 59, 82, 35, 40")
print("3. Untuk setiap angka di dalam daftar:")
print("   - Cek apakah angka tersebut bilangan prima atau bukan")
print("   - Bilangan prima adalah angka yang hanya bisa dibagi oleh 1 dan dirinya sendiri")
print("4. Tampilkan hasil 'Prima' atau 'Bukan Prima' untuk setiap angka")
print("5. Selesai")

print()
print("Pseudocode:")
print("Start")
print("  numbers ← [13, 80, 8, 59, 82, 35, 40]")
print("  For each num in numbers do")
print("      if num < 2 then")
print("          print num, 'Bukan Prima'")
print("      else")
print("          set isPrime = True")
print("          for i = 2 to num - 1 do")
print("              if num mod i = 0 then")
print("                  isPrime = False")
print("                  break")
print("          if isPrime = True then")
print("              print num, 'Prima'")
print("          else")
print("              print num, 'Bukan Prima'")
print("Stop")

def cek_prima(angka):
    if angka < 2:
        return False
    for i in range(2, angka):
        if angka % i == 0:
            return False
    return True

numbers = [13, 80, 8, 59, 82, 35, 40]

print()
print("Hasil Program:")
for num in numbers:
    if cek_prima(num):
        print(num, "= Prima")
    else:
        print(num, "= Bukan Prima")
