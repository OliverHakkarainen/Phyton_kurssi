name = input("kerro nimesi")
print(f'nimesi on', name)
if name == "matti":
    print(f'seuraava kiitos!')
else:
    keittoannos = float(input("kuinka monta keittoannosta"))
    hinta = keittoannos * 5,90
    print(f'kokonaishinta on {hinta} euroa')
    print(f'seuraava kiitos!')
