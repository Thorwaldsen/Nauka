# Przykład przekazywania nieokreślonej liczby argumentów pozycyjnych


def pole_kola(*args, pi=3.14159):
    print("Przekazane argumenty:", args, type(args))
    promienie = args
    nr_figury = 1
    for promien in promienie:
        wynik = pi * promien ** 2
        print("Pole koła nr", nr_figury, "wynosi:", wynik)
        nr_figury += 1


pole_kola(1, 2, 3, 4, 5, 6, 7, pi=3.14)
