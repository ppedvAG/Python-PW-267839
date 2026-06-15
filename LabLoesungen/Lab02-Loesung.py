# Übung 1
# Lege drei numerische Variablen an, addiere sie zusammen und schreibe das Ergebnis in eine neue Variable.
# Potenziere danach die Variable mit sich selbst und schreibe das Ergebnis erneut in eine Variable .

num1 = 1
num2 = 2
num3 = 3

numSum = num1 + num2 + num3

numSumExp = numSum ** numSum

print("numSumExp:", numSumExp)

# Übung 2
# Nimm die potenzierte Zahl aus Übung1 und stelle fest ob diese Restlos durch 2 teilbar (gerade) ist

numSumExpMod = numSumExp % 2
print("numSumExpMod:", numSumExpMod)

# Übung 3
# Lege zwei Variablen an: Vorname befüllt mit Max und Nachname befüllt mit Mustermann
# Verbinde diese zwei Variablen und zähle danach die Buchstaben 'M' und 'm'
# Das Ergebnis soll 3 sein

vorname = "Max"
nachname = "Mustermann"

vollerName = vorname + " " +  nachname
numOfLetters_M = vollerName.casefold().count("m")
print("Buchstabe 'M' und 'm' in der Variable 'numOfLetters_M':", numOfLetters_M)

# Übung 4
# Schreibe deinen Vornamen ohne Großbuchstaben in eine Variable
# Verwende danach diese Variable, und gib diese mit dem ersten Buchstaben groß geschrieben aus

meinVorname = "max"
print(meinVorname.capitalize())

# Übung 5
# Nimm die drei Variablen Vorname, Nachname (aus Übung 3) und dein Vorname (Übung 4)
# und gib die gesamte Länge dieser drei Strings aus

combinedNames = vorname + nachname + meinVorname
print("Länge des gesamten kombinierten Strings:", len(combinedNames))