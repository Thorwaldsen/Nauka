def potega(a):
    return a ** 2


# przypisanie funkcji do nazwy "g"
g = potega
print(g(2))
print(potega(2))


# przekazujemy funkcję jako parametr innej funkcji
def wyswietl_obliczenia(funkcja, lista):
    for x in lista:
        print(funkcja(x))


def zwieksz2(a):
    return a + 2


lista = [1, 3, 5]

wyswietl_obliczenia(g, lista)
wyswietl_obliczenia(zwieksz2, lista)


# Mozemy zwracac funkcje
def zwieksz_liczbe(a):
    def zwieksz(liczba):
        print("a to: ", a)
        print("Liczba to: ", liczba)
        return a + liczba

    return zwieksz


g = zwieksz_liczbe(8)
print(g(4))
print(zwieksz_liczbe(9)(7))

# mozemy umieszczać funkcję w strukturach danych
lista_funkcji = [potega, zwieksz2]
for funkcja in lista_funkcji:
    for x in lista:
        print(funkcja(x))
