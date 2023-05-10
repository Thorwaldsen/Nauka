"""
for(dla) elementu in(w) obiekcie_iterowalnym:
    wykonaj zawarte tutaj instrukcje (w bloku)
else(w przeciwnym razie):
    wykonaj zawarte tutaj instrukcje,
    gdy pętla zakończy swoje działanie
"""

# wyraz = "Konstantynopoliltańczykowianeczka"
# for litera in wyraz:
#     print(litera, end=". ")

# suma = 0
# for liczba in range(1, 25):
#     print(suma, end=" | ")
#     suma += liczba # Ekwiwalent suma = suma + liczba
# else:
#     print("Suma:", suma)

# lista_krotek = [('a', 1), ('b', 2), ('c', 3)]
# for litera, liczba in lista_krotek:
#     print(litera, liczba)

# planeta_ziemia = dict([
#     ("Typ planety", "Planeta skalista"),
#     ("Masa (kg)", 5.91219e24),
#     ("Promień równikowy (km)", 6_378.137),
#     ("Promień biegunowy (km)", 6_356.752),
#     ("Obwód (km)", 40_075.014),
#     ("Okres obrotu (h)", 23.9345),
#     ("Przyspieszenie grawitacyjne (m/s2)", 9.80665),
#     ("Prędkość ucieczki (km/s)", 11.19)
# ])
# for (klucz, wartość) in planeta_ziemia.items():
#     print(klucz + ":", wartość)

for i in range(1, 11):
    for j in range(1, 11):

        liczba = str(i*j)
        dlugosc_liczby = len(liczba)

        if dlugosc_liczby == 1:
            liczba = "  " + liczba
        elif dlugosc_liczby == 2:
            liczba = " " + liczba

        print(liczba, end=" | ")
    print()
