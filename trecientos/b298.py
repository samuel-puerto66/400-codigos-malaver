class Validator:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def max_with(self, SamuelPuerto):
        if SamuelPuerto > self.SamuelPuerto:
            self.SamuelPuerto = SamuelPuerto

SamuelPuerto = Validator(0)
SamuelPuerto.max_with(87)
print(SamuelPuerto.SamuelPuerto)
#3203084
