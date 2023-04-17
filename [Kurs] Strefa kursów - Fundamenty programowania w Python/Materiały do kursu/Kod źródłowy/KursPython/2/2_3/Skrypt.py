# PRZYKŁADY ZNAKÓW I ICH CIĄGÓW
# Znaki i łańcuchy możemy zamykać pomiędzy apostrofami ('') lub cudyszłowami ("")
x = 'x'
y = "x"
print(x, y, type(x), type(y))

# Apostrofy i cudzysłowy mogą być wykorzystywane w tych samych łańcuchach
x = "I'm Batman!"
print(x)
x = 'Grażyna zakrzyknęła - "Zostaw ten kapuśniak!"'
print(x)

# Możemy użyc potrójnego apostrofu lub cudysłowu do łańcuchów wielowierszowych...
x = '''"Any fool can write code that a computer can understand.
Good programmers write code that humans can understand."
- Martin Fowler'''
print(x)

# ...oraz do zamykania łańcuchów zawierających oba rodzaje zamknięć
x = '''She said, "Thank you! It's mine"'''
print(x)

# OPERATORY ARYTMETYCZNE
# Łączenie łańcuchów z użyciem operatora dodawania
x, y = '123', '456'
z = x + y
print(x, y, z)

# Pomnażanie, powtarzanie łańcuchów z użyciem operatora mnożenia
q = z * 2
print(q)

# Wybieranie konkretnego elementu z łańcucha
element = q[0]  # Wybranie pierwszego elementu łańcucha 'q'
elements = q[0:3]  # Wybranie pierwszych trzech elementów łańcucha 'q'
print(element, elements)

# Podmienianie znaków
name = "Piotr Dzwiniel"
new_name = name.replace("Piotr", "Stanisław")

# Dzielenie łańcuchów z wykorzystaniem metody 'split()'
splitted = q.split('4')  # Podzielenie łańcucha 'q' w miejscu występowania '4'
print(splitted, type(splitted))  # Metoda 'split()' zwraca nowy typ danych - listę
