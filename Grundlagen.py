# Kommentare schreibt man mit #
# Print schreibt in die Konsole ist ein Befehl
print("Hallo Welt!")
print("Zweite Zeile Text")

# Variablen und Typen
x = 5 # int Variable (Ganze Zahlen=
y = 10.3 # float Variable (Gleitkommazahlen) Komma mit "." schreiben
z = "Text Beispiel"

print (z)
# wenn ich variablen ausgeben will, dann verwende ich einen f-String also f""
# darin kann man mit {} python code ausführen
print (f"{x} * {y} = {x*y}") # wenn ich Ganzzahlen mit Gleitkommazahlen multipliziere
                             # wird automatisch Gleitkommazahl verwendet



# Bool variablen
zustand = False # groß schreiben
zustand = True

print (zustand)

# Arithmetische Operationen
summe = x+y
differenz = x-y
produkt = x*y
quotient = x/y

print(summe)
print(differenz)
print(produkt)
print(quotient)

# Modulus Operator gibt den Rest einer Division.
# Wenn eine Modulus Operation 0 ergibt, heißt es, dass die Zahl teilbar ist.

print(x%2 == 0) # False: 5 ist nicht durch 2 teilbar

print(3**2) # hoch rechnen, 2^3
