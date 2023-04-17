# Instrukcja pass.
if True:
    pass

for i in range(10):
    pass

# Instrukcja continue.
for i in range(10):
    if i % 2 == 0:
        print(i)
        continue
    print(":)")

# Instrukcja break.
for i in range(10):
    if i < 5:
        print("$$$")
    else:
        break
