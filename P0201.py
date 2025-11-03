print("Kode Tugas: P0201")
print("Nama: Najwa Karimah N")
print("NIM: 251080200005")

print()
print("Algoritma:")
print("1. Mulai")
print("2. Input nilai panjang dan lebar untuk persegi panjang")
print("3. Hitung luas persegi panjang = panjang x lebar")
print("4. Input nilai alas dan tinggi untuk segitiga")
print("5. Hitung luas segitiga = 0.5 x alas x tinggi")
print("6. Input nilai sisi untuk persegi")
print("7. Hitung luas persegi = sisi x sisi")
print("8. Input nilai alas dan tinggi untuk jajar genjang")
print("9. Hitung luas jajar genjang = alas x tinggi")
print("10. Tampilkan hasil luas")
print("11. Selesai")

print()
print("Pseudocode:")
print("Mulai")
print("  Input panjang, lebar")
print("  Luas_persegi_panjang ← panjang * lebar")
print("  Input alas, tinggi")
print("  Luas_segitiga ← 0.5 * alas * tinggi")
print("  Input sisi")
print("  Luas_persegi ← sisi * sisi")
print("  Input alas, tinggi")
print("  Luas_jajargenjang ← alas * tinggi")
print("  Cetak semua hasil luas")
print("Selesai")

def luas_persegi_panjang(p, l):
    return p * l

def luas_segitiga(a, t):
    return 0.5 * a * t

def luas_persegi(s):
    return s * s

def luas_jajargenjang(a, t):
    return a * t

p = float(input("Masukkan panjang persegi panjang: "))
l = float(input("Masukkan lebar persegi panjang: "))
print("Luas Persegi Panjang =", luas_persegi_panjang(p, l))

a1 = float(input("Masukkan alas segitiga: "))
t1 = float(input("Masukkan tinggi segitiga: "))
print("Luas Segitiga =", luas_segitiga(a1, t1))

s = float(input("Masukkan sisi persegi: "))
print("Luas Persegi =", luas_persegi(s))

a2 = float(input("Masukkan alas jajar genjang: "))
t2 = float(input("Masukkan tinggi jajar genjang: "))
print("Luas Jajar Genjang =", luas_jajargenjang(a2, t2))
