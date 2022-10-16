def funkcja(f, liczba):
    return f(liczba)
print(funkcja(lambda x: x * x, 5))

def kwadrat(x):
    return x * x
print(kwadrat(7))

wynik = (lambda x: x * x)(8)
print(wynik)

lam = lambda x: x * x
print(lam(5))
print(lam(4))

lam2 = lambda x,y: x * y
print(lam2(5,4))

lam3 = (lambda x,y: x * y)(5,6)
print(lam3)
