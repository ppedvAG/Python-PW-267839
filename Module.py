# import FunktionsModule.Calculator as Calc
# print(Calc.addieren(12,3))
# print(Calc.subtrahieren(54,8.7))
# Calc.multipliziere(10_000_000, 2)
# print(Calc.dividiere(10_000_000, 2))

from FunktionsModule.Mathematik.Calculator import addieren
from FunktionsModule.Begruessungen import hallo

print(addieren(1.2,54))

hallo("Dominik")
hallo()