import re

'''
. dowolny znak
przykład: '.ala' pasuje: fala, gala, mala, nala

[] dowolny znak z pomiędzy nawiasów
przykład: '[dm]am' pasuje: mam, dam

[^ ] wszystkie znaki niewymienione między nawiasami (działanie przeciwne do powyższego)
przykład: '[dm]am' pasuje: sam, ram

* wszelkie możliwe kombinacje znaków
przykład: 'k.*' pasuje: każde słowo zaczynające się na k (kam, kos, kot, kalafior)
 
'''

napis = "James lubi jeść tuńczyki jako jedzenie"
wyrazenie = re.compile('j[^ ]*')

# wzorzec i tekst muszą być takie same
if re.match('.*lubi.*', napis):
    print("Znaleziono za pomocą match")

# wzorzec występuje w tekście
if re.search("[jdsal]u.i", napis):
    print("Znaleziono za pomocą search")

for i in re.findall(wyrazenie, napis):
    print(i)
