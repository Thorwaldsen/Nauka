# x, y =True, False
# print(x, y, type(x), type(y))
# w_kolekcji = 1 not in [1, 2, 3]
# print(w_kolekcji, type(w_kolekcji))
# x = True + 7
# print(x, type(x))
# x, y = True, False
# z = x and y # z = True, gdy x, y = True, True
# z = x or y # z = False, gdy x, y = False, False
# x = not y # x = True, gdy y == False
# print(x, y, z)
from decimal import Decimal
from fractions import Fraction
# x = Decimal('0.1')
# y = Decimal('0.1')
# z = Decimal('0.1')

# print(x)
# print(y)
# print(z)
# print(x + y + z)

# x = Fraction(1, 3) + 3
# print(x, type(x))
x = range(10)
y = range(5, 10)
z = range(0, 100, 5)

print(list(x), type(x))
print(list(y), type(y))
print(list(z), type(z))
