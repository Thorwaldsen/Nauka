print("Dawno, dawno temu na dzikim zachodzie żył sobie pewien rewolwerowiec. Był najszybszy na dzikim zachodzie")
input("Naciśnij aby kontynuować opowieść")

print("Pewnego dnia jeden śmiałek rzucił mu wyzwanie...\nStaneli razem w samo południe twarzą w twarz. Kabury były "
      "odbezpieczone. Z dwunastym biciem ddzwona mieli oddać strzał. Na dzikim zachodzie nie ma miejsca na dwóch "
      "rewolwerowców")
input("Naciśnij aby kontynuować opowieść")

print("Dong")
input("Dong")

print("Dong")
input("Dong")

print("Dong")
input("Dong")

gracz = "Ucieczka"

if gracz == "Strzał":
    print("Rewolweowiec nie żyje - wygrałeś")
    stan_gry = "Wygrałeś"
elif gracz == "Ucieczka":
    print("Jesteś pośmiewiskiem całego dzikiego zachodu")
    stan_gry = "Przegrałeś ale żyjesz"
else:
    print("Rewolweowiec był szybszy - Przegrałeś")
    stan_gry = "Przegrałeś"

print("Koniec gry - {}".format(stan_gry))