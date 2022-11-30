import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10, 0.2)

# tworzymy pustą listę do której następnie dodawane są funkcje
funkcje = []
funkcje.append(x ** 2)
funkcje.append(x ** 3)
funkcje.append(np.sqrt(x))
funkcje.append(x ** 2 * np.sin(x))
funkcje.append(np.sin(x))

# tutaj tworzymy okno i nadajemy mu wartości
okno = plt.figure(figsize=(12, 8), dpi=100)
okno.suptitle('Przykładowe wykresy',
              color='red',
              fontsize=16,
              fontweight='bold')

# tutaj tworzymy kolejną listę do której dodajemy odpowiednio zdefiniowane podokienka
ListaOkien = []
ListaOkien.append(plt.subplot(3, 2, 1))
ListaOkien.append(plt.subplot(3, 2, 2))
ListaOkien.append(plt.subplot(3, 2, 5))
ListaOkien.append(plt.subplot(3, 2, 6))
ListaOkien.append(plt.subplot(3, 1, 2))

# tworzymy krotki z kolorami, grubościami linii oraz etykietami
kolory = ('red', 'blue', 'green', 'magenta', 'black')
gruboscLinii = (1, 3, 2, 5, 3)
etykiety = ('$y=x^2$', '$y=x^3$',
            '$y=\sqrt{x}$', '$y=x^2*sin(x)$',
            '$y=sin(x)$')

# w tej pętli rysujemy wszystkie wykresy nadając im wartości z poprzednich kolekcji
for i in range(5):
    ListaOkien[i].plot(x, funkcje[i],
                       color=kolory[i],
                       lw=gruboscLinii[i], )
    ListaOkien[i].set_title(etykiety[i])

# na koniec wyświetlamy wszystkie narysowane wykresy
plt.show()
