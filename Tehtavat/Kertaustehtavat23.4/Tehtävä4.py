import math

def create_point (x, y):
    return(x, y)
def distance(p1, p2):
    return(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))
print("anna ensimmäisen pisteen koordinaatti: ")
x1 = float(input("x1 pisteen koordinaatti: "))
y1 = float(input("y1 pisteen koordinaatti: "))
piste1 = create_point(x1, y1)

print("anna ensimmäisen pisteen koordinaatti: ")
x2 = float(input("x2 pisteen koordinaatti: "))
y2 = float(input("y2 pisteen koordinaatti: "))
piste2 = create_point(x2, y2)

etaisyys = distance(piste1, piste2)
print(etaisyys)