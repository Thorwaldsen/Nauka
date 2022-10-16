plik = open("tekst.txt", "r")
tekst = plik.read()
plik.close()

def policz(txt, znak):
    licznik = 0
    for ilosc in txt:
        if ilosc == znak:
            licznik += 1
    return licznik

#print(policz(tekst.lower(), "b"))

for z in "abcdefghijklmnopqrstuwxyz":
    ile = policz(tekst.lower(), z)
    procent = 100 * ile / len(tekst)
    print("{0} - {1} - {2}%".format(z.upper(), ile, round(procent, 2)))
