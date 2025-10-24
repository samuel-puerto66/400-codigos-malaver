class Rectangle:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def push(self, SamuelPuerto):
        if isinstance(SamuelPuerto, int):
            self.SamuelPuerto.append(SamuelPuerto)

SamuelPuerto = Rectangle([])
SamuelPuerto.push(26)
print(SamuelPuerto.SamuelPuerto)
#3203084
