from main import Car

value = float(input("Provide the amount of fluids: "))
unit = input("L for liters and G for gallons:")

my_car = Car()
my_car.set_tank(value, unit)

while True:
    choice = int(input("0 - liters to gallons\n1 - change tank size\n2 - exit\n"))
    if choice == 2:
        break
    elif choice == 0:
        unit = input("L for liters and G for gallons:")
        print(my_car.get_tank(unit))
    elif choice == 1:
        value = float(input("Provide the amount of fluids: "))
        unit = input("L for liters and G for gallons:")
        my_car.set_tank(value, unit)
    else:
        pass
