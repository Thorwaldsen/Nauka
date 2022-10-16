class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstawSie(self, powitanie = "Cześć"):
        return powitanie + ", mam na imie " + self.imie + " i mam " + str(self.wiek) + "."


objekt = Czlowiek("Artur", 30)
print(objekt.imie)
print(objekt.przedstawSie("Witam"))

objekt2 = Czlowiek("Kamil", 30)
objekt2.imie = "Kamil"
print(objekt2.imie)
print(objekt2.przedstawSie())