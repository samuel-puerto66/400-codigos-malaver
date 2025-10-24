class Counter:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def increment(self):
        if self.SamuelPuerto < 11:
            self.SamuelPuerto += 1

SamuelPuerto = Counter(0)
SamuelPuerto.increment()
print(SamuelPuerto.SamuelPuerto)
#3203084
