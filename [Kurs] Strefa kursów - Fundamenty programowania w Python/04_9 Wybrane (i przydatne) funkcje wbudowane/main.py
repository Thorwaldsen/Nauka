#x = complex(2, 3)
# print(x, type(x))
#
# x_abs = abs(x)
# print(x_abs, type(x_abs))
#
# x_round = round(x_abs, 2)
# print(x_round, type(x_round))
# dane = [1, 2, 3, 4, 5, 6]
# dane_min = min(dane)
# dane_max = max(dane)
# dane_sum = sum(dane)
# print("Dane:", dane, type(dane))
# print("wartość minimalna:", dane_min, type(dane_min))
# print("Wartość maksymalna:", dane_max, type(dane_max))
# print("Suma wartości:", dane_sum, type(dane_sum))
dane = [9, 8, 7, 6, 5, 4, 3, 2, 1]
dane_odwrocone = list(reversed(dane))
daje_enum = enumerate(dane_odwrocone)
for nr_iter, element in daje_enum:
    print("Nr iteratora:", nr_iter, "Element:", element, "Do kwadratu", pow(element, 2))