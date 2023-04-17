# PRZYKŁADY LIST
x = []  # Pusta lista
x = [1]  # Lista z jednym elementem typu int
x = [1, 2, 3]  # Lista z trzema elementami typu int
x = ['a', 'b', 'c']  # Lista z trzema elementami typu str
x = ["Imię", "Nazwisko"]  # Lista z dwoma elementami typu str
x = [1, '2_8', [3]]  # Lista z elementami typu int, str oraz list
x = list("dadasfgsfakj")  # Konwersja łańcucha znaków "dadasfgsfakj" na listę

# KORZYSTANIE Z INDEKSOWANIA LIST
y = x[0]  # Wybór elementu o podanym indeksie od lewej do prawej (numerowanie od 0, więc wybieramy pierwszy element z listy)
y = x[-1]  # Wybór elementu o podanym indeksie od prawej do lewej (numerowanie od 1, więc wybieramy ostatni element z listy)
y = x[0:]  # Wybór wszystkich elementów od podanego indeksu
y = x[:3]  # Wybór wszystkich elementów do podanego indeksu
y = x[0:2]  # Wybór elementów z zakresu [start:stop]
y = x[0:-1:2]  # Wybór elementów z zakresu z krokiem [start:stop:krok]
y = x[::-1]  # Odwrócenie listy
x = [1, 2, 3, [4, 5, 6]]
y = x[3][0]  # Wybór pierwszego elementu z zagnieżdżonej listy (czyli czwórki)

# OPERACJE NA LISTACH
x = [1, 2, 3]
x[0] = 9  # Zmiana elementu o indeksie 0 na wartość 9 typu int
y = x + x  # Konkatenacja (dodawanie) list do siebie
y = x * 3  # Powtarzanie (pomnażanie) list przez daną wartość

# METODY WYKORZYSTYWANE NA LISTACH
y = x.insert(0, 9)  # Wstawianie nowych elementów do listy na podaną pozycję
y = x.append(9)  # Wstawianie nowych elementów do listy na jej koniec
