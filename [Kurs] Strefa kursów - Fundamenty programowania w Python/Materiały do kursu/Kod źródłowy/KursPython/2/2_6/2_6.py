# PRZYKŁADY ZBIORÓW
x = set()  # Pusty zbiór
x = set([1])  # Zbiór z jednym elementem typu int
x = set((1,))  # Zbiór z jednym elementem typu int
x = {1}  # Zbió z jednym elementem typu int
x = set("abcd")  # Zbiór z czterema elementami typu str {'a', 'b', 'c', 'd'}
x = {1, 2, 3}  # Zbiór z trzema elementami typu int
x = {1.0, "Dwa", ('T', 'r', 'z', 'y')}  # Zbiór z trzema, niemutowalnymi obiektami różnego typu

# POBIERANIE WARTOŚCI
element = x.pop()  # Pobieramy element i usuwamy go ze zbioru
element = next(iter(x))  # Pobieramy element i nie usuwamy go ze zbioru

# OPERACJE NA ZBIORACH
zbior1 = set([0, 1, 2, 3, 4, 5, 6])
zbior2 = set([3, 4, 5, 6, 7, 8, 9])

suma_zbiorow = zbior1.union(zbior2)  # Wylicza sumę (unię) zbiorów
suma_zbiorow = zbior1 | zbior2  # J/w

iloczyn_zbiorów = zbior1.intersection(zbior2)  # Wylicza iloczyn (część wspólną) zbiorów
iloczyn_zbiorów = zbior1 & zbior2  # J/w

roznica_zbiorow = zbior1.difference(zbior2)  # Wylicza różnicę między zbiorem 1 a zbiorem 2_8
roznica_zbiorow = zbior1 - zbior2  # J/w

roznica_zbiorow = zbior2.difference(zbior1)  # Wylicza rożnicę między zbiorem 2_8 a zbiorem 1
roznica_zbiorow = zbior2 - zbior1  # J/w

roznica_symetryczna = zbior1.symmetric_difference(zbior2)  # Wylicza różnicę symetryczną zbiorów
roznica_symetryczna = zbior1 ^ zbior2  # J/w

# POZOSTAŁE OPERACJE NA ZBIORACH
x = {1, 2, 3, 4, 5, 6}
x.remove(1)  # Usuwa 1 ze zbioru. Jeżeli nie ma 1 w zbiorze, metoda zwróci błąd.
x.discard(1)  # Usuwa 1 ze zbioru. Metoda nie zgłosi błędu, jeżeli nie ma 1 w zbiorze.
x.add(1)  # Dodaje 1 do zbioru.
x.clear()  # Usuwa wszystkie elementy ze zbioru.
