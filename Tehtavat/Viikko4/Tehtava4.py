import random

print("Arvaa luku 1-10")

vastaus = random.randint(1, 10)
arvaus = int(input("arvaus: "))

while arvaus != vastaus:
    if arvaus < vastaus:
        print("liian pieni, arvaa uudelleen")
    else:
        print("liian suuri, arvaa uudelleen")
    arvaus = int(input("arvaus: "))

print("oikein")
