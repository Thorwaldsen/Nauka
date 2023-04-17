# Przykład funkcji zwracającej dane wyjściowe


def do_potegi(podstawa, wykladnik):
    return podstawa ** wykladnik


x = do_potegi(2, 10)
print(x, type(x))

# Przykład wielokrotnego wykorzystania instrukcji return w jednej funkcji
from typing import Union


def sprawdz_dane(dane: list) -> Union[tuple[int, list], list]:
    for element in dane:
        if element is None:
            idx = dane.index(element)
            print(f"Przekazane dane są niepoprawne. Element {idx} jest typu None.")
            return idx, dane

    print("Przekazane dane są poprawne.")
    return dane


zbior_danych = [1, 2, 3, 4, None, 6, 7, 8, 9]
wynik = sprawdz_dane(zbior_danych)
print("Wynik:", wynik, type(wynik))
