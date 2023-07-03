# Wątki to części programu, które mogą działać jednocześnie
# Wątki istnieją w obrębie jednego procesu
# Współdzielą zasoby

from threading import Thread
import time


# Funkcja do wyświetlania czasu
def wyswietl_czas(nazwa, opoznienie, liczba_powtorzen):
    print(nazwa, " został uruchomiony")
    for i in range(liczba_powtorzen):
        time.sleep(opoznienie)
        print(nazwa, " ", str(time.ctime(time.time())))
    print(nazwa, "zakończył działanie")


lista_watkow = []
for i in range(3):
    lista_watkow.append(Thread(target=wyswietl_czas, args=("Licznik " + str(i + 1), i + 1, (i + 1) ** 2)))

for x in lista_watkow:
    x.start()
