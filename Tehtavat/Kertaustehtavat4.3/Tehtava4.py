tarina = ""

while True:
    sana = input(f'anna sana')
    print(f'{sana}')
    if sana == "loppu":
        print(f'{tarina}')
        break
    tarina = tarina + " " + sana
    print(f'{tarina}')

