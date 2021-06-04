class BmrCalculator:

    def woman_ppm(self, waga, wzrost, wiek):
        return 655.1 + (9.563 * waga) + (1.85 * wzrost) - (4.676 * wiek)

    def men_ppm(self, waga, wzrost, wiek):
        return 66.5 + (13.75 * waga) + (5.003 * wzrost) - (6.775 * wiek)

if __name__=='__main__':
    bmr = BmrCalculator()
    print(bmr.men_ppm(73, 181, 21))