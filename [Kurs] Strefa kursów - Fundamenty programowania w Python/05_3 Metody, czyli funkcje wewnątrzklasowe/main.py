class MojaKlasa:
    x = 0
    y = 0

    def metoda(self):
        return 'metoda instancyjna', self

    @classmethod
    def metoda_klasowa(cls):
        return 'metoda klasowa', cls

    @staticmethod
    def metoda_statyczna():
        return 'metoda statyczna'


instancja = MojaKlasa()
print(instancja.metoda())
print(instancja.metoda_klasowa())

print(MojaKlasa.metoda_statyczna())
print(instancja.metoda_statyczna())
