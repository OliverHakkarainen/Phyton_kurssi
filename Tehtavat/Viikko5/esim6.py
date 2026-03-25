def tervehdi(nimi):
    print(f'tervehdys {nimi}')
    return

def tervehdi_monesti(nimi, kerrat):
    while kerrat > 0:
        tervehdi(nimi)
        kerrat -= 1
    return


tervehdi_monesti("Longjohn", 5)