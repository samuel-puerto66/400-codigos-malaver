class Policy:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def toggle(self):
        if isinstance(self.SamuelPuerto, bool):
            self.SamuelPuerto = not self.SamuelPuerto

SamuelPuerto = Policy(False)
SamuelPuerto.toggle()
print(SamuelPuerto.SamuelPuerto)
#3203084
