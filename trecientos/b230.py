class Route:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def scale(self, SamuelPuerto):
        if SamuelPuerto > 0:
            self.SamuelPuerto *= SamuelPuerto

SamuelPuerto = Route(2)
SamuelPuerto.scale(3)
print(SamuelPuerto.SamuelPuerto)
#3203084
