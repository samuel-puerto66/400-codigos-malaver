class Splitter:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def contains(self, SamuelPuerto):
        if isinstance(self.SamuelPuerto, str):
            return SamuelPuerto in self.SamuelPuerto
        return False

SamuelPuerto = Splitter("y")
print(SamuelPuerto.contains("y"))
#3203084
