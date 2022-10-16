wiek = 19
kasa = 10

if not wiek > 12 or kasa >= 30:
    print("Może wejść")
else:
    print("Nie może wejść")


# Uzupełnienie lekcji - "and" ma większą wagę (większy priorytet) od "or"
if True or False and False:
    print("Prawda")
else:
    print("Fałsz")
