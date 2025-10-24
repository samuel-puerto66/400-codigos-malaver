class Proxy:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def contains(self, SamuelPuerto):
        if isinstance(self.SamuelPuerto, str):
            return SamuelPuerto in self.SamuelPuerto
        return False

SamuelPuerto = Proxy("k")
print(SamuelPuerto.contains("k"))
#3203084
