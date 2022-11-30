# aplikacja ma na celu wyszukiwanie we wpisanym wcześniej tekście podanych słów
tekst = input("Wpisz tekst: ")
slowo = input("Wpisz szukane słowo: ")

def search(szukanyTekst, szukaneSlowo):
    rozbityTekst = tekst.split()
    iloscSlow = int(len(tekst.split()))-1
    znalazloSie = "Słowo występuje"
    nieZnalazloSie = "Slowo nie wystepuje"

    while iloscSlow != 0:
        if rozbityTekst[iloscSlow].lower() == slowo.lower():
            return znalazloSie
        elif rozbityTekst[iloscSlow].lower() != slowo.lower():
            iloscSlow -= 1
            if iloscSlow == 0:
                return nieZnalazloSie
            continue

print(search(tekst, slowo))