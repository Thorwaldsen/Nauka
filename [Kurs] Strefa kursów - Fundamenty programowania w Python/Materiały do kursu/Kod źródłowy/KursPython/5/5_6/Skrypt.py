class Zamowienie:
    def __init__(self, koszyk, klient):
        self.koszyk = list(koszyk)
        self.klient = klient

    def __len__(self):
        return len(self.koszyk)

    def __add__(self, artykul):
        nowy_koszyk = self.koszyk.copy()
        nowy_koszyk.append(artykul)
        return Zamowienie(nowy_koszyk, self.klient)


zamowienie = Zamowienie(['jabłko', 'mleko', 'chleb'], 'Marcin Mikiciuk')
print(len(zamowienie))

zamowienie = zamowienie + 'masło' + 'szynka' + 'pomidor'
print(zamowienie.koszyk)
