import Ducks as Duck


duck = Duck.Duck(3, "Dziwaczka")
toy_duck = Duck.DuckToy("Red", "Wood")
cat = Duck.Cat()

duck_list = [duck, toy_duck, duck, toy_duck, cat]

for object_in_duck_list in duck_list:
    try:
        object_in_duck_list.fly()
    except AttributeError:
        print("Object", object_in_duck_list, "has no fly method")