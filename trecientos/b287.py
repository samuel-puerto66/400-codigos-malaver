class Converter:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def push(self, SamuelPuerto):
        if isinstance(SamuelPuerto, int):
            self.SamuelPuerto.append(SamuelPuerto)

SamuelPuerto = Converter([])
SamuelPuerto.push(36)
print(SamuelPuerto.SamuelPuerto)
#3203084
