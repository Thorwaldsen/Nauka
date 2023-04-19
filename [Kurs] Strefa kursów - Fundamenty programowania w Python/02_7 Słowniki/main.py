# slownik = {
#     "Imie": "Artur",
#     "Nazwisko" : "Rosiek",
#     "Wiek" : 31
# }
# print(slownik)
# x = {}
# x = dict()
# print(x, type(x))

# x["Pracownik"] = "Artur Rosiek"
# x["Stanowisko"] = "Elektryk"
# x["Wiek"] = 31
# print(x, type(x))

# x["Stanowisko"] = "Administrator danych"
# print(x, type(x))

# wiek = x.pop("Zarobki", "Nie ma takiego klucza!")
# print(x, "Zarobki:", wiek)
# del x["Stanowisko"]
# print(x)
x = dict([
    ("Nazwisko", "Rosiek"),
    ("Zarobki", 9000.0)
])
print(x)

y = dict(Nazwisko="Rosiek", Zarobki=9000.0)
print(y)