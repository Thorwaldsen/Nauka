# program ma przyjąć od użytkownika ciąg cyfr oddzielonych przecinkiem i na tej podstawie wygenerować listę i krotkę
userInput = input("Numbers: ")

list = userInput.split()
tuple = tuple(list)

print(list)
print(tuple)