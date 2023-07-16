class Wezel():
    def __init__(self, dane=None):
        self.dane = dane
        self.nastepny = None


class Lista():
    def __init__(self):
        self.head = Wezel()

    def append(self, dane):
        dostawiany_wezel = Wezel(dane)
        if self.head.dane == None:
            self.head = dostawiany_wezel
        else:
            licznik = self.head
            while licznik.nastepny != None:
                licznik = licznik.nastepny
            licznik.nastepny = dostawiany_wezel

    def wyswietl(self):
        licznik = self.head
        print(licznik.dane)
        while licznik.nastepny != None:
            print(licznik.nastepny.dane)
            licznik = licznik.nastepny

    def dlugosc(self):
        licznik = self.head
        if self.head.dane == None:
            return 0
        wynik = 1
        while licznik.nastepny != None:
            licznik = licznik.nastepny
            wynik += 1
        return wynik

    def usun(self, i):
        if self.head.dane == None:
            print("Lista jest pusta")
            return
        if i >= self.dlugosc() or i < 0:
            print("Zły indeks")
            return
        if i == 0:
            self.head = self.head.nastepny
        licznik = self.head
        pozycja = 0
        while licznik.nastepny != None:
            poprzednik = licznik
            licznik = licznik.nastepny
            if pozycja+1 == i:
                poprzednik.nastepny = licznik.nastepny
                return
            pozycja += 1

    def podziel(self):
        dlugosc = self.dlugosc()
        if dlugosc == 0:
            return None
        if dlugosc == 1:
            return None

        a = Lista()
        b = Lista()

        srodek = int(dlugosc/2)
        licznik = self.head
        pozycja = 0
        while pozycja < srodek:
            a.append(licznik.dane)
            licznik = licznik.nastepny
            pozycja += 1
        while licznik:
            b.append(licznik.dane)
            licznik = licznik.nastepny

        return a, b

lista = Lista()

lista.append(3)
lista.append(4)
lista.append(6)
lista.append(7)
lista.append(9)
lista.append(11)

a, b = lista.podziel()

print("Lista A:")
a.wyswietl()
print("Lista B:")
b.wyswietl()


