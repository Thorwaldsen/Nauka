class Osoba:
    def __init__(self, imie="Anon", wiek=0, zarobki=0):
        self.imie = imie
        self.wiek = wiek
        self.zarobki = zarobki

    def przywitanie(self):
        print('Hej, jestem', self.imie, 'i mam', self.wiek, 'lat')


Ja = Osoba('Artur', 30, 5500.0)
James = Osoba('James', 35, 6500.0)
Anon = Osoba()

print(Ja.imie, Ja.wiek, Ja.zarobki)
print(James.imie, James.wiek, James.zarobki)
print(Anon.imie, Anon.wiek, Anon.zarobki)

Ja.przywitanie()
James.przywitanie()
Anon.przywitanie()