
lista = []

while True:
    luku = int(input("anna luku: "))

    if luku == 0:
        print("ohjelma loppuu")
        break

    lista.append(luku)

    print("lista nyt: ", lista)
    print("lista nyt: ", (sorted(lista)))


