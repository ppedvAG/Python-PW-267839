#Schreiben eine Schleife, welche von 1 bis inklusive 100 hochzählt
# Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
    # Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
    # Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
    # Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBzz" ausgegeben werden
    # Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
i = 1
while i < 101:
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
            print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)
    i += 1

# Schreibe eine Schleife die dir alle Zahlen von 1 bis 200 zur Verfügung stellt.
# Lass dir jede Zahl erst in der kardinalen und dann daneben in der ordinalen Schreibweise darstellen
# (Zahl + Endung 'st', 'nd', 'rd' oder 'th')
# Hinweis: Der Modulo Operator ist hier sehr nützlich
# Bonus: Berücksichtige alle Zahlen die mit 11, 12 oder 13 enden

i = 1
while i < 201:
    iString = str(i)
    # Bsp: 32 -> "32"
    # '3' iString[0]
    # '2' iString[1]
    # len(iString) ist 2
    # len(iString)-1 ist der letzte Index
    #iString[len(iString)-1] gleich iString[1] -> Ziffer 2
    if i<11:
        if iString[len(iString)-1] == "1":
            print(f"{i}st")
        elif iString[len(iString)-1] == "2":
            print(f"{i}nd")
        elif iString[len(iString)-1] == "3":
            print(f"{i}rd")
        else:
            print(f"{i}th")
    else:
        if iString[len(iString)-2] == "1":
            print(f"{i}th")
        else:
            if iString[len(iString) - 1] == "1":
                print(f"{i}st")
            elif iString[len(iString) - 1] == "2":
                print(f"{i}nd")
            elif iString[len(iString) - 1] == "3":
                print(f"{i}rd")
            else:
                print(f"{i}th")
    i+=1