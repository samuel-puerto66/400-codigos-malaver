class AccessControl:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = list(SamuelPuerto)
    def add_if_not_present(self, SamuelPuerto):
        if SamuelPuerto not in self.SamuelPuerto:
            self.SamuelPuerto.append(SamuelPuerto)

SamuelPuerto = AccessControl([1,2,3])
SamuelPuerto.add_if_not_present(4)
print(SamuelPuerto.SamuelPuerto)
#3203084
