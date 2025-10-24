class Student:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = SamuelPuerto
    def is_even(self):
        return self.SamuelPuerto % 2 == 0

SamuelPuerto = Student(14)
print(SamuelPuerto.is_even())
#3203084
