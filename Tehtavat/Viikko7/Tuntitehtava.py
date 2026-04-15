hedelmat = {"päärynä" : 2.12,
            "granaattiomena" : 7.20,
            "banaani" : 2.37}

yhteishinta = 0

while True:
    hedelma = input("anna hedelmät joiden hinnat haluat tarkistaa (tyhjä lopettaa)").lower()

    if hedelma == " ":
        print("tilaus päättyy..")
        break

    if hedelma in hedelmat:
        print(f'hedelmän {hedelma} kilohinta on {hedelmat[hedelma]}')
        yhteishinta += hedelmat[hedelma]
    else:
        print("meiltä ei löydy kyseystä hedelmää varastosta")
        lisataanko = input("haluatko lisätä tuotteet hinnastoon (Y/N)").upper()

        if lisataanko == "Y":
            hinta = float(input(f'anna kilohinta {hedelma}lle: '))
            hedelmat[hedelma] = hinta
            print(f'{hedelma} on lisätty kilohinnalla {hinta}!')

print("yhteishinta tilaukselle on", yhteishinta, "€")

print("päivitetty hinnasto: ")
for hedelma in hedelmat:
    print(f'Hedelmä {hedelma}, hinta {hedelmat[hedelma]}')



