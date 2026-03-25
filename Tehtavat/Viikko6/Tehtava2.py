import random

def noppa(tahkot):
    luku = random.randint(1,tahkot)
    return luku

tahkot = int(input("Anna nopan tahkojen määrä: "))

luku = 0
while luku != tahkot:
    luku = heita_noppaa(tahkot)
    print(luku)