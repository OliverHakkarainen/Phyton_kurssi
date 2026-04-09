#esim1
viikko = ("ma", "ti", "ke", "to", "pe", "la", "su")
paiva = int(input("anna viikonpäivän järjestysnumero (1-7): "))
vkpaiva = viikko[paiva -1]

print(f'viikon {paiva}. päivä on {vkpaiva}')

#esim2

hedelmat = ("päärynä", "Granaattiomena", "mango")

(h1, h2, h3) = hedelmat

print("hedelmä 1 on", h1)
print("hedelmä 2 on", h2)
print("hedelmä 3 on", h3)

#esim3
import random
def heita():
    eka = random.randint(1,6)
    toka = random.randint(1,6)
    return (eka, toka)

noppa1, noppa2 = heita()
print(f'heitit nopasta 1: {noppa1} ja nopasta 2: {noppa2}. Liiku siis yhteensä {noppa1 + noppa2} askelta.')