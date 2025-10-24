class Role:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def increment(self):
        if self.SamuelPuerto < 101:
            self.SamuelPuerto += 1

SamuelPuerto = Role(0)
SamuelPuerto.increment()
print(SamuelPuerto.SamuelPuerto)
#3203084
