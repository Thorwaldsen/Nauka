import math
import statistics

print('PI:', math.pi)
print('E:', math.e)

print('POW:', math.pow(2, 2))
print('SQRT:', math.sqrt(4))

print('DEG -> RAD:', math.radians(90))
print('RAD -> DEG:', math.degrees(math.pi))
print('DIST between A[2, 1] and B[5, 9]:', math.dist([2, 1], [5, 9]))

dane = [1, 23, 12, 12, 45, 123, 12, 235, 12, 12, 53, 12]
print('Dane:', dane)

srednia = statistics.mean(dane)
print('Średnia:', srednia)

mediana = statistics.median(dane)
print('Mediana:', mediana)

odchylenie = statistics.stdev(dane)
print('Odchylenie:', odchylenie)

wariancja = statistics.variance(dane)
print('Wariancja:', wariancja)
