class Tunczyk:
    # Tworzymy zmienną statyczną
    ilosc_tunczykow = 0

    def __init__(self, imie):
        self.imie = imie
        Tunczyk.ilosc_tunczykow += 1

    # Tworzymy metodę statyczną
    @staticmethod
    def getIloscTunczykow():
        print("Aktualna ilosc tunczyków to", Tunczyk.ilosc_tunczykow)

    # Nadpisujemy destruktor
    def __del__(self):
        print("Tunczyk ", self.imie, "został usunięty")
        Tunczyk.ilosc_tunczykow -= 1


Tunczyk.getIloscTunczykow()

tunczyk1 = Tunczyk("James")
Tunczyk.getIloscTunczykow()

tunczyk2 = Tunczyk("Greg")
Tunczyk.getIloscTunczykow()

del tunczyk2
Tunczyk.getIloscTunczykow()
