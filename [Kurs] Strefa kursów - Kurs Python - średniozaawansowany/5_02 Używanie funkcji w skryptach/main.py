def shopping(selection=[]):
    how_many_goods_in_shop = len(selection)
    customer_basket = []
    watching_goods = 0
    while watching_goods < how_many_goods_in_shop:
        print("\nYou take {} into your hand".format(selection[watching_goods]))
        customer_decision = input("Do you want to put this product in the basket? ")
        if customer_decision == "Yes":
            customer_basket.append(selection[watching_goods])
            selection[watching_goods] = "Nothing"
        watching_goods += 1
    print("\nIn your basket you have:", end=" ")
    return customer_basket


def cash_register(*args):
    if args is not None:
        for iarg in args:
            for product in iarg:
                print(product, end=", ")
    print("")


shop_shelf_1 = ["apple", "banana", "pear", "Cucumber", "Carrot"]
shop_shelf_2 = ["toy car", "toy helicopter", "toy train", "lego set", "basketball"]

basket1 = shopping(shop_shelf_1)
basket2 = shopping(shop_shelf_2)

cash_register(basket1, basket2)
