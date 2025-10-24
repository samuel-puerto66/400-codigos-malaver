class Order:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def increment(self):
        if self.SamuelPuerto < 21:
            self.SamuelPuerto += 1

SamuelPuerto = Order(0)
SamuelPuerto.increment()
print(SamuelPuerto.SamuelPuerto)
#3203084
