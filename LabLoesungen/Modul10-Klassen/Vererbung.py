# Basisklassen definieren, welche ihre Inhalte (Attribute und Funktionen) an alle Unterklassen weitergeben

# Beispiel: Object
# In Python gibt es eine Klasse namens object
# Diese Klasse fungiert als Oberklasse von allen anderen Klassen
# Diese Klasse gibt alle Methoden weiter, die beginnen mit __ (__init__, __str__)

# Beispiel Lebewesen -> Mensch, Hund, Katze
# Funktionsklassen, weil sie Dinge können (Methoden
class Lebewesen:
    def __init__(self, alter: int):
        self.alter = alter

    def bewegen(self, distanz: int):
        print(f"Das Lebewesen bewegt sich um {distanz}m.")

    # Standardimplementation
    # Kann in den Unterklassen angepasst werden; ist dies nicht der Fall, wird dieser Output erzeugt
    def __str__(self):
        if type(self) == Mensch:
            print("Es ist ein Mensch")
        elif type(self) == Katze:
            print("Es ist ein Katze")
        return f"Lebewesen Alter: {self.alter}"

# Vererbung herstellen über Klassenname in Klammer
class Mensch(Lebewesen):
    # Wenn Mensch selebt __init__ implementieren soll, muss hier eine Verkettung stattfinden
    def __init__(self, alter: int, vorname: str):
        super().__init__(alter)
        self.vorname = vorname

    def __str__(self):
        x = super().__str__()
        return x + f", Vorname: {self.vorname}"


# Vererbung herstellen über Klassenname in Klammer
class Katze(Lebewesen):
    # Wenn Mensch selebt __init__ implementieren soll, muss hier eine Verkettung stattfinden
    def __init__(self, alter: int, fellfarbe: str):
        super().__init__(alter)
        self.fellfarbe = fellfarbe

    def __str__(self):
        x = super().__str__()
        return x + f", Fellfarbe: {self.fellfarbe}"

########################################

l = Lebewesen(5)
print(l)
l.bewegen(10)
m = Mensch(50, "Elisabeth")
print(m)
m.bewegen(10)
k  = Katze(10, "trifarbig")
print(k)
k.bewegen(100)