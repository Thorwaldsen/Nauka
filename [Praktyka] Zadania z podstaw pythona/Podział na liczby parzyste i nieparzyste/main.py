podanaWartosc = input("Podaj ilosc liczb: ")

iloscLiczbDoPodzialu = int(podanaWartosc)

print("\nParzyste:", end = ',')
for x in range(iloscLiczbDoPodzialu):
    if x % 2 == 0:
        print(x, end = ',')

print("\nNieparzyste:", end = ',')
for x in range(iloscLiczbDoPodzialu):
    if x % 2 != 0:
        print(x, end = ',')
print("\n")