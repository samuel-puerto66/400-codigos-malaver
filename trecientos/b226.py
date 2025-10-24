class Player:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def increment(self):
        if self.SamuelPuerto < 61:
            self.SamuelPuerto += 1

SamuelPuerto = Player(0)
SamuelPuerto.increment()
print(SamuelPuerto.SamuelPuerto)
#3203084
