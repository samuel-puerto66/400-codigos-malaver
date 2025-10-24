class Cache:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def max_with(self, SamuelPuerto):
        if SamuelPuerto > self.SamuelPuerto:
            self.SamuelPuerto = SamuelPuerto

SamuelPuerto = Cache(0)
SamuelPuerto.max_with(17)
print(SamuelPuerto.SamuelPuerto)
#3203084
