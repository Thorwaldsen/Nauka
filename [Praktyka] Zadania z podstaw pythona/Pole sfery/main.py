# program przyjmie od użytkownika wartość promienia (R) i na jego podstawie wyliczy pole sfery
import math
r = input("Set radious: ")
rint = int(r)
v = 4/3 * math.pi * rint**3

print("The volume of the sphere is: ", float(v))