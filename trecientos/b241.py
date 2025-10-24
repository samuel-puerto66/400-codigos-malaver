class Connection:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def is_even(self):
        return self.SamuelPuerto % 2 == 0

SamuelPuerto = Connection(94)
print(SamuelPuerto.is_even())
#3203084
