class Fahrzeug:
    def __init__(self, name, price, highest_speed, current_speed=0, engine_status=False):
        self.name = name
        self.price = price
        self.highest_speed = highest_speed
        self.current_speed = current_speed
        self.engine_status = engine_status

    def beschleunige(self, a):
        if self.engine_status:
            if a + self.current_speed > self.highest_speed:
                print("Zu hohe Geschwindigkeit")
            elif a + self.current_speed < 0:
                print("Geschwindigkeit unter 0 nicht erlaubt")
            else:
                self.current_speed += a
                print(f"Fahrzeug fährt jetzt mit {self.current_speed}km/h")
        else:
            print("Motor läuft nicht")

    def starteMotor(self):
        if self.engine_status:
            print("Motor läuft bereits")
        else:
            print("Motor wird gestartet")
            self.engine_status = True

    def stoppeMotor(self):
        if self.current_speed != 0:
            print("Motor kann nicht stoppen, wenn sich das Fahrzeug bewegt!")
        elif self.engine_status:
            print("Motor wird gestoppt")
            self.engine_status = False
        else:
            print("Motor läuft eh nicht!")

    def __str__(self):
        return (f"Fahrzeug: {self.name}\n"
            f"Preis: {self.price} €\n"
            f"Maximale Geschwindigkeit: {self.highest_speed} km/h\n"
            f"Aktuelle Geschwindigkeit: {self.current_speed} km/h\n"
            f"Motor: { "läuft" if self.engine_status else "läuft nicht" }")
#########################################################################
# f1 = Fahrzeug("VW", 12_000, 200)
# f1.starteMotor()
# f1.starteMotor()
# f1.beschleunige(5)
# f1.beschleunige(500)
# f1.beschleunige(-500)
# f1.stoppeMotor()
# f1.beschleunige(-5)
# f1.stoppeMotor()
# f1.stoppeMotor()
# print(f1)
