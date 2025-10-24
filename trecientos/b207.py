class Pipeline:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def is_even(self):
        return self.SamuelPuerto % 2 == 0

SamuelPuerto = Pipeline(44)
print(SamuelPuerto.is_even())
#3203084
