def keskiarvo(_luku1, _luku2, _luku3):
    _tulos = (_luku1 * _luku2 * _luku3) / 3
    return _tulos


luku1 = float(input("anna ensimmäinen luku: "))
luku2 = float(input("anna toinen luku: "))
luku3 = float(input("anna kolmas luku: "))

tulos = keskiarvo(luku1, luku2, luku3)
print("keskiarvo on;", tulos)