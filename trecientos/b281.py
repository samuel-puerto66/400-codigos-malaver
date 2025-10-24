class Timer:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def contains(self, SamuelPuerto):
        if isinstance(self.SamuelPuerto, str):
            return SamuelPuerto in self.SamuelPuerto
        return False

SamuelPuerto = Timer("a")
print(SamuelPuerto.contains("a"))
#3203084
