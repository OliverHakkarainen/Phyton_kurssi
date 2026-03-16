import random

nopat = int(input("kuinka montaa noppaa heitetään?"))
kokonaisluku = 0

for i in range(nopat):
    luku =random.randint(1,6)
    print(luku)
    kokonaisluku = luku + kokonaisluku
print(f'silmälukujen summa: {kokonaisluku}')