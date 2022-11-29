import numpy as np
import matplotlib.pyplot as plt

# Tutaj tworzymy okno - nadajemy rozmiar 1200 na 800 pikseli i rozdzielczość 100dpi
okno = plt.figure(figsize=(12, 8), dpi=100)

# Tutaj przy pomocy metody suptitle tworzymy tutuł okna a następnie ustaiwamy
# rozmiar czcionki na 16 oraz ustawiamy pogrubienie
okno.suptitle('To jest całe okno:)',
              fontsize=16,
              fontweight='bold')

# Tutaj tworzymy sekwencję wartości x
x = np.arange(-20, 20, 0.1)

# Tutaj definiujemy 4 przykładowe funkcje
# y1 - Funkcja kwadratowa
# y2 - Funkcja 3 stopnia x^3
# y3 - sinus x
# y4 - druga postać funkcji kwadratowej
# Na podstawie podstawiennia powstaje tablica wartości gdzie dla każdego x jest wyliczana odpowiadnia wartość
y1 = (x ** 2) - (2 * x) + 4
y2 = x ** 3
y3 = np.sin(x)
y4 = -2 * x ** 2

# tutaj przy pomocy metody subplot definiujemy podział okna głownego na 2 wiersze (pierwsza wartość)
# 2 kolumny (2 wartość), oraz wskazujemy okno aktywne (trzecia wartość). Innymi słowy:
# Aktywne mamy pierwsze okno przy podziale 2x2
# następnie przy pomocy funkcji "plot" rysujemy funkcje "y1" dla wartości "x".
# bonusowo dodany został marker zaznaczający punk * na wykresie
# przy pomocy metody title ustawiamy tytuł funkcji
plt.subplot(2, 2, 1)
plt.plot(x, y1, marker="*", markersize=1, c="red")
plt.title("Wykres funkcji " + "$y=x^2-2x+4$")

# tutaj robimy to co wyżej z tym że rysujemy okno 2
# jedyna róznica to dodano metodę wykreślenia prostych linii na wykresie
# przy pomocy metody axhline oraz axvline
# efektem tego jest prosty układ współrzędnych widoczny na wykresie
plt.subplot(2, 2, 2)
plt.title("Wykres funkcji " + "$y=x^3$")
plt.plot(x, y2)
plt.axhline(y=0, lw=1, color="black")
plt.axvline(x=0, lw=1, color="black")

# tutaj robimy to co wyżej z tym że rysujemy okno 3
plt.subplot(2, 2, 3)
plt.title("Wykres funkcji y=sin(x)")
plt.plot(x, y3)

# tutaj robimy to co wyżej z tym że rysujemy okno 4
plt.subplot(2, 2, 4)
plt.title("Wykres funkcji " + "$y=-2x^2$")
plt.plot(x, y4)

# przy pomocy metody show() wyświetlamy wszystkie poprzednio zdefiniowane wykresy
plt.show()
