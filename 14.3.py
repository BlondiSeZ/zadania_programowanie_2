import math
class Figura:
    def __init__(self, figura):
        self.figura = figura

def Pole():
    rodzaj = input("Podaj rodzaj figury (kwadrat(1), prostokat(2), trójkąt(3), koło(4), romb(5), trapez(6)): ")
    if rodzaj == "1":
        a = int(input("Podaj długość boku: "))
        P = a*a
        L = 4*a
        print ("Pole to :", P)
        print ("Obwód to :", L)
    elif rodzaj == "2":
        a = int(input("Podaj długość boku a: "))
        b = int(input("Podaj długość boku b: "))
        P = a*b
        L = 2*a + 2*b
        print ("Pole to :", P)
        print ("Obwód to :", L)
    elif rodzaj == "3":
        a = int(input("Podaj długość podstawy : "))
        b = int(input("Podaj długość jednego boku : "))
        c = int(input("Podaj długość drugiego boku : "))
        h = int(input("Podaj długość wysokosci: "))
        P = (a*h)/2
        L = a+b+c
        print ("Pole to :", P)
        print("Obwód to :", L)
    elif rodzaj == "4":
        r = int(input("Podaj długość promienia : "))
        P = r*(math.pi)
        L = r*r*(math.pi)
        print ("Pole to :", P)
        print("Obwód to :", L)
    elif rodzaj == "5":
        a = int(input("Podaj długość boku a: "))
        h = int(input("Podaj długość wysokości: "))
        P = a*h
        L = 4*a
        print ("Pole to :", P)
        print("Obwód to :", L)
    elif rodzaj == "6":
        a = int(input("Podaj długość pierwszej podstawy: "))
        b = int(input("Podaj długość drugiej podstawy: "))
        c = int(input("Podaj długość boku c: "))
        d = int(input("Podaj długość boku d: "))
        h = int(input("Podaj długość wysokości: "))
        P = ((a+b)*2)/h
        L = a+b+c+d
        print ("Pole to :", P)
        print("Obwód to :", L)
    else:
        print("nara")

Pole()