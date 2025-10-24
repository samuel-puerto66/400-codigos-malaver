class Signal:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def max_with(self, SamuelPuerto):
        if SamuelPuerto > self.SamuelPuerto:
            self.SamuelPuerto = SamuelPuerto

SamuelPuerto = Signal(0)
SamuelPuerto.max_with(57)
print(SamuelPuerto.SamuelPuerto)
#3203084
