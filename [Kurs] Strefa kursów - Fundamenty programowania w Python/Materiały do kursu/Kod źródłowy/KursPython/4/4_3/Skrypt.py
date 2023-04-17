"""
OGÓLNY FORMAT DEKLAROWANIA PARAMETRÓW I PRZEKAZYWANIA ARGUMENTÓW
def funkcja(parametr, parametr=wartość):
    wyrażenia i instrukcje na parametrach

funkcja(argument_pozycyjny, argument_kluczowy=wartość)
"""

# Przykład deklaracji parametrów i przekazywania argumentów


def iloczyn(a, b, c, d=5):
    wynik = a * b + c * d
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print("Wynik:", wynik)


iloczyn(2, c=3, b=4)
