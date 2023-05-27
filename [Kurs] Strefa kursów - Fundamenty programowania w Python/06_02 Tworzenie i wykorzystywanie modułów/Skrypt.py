from geometria import Okrag as Ok, oblicz_pi as pi

print("Wartość pi:", pi())

okrag = Ok(promien=10)
print("Obwod okregu:", round(okrag.obwod(), 2))