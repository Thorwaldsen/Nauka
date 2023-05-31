import random
from time import sleep

class Wojownik():
    def __init__(self, imie='anonim', punkty_zycia=0, punkty_ataku=0, punkty_obrony=0):
        self.imie = imie
        self.punkty_zycia = punkty_zycia
        self.punkty_ataku = punkty_ataku
        self.punkty_obrony = punkty_obrony

    def atak(self):
        return random.randint(0, self.punkty_ataku) * random.randint(2, 5)

    def obrona(self):
        return random.randint(0, self.punkty_obrony)

    def zadaneObrazenia(self, ilosc):
        self.punkty_zycia -= ilosc
        if self.punkty_zycia <= 0:
            print(self.imie, "poległ w walce")

    def czyPostacZywa(self):
        if self.punkty_zycia <= 0:
            return False
        else:
            return True

    def __str__(self):
        return self.imie


def walka(malpa, rycerz):
    numer_rundy = 1
    while(malpa.czyPostacZywa() and rycerz.czyPostacZywa()):
        print("Runda numer", numer_rundy)
        wyswietl_statystyki(malpa, rycerz)

        if random.randint(0, 1) == 0:
            pojedynek(malpa, rycerz)
        else:
            pojedynek(rycerz, malpa)

        print('')
        sleep(3)
        numer_rundy += 1

    if rycerz.czyPostacZywa():
        print('Rycerz wygrał walkę')
    else:
        print("Małpi wojownik wygrał walkę")


def pojedynek(postac1, postac2):
    print(postac1, "został zaatakowany przez", postac2)
    obrazenia = postac2.atak() - postac1.obrona()
    print(postac1, "stracil ", obrazenia, "punktów życia.")
    postac1.zadaneObrazenia(obrazenia)

def wyswietl_statystyki(postac1, postac2):
    for postac in (postac1, postac2):
        print(postac, " ma ", postac.punkty_zycia, " punktów życia.")

rycerz = Wojownik("Rycerz", random.randint(100, 1000), random.randint(10, 50), random.randint(5, 30))
malpa = Wojownik("Małpi wojownik", random.randint(100, 1000), random.randint(10, 50), random.randint(5, 30))

walka(malpa, rycerz)