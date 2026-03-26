

numero = int(input(f'Anna kertaulun numero 1-10: '))

kertolasku = 0

for i in range(1,11):
    kertolasku = numero * i
    print(kertolasku)
    if numero >= 11:
        print("anna numero väliltä 1-10")
        break
    if numero <= 0:
        print("anna numero väliltä 1-10")
        break
