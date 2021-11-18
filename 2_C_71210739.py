# Odilio Ganesha Nugroho - 71210739
# Unguided 10 Grup C Soal 2

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Kalkulator Volume Bangun Ruang")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Pilih bangun ruang yang ingin dihitung volumenya:")
print("1. Limas")
print("2. Bola")
print("3. Kerucut")

i1 = int(input("Masukan pilihan anda: "))

if i1 == 1:
    i2 = float(input("Masukan panjang sisi alas limas: "))
    i3 = float(input("Masukan tinggi limas: "))

    rumus = 1/3 * (i2 * i2) * i3
    print("Volume limas tersebut adalah", float(rumus))
elif i1 == 2:
    i2 = float(input("Masukan panjang jari-jari bola: "))

    rumus = 4/3 * 3.14 * i2 ** 3
    print("Volume bola tersebut adalah", float(rumus))
elif i1 == 3:
    i2 = float(input("Masukan jari-jari kerucut: "))
    i3 = float(input("Masukan tinggi kerucut: "))

    rumus = 1/3 * 3.14 * i2 ** 2 * i3
    print("Volume kerucut tersebut adalah", rumus)
else:
    print("Pilihan anda tidak tersedia di menu kalkulator ini")
