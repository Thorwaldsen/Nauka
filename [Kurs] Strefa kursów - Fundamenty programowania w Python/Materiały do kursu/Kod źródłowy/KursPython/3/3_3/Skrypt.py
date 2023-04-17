"""
OGÓLNY FORMAT PĘTLI FOR
for(dla) elementu in(w) obiekcie_iterowalnym:
    wykonaj zawarte tutaj(w bloku) instrukcje
else(w przeciwnym razie):
    wykonaj zawarte tutaj instrukcje,
    gdy pętla zakończy swoje działanie
"""

# PRZYKŁADY PĘTLI
for litera in "Marcin Mikiciuk":  # Iterowanie po łańcuchu znaków
    print(litera)

for liczba in [1, 2, 3]:  # Iterowanie po liście
    print(liczba)

for litera in ('a', 'b', 'c'):  # Iterowanie po krotce
    print(litera)

for (a, b) in [('a', 1), ('b', 2)]:  # Iterowanie po liście krotek
    print(a, b)

for klucz in {"Klucz": 1}:  # Iterowanie po kluczach słownika
    print(klucz)

for (klucz, wartość) in {"Klucz": 1}.items():  # Iterowanie po parach klucz-wartość słownika
    print(klucz, wartość)

for i in range(5):  # Przykład pętli zagnieżdżonej
    for j in range(5):
        print(i, j)

for i in "Rzekłem":  # Przykład wykorzystania pętli for z klauzulą else
    print(i, end="")
else:
    print(".")
