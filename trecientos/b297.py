class Form:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def push(self, SamuelPuerto):
        if isinstance(SamuelPuerto, int):
            self.SamuelPuerto.append(SamuelPuerto)

SamuelPuerto = Form([])
SamuelPuerto.push(86)
print(SamuelPuerto.SamuelPuerto)
#3203084
