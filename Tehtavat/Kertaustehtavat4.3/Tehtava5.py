laskutoimitus = input("anna haluamasi laskutoimitus (plus/miinus/kertojako) loppu lopettaa laskutehtävän")

if laskutoimitus != "loppu":
    luku1 = float(input("anna luku"))
    luku2 = float(input("anna luku2"))

while True:
    if laskutoimitus == "plus":
            print(luku1 + luku2)
    elif laskutoimitus == "miinus":
            print(luku1 - luku2)
    elif laskutoimitus == "kerto":
            print(luku1 * luku2)
    elif laskutoimitus == "jako":
            print(luku1 / luku2)

    else:
        print("loppuu")
        break

    laskutoimitus = input("anna haluamasi laskutoimitus (plus/miinus/kertojako) loppu lopettaa laskutehtävän")
    if laskutoimitus == "loppu":
        break
    luku1 = float(input("anna luku"))
    luku2 = float(input("anna luku2"))


print("Ohjelma loppuu...")