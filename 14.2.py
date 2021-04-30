class Zwierze:
    def __init__(self, gatunek):
        self.gatunek = gatunek

    def printgatunek(self):
        print("Tutaj:" + self.gatunek)

class Kot(Zwierze):
    def miaucze(self):
        print("Umiem miauczeć")

class Pies(Zwierze):
    def szczekam(self):
        print("Umiem szczekać")

class Ptak(Zwierze):
    def latam(self):
        print("Umiem latać")

class Ryba(Zwierze):
    def oddycham(self):
        print("Umiem oddychać pod wodą")

kot1 = Kot("Kot")
pies1 = Pies("Pies")
ptak1= Ptak("Ptak")
ryba1= Ryba("Ryba")

kot1.printgatunek()
kot1.miaucze()
print("-------")
pies1.printgatunek()
pies1.szczekam()
print("-------")
ptak1.printgatunek()
ptak1.latam()
print("-------")
ryba1.printgatunek()
ryba1.oddycham()
print("-------")