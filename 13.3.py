class smartfon:
    def __init__(self, marka, typ, kolor, pojemnosc, ekran):
        self.marka = marka
        self.typ = typ
        self.kolor = kolor
        self.pojemnosc = pojemnosc
        self.ekran = ekran
    def info(self):
        print("Marka:", self.marka)
        print("Typ:", self.typ)
        print("Kolor:", self.kolor)
        print("Pojemność:", self.pojemnosc, "litrów")
        print("Ekran:", self.ekran)
    def pomoc(self):
        print("Zostałes umówiony do serwisu")

iphone = smartfon("iphone", "smartfon", "czarny", 64, "ips")
samsung = smartfon("samsung", "smartfon", "biały", 128, "oled")

iphone.info()
iphone.pomoc()
print("-------------")
samsung.info()
samsung.pomoc()