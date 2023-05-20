# def funkcja(*args, **kwargs):
#     print(args, type(args))
#     print(kwargs, type(kwargs))
#
#
# funkcja(1, 2, 3, kwarg_1=4, kwarg_2=5, kwarg_3=6)

"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    ------------     ----------     ----------
          |              |               |
    Tylko pozycyjne      |               |
               Pozycyjne lub kluczowe    |
                                    Tylko kluczowe
"""


def k(a, b, /, c, d, *, e, f):
    print("a:", a, type(a))
    print("b:", b, type(b))
    print("c:", c, type(c))
    print("d:", d, type(d))
    print("e:", e, type(e))
    print("f:", f, type(f))


k(1, 2, c=3, d=4, e=5, f=6)
