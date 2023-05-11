"""
while(dopóki) warunek(jest prawdziwy):
    wykonuj zawarte tutaj instrukcje
else:
    wykonaj zawarte tutaj instrukcje,
    gdy pętla zakończy swoje działanie
"""
# while True:
#      print("Pętla teoretycznie nieskończona")

# x = 0
# y = 10
# while x < y:
#     x += 1
#     print(x)
# print("x =", x, "| y =", y)
# x = set([1, 2, 3])
# while x:
#     print(x.pop())
# else:
#     print("Zbiór x jest pusty:", x)
# x = 20
# while x:
#     if x % 2 == 0:
#         print(x, end=" | ")
#     x -= 1
#     if x == 0:
#         print(x, end=" | ")

x = 5
y = 5
while x:
    while y:
        print("W pętli II poziomu")
        y -= 1
    print("W pętli I poziomu")
    x -= 1
print("x: ", x, "y: ", y)
