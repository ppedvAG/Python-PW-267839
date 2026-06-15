# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
# Kombiniere die drei Listen in eine ganze Liste und schließe Duplikate aus

# Jede Liste wird zu einer Menge. Duplikate werden dabei entfernt
combinedList = list(set(list1) | set(list2) | set(list3))
print(combinedList)
combinedList = list(set(list1+list2+list3)) # identisches ergebnis
print(combinedList)

# Übung 2
# Erstelle einen String und wandele ihn in eine Liste um.
# Dabei soll jedes einzelne Zeichen ein Element der Liste werden.

testString = "string"

print(list(testString))

# Übung 3
# Lasse eine Liste erstellen, die bei 0 beginnt und alle geraden Zahlen bis 20 enthält
# Nicht selbst schreiben, sondern Python machen lassen

l = list(range(0,21,2))
print (l)