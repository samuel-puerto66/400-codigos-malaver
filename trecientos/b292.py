class Builder:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def increment(self):
        if self.SamuelPuerto < 91:
            self.SamuelPuerto += 1

SamuelPuerto = Builder(0)
SamuelPuerto.increment()
print(SamuelPuerto.SamuelPuerto)
#3203084
