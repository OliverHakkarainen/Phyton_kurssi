tuntipalkka = float(input(f'mikä on tuntipalkkasi?'))
tunnit = float(input(f'anna tehdyt tunnit'))
paiva = input(f'mikä viikonpäivä on?')

if paiva == "sunnuntai":
    palkka = tuntipalkka * tunnit *2
    print(f'palkkasi on {palkka} euroa')

else:
    palkka = tuntipalkka * tunnit
    print(f'palkkasi on {palkka} euroa')
