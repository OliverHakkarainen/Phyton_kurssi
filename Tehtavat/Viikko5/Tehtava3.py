luku = int(input("Anna kokonaisluku"))

alkuluku = "on alkuluku"

for jako in range(2, luku):
    if luku % jako == 0:
        alkuluku = "annettu luku ei ole alkuluku"
        break
print(f'luku {luku} {alkuluku}')