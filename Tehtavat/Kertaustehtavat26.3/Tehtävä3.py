sanat = ["sima", "pupu", "rairuoho", "tippaleipä", "pääsiäismuna", "vappumunkki", "jokujeesus", "raijuusto", "vitsa"]
lista = 0

for i in sanat:
    if len(i) > 5:
        lista += 1

print("sanoja joissa on yli 5 kirjainta: ", lista)
