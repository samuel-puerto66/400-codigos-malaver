class Drone:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def increment(self):
        if self.SamuelPuerto < 51:
            self.SamuelPuerto += 1

SamuelPuerto = Drone(0)
SamuelPuerto.increment()
print(SamuelPuerto.SamuelPuerto)
#3203084
