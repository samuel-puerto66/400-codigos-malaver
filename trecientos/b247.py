class Logger:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def push(self, SamuelPuerto):
        if isinstance(SamuelPuerto, int):
            self.SamuelPuerto.append(SamuelPuerto)

SamuelPuerto = Logger([])
SamuelPuerto.push(6)
print(SamuelPuerto.SamuelPuerto)
#3203084
