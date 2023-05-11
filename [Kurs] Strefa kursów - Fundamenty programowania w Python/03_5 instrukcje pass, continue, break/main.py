# print("Przed pętlą.")
# for i in range(10):
     #komentarz w pętli
#    pass
# print("Za pętlą")

# for liczba in range(5):
#     if liczba == 2:
#         continue
#     print(liczba)

# x = 10
# while x:
#     x -= 1
#     if x % 2 == 0:
#         continue
#     print(x)
# else:
#     print("Koniec programu.")

# znaki = []
# print("ZLICZATOR PODANYCH ZNAKÓW")
# while True:
#     dane_wejściowe = input("dane wejściowe: ")
#     if dane_wejściowe == "red pill":
#         break
#     else:
#         znaki += list(dane_wejściowe)
# print("Wystąpienia:", end=" ")
# for element in sorted(set(znaki)):
#     print(element, "=", znaki.count(element), end=" | ")

for i in range(10):
    if i != 5:
        print(i)
    else:
        break
else:
    print("W kauluzi else")
