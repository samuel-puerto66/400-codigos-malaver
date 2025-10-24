class Repository:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def increment(self):
        if self.SamuelPuerto < 81:
            self.SamuelPuerto += 1

SamuelPuerto = Repository(0)
SamuelPuerto.increment()
print(SamuelPuerto.SamuelPuerto)
#3203084
