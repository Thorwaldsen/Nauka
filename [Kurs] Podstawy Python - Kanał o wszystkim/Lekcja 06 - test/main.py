from random import randint

wylosowanaLiczba = randint(1, 10)
odpowiedzUzytkownika = -1
iteracja = 0

print("Zgadnij liczbę z przedziału od 1 do 10")

while odpowiedzUzytkownika != wylosowanaLiczba:
    iteracja += 1
    odpowiedzUzytkownika = int(input("Podaj liczbę: "))
    if odpowiedzUzytkownika < wylosowanaLiczba:
        print("Wylosowana liczba jest większa od Twojej")
    elif odpowiedzUzytkownika > wylosowanaLiczba:
        print("Wylosowana liczba jest mniejsza od Twojej")
print("Gratulacje, zgadłeś za", iteracja, "razem")
