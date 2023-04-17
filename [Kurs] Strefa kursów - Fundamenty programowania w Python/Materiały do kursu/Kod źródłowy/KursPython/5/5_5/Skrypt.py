class Firma:
    def __init__(self):
        self._projekt = 'TR3B'
        self.__finansowanie = 'GOV'


class Pracownik(Firma):
    def __init__(self, pracownik):
        self.pracownik = pracownik
        Firma.__init__(self)

    def wyswietl_informacje(self):
        print("Pracownik:", self.pracownik)
        print("Pracuje nad:", self._projekt)


p = Pracownik("Bob")
p.wyswietl_informacje()
