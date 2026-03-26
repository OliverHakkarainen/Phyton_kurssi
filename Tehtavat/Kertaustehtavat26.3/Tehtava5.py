def suurin_arvo(a, b, c):
    suurin = a

    if b > suurin:
        suurin = b
    if c > suurin:
        suurin = c

    return suurin

luku1 = int(input("anna ensimmäinen luku: "))
luku2 = int(input("anna toinen luku: "))
luku3 = int(input("anna kolmas luku: "))

suurin = suurin_arvo(luku1, luku2, luku3)
print("suurin arvo: ", suurin)