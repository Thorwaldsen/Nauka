zmienna = 1
zmienna2 = "ABC"

lista = [1, 2, "c", "d", "e", ]
print(lista)
print(lista[0])
lista[2] = 3
print(lista)
tekst = "Hello world"
print(tekst[0])
print(lista + ["f", "g"])
print(lista * 3)
print("Ilość elementów: ", len(lista))
lista.append("f")
print(lista)
lista.append(["g", "h"])
print(lista)
print(lista[6][0])
lista.insert(2, 3)
print(lista)
print("Ilość: ", lista.count(1))
print("Index: ", lista.index("f"))
lista.remove("f")
print(lista)

lista2 = [1, 20, 35, -5, 0]
print("Min", min(lista2))
print("Max", max(lista2))
lista2.sort()
print(lista2)
lista2.reverse()
print(lista2)
lista2.clear()
print(lista2)