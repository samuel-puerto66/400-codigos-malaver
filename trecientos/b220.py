class Movie:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def push(self, SamuelPuerto):
        if isinstance(SamuelPuerto, int):
            self.SamuelPuerto.append(SamuelPuerto)

SamuelPuerto = Movie([])
SamuelPuerto.push(16)
print(SamuelPuerto.SamuelPuerto)
#3203084
