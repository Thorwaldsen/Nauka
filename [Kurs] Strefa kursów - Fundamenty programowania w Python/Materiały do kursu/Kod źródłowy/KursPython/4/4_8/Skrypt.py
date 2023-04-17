# Tworzenie liczby zespolonej 2+3i.
x = complex(2, 3)
print(x, type(x))

# Wyliczanie wartości bezwzględnej.
x_abs = abs(x)
print(x_abs, type(x_abs))

# Zaokrąglanie do dwóch miejsc po przecinku.
x_round = round(x_abs, 2)
print(x_round, type(x_round))

# Funkcje min, max i sum.
dane = [1, 2, 3, 4, 5, 6]
print("Dane:", dane, type(dane))
dane_min = min(dane)
print("Wartość minimalna:", dane_min, type(dane_min))
dane_max = max(dane)
print("Wartość maksymalna:", dane_max, type(dane_max))
dane_sum = sum(dane)
print("Suma wartości:", dane_sum, type(dane_sum))

# Odwracanie elementów w liście.
dane = [9, 8, 7, 6, 5, 4, 3, 2, 1]
dane_odwrocone = list(reversed(dane))

# Tworzenie obiektu wyliczeniowego.
dane_enum = enumerate(dane_odwrocone)
for nr_iter, element in dane_enum:
    print("Nr iteratora:", nr_iter, "Element:", element, "Do kwadratu:",
          pow(element, 2))
