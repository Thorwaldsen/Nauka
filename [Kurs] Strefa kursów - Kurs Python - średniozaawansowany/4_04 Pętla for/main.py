kolory = ["Niebieski", "Zielony", "Czerwony", "Biały", "Czarny"]
licznik = 0

ulubiony_kolor = input("Podaj swój ulubiony kolor\n")
ulubiony_kolor.lower()

for kolor in kolory:
    licznik += 1
    if kolor == ulubiony_kolor:
        print(licznik, "kolor to {}".format(kolor.lower()), "- jest to mój ulubiony kolor")
    else:
        print(licznik, "kolor to {}".format(kolor.lower()))
