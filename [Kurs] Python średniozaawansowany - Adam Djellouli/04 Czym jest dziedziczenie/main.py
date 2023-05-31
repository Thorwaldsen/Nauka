class Ryba():
    def __init__(self, imie="Nemo", wiek=0):
        self.imie = imie
        self.wiek = wiek

    def wyswietl(self):
        print("Jestem", self.imie, "i mam", self.wiek, "lat.")

class Tuńczyk(Ryba):
    def __init__(self, imie, wiek):
        super().__init__(imie, wiek)

    def wyswietl(self):
        super().wyswietl()
        print("A w dodatku jestem fajnym tuńczykiem")

    def pozegnanie(self):
        print(self.imie, "was zegna")

james = Ryba("James", 100)
george = Tuńczyk("George", 34)

james.wyswietl()
george.wyswietl()
george.pozegnanie()

print(type(james))
print(type(george))

print("Czy james jest rybą? " + str(isinstance(james, Ryba)))
print("Czy james jest tuńczykiem? " + str(isinstance(james, Tuńczyk)))

print("Czy george jest rybą? " + str(isinstance(george, Ryba)))
print("Czy george jest tuńczykiem? " + str(isinstance(george, Tuńczyk)))