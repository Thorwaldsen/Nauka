# Zadanie polaga na tym że trzeba podzielić lody. Jeśli lody można podzielić równo wtedy dzielimy.
# Jeśli wyjdzie nierówno to wtedy zachowujemy lody dla siebie

liczbaRodzenstwa = int(input("Podaj ilość rodzeństwa: "))
liczbaLodow = int(input("Podaj liczbę lodów do podziału: "))

wynik = liczbaLodow % liczbaRodzenstwa

if wynik == 0:
    print("Lody do podziału")
else:
    print("Lody zjedz sam")