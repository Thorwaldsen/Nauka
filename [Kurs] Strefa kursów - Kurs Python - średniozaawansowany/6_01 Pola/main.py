class Car:
    def __init__(self, model, brand, vin_number):
        self.model = model
        self.brand = brand
        self.vin_number = vin_number

    def print_information(self):
        print("My model is", self.model)
        print("My car brand is", self.brand)
        print("My Car Vin Number is", self.vin_number)


my_car_1 = Car("126p", "Fiat", "dsfdfjnsdg")
my_car_2 = Car("125p", "Fiat", "djsadasjdi")

my_car_1.print_information()
print("\n")
my_car_2.print_information()