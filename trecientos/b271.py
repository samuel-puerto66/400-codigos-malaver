class Queue:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def increment(self):
        if self.SamuelPuerto < 31:
            self.SamuelPuerto += 1

SamuelPuerto = Queue(0)
SamuelPuerto.increment()
print(SamuelPuerto.SamuelPuerto)
#3203084
