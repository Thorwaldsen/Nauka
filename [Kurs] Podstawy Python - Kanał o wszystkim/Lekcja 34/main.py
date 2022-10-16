import re

if re.match("^[A-Z][a-z]*$", "Alaaaaaaaaaa"):
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]+$", "Ala"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]?[A-Z]$", "AlA"):
    print("Dopasowano.")
else:
    print("Nie dopasowano.")

if re.match("^[A-Z][a-z]{,5}$", "Kazimierz"):
    print("Dopasowano")
else:
    print("Nie dopasowano")