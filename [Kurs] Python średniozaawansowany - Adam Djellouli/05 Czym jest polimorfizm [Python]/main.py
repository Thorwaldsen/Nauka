# polimorfizm umozliwia uzycie metody tej samej nazwy w roznych klasach

class Ksztalt:
    def __init__(self, nazwa='Ksztalt'):
        self.nazwa = nazwa

    def pole(self):
        print('Brak danych na temat', self.nazwa)


class Trojkat(Ksztalt):
    def __init__(self, nazwa='Trojkat', a=2, h=2):
        super().__init__(nazwa)
        self.a = a
        self.h = h

    def pole(self):
        print('Pole figury', self.nazwa, 'wynosi', self.a * self.h / 2)


def wyswietl_pole(lista):
    for x in lista:
        x.pole()


ksztalt = Ksztalt()
trojkat = Trojkat()

lista = [ksztalt, trojkat]

wyswietl_pole(lista)
