class Broker:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def increment(self):
        if self.SamuelPuerto < 71:
            self.SamuelPuerto += 1

SamuelPuerto = Broker(0)
SamuelPuerto.increment()
print(SamuelPuerto.SamuelPuerto)
#3203084
