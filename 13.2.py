class Książka:
    def __init__(self, autor, tytul, oprawa, strony, przykladowy_tekst, koniec):
        self.tytul = tytul
        self.autor = autor
        self.oprawa = oprawa
        self.strony = strony
        self.przykladowy_tekst = przykladowy_tekst
        self.koniec = koniec
    def moja_nazwa(self):
        print(self.autor)
        print(self.tytul)
        print(self.oprawa)
        print(self.strony)
        print(self.przykladowy_tekst)
        print(self.koniec)
wiedzmin = Książka("Sapkowski Andrzej", "Wiedźmin - ostatnie rozszczenie", "twarda", 300, "wiedzmin", "----------")
malyksiaze = Książka("Antoine de Saint-Exupery", "Mały Książe", "twarda", 80, "róża", "----------")
ksiazki = []
def Main():
    ksiazki.append(wiedzmin)
    ksiazki.append(malyksiaze)
    print("Witaj!")
    analizuj()
    while True:
        choice = input("Czy chcesz wykonać jeszcze jakąś operację? Tak / Nie")
        if choice == "Tak":
            analizuj()
        else:
            break
def analizuj():
    choice = input("Czy chcesz dodać nową książke lub wyświetlić listę obecnie istniejących książek? wybierz 1 lub 2")
    if (choice == "1"):
        dodajksiążka()
    else:
        print ("Książki:")
        pokazksiazki()
def dodajksiążka():
    autor = input("Podaj autora: Nazwisko Imie")
    tytul = input("Podaj tytuł")
    oprawa = input("Podaj rodzaj oprawy")
    strony = int(input("Podaj ilość stron"))
    przykladowy_tekst = input("Podaj przykładowy fragment tekstu")
    książka = Książka(autor, tytul, oprawa, strony, przykladowy_tekst)
    print("Dodano nową książke!")
    ksiazki.append(książka)
def pokazksiazki():
    ksiazki.sort(key=SortKey)
    for i in ksiazki:
        i.moja_nazwa()
def SortKey(obj):
    return obj.autor
Main()