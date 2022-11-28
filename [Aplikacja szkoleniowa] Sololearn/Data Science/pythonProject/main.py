import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3, 3, 0.2)
y1 = np.sin(x)
y2 = 0.2 * (x ** 2) - 1

okno, obszar = plt.subplots()
obszar.plot(x, y1, color='#FF0000', label='y = sin(x)', lw=2)
obszar.plot(x, y2, color='blue', label='$y = 0.2*x^2-1$', lw=4)

okno.suptitle('Pierwszy wykres', color='red', fontsize='16')
obszar.set_title('Nasze wykresy - tytuł obszaru rysowania wykresu')
legenda = obszar.legend(loc='upper left', shadow=True, fontsize='14')
legenda.get_frame().set_facecolor('lightgray')
plt.savefig('Okno.pdf')
plt.show()
