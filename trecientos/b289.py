class Engine:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def average(self, SamuelPuerto):
        if len(SamuelPuerto) > 0:
            self.SamuelPuerto = sum(SamuelPuerto)/len(SamuelPuerto)

SamuelPuerto = Engine(0)
SamuelPuerto.average([1,2,3,38])
print(SamuelPuerto.SamuelPuerto)
#3203084
