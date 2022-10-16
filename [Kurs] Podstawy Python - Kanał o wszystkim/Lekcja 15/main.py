slownik = {1: "Poniedziałek", 2: "Wtorek", 7: "Niedziela"}

print(slownik)
slownik[3] = "Środa"
slownik[4] = False
slownik[5] = 5
print(slownik)
slownik["a"] = 1
print(slownik["a"])
print(slownik)
#print(slownik[8])
print(slownik.get(8, "Inny dzień"))
print("\nPętla:")
for lenght in slownik.values():
    print(lenght)

print("--------")
print(slownik.pop(1))
print(slownik)