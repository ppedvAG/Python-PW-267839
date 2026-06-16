import os.path

# funktion workingWithFiles
# Params: path:str -> Dateipfad
# return: nichts
# Funktionsweise:
#   Auswahl Modus zum öffnen der Datei (input)
#   w/a ->  Erfolgsmeldung in Datei schreiben
#   r   ->   Dateiinhalt in Konsole schreiben
def workingWithFiles(path: str):
    choice = ""
    # while choice != "w" and choice != "r" and choice != "a":
    while choice not in ("w", "r", "a"):
        choice = input("Modus auswählen: \nwrite (w) | read (r) | append (a)\nAuswahl:")

    print("Deine Auswahl: " + choice)
    if(choice == "w"):
        with open(path, "w") as file:
            file.write("Erfolg! Text mit Modus \"w\" - write, geschrieben\n")
    elif(choice == "a"):
        with open(path, "a") as file:
            file.write("Erfolg! Text mit Modus \"a\" - append, geschrieben\n")
    elif(os.path.exists(path)):
        with open(path, "r") as file:
            print("Dieser Text steht in "+path)
            for line in file:
                print("\t"+line, end="")


# Aufruf der Funktion mit einem Pfad
# Input Pfad von User
path = input("Einen Pfad eingeben: ")
workingWithFiles(path)


# Übung 2
# Wir wollen einen Taschenrechner erstellen. Frage zuerst vom Benutzer zwei Eingaben ab.
# Prüfe diese Eingaben darauf, ob diese numerisch sind.
# Falls eine der beiden Eingaben nicht numerisch ist, soll das Programm abgebrochen werden.
# Gib dem Nutzer die Möglichkeit per Tastendruck zwischen Addition, Subtraktion, Multiplikation und Division zu wählen
# (Zahl zwischen 1 und 4 mittels input() abfragen à Rechenoperation auswählen).
# Bei Ungültiger Eingabe soll der Benutzer erneut nach seiner Entscheidung gefragt werden.
# Lasse das Ergebnis inklusive der Rechnung in der Konsole ausgeben.
# Frage nach Ende der Operation ob der Benutzer eine neue Rechnung (Wiederholen) durchführen will.


def calculator():
    while True:
        input1 = input("Gib die erste Zahl ein: ")
        input2 = input("Gib die zweite Zahl ein: ")

        if input1.isdigit() and input2.isdigit():
            number1 = int(input1)
            number2 = int(input2)
        else:
            print("Mindestens eine Eingabe war keine numerische Zahl. Programm wird beendet.")
            return

        while True:
            print("\nWähle die Rechenoperation:")
            print("1: Addition (+)")
            print("2: Subtraktion (-)")
            print("3: Multiplikation (*)")
            print("4: Division (/)")
            op = input("Deine Wahl (1-4): ")

            if op == "1":
                sum = number1 + number2
                symbol = "+"
                break
            elif op == "2":
                sum = number1 - number2
                symbol = "-"
                break
            elif op == "3":
                sum = number1 * number2
                symbol = "*"
                break
            elif op == "4":
                if number2 == 0:
                    print("Division durch 0 ist nicht erlaubt. Programm wird beendet.")
                    return
                sum = number1 / number2
                symbol = "/"
                break
            else:
                print("Ungültige Eingabe, bitte eine Zahl zwischen 1 und 4 wählen.\n")

        print(f"\nRechnung: {number1} {symbol} {number2} = {sum}")

        while True:
            repeat = input("\nNeue Rechnung durchführen? (j/n): ").lower()
            if repeat == "j":
                print()
                break
            elif repeat == "n":
                print("Programm wird beendet.")
                return
            else:
                print("Bitte 'j' oder 'n' eingeben.")
calculator()
