# PRZYPISANIE ZMIENNEJ DO NOWO UTWORZONEGO OBIEKTU TYPU INTEGER (INT)
x = 1000  # Ekwiwalent operacji 'x = int(1000)'
x = 1_000  # Inny zapis '1000' - Znak '_' zwiększa czytelność dużych liczb

# UŻYCE OPERATORÓW ARYTMETYCZNYCH
x = (x + 1 - 2) * 3  # Dodawanie, odejmowanie, mnożenie
x = x // 10  # Dzielenie całkowite
x = (x % 7) ** 2  # Dzielenie modulo, potęgowanie
x = x / 3  # Dzielenie - Domyślnie wynik jest zawsze wyrażany typem 'float'
print(x, type(x))

# MOŻLIWE ZAPISY LICZB ZMIENNOPRZECINKOWYCH - FLOATING POINT NUMBERS (FLOAT)
q, x = 1000.0, 1_000.0
y, z = 1e3, 1e-3  # Zapis z wykorzystaniem notacji naukowej, '1e3' == '1*10**3'

print(q, x, y, z)
print(type(q), type(x), type(y), type(z))
