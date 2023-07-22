shop_shelf = ["Apple", "Toy", "Orange", "Banana", "Kiwi", "Pear"]
basket = []

goods = len(shop_shelf) - 1

print("In our store: ")
for product in shop_shelf:
    print(product, end=", ")

waching_goods = 0
while waching_goods <= goods:
    print("\nYou are holding {} in your hand".format(shop_shelf[waching_goods]))
    decion = input("Do you want to put this product in the basket?")
    if decion == "Yes":
        basket.append(shop_shelf[waching_goods])
        shop_shelf[waching_goods] = " "
    waching_goods += 1

print("\nIn your basket: ")
for in_basket in basket:
    print(in_basket, end=", ")
print("")

print("\nIn our store: ")
for product in shop_shelf:
    print(product, end=", ")
print("")

