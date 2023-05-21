# def do_potęgi(podstawa, wykładnik):
#     return podstawa ** wykładnik
#
#
# x = do_potęgi(2, 10)
# print(x, type(x))
def sprawdz_dane(dane: list) -> tuple[int, list] | list:
    for element in dane:
        if element is None:
            idx = dane.index(element)
            print(f"Przekazane dane nie są poprawne. Element {idx} jest typu None.")
            return idx, dane

    print("Przekazane dane są poprawne.")
    return dane


zbior_danych = [1, 2, 3, 4, None, 6, 7, 8, 9]
wynik = sprawdz_dane(zbior_danych)
print("Wynik:", wynik, type(wynik))
