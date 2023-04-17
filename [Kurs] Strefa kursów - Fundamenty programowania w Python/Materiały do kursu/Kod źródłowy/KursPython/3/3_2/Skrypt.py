"""
OGÓLNY FORMAT INSTRUKCJI WARUNKOWYCH
if wyrażenie -> bool:
    zagnieżdżony blok instrukcji sterującej
elif wyrażenie2 -> bool:
    zagnieżdżony blok kodu
elif wyrażenieN -> bool:
    zagnieżdżony blok kodu
...
else:
    blok kodu wykonywany wtedy, gdy wczesniejsze wyrażenia zwrócą False
"""

print("Pierwsza część kodu")
x, y, z = 9, 2, 3
if x < y and z == 3:
    print("Druga część kodu")
elif x > z:
    print("Blok kodu zagnieżdżony w ELIF")
else:
    print("Dodatkowa część kodu")
print("Trzecia część kodu")

# if wyrażenie -> bool:
#     zagnieżdżony blok instrukcji sterującej
# elif wyrażenie2 -> bool:
#     zagnieżdżony blok kodu
# elif wyrażenieN -> bool:
#     zagnieżdżony blok kodu
# ...
# else:
#     blok wykonywany wtedy, gdy wyrażenie zwróci False
