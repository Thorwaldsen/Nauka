# PRZYKŁADY KROTEK
x = ()  # Pusta krotka
x = 1,  # Krotka z jednym elementem typu int
x = (1,)  # Jak wyżej
x = 1, 2  # Krotka z dwoma elementami typu int
x = (1, 2)  # Jak wyżej
x = 1, (2, 3)  # Krotka z jednym elementem typu int i zagnieżdżoną krotką (2_8, 3)
x = (1, (2, 3))  # Jak wyżej
x = 1, 'a', "Neptun", 2.0, [1, 2, 3], (1, 2, 3)  # Krotka złożona z elementów różnych typów
x = (1, 'a', "Neptun", 2.0, [1, 2, 3], (1, 2, 3))  # Jak wyżej
x = tuple("oierieijfdkjs")  # Konwersja łańcucha znaków "oierieijfdkjs" na krotkę

# KORZYSTANIE Z INDEKSOWANIA KROTEK
# Identycznie jak w przypadku list

# OPERACJE NA KROTKACH
# Identycznie jak w przypadku list, ale z wykluczeniem modyfikacji elementów

# METODY WYKORZYSTYWANE NA KROTKACH
y = x.index('o')  # Jeżeli przekazany obiekt istnieje w krotce, to podaj jego indeks
y = x.count('i')  # Policz wszystkie wystąpienia przekazanego obiektu w krotce
