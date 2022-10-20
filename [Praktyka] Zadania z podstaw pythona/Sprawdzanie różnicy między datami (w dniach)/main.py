# program jako wartości przyjmuje dwie daty a następnie wypisuje ile jest między nimi dni różnicy

from datetime import date

firstDate = date(2014, 5, 2)
secondDate = date(2014, 6, 11)

diffrence = firstDate - secondDate

print(diffrence.days)

