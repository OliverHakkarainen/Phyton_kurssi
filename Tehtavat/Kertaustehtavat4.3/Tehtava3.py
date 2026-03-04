import math
from math import sqrt

while True:
        kokonaisluku = int(input("anna kokonaisluku"))
        if kokonaisluku <0:
            print(f'virheellinen numero')
        if kokonaisluku == 0:
            print(f'poistuu loopista')
            break
        else:
            print(math.sqrt(kokonaisluku))





