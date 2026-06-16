def addieren(x, y):
    return x + y

def subtrahieren(x:int|float, y:int|float):
    return x-y

def multipliziere(x:int|float, y:int|float):
    # Überprüfung von x und y sind logisch identisch, type(x) in [int, float] ist kürzer
    if(type(x) in [int, float] and (type(y) == int or type(y) == float)):
        print(f"{x} * {y} = {x*y}")
    else:
        raise TypeError("X und Y müssen Zahlen sein!") # raise lässt das Programm abstürzen

def dividiere(x:int|float, y:int|float = 2):
    if y == 0:
        raise ZeroDivisionError("Division durch 0") # wird eigentlich sowieso geworfen, hier mit extra deutscher Fehlermeldung
    return x/y