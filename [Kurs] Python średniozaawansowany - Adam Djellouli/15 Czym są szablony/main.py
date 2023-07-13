import string

szablon = string.Template("$x ma brata $y")

slownik = {
    "x": "James",
    "y": "Tunczyk"}

print(szablon.substitute(slownik))

slownik2 = {
    "x": "Adam",
    "y": "Adama"}

print(szablon.substitute(slownik2))

slownik3 = {
    "x": "Brokuł",
    "y": "Kukurydza"}

print(szablon.substitute(slownik3))

lista_studentow = [("Adam", 30), ("Hans", 50), ("James", 100)]
wiadomosc = string.Template("$x otrzymał $y punktów na egzaminie")

for i in lista_studentow:
    print(wiadomosc.substitute(x=i[0], y=i[1]))

lista_produktow = [{"nazwa": "Tunczyk", "cena": 30, "Ilosc": 10},
                   {"nazwa": "Pomidor", "cena": 3, "Ilosc": 10},
                   {"nazwa": "Brokuł", "cena": 7, "Ilosc": 20}]

zakupy = string.Template("Dodałeś do koszyka $Ilosc produktów $nazwa w cenie $cena za sztukę")

for i in lista_produktow:
    print(zakupy.substitute(i))
