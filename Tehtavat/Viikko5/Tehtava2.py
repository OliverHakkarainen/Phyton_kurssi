luku = input("anna luku")
lista = []

while luku != " ":
    numero = int(luku)
    lista.append(numero)
    luku = input("anna seuraava luku")

lista.sort(reverse=True)
print(*lista[:5],sep = ",")