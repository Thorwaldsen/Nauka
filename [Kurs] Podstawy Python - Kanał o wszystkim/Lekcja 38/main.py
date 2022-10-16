a = "Parzysta" if 10 % 2 == 0 else "Nieparzysta"
print(a)

for i in range(10):
    if  i > 5:
        continue
else:
    print("Koniec")

try:
    a = 5/1
except ZeroDivisionError:
    print("Bład")
else:
    print("Koniec.")
finally:
    print("Zawsze mnie widać")