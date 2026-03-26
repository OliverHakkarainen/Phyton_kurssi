laskutoimitus = input("anna haluamasi laskutoimitus (plus/miinus/kertojako) loppu lopettaa laskutehtävän")
def plus(a,b):
    return a + b

def miinus(a,b):
    return a - b

def kerto(a,b):
    return a * b

def jako(a,b):
    return a / b


if laskutoimitus != "loppu":
    luku1 = float(input("anna ensimmäinen luku"))
    luku2 = float(input("anna toinen luku"))

while True:
    if laskutoimitus == "plus":
            print("luvut yhteenlaskettuna on: ", luku1 + luku2)
    elif laskutoimitus == "miinus":
            print("luvut vähennettynä on: ", luku1 - luku2)
    elif laskutoimitus == "kerto":
            print("luvut kerrottuna on: ", luku1 * luku2)
    elif laskutoimitus == "jako":
            print("luvut jaettuna on: ", luku1 / luku2)

    else:
        print("loppuu")
        break

    laskutoimitus = input("anna haluamasi laskutoimitus (plus/miinus/kertojako) loppu lopettaa laskutehtävän")
    if laskutoimitus == "loppu":
        break
    luku1 = float(input("anna luku"))
    luku2 = float(input("anna luku2"))