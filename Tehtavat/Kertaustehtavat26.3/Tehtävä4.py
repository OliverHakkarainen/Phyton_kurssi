def kuusi(koko):
    print("tulee kiva kuusi")

    for i in range(koko):
        pisteet = "*" *(2 * i + 1)
        valit = " " *(koko - i -1)
        print(valit + pisteet)

    valit = " " * (koko - 1)
    print(valit + "*")

uusikuusi = int(input("kuinka suuri kuusi tehdään?: "))
kuusi(uusikuusi)