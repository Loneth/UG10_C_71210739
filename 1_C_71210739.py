# Odilio Ganesha Nugroho - 71210739
# Unguided 10 Grup C Soal 1

i1 = str(input("Masukan nama lengkap Anda      : "))
i2 = int(input("Masukan tinggi badan Anda (cm) : "))
i3 = int(input("Masukan berat badan Anda (kg)  : "))

print("\nHello,", i1.title(), "!")

rumus = i3 / ((i2 / 100) ** 2)
print("Indeks masa tubuh (BMI) Anda adalah", "{:.1f}".format(rumus))

if rumus <= 18.5:
    print("Anda termasuk ke dalam kategori kekurangan berat badan!")
elif 18.5 < rumus <= 25:
    print("Anda termasuk ke dalam kategori berat badan ideal!")
elif 25 < rumus <= 30:
    print("Anda termasuk ke dalam kategori kelebihan berat badan!")
elif rumus > 30:
    print("Anda termasuk ke dalam kategori obesitas!")
else:
    print("kosong")
