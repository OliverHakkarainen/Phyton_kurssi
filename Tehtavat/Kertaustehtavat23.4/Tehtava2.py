opiskelijat = {"Young Sale" : ["Young Sale", 1, "Köksä"], "Oliver Jr." : ["Oliver Jr.", 3, "TutaInsMa"]}

print(f"Young Salen vuosiluokka: {opiskelijat['Young Sale'][1]}")
print(f'Oliver Jr:in lempi aine: {opiskelijat["Oliver Jr."][2]}')

opiskelijat["Oliver Jr."][2] = "Puutyöt"
opiskelijat["Anna"] = ["Anna", 3, "Vapaapäivä"]

del opiskelijat["Young Sale"]
print("\nPäivitetty sanakirja:")
for avain, tiedot in opiskelijat.items():
    print(f'{avain}:{tiedot}')