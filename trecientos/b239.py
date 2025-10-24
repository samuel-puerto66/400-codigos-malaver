class Transaction:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def push(self, SamuelPuerto):
        if isinstance(SamuelPuerto, int):
            self.SamuelPuerto.append(SamuelPuerto)

SamuelPuerto = Transaction([])
SamuelPuerto.push(96)
print(SamuelPuerto.SamuelPuerto)
#3203084
