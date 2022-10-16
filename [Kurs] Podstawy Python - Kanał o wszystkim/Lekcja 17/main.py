lista = list(range(10))
nowa = [i * 2 for i in lista]
nowa2 = [i + 2 for i in lista if i% 2 == 0]

print("Stara lista: ", lista)
print("Nowa lista: ", nowa)
print("Druga nowa lista:", nowa2)

#formatowanie String

argumenty = ["Artur", 29]
tekst = "Cześć mam na imię {imie} i mam {wiek} lat.".format(imie = argumenty[0], wiek = argumenty[1])
print(tekst)
