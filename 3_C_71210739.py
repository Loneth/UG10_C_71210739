# Odilio Ganesha Nugroho - 71210739
# Unguided 10 Grup C Soal 3

i1 = int(input("Masukan angka: "))

if i1 % 5 == 0 or i1 % 3 == 0:
    hasil1 = "YA"

    if i1 % 2 == 0 and i1 % 4 == 0:
        hasil2 = "TENTU"
    else:
        hasil2 = "TIDAK"

    print("Bilangan tersebut habis dibagi 5 atau 3? Jawab:", hasil1)
    print("\nApakah Bilangan tersebut juga habis dibagi 2 dan 4? Jawab:", hasil2)
else:
    print("Bilangan tersebut tidak habis dibagi 5 atau 3. Program dihentikan")
