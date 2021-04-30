class Pojazd:
    def __init__(self, marka, model, cena, poj_silnika, paliwo, przebieg, nr_tablica, bak, stan_baku):
        self.marka = marka
        self.model = model
        self.cena = cena
        self.poj_silnika = poj_silnika
        self.paliwo = paliwo
        self.przebieg = przebieg
        self.nr_tablica = nr_tablica
        self.bak = bak
        self.stan_baku = stan_baku

    def tankowanie(self):
        print("Zatankuj", self.paliwo)
        cena = 4.32
        ile_wlac = self.bak - self.stan_baku
        koszt = ile_wlac * cena
        print("Do pełna kosztuje ", koszt)

    def bak_stan(self):
        print("Stan twojego baku wynosi: ", self.stan_baku)
        wybor = input("Czy zatankować?")
        if wybor == "Tak" or wybor == "tak":
            self.tankowanie()
        else:
            print("No to nie.")

    def __del__(self):
        print("Usunięto")


class Samochod(Pojazd):
    def __init__(self, marka, model, cena, poj_silnika, paliwo, przebieg, ilosc_drzwi, poj_bagaznika, nr_tablica, bak,
                 stan_baku):
        super().__init__(marka, model, cena, poj_silnika, paliwo, przebieg, nr_tablica, bak, stan_baku)
        self.ilosc_drzwi = ilosc_drzwi
        self.poj_bagaznika = poj_bagaznika

    def bagaznik(self):
        print("Twój bagażnik ma :", self.poj_bagaznika, " pojemności")


class Motor(Pojazd):
    def __init__(self, marka, model, cena, poj_silnika, paliwo, przebieg, ilosc_miejsc, nr_tablica, bak, stan_baku):
        super().__init__(marka, model, cena, poj_silnika, paliwo, przebieg, nr_tablica, bak, stan_baku)
        self.ilosc_miejsc = ilosc_miejsc


# lista obiektów
samochod1 = Samochod("Fiat", "124", "13000", "1.6", "benzyna", "250000", "5", "300l", "ABC-1234", 40, 10)
motor1 = Motor("Kawasaki", "Ninja", "7000", "650", "benzyna", "200000", "2", "ABD-1242", "25", "5")
samochod1.bak_stan()