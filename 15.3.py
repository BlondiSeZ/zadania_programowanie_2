class Obywatel:
    def __init__(self, imie, nazwisko, ulica, nr_domu, kod_pocztowy, miejscowosc):
        self.nazwisko = nazwisko
        self.imie = imie
        self.ulica = ulica
        self.nr_domu = nr_domu
        self.kod_pocztowy = kod_pocztowy
        self.miejscowosc = miejscowosc
    def Wizytowka(self):
        print("-----------------" + "\n" + self.imie + " " + self.nazwisko)
        print("ul." + self.ulica + " " + str(self.nr_domu))
        print(str(self.kod_pocztowy) + " " + self.miejscowosc + "\n-----------------")
gosciu1 = Obywatel("Andrzej", "Sapkowski", "Zbożowa", 36, "95-398", "Michałów")
obywatele = []
def Main():
    obywatele.append(gosciu1)
    print("Witaj!")
    AnalizeChoice()
    while True:
        choice = input("Czy chcesz wykonać jeszcze jakąś operację? tak / nie ")
        if choice == "tak":
            AnalizeChoice()
        else:
            break
def AnalizeChoice():
    choice = input("Czy chcesz dodać nowego obywatela czy wyswietlic istiniejących? wybierz 1 lub 2 ")
    if (choice == "1"):
        AddObywatel()
    else:
        Showobywatele()
def AddObywatel():
    imie = input("Podaj imie ")
    nazwisko = input("Podaj nazwisko ")
    ulica = input("Podaj nazwe ulicy ")
    nr_domu = int(input("Podaj numer domu "))
    kod_pocztowy = input("Podaj kod pocztowy ")
    miejscowosc = input("Podaj miejscowość " )
    gosciu = Obywatel(imie, nazwisko, ulica, nr_domu, kod_pocztowy, miejscowosc)
    print("Dodano nowego obywatela!")
    obywatele.append(gosciu)
def Showobywatele():
    obywatele.sort(key=SortKey)
    for a in obywatele:
        a.Wizytowka()
def SortKey(obj):
    return obj.imie

Main()