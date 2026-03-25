def laske_summa(lista):
    summa = 0
    for i in lista:
        summa = summa + i
    return summa

lista = [3, 7, 20, 21, 32, 50]

tulos = laske_summa(lista)

print("Listan summa on:", tulos)