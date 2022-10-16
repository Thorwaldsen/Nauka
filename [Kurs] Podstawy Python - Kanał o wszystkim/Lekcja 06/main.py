from random import randint

wartoscLosowania = randint(1, 10)
odpowiedzUzytkownika = -1
proby = 0

print("Zgadnij liczbę z przedziału od 1 do 10")

while odpowiedzUzytkownika != wartoscLosowania:
    proby += 1
    odpowiedzUzytkownika = int(input("Podaj liczbę: "))
    if odpowiedzUzytkownika > wartoscLosowania:
        print("Niestety wylosowana liczba jest mniejsza od Twojej")
    elif odpowiedzUzytkownika < wartoscLosowania:
        print("Niestety wylosowana liczba jest większa od Twojej")
print("Brawo, odgadłeś za", proby, "razem.")
