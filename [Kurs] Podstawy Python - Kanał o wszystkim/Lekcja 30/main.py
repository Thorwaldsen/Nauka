class Czlowiek:
    def __init__(self, imie):
        self.imie = imie

    def przedstawSie(self):
        print("Cześć. Nazywam się " + self.imie)

    @classmethod
    def nowy_czlowiek(cls, imie):
        return cls(imie)

    @staticmethod
    def przywitaj(arg):
        print("Cześć " + arg)

cz1 = Czlowiek.nowy_czlowiek("Artur")
cz1.przedstawSie()
cz2 = cz1.nowy_czlowiek("Kamil")
cz2.przedstawSie()
Czlowiek.przywitaj("ziomeczku!")
cz2.przywitaj("człowieku!")
