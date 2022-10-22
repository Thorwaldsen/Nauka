# program przyjmiuje od uzytkownika zdanie będące ciągiem znaków, a następnie zlicza ilość wyrazów,
# ilość liter oraz częstotliwość wystąpienia danej litery
ignored = [" "]
zdanie = input("Tutaj wpisz tekst: ")
iloscSlow = len(zdanie.split())
iloscZnakow = len(zdanie)
licznikBezSpacji = 0
tablicaZnakow = {}

for i in zdanie:
    if i != " ":
        licznikBezSpacji += 1

for char in zdanie:
    char = char.lower()
    if char in tablicaZnakow:
        tablicaZnakow[char] += 1
    else:
        tablicaZnakow[char] = 1

print(f"""\nAnaliza podanego zdania wygląda następująco:
Podane zdanie: {zdanie}
Ilość słów: {iloscSlow}
Ilość znaków: {iloscZnakow}
Ilość znaków bez spacji: {licznikBezSpacji}
Częstotliwość wystąpienia danej litery: {tablicaZnakow}""")
