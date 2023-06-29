# generator to funkcja do tworzenia iteratora

def generator():
    yield 1
    yield 2
    yield 3


print("Generator 1")
for i in generator():
    print(i)

x = generator()
print(next(x))
print(next(x))
print(next(x))


def generator2(a, b):
    while a < b:
        yield a
        a += 1


print("Generator 2:")
for i in generator2(2, 20):
    print(i)

print("Generator 3")


def odwroc(dane):
    for i in range(len(dane) - 1, -1, -1):
        yield dane[i]


for i in odwroc("kukulka"):
    print(i, end="")

for i in odwroc((4, 4, 5, 2, 5, 2)):
    print(i, end="")
