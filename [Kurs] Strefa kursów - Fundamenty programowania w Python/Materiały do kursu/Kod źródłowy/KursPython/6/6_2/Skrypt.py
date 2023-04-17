from geometria import Okrag as Ok, oblicz_pi as pi

print("Wartość PI:", pi())

okrag = Ok(promien=10)
print("Obwód okręgu:", round(okrag.obwod(), 2))
