class PathFinder:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def push(self, SamuelPuerto):
        if isinstance(SamuelPuerto, int):
            self.SamuelPuerto.append(SamuelPuerto)

SamuelPuerto = PathFinder([])
SamuelPuerto.push(56)
print(SamuelPuerto.SamuelPuerto)
#3203084
