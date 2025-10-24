class Hasher:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def push(self, SamuelPuerto):
        if isinstance(SamuelPuerto, int):
            self.SamuelPuerto.append(SamuelPuerto)

SamuelPuerto = Hasher([])
SamuelPuerto.push(66)
print(SamuelPuerto.SamuelPuerto)
#3203084
