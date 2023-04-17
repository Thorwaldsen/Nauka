"""
OGÓLNY FORMAT WYMUSZANIA KOLEJNOŚCI PRZEKAZYWANIA ARGUMENTÓW
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      ----------     ----------     ----------
          |              |              |
    Tylko pozycyjne      |              |
                Pozycyjne lub kluczowe  |
                                 Tylko kluczowe
"""

# Przykład funkcji przyjmującej nieokreśloną liczbę argumentów pozycyjnych
# oraz kluczowych


def funkcja(a, b, *args, c, d, **kwargs):
    print("a:", a, type(a))
    print("b:", b, type(b))
    print(args, type(args))
    print()
    print("c:", c, type(c))
    print("d:", d, type(d))
    print(kwargs, type(kwargs))


funkcja(1, 2, 3, 4, c=5, d=6, e=7, f=8)

# Przykład funkcji wykorzystującej specjalne parametry wymuszające
# określoną kolejność przekazywania argumentów danego typu do funkcji


def k(a, b, /, c, d, *, e, f):
    print("a:", a, type(a))
    print("b:", b, type(b))
    print("c:", c, type(c))
    print("d:", d, type(d))
    print("e:", e, type(e))
    print("f:", f, type(f))


k(1, 2, 3, d=4, e=5, f=6)
