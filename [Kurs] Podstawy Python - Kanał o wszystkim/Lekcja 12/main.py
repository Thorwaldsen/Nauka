x = 12
y = 1

try:
    lista = [3]
    print(lista[0])
    print(x + 4)
    print(x/y)
    print("Linijka po")
except (ZeroDivisionError, TypeError):
    print("Wystąpił 1 z 2 błędów!")
except:
    print("Inny błąd")
finally:
    print("Finally: wykonam się i tak")

print("Dalsze instrukcje...")
