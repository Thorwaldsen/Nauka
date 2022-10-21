# Wypisz liczby od 1 do 100, przy czym liczby podzielne przez 3 zastąp słowem ‘Fizz’,
# liczby podzielne przez 5, zastąp słowem ‘Buzz’,
# natomiast liczby podzielne i przez 3 i przez 5 zastąp słowem ‘FizzBuzz’.

theNumbers = range(0, 101)

for i in theNumbers:
    if theNumbers[i] == 0:
        continue
    elif theNumbers[i] % 3 == 0 and theNumbers[i] % 5 == 0:
        print(theNumbers[i], "FizzBuzz")
    elif theNumbers[i] % 3 == 0:
        print(theNumbers[i], "Fizz")
    elif theNumbers[i] % 5 == 0:
        print(theNumbers[i], "Buzz")
    else:
        print(theNumbers[i])
