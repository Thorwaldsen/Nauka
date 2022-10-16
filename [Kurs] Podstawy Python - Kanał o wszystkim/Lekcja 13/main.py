def dzielenie(dzielna, dzielnik):
    assert dzielnik != 0, "Dzielnik nie może wynosić zero"
    if dzielnik == 0:
        raise ZeroDivisionError("Dzielenie przez zero")
    else:
        print(dzielna/dzielnik)

try:
    dzielenie(10, 5)
except ZeroDivisionError:
    print("Błąd - dzielisz przez zero")
    raise
