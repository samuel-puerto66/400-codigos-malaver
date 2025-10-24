class Packet:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def toggle(self):
        if isinstance(self.SamuelPuerto, bool):
            self.SamuelPuerto = not self.SamuelPuerto

SamuelPuerto = Packet(False)
SamuelPuerto.toggle()
print(SamuelPuerto.SamuelPuerto)
