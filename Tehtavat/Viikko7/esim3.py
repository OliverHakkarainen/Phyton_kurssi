numerot = {"Viivi" : "050-412359",
            "Ahmed" : "040-123423",
            "Pekka" : "050-412359"}

numerot["Olga"] = "044-1324093"

for nimi in numerot:
    print(f' henkilön {nimi} puhelinnumero on {numerot[nimi]}.')
