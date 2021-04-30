def getpietra():
    pietra = int(input("Podaj ilość pięter: "))
    if pietra < 0:
        print("Podaj ilość większą niż 0: ")
    else:
        return pietra


def getpokoje():
    pokoje = int(input("Ile pokoi jest na tym piętrze: "))
    if pokoje <= 5:
        print("Podaj numer większy niż 5: ")
        raise SystemExit
    else:
        return pokoje


def zajetepokoje(pokoje):
    zajete_pokoje = int(input("Ile pokoi jest zajętych? "))
    if zajete_pokoje > pokoje:
        print("Hotel jest pełny ")
    else:
        occRate = zajete_pokoje / pokoje
        print("Wspołczynnik zajętych pokoi to: ", occRate)
        return occRate, zajete_pokoje


def hotel():
    totalOcc = 0
    totalpokoje = 0
    totalOccRate = 0
    pietra = getpietra()
    for room in range(pietra):
        pokoje = getpokoje()
        occRate, zajete_pokoje = zajetepokoje(pokoje)
        totalpokoje = totalpokoje + pokoje
        totalOcc = totalOcc + zajete_pokoje
        totalOccRate = totalpokoje / totalOcc
    print("Lączny numer pokoi: ", str(totalpokoje))
    print("Laczny numer zajetych pokoi: ", str(totalOcc))
    print("Wspolczynnik zajetych pokoi:  ", str(totalOccRate))


hotel()
