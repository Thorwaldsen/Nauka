# tuples

point = (10.0, 40.4, 50)
my_list = [1, 2, 3, 4, 5, 6]
my_string = "Tutaj mój dowolny string"

# print("Adres w pamięci Tuple: {}".format(id(point)))
# print("Adres w pamięci Listy: {} <-------------".format(id(my_list)))
# print("Adres w pamięci String: {}".format(id(my_string)))

# point = point + (10, 20)
# my_list[2:5] = ["A", "B", "C", "D", "E"]
# my_string += "dowolny dodany string"

# print("-------------------------------------")
# print("Adres w pamięci Tuple: {}".format(id(point)))
# print("Adres w pamięci Listy: {} <-------------".format(id(my_list)))
# print("Adres w pamięci String: {}".format(id(my_string)))


z, x, y = point

print("x:{}, y:{}, z:{}".format(x, y, z))
print("Wspolrzedne: x: %s y %s z: %s" % point)
