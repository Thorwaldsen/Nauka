class Klasa:
    x = 0
    y = 0

    def powitanie(self):
        return "Witaj Kursancie!", self

    def ustaw_wartosci_instancyjnie(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def ustaw_wartosci_klasowo(cls, x, y):
        cls.x = x
        cls.y = y

    @staticmethod
    def metoda_statyczna():
        print("To jest metoda statyczna.")


k = Klasa()
print(k.powitanie())

x = 5
y = 9
print(k.x, k.y)
k.ustaw_wartosci(x, y)
print(k.x, k.y)

Klasa.metoda_statyczna()
