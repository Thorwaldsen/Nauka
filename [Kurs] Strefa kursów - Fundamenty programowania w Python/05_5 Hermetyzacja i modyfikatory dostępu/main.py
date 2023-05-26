class Firma:
    def __init__(self):
        self._projekt = "C3P0"
        self.__finansowania = "GOV"

class Pracownik(Firma):
    def __init__(self, pracownik):
        self.pracownik = pracownik
        Firma.__init__(self)

    def wyswietl_informacje(self):
        print("Pracownik:", self.pracownik)
        print("Pracuje nad:", self._projekt)


p = Pracownik("Bob")
p.wyswietl_informacje()

