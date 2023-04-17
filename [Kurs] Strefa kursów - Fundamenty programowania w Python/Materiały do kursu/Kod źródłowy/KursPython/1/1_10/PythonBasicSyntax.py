# PIERWSZY PROGRAM.
print("I'm Batman!")

# ZAREZERWOWANE SŁOWA KLUCZOWE (NIE NAZYWAMY TAK ZMIENNYCH, FUNKCJI, KLAS ETC).
python_keywords = ['and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
                   'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'None',
                   'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield']

# PRZYKŁADY NAZYWANIA ZMIENNYCH.
johnwick = 0
johnwick2 = 0
johnwick_3 = 0
john_wick = 0
_john_wick = 0
johnWick = 0
JohnWick = 0
JOHNWICK = 0
JOHN_WICK = 0

# PRZYPISYWANIE ZMIENNYCH.
x = 1
x, y, z = [1, 2, 3]
x, y = z, 1
x = y = z = 1

# TYPY WBUDOWANE.
x = "Raz, dwa trzy, John Wick patrzy."  # str (string, łańcuch/ciąg znaków)
x = 'a'  # str (string, łańcuch/ciąg znaków)
x = 20  # int (integer, wartość całkowitoliczbowa)
x = 20.5  # float (floating point, wartość zmiennoprzecinkowa)
x = 1j  # complex (liczby zespolone)
x = ["Seat", "Subaru", "Suzuki"]  # list (lista)
x = ("Seat", "Subaru", "Suzuki")  # tuple (krotka)
x = range(1, 11, 1)  # range (zakres)
x = {"Marka": "Seat", "Data założenia": "09-05-1950"}  # dict (dictionary, słownik)
x = {"Seat", "Subaru", "Suzuki"}  # set (zbiór)
x = True  # boolean (wartość logiczna)
x = None  # NoneType (pustka, nicość, bezsens... :<)

# WSKAZÓWKI TYPÓW (TYPE HINTS).
x: int
x: int = 1
x = 1  # type: int
x = 'jeden'  # Zwraca ostrzeżenie: "Expected type 'int', got 'str' instead."

# OPERATORY.
x = y + 1 - 1 * 1 / 1  # Dodawanie, odejmowanie, mnożenie, dzielenie
x = y % 1  # Reszta z dzielenia (modulo)
x = y // 1  # Dzielenie całkowite
x = y ** 2  # Potęgowanie

x += y  # Ekwiwalent x = x + y
x -= y  # Ekwiwalent x = x - y
x *= y  # Ekwiwalent x = x * y
x /= y  # Ekwiwalent x = x / y
x %= y  # Ekwiwalent x = x % y
x //= y  # Ekwiwalent x = x // y
x **= y  # Ekwiwalent x = x ** y

x = x == y  # x = True, jeżeli x jest równe y
x = x != y  # x = True, jeżeli x nie jest równe y
x = x > y  # x = True, jeżeli x jest większe od y
x = x < y  # x = True, jeżeli x jest mniejsze od y
x = x >= y  # x = True, jeżeli x jest większe lub równe względem y
x = x <= y  # x = True, jeżeli x jest mniejsze lub równe względem y
x = x is y  # x = True, jeżeli x i y, to te same obiekty.
x = x is not y  # x = True, jeżeli x i y, to różne obiekty.

z = x or y  # z = False, gdy x, y = False, False
z = x and y  # z = True, gdy x, y = True, True
x = not y  # x = True, gdy y == False

# PĘTLE I INSTRUKCJE.

# Instrukcje if, elif, else.
if x:
    print(x)  # Wykonać, jeżeli x = True.
elif y:
    print(y)  # Wykonać, jeżeli x = False, a y = True. Opcjonalne.
else:
    print(x, y)  # Wykonać, jeżeli x = False i y = False. Opcjonalne.

# Pętla while.
while x:
    print(x)  # Wykonywać, dopóki x = True.
else:
    print(y)  # Wykonać, gdy x = False. Opcjonalne

# Pętla for.
for x in range(10):
    print(x)  # Wykonywać, dopóki wykorzystane zostaną wszystkie elementy z range(10).
else:
    print(y)  # Wykonać, gdy skończą się elementy z range(10). Opcjonalne.

# Instrukcje pass, break, continue.
for x in range(10):
    pass  # Instrukcja wypełniacz, która nie wykonuje żadnych działań.
    print(x)  # Wartość x zostanie wyświetlona. Pętla będzie działać dalej.

for x in range(10):
    break  # Instrukcja przerwania przerwania iterowania/wykonywania instrukcji/pętli.
    print(x)  # Wartość x nie zostanie wyświetlona. Pętla zakończy swoje działanie.

for x in range(10):
    continue  # Instrukcja przejścia do kolejnej iteracji/wykonywania instrukcji/pętli.
    print(x)  # Wartość x nie zostanie wyświetlona. Pętla będzie działać dalej.


# FUNKCJE.


def function(n):  # Najprostsza definicja funkcji.
    print(n)


function(10)  # Wywołanie funkcji. Funkcja wyświetli: 10


def function(n):  # Funkcja zwracająca wartość.
    return n  # Instrukcja return zwraca wartość n.


x = function(10)  # Wywołanie funkcji spowoduje ustawienie wartości x na 10.


def function(n, m="default", *args, **kwargs):  # Funkcja przyjmuje obligatoryjny argument pozycyjny n.
    print(n, m, args, kwargs)


function(1)  # Funkcja wyświetli: 1, default, (), {}


def function(n: int) -> str:
    """
    Funkcja prezentująca wykorzystanie wskazówek typów danych.
    :param n: Spodziewana wartość typu całkowitoliczbowego (int).
    :return: Spodziewana wartość typu łańcuch znaków (str).
    """
    return str(n)

# KLASY.


class Batman:
    pojazd = "Batmobil"


superbohater = Batman()
print(superbohater.pojazd)  # Funkcja wyświetli: Batmobil

# MODUŁY I PAKIETY.
import statistics  # Importowanie całego modułu. Wykonujemy zawsze na początku skryptu.
from statistics import mean  # Importowanie konkretnej funkcji z modułu. Wykonujemy zawsze na początku skryptu.

med = statistics.median([1, 2, 3])  # Użycie modułu i jego funkcji.
avg = mean([1, 2, 3])  # Użycie funkcji z modułu.
