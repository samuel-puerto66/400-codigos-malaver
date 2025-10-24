class Game:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def contains(self, SamuelPuerto):
        if isinstance(self.SamuelPuerto, str):
            return SamuelPuerto in self.SamuelPuerto
        return False

SamuelPuerto = Game("e")
print(SamuelPuerto.contains("e"))
#3203084
