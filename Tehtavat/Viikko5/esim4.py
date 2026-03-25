def neliosumma(a, b):
    _tulos = a**2 + b**2
    return _tulos

luku1 = float(input("anna eka luku:"))
luku2 = float(input("anna toka luku:"))
tulos = neliosumma(luku1, luku2)

print(f'lukujen {luku1} ja {luku2} neliösumma on {tulos: .2f}')

