class KontoBankowe:
    __stanKonta = 0

    @property
    def stanKonta(self):
        return self.__stanKonta

    @stanKonta.getter
    def stanKonta(self):
        return "Stan konta: " + str(self.__stanKonta) + "zł"

    @stanKonta.setter
    def stanKonta(self, value):
        self.__stanKonta += value

konto = KontoBankowe()
print(konto.stanKonta)

konto.stanKonta = 50
print(konto.stanKonta)

konto.stanKonta = 100
print(konto.stanKonta)

konto.stanKonta = -150
print(konto.stanKonta)

