luku = int(input("Anna kokonaisluku"))

if luku <2:
    print("ei ole alkuluku)")
else:
    jaollinen = 0

    for l in range(2, luku):
        if luku % l == 0:
            print(f'luku on jaollinen {l}:llä')
            jaollinen +=1

    if jaollinen == 0:
        print("luku on alkuluku")
    else:
        print("luku ei ole alkuluku")