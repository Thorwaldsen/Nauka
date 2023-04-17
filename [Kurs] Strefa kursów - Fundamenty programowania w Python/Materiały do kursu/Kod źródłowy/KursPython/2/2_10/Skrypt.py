# TWORZENIE NOWEGO PLIKU
plik = open("plik.txt", 'w')
plik.write("Ten tekst zostanie zapisany do pliku.")
plik.write("\n")  # Przejście do nowej linii
plik.write("Ten tekst również zostanie zapisany do pliku.")
plik.close()  # Zamknięcie strumienia wejściowego do pliku.

# OTWIERANIE ISTNIEJĄCEGO PLIKU
# Pierwsze podejście.
plik = open("plik.txt")
plik = open("plik.txt", 'r')
zawartosc_pliku = plik.read()
plik.close()

# Drugie podejście. Może być wykorzystywane w dowolnej pracy z plikami.
with open("plik.txt") as plik:
    zawartosc_pliku = plik.read()

# DODAWANIE TREŚCI DO ISTNIEJĄCEGO PLIKU
plik = open("plik.txt", 'a')
plik.write("\n")  # Dodawanie treści od nowej linii
plik.write("Ta linia zostanie dodana do pliku.")
plik.close()
