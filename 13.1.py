class Samochod:
    def __init__(self, brand, age, type, color, capacity, fuelType):
        self.brand = brand
        self.age = age
        self.type = type
        self.color = color
        self.capacity = capacity
        self.fuelType = fuelType
    def tankowanie(self):
        print("Zatankowano: {} {} litrów ".format(self.fuelType, self.capacity))
    def info(self):
        print("Marka:", self.brand)
        print("Wiek:", self.age, "lat")
        print("Kolor:", self.color)
        print("Pojemność baku:", self.capacity, "litrów")
        print("Rodzaj paliwa:", self.fuelType)
    def kolor(self, newColor):
        print("Zmieniono kolor z {} na {}".format(self.color, newColor))
    def szybkosc(self):
        if(self.color == "red"):
            print("Szybko")
        else:
            print("Nie tak szybki jak czerwony")
    def serwis(self):
        print("Jesteś 2 w kolejce")

opel = Samochod("Opel", 10, "kombi", "brązowy", 50, "benzyna")
ferrari = Samochod("Ferrari", 5, "kabriolet", "czerwony", 45, "benzyna")

opel.tankowanie()
opel.kolor("czarny")
opel.info()
opel.szybkosc()
opel.serwis()
print("-------------")
ferrari.tankowanie()
ferrari.info()
ferrari.szybkosc()
ferrari.serwis()