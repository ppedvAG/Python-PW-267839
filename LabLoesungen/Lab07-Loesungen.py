# Übung 1
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# und uns die größte dieser Zahlen zurückgibt.
# Bonus: Berücksichtige auch das Szenario, das ausschließlich negative Zahlen in die Funktion kommen.

def maximum(*numbers):
    return print(max(numbers))


maximum(-2, -3)


# Übung 2
# Wir wollen eine Funktion erstellen, die einen String als Parameter erhält.
# Diese Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht.
# Die Funktion soll zusätzlich zählen wie viele Sonderzeichen (Nummern inkludiert) enthalten sind und das ebenfalls ausgeben.

def checkString(text):
    groß = 0
    klein = 0
    sonder = 0

    for symbol in text:
        if symbol.isupper():
            groß += 1
        elif symbol.islower():
            klein += 1
        else:
            sonder += 1

    return f"Sonderzeichen (inkl. Ziffern): {sonder}, Groß: {groß}, Klein: {klein}"


checkString("test1!")


# Übung 3
# Schreibe eine Funktion, die eine Liste von Strings (Vornamen) als Parameter empfängt.
# Diese Funktion soll die Vornamen als eine Aufzählung zusammenbauen und am Ende zurückgeben.
# Dabei sollen alle Namen mit einem Komma und der letzte Name mit einem "und" angehängt werden.


def vornamen(namen: list):
    if namen == []:
        return "Keine Parameter angegeben"
    elif len(namen)==1:
        return namen[0] # namen:["T1"] namen[0]: "T1"
    else:
        vorne = ""
        for name in namen[0:-2]:
            vorne += name+", "
        return vorne + namen[-2] + " und " + namen[-1]
        # Einfacher:
        # vorne = ", ".join(namen[0:-1])
        # return vorne + " und " + namen[-1]

print(vornamen(["T1", "T2", "T3", "T4"]))
print(vornamen(["T1"]))
print(vornamen(["T1", "T2"]))
print(vornamen([]))

