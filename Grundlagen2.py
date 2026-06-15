# # Aufzählungstypen
# # List: Ungeordnete Sammlung von Werten
# zahlen = [1,2,3,4,5,6,7,8,9,10] # Liste von Zahlen mit 10 Werten
# namen = ["Maria", "Jordan", "Sabine"] # Liste von Strings mit 3 Werten
# zustaende = [True, False, False] # Liste von Boolean mit 3 Werten
#
#
# # Werte verändern
# zahlen[0] = 12 # 12,2,3,4,5,6,7,8,9,10
# namen.append("Jake")
# print(f"index von element False: {zustaende.index(False)}")
# zustaende.remove(True) # False, True
# print(f"index von element 10: {zahlen.index(10)}")
# print ()
# del zahlen[9]
# print(namen)
# print(zahlen)
# print(zustaende)
from operator import truediv

# Tupel sind wie listen nur unveränderbar
x = (1,2,34,5)
# x[1] = 0 ist nicht erlaubt, weil unveränderbar
# x.append(6) ist ebenfalls nicht erlaubt

listX = list(x) # kopie von tupel als liste
print(listX)
# liste ist veränderbar
listX[3] = 100
listX.append(7)
listX.pop(0)
print(listX)


# so kann man tuple verändern, wenn man es unbedingt muss
# 1. tuple in eine liste kopieren, 2. liste verändern, 3. liste wieder in tuple kopieren
x = tuple(listX)
print(x)

# range erzeugt zahlen von start bis endpunkt
r = range(10)
print(list(r))
r = range(10, 20)
print(list(r))
r = range(10, 20, 2)
print(list(r))

# sets haben eindeutige Werte
s = {15,654,71}
print(s)
s.add(10)
print(s)
s.add(10) # 10 ist bereits vorhanden, diese zeile ändert nichts an meinem set
print(s)
# einträge sind nicht mehr veränderbar, ich kann sie löschen oder neue hinzufügen

# dictionaries
l1 = list(range(10))
print(l1)
l2 = list(range(10, 20))
print(l2)

d = {"liste 1": l1, "liste 2": l2}

print(d)

teilnehmerEmails = {
    "Sahra": "asdfs@gmail.com, zweite@email.com",
    "Laura": "jklö@gmx.at"
}
teilnehmerEmails["Dominik"] = "dominike@ppedv.de"
print(f"Sahra : {teilnehmerEmails['Sahra']}")
print(f"Laura : {teilnehmerEmails['Laura']}")
teilnehmerEmails["Sahra"] = "asdfadsfawefweaf@gmail.com"
print(teilnehmerEmails)

# String in Liste umwandeln
wort = "Hallo"
print(list(wort))


l1 = [1,2,3]
l2 = [3,5,6]
t = set(l1 + l2)
print (list(t))

