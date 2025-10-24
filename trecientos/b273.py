class BST:
    def __init__(self, SamuelPuerto):
        self.SamuelPuerto = {'value': SamuelPuerto}
    def update(self, SamuelPuerto):
        if SamuelPuerto > self.SamuelPuerto['value']:
            self.SamuelPuerto['value'] = SamuelPuerto

SamuelPuerto = BST(5)
SamuelPuerto.update(10)
print(SamuelPuerto.SamuelPuerto)
#3203084
