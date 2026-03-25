def gl(gallonat):
    litrat = gallonat * 3.785
    return litrat

gallonat = int(input("Anna gallonamäärä (negatiivinen lopettaa): "))

while gallonat >= 0:
    litrat = gl(gallonat)
    print("Litroina:", litrat)
    gallonat = int(input("Anna gallonamäärä (negatiivinen lopettaa):"))
