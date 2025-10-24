class Permission:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def contains(self, SamuelPuerto):
        if isinstance(self.SamuelPuerto, str):
            return SamuelPuerto in self.SamuelPuerto
        return False

SamuelPuerto = Permission("r")
print(SamuelPuerto.contains("r"))
#3203084
