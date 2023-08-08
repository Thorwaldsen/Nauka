import Ducks as Duck

my_duck = Duck.Duck(4, "Krzyżówka")
print("------Real duck------")
my_duck.fly()
my_duck.say()
my_duck.go_to()

my_toy_duck = Duck.DuckToy("Zielona", "Aluminiowa")
print("\n------Toy Duck-------")
my_toy_duck.fly()
my_toy_duck.say()
my_toy_duck.go_to()
