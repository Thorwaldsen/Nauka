# SPRAWDZANIE TYPU DANEGO OBIEKTU
print(type(47))  # Zwrócenie: "<class 'int'>"

# PRZYPISYWANIE ZMIENNYCH DO WARTOŚCI (OBIEKTÓW)
x = 47
y = x
x = y = z = 1
x, y = z, 1

# KORZYSTANIE ZE WSKAZÓWEK TYPÓW
# Zobacz PEP 484 (https://peps.python.org/pep-0484/)
x: int
x: int = 1
x = 1  # type: int
x = "jeden"  # Ostrzeżenie: "Expected type 'int', got 'str' instead"
