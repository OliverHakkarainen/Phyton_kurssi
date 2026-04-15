vuodenajat = ("kevät", "kesä", "syksy", "talvi")
kuukausinumero = int(input("Anna kuukauden numero (1-12): "))

if kuukausinumero <= 2 or kuukausinumero == 12:
    print("Vuodenaika on", vuodenajat[3])

elif kuukausinumero <=5:
    print("Vuodenaika on", vuodenajat[0])

elif kuukausinumero <=8:
    print("Vuodenaika on", vuodenajat[1])

elif kuukausinumero <= 11:
    print("Vuodenaika on", vuodenajat[2])

else:
    print("Virheellinen numero!")