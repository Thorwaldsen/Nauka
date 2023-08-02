from classes import *

kwadrat = Square(10)
prostokat = Rectangle(10, 20)

slownik = {
    "kwadrat" : kwadrat,
    "prostokat" : prostokat
}

for key, figure in slownik.items():
    print(f"Pole {key} wynosi:", figure.area())
    print(f"Obwod {key} wynosi:", figure.perimeter())