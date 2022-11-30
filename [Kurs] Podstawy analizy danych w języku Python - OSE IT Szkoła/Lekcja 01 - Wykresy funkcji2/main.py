import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

x = np.arange(0.0, 5.0, 0.01)
y = np.cos(2 * np.pi * x)
ax.plot(x, y, lw=2)
fig.suptitle('Przykładowe okno')
ax.annotate('lokalne maximum',
            color='blue',
            xy=(2, 1),
            xytext=(3, 1.5),
            arrowprops=dict(facecolor='red', shrink=0.05), )
ax.text(1, 1.5, 'Dowolny opis', color='green')

ax.set_ylim(-2, 2)
plt.show()
