username = "käyttäjätunnus"
password = "salasana"
oikein=False
i=5

while i > 0:
    user_input = input("anna käyttäjätunnus:")
    pass_input = input("anna salasana: ")

    if user_input == username and pass_input == password:
        oikein = True
        break
    else:
        i -= 1
        if i > 0:
            print(f"kirjautumistiedot väärin. {i} yritystä jäljellä")

if oikein == True:
    print("tervetuloa")
else:
    print("pääsy evätty")