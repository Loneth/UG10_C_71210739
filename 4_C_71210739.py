# Odilio Ganesha Nugroho - 71210739
# Unguided 10 Grup C Soal 4

a = int(input("Masukan bilangan 1: "))
b = int(input("Masukan bilangan 2: "))
c = int(input("Masukan bilangan 3: "))

if a > b and a > c:
  print('\nBilangan terbesar adalah', a)
elif b > a and b > c:
  print('\nBilangan terbesar adalah', b)
else:
  print('\nBilangan terbesar adalah', c)

if a < b and a < c:
  print('Bilangan terkecil adalah', a)
elif b < a and b < c:
  print('Bilangan terkecil adalah', b)
else:
  print('Bilangan terkecil adalah', c)
