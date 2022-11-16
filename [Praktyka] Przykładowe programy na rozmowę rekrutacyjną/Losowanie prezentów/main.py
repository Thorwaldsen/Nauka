import random
from random import randint

listaGosci = {
    1: "Artur Rosiek",
    2: "Paulina",
    3: "Ludwik",
    4: "Anita",
    5: "Norbert",
    6: "Artur Wochal",
    7: "Dorian",
    8: "Grzesiu",
    9: "Iza",
    10: "Polańska",
    11: "Karolina",
    12: "Kasia",
    13: "Krzychu",
    14: "Kuba od Patki",
    15: "Kuba od Kasi",
    16: "Michał",
    17: "Święta",
    18: "Patryk",
    19: "Sylwia",
    20: "Weronika",
}

pomieszanaListaGosci = list(listaGosci.items())
random.shuffle(pomieszanaListaGosci)
listaGosci2 = dict(pomieszanaListaGosci)

dlugoscListy = len(listaGosci)

randomizer = random.sample(range(1, 21), 20)
wytypowane = [20]
ok = True


def losowanie():
    licznik = 0
    global ok
    while ok:
        for i in range(dlugoscListy):
            if listaGosci[i+1] != listaGosci2[randomizer[i]]:
                licznik += 1
                if licznik == 20:
                    print("Na imprezie będzie", licznik, "osób.")
                    for j in range(dlugoscListy):
                        if listaGosci[i+1] != listaGosci2[randomizer[i]]:
                            print(j+1, ":", listaGosci[j+1], "kupuje prezent dla", listaGosci2[randomizer[j]])
                            ok = False


losowanie()
