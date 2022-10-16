print(", ".join(["a", "b", "c"]))
print("Witaj świecie".replace("Witaj", "Cześć"))
print("To jest zdanie".startswith("To"))
print("To jest zdanie".startswith("Nie"))
print("To jest zdanie".endswith("zdanie"))
print("To jest zdanie".endswith("."))
print("j" in "To jest zdanie")
print("Q" in "To jest zdanie")
print("To jest zdanie".upper())
print("To jest zdanie".lower())

print("-------------------")

lista = [10, 20, 25, 36, 40]

if all([i % 2 == 0 for i in lista]):
    print("Wszystkie parzyste")

if any([i % 2 == 0 for i in lista]):
    print("Chociaż jedna parzyszta")

for i in enumerate(lista):
    print(i[0] + 1,"-", i[1])