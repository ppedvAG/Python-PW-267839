# Klassen und Objekte

# Klasse
# Komplexe Datentypen darstellen

# Datentyp Quiz
# - str: Zeichenkette
# - int: Ganze Zahl
# - float: Gleitkommazahl
# - list: Aufzählung von Daten
# - dict: Aufzählung von Key-Value Paaren
# - Person?

# Für Person müssen wir eine eigene Klasse definieren (weil Person komplex ist)

# 2 Typen von Klassen
# - Funktionsklassen
# - Datenklassen

# Person als Datenklasse:
# Datenpunkte:
# - Alter: int
# - Größe: float
# - Geschlecht: str
# - Vorname: str
# - Nachname: str
# ...
class Person:
    """
    docstring for Person
    Dokumentationskommentar
    Beschreibt eine Funktion/Klasse (mit Maus über Typname wird die Doku angezeigt)
    Muss unter Definition verwendet werden.
    Person stellt eine Person mit seinen Eigenschaften dar
    """

    def __init__(self, v:str, n:str, a: int, g:str):
        """
        Wird immer ausgeführt, wenn das Objekt erstellt wird (-> der Startcode von jedem Objekt)
        Hier werden die konkreten Werte empfangen, und angegeben
        """
        self.vorname = v
        self.nachname = n
        self.alter = a
        self.geschlecht = g
#############################

# Objekte
# Konkrete Instanzen von dem Bauplan (Klasse)
# Hier werden die verschiedenen Objekte erzeugt, und anhand ihrer Inhalte voneinander unterschieden
person1 = Person("Dominik", "Enzenhofer", 23, "m")
person2 = Person("Maria", "Musterfrau", 99, "f")

print(person1.vorname+" "+person1.nachname)
print(person2.vorname+" "+person2.nachname)
print(person1)

######################################
# Person verbessern
# - Parameter in __init__ optional machen
# - Funktion hinzufügen
# - __str__ überschreiben
class PersonCool:
    def __init__(self, v:str, n:str, a:int = None, g:str = None):
        self.vorname = v
        self.nachname = n
        self.alter = a
        self.geschlecht = g

    def __str__(self):
        """
        Gibt eine Stringrepräsentation von dem Objekt zurück
        normalerweise <__main__.PersonCool object at 0x0000014399D8D400> (Typname + Speicheradresse)
        Hier kann die Stringausgabe angepasst werden
        """
        return f"Person: (Vorname: {self.vorname}, Nachname: {self.nachname})"

    # eigene Funktionen sind eher selten in Datenklassen
    def sprechen(self, text:str):
        print(f"{self.vorname} sagt '{text}'")

#############################################

person3 = PersonCool("Toby", "Supercool")
print(person3)
person3.sprechen("servus")

# Liste von Personen
personenListe = [person3]
personenListe.append(PersonCool("Heidi", "Megacool"))
personenListe.append(PersonCool("Franz", "Semicool"))

for person in personenListe:
    print(person)
    person.sprechen("Hallo")

personenDict =  {
    f"{person3.vorname} {person3.nachname}": person3,
    "Susi Samba": PersonCool("Susi", "Samba", 12, "f")
}

print(personenDict)

