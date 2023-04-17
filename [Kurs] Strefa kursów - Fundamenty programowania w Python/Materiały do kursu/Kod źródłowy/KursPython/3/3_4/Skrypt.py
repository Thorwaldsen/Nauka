"""
OGÓLNY FORMAT PĘTLI WHILE
while(dopóki) warunek(jest prawdziwy):
    wykonuj zawarte tutaj instrukcje
else(w przeciwnym razie):
    wykonaj zawarte tutaj instrukcje,
    gdy pętla zakończy swoje działanie
"""

# PRZYKŁADY PĘTLI

# Przykład pętli teoretycznie nieskończonej.
while True:
    print("To jest pętla teoretycznie nieskończona.")
    # Możesz ją zakończyć przy użyciu CTRL + C (w wierszu poleceń),
    # lub przerywając sesję PyCharma przyciskiem STOP.

# Przykład "typowej" pętli while.
x = 0
y = 10
while x < y:
    x += 1
    print(x)

# Przykład pętli while z opcjonalną klauzulą else.
x = set([1, 2, 3])
while x:
    print(x.pop())
else:
    print("Zbiór x jest już pusty.")

# Przykład zagnieżdżonej pętli while.
x = 5
y = 5
while x:
    while y:
        print("W pętli II poziomu.")
        y -= 1
    print("W pętli I poziomu.")
    x -= 1
