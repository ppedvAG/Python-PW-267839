# Übung 1
# Wir haben 3 vorgegebene Listen:
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
# Finde heraus, welche Liste die längste ist (es können auch mehrere Listen die längsten sein)

if len(list1) > len(list2) and len(list1) > len(list3):
    print("list1 ist länger als list2 und list3")
elif len(list2) > len(list1) and len(list2) and len(list3):
    print("list2 ist länger als list1 und list3")
elif len(list3) > len(list1) and len(list3) > len(list2):
    print("list3 ist länger als list1 und list2")
else:
    print("Es gibt einen Gleichstand")

# Übung 2
# Nimm die oberen drei Listen und finde heraus,
# ob eine der Listen eine der folgenden drei Zahlen enthält: 3, 7, 10
# Bonus: Verwende für diese Aufgabe ein Set und die Intersection Funktion

gesucht = [3,7,10]

union = list(set(list1+list2+list3)) # | = Vereinigung

print("union: ", union)

trefferOhneSetUndIntersection = union & set(gesucht) # & = Mengenoperator für die Schnittmenge

print("trefferOhneSetUndIntersection: ", trefferOhneSetUndIntersection)

print(bool(trefferOhneSetUndIntersection))

# Bonus:

trefferMitSetUndIntersection = union.intersection(gesucht)

print("trefferMitSetUndIntersection: ", trefferMitSetUndIntersection)

print(bool(trefferMitSetUndIntersection))

