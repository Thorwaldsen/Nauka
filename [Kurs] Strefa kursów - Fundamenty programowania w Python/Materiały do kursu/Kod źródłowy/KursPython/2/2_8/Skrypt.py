# TYP BOOLEAN
x, y = True, False  # Składa się z dwóch stałych oznaczajacych Prawdę i Fałsz

# TYP BOOLEAN - NIEKTÓRE OPERACJE
x = not y  # x = True, gdy y == False
z = x and y  # z = True, gdy x, y = True, True
z = x or y  # z = False, gdy x, y = False, False

z = 1 in [1, 2, 3]  # z = True, jeżeli 1 występuje w kolekcji [1, 2, 3]
z = 1 not in [1, 2, 3]  # z = True, jeżeli 1 nie występuje w kolekcji [1, 2, 3]

# TYPY DECIMAL I FRACTION
# Żeby móc z nich skorzystać, należy dwie poniższe linie na początek skryptu
from decimal import Decimal
from fractions import Fraction

# TYPY DECIMAL I FRACTION - NIEKTÓRE OPERACJE
x_decimal = Decimal('0.1')  # Tworzenie obiektu typu Decimal.
x_fraction = Fraction(1, 10)  # Tworzenie obiektu typu Fraction.

# TYP RANGE
x = range(10)  # Tworzenie ciągu liczb od 0 do 9 (włącznie)
x = range(5, 10)  # Tworzenie ciągu liczb od 5 do 9 (włącznie)
x = range(5, 50, 5)  # Tworzenie ciągu liczb od 5 do 45 (włącznie) z krokiem co 5, czyli 5, 10, 15 itd.

# KONWERSJA TYPÓW
lancuch_znaków = "dkhfjdkfhdjkhsf"
lista = [1, 2, 3]
liczba_całkowita = 9
liczba_zmiennoprzecinkowa = 10.0
ciag_liczb = range(10)

print(list(lancuch_znaków))  # Konwersja str na list
print(tuple(lancuch_znaków))  # Konwersja str na tuple
print(tuple(lista))  # Konwersja list na tuple
print(float(liczba_całkowita))  # Konwersja int na float
print(int(liczba_zmiennoprzecinkowa))  # Konwersja float na int
print(list(ciag_liczb))  # Konwersja range na list
print(tuple(ciag_liczb))  # Konwersja range na tuple
