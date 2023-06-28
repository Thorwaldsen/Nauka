# iterator to obiekt do przeglądania kolekcji (struktur iterowalnych)

lista = [1, 3, 4]

iterator_listowy = iter(lista)
print(iterator_listowy)
print(next(iterator_listowy))
print(next(iterator_listowy))
print(next(iterator_listowy))

# iter inicjuje iteracje a next zwraca wartość danego elementu i przechodzi do następnego
# zwraca wyjątek jak dojdzie do końca

class MojIterator:
    def __init__(self, maks=10):
        self.x = 1
        self.max = maks

    def __iter__(self):
        return self

    def __next__(self):
        x = self.x
        if x > self.max:
            raise StopIteration
        self.x += 1
        return x


for i in MojIterator(40):
    print(i)