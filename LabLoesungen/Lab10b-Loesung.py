from LabLoesungen.Lab10Loesung import Fahrzeug

class PKW(Fahrzeug):
    def __init__(self, name, price, highest_speed, current_speed = 0, engine_status = False, doorsOpen=False):
        super().__init__(name, price, highest_speed, current_speed,  engine_status)
        self.doorsOpen = doorsOpen

    def openDoors(self):
        if self.current_speed == 0:
            self.doorsOpen = True
        else:
            print("Türen bei Fahrt geschlossen halten")

    def closeDoors(self):
        if self.doorsOpen:
            self.doorsOpen = False
        else:
            print("Türen sind schon zu.")

    def __str__(self):
        s = super().__str__()
        return s + f"\nTüren sind {"offen" if self.doorsOpen else "zu"}"

f = PKW("VW", 45, 100)
print(f)
f.closeDoors()
f.starteMotor()
f.beschleunige(54)
f.openDoors()
f.beschleunige(-54)
f.openDoors()
print(f)


