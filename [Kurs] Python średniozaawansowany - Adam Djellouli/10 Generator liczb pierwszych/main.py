import math


def czy_pierwsza(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def generator_liczb_pierwszych(n):
    for i in range(2, n+1):
        if czy_pierwsza(i):
            yield i


print(list(generator_liczb_pierwszych(100)))

# Rozwiązanie alternatywne-iterator

class IteratorPierwszych:
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        while 1:
            self.i += 1
            if self.i > self.n:
                raise StopIteration
            if czy_pierwsza(self.i):
                return self.i

print(list(IteratorPierwszych(100)))