x = 5
y = 3
z = "2"
v = "2.3"

# Dodawanie
wynik = x + int(z)
print("Wynik to {}. Typ: {}".format(wynik, type(wynik)))

# Odejmowanie
wynik = x - int(z)
print("Wynik to {}. Typ: {}".format(wynik, type(wynik)))

# Mnożenie
wynik = x * int(z)
print("Wynik to {}. Typ: {}".format(wynik, type(wynik)))

# Dzielenie
wynik = x / int(z)
print("Wynik to {}. Typ: {}".format(wynik, type(wynik)))

# Floor division
wynik = x // int(z)
print("Wynik to {}. Typ: {}".format(wynik, type(wynik)))

# Modulo
wynik = x % int(z)
print("Wynik to {}. Typ: {}".format(wynik, type(wynik)))

# Potęga
wynik = x ** int(z)
print("Wynik to {}. Typ: {}".format(wynik, type(wynik)))

print("Zmienna x jest typu {}".format(type(x)))
print("Zmienna y jest typu {}".format(type(y)))
print("Zmienna z jest typu {}".format(type(int(z))))
print("Zmienna v jest typu {}".format(type(float(v))))
