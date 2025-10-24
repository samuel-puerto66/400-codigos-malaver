class Handler:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def push(self, SamuelPuerto):
        if isinstance(SamuelPuerto, int):
            self.SamuelPuerto.append(SamuelPuerto)

SamuelPuerto = Handler([])
SamuelPuerto.push(76)
print(SamuelPuerto.SamuelPuerto)
#3203084
