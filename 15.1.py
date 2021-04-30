class Restaurant:
    def __init__(self, nazwa):
        self.nazwa= nazwa

    def restauracja(self):
        print("Restauracja " + self.nazwa + " wita wszystkich gości")

class IceCreamStand(Restaurant):
    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.flavors = []

    def pokaz_smaki(self):
        print("Mamy takie smaki do wyboru:")
        for smak in self.flavors:
            print("- " + smak.title())

class Coffee(Restaurant):
    def __init__(self, nazwa):
        super().__init__(nazwa)
        self.coffee = []

    def pokaz_kawy(self):
        print("Mamy takie kawy do wyboru:")
        for kawa in self.coffee:
            print("- " + kawa.title())


lodziarnia = IceCreamStand("Top1 lody na swiecie")
lodziarnia.flavors = ['truskawka', 'wanilia', 'czekolada', 'straciatella']

kawiarnia = Coffee("Top1 kawy na swiecie")
kawiarnia.coffee = ['americano', 'latte', 'gbs', 'kawa mrozona']

lodziarnia.restauracja()
lodziarnia.pokaz_smaki()

kawiarnia.restauracja()
kawiarnia.pokaz_kawy()