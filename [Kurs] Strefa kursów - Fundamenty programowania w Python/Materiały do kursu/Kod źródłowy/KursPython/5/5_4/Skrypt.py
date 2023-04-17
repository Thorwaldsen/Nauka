class Prostokat:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def obwod(self):
        return 2 * self.dlugosc + 2 * self.szerokosc

    def pole_powierzchni(self):
        return self.dlugosc * self.szerokosc


class Kwadrat(Prostokat):
    def __init__(self, dlugosc):
        super().__init__(dlugosc=dlugosc, szerokosc=dlugosc)


class Szescian(Kwadrat):
    def pole_powierzchni(self):
        pole_czastkowe = super().pole_powierzchni()
        return pole_czastkowe * 6

    def objetosc(self):
        pole_czastkowe = super().pole_powierzchni()
        return pole_czastkowe * self.dlugosc


prostokat = Prostokat(dlugosc=10, szerokosc=5)
kwadrat = Kwadrat(dlugosc=7)
szescian = Szescian(dlugosc=9)

print('prostokat.dlugosc', prostokat.dlugosc, 'prostokat.szerokosc', prostokat.szerokosc)
print('kwadrat.dlugosc', kwadrat.dlugosc)
print('szescian.dlugosc', szescian.dlugosc)

print('P obwód:', prostokat.obwod(), 'P pole:', prostokat.pole_powierzchni())
print('K obwód:', kwadrat.obwod(), 'K pole:', kwadrat.pole_powierzchni())
print('Sz pole powierzchni:', szescian.pole_powierzchni(), 'Sz objętość:', szescian.objetosc())
