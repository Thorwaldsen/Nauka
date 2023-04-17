# PROGRAM WYŚWIETLAJĄCY TABLICZKĘ MNOŻENIA LICZB OD 1 DO 10 WŁĄCZNIE
for i in range(1, 11):
    for j in range(1, 11):

        liczba = str(i*j)
        dlugosc_liczby = len(liczba)

        if dlugosc_liczby == 1:
            liczba = "  " + liczba
        elif dlugosc_liczby == 2:
            liczba = " " + liczba

        print(liczba, end=" | ")
    print()
