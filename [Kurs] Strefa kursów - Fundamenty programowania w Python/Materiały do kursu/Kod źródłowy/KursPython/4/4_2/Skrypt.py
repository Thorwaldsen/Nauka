"""
OGÓLNY FORMAT FUNKCJI
def(definiuję) funkcja()(funkcję o nazwie 'funkcja', która...):
    ...wykonuje instrukcje i wyrażenia tutaj opisane
"""

# Przykład funkcji


def funkcja():
    print("Nasza pierwsza funkcja!")


# Wywołanie funkcji
funkcja()

# Użycie funkcji, jako obiektu
x = funkcja
print(x, type(x))

# Inny przykład funkcji


def interakcja_z_handlarzem():
    print("Handlarz: Witaj Wędrowcze!")
    print("Handlarz: Czy masz może ochotę pohandlować?")
    while True:
        odpowiedz = input("Ty: ")
        if odpowiedz == "Tak":
            print("Handlarz: To świetnie! Nie zawiedziesz się!")
            print("*Handlarz pokazuje Ci swoje towary*")
            break
        elif odpowiedz == "Nie":
            print("Handlarz: Może następnym razem...")
            print("*Handlarz uśmiecha się krzywo*")
            break
        else:
            print("Handlarz: Przykro mi, ale chyba nie zrozumiałem...")
            continue


interakcja_z_handlarzem()

# Deklaracja funkcji w zależności od warunku
x = 10
y = 12
if x > y:
    def function():
        print("x jest WIĘKSZE od y")
else:
    def function():
        print("x jest MNIEJSZE od y")

function()
