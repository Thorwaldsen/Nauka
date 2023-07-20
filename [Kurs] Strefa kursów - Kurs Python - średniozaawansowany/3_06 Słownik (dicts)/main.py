# słowniki

ages = {"Piotr ": 30,
        "Adam ": 40,
        "Karolina": 50}

# print("Piotr ma: {} lat".format(ages["Piotr"]))
print(ages)

ages["Roman"] = 19
ages["Natalia"] = 20

print(ages)

ages["Karolina"] = 30
print(ages)

del ages["Karolina"]
print(ages)

ages.pop("Roman")
print(ages)

ages["Kaziu"] = 43
ages["Artur"] = 30

print(ages.keys())

lista_imion = list(ages.keys())

print("Na liście mamy: {} jest to typ {}".format(lista_imion, type(lista_imion)))

print(ages.values())

ages = dict(piotr=30, adam=40, karolina=50)
print(ages, type(ages))

ages = dict([("piotr", 30), ("adam", 40), ("karolina", 50)])
print(ages, type(ages))
