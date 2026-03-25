def invis(tavarat):
    print("sinulla on seuraavat tavarat repussa: ")
    for t in tavarat:
        print("- " + t)
    tavarat.clear()
    return

reppu = ["taskulamppu", "otsalamppu" ,"pöytälamppu"]
invis(reppu)
reppu.append("eväsleipä")
invis(reppu)