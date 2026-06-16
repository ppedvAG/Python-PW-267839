# # Output auf Konsole
# print("Hallo Welt")
#
# # Input von Konsole (Rückgabetyp string, Parameter: Meldung)
# name = input("Name Eingeben: ")
# print(f"Hallo {name}")
#
# # Zahlen Input
# x = input("Zahl 1 eingeben: ")
# y = input("Zahl 2 eingeben: ")
# print(f"{x} + {y} = {x+y}") # 12 + 13 = 1213 -> Strings werden einfach aneinander gehängt
#
# x = float(input("Zahl 1 eingeben: "))
# y = float(input("Zahl 2 eingeben: "))
# print(f"{x} + {y} = {x+y}")
#
# b = bool(input("True/False eingeben: "))
# if(b):
#     print("Wahr")
# else:
#     print("Falsch")
# print(b)

# open
# Datei öffnen
# Muss einen Modes enthalten (r Read, w Write, a Append)
file = open("Output.txt", "w")
file.write("Hello World\n")
file.write("Zeile 2\n") # \n macht neue Zeile
file.write("\tZeile 3\n") # \t Tabulator
file.write("Zeile \\ 3\n") # \\ um \ zu schreiben
file.write("Zeile \"3\"\n") # \" um " zu schreiben
file.close()

file = open("Output.txt", "r")
lines = file.readlines()
file.close()
print(lines)

for line in lines:
    print(line, end="")


# with brauch ich das close() nicht mehr
# files werden automatisch geschlossen
with open("Output.txt", "a") as file:
    file.write(input("neue Zeile eingeben: \n"))

# rstring
# Raw String
# Escape Sequenzen ignoriert (zB. \n)
# \ kann normal verwendet werden -> gut für Dateipfade
filename = r"C:\Users\de2\OneDrive - ppedv AG\Anlagen\Schulungsunterlagen\Python\Python-PW-267839\Output.txt"


# os.path
# damit kann ich überprüfen ob Dateien existieren
import os.path
if os.path.exists("Output.txt"):
    print("Output.txt exists and is going to be deleted")
    # os.remove("Output.txt") # löscht datei
