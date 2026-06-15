# If
from operator import truediv

a = 2
b = 4

# kleiner
if a < b:
    print(f"a ({a}) ist kleiner als b({b})")
    # solange man eingerückt ist gehört der code zur if verzweigung
    print("nur wenn if true ist")
print("auch wenn if false ist")

b= -2

# größer gleich
if a >= b:
    print(f"a ({a}) ist größer als b({b})")

b = 2
# gleich
if a == b:
    print(f"a ({a}) ist gleich b({b})")

# ungleich
if a != 12:
    print(f"a ({a}) ist ungleich 12")


zustand = True
if zustand:  # zustand == true ist sinlos, weil zustand eh schon true ist
    print("zustand ist true")

zustand = False
if not zustand:
    print("zustand ist false")

if not a > b:
    print(f"a ({a}) ist kleiner gleich als b({b})")

zustandNegiert = not zustand

if a<b:
    print("a kleiner")
    if zustandNegiert:
        print("und zustandNegiert ist true")
    else:
        print("und zustandNegiert ist false")
elif a > b:
    print("a größer")
else:
    print("gleich")
    if zustandNegiert:
        print("und zustandNegiert ist true")
    else:
        print("und zustandNegiert ist false")


# schaltjahr berechnen

jahr = 2000
istSchaltjahr = False;
if jahr % 4 == 0:
    istSchaltjahr = True
    if jahr % 100 == 0:
        istSchaltjahr = False
        if jahr % 400 == 0:
            istSchaltjahr = True
print (istSchaltjahr)

l = list(range(1,11))
print(len(l))



