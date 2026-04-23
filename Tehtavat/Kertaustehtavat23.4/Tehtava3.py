kirjasto = {"Holly" : ["Stephen King", 2024, "Kauhu"],
            "Turms, kuolematon" : ["Mika Waltari", 1955, "Historiallinen Romaani"],
            "Vieterilintukronikka" : ["Haruki Murakami", 2024, "Kaunokirja"] }


print(f'Kirjan Holly kirjoittaja: {kirjasto["Holly"][0]}')
print(f'Kirjan Vieterilintukronikka genre: {kirjasto["Vieterilintukronikka"][2]}')

kirjasto["Turms, kuolematon"][2] = "Romaani"
kirjasto["Valtaistuinpeli"] = ["George R.R. Martin", 1997, "Fantasia"]

del kirjasto["Vieterilintukronikka"]
print(kirjasto)
