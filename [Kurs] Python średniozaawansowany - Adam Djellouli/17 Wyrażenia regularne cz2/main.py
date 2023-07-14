import re

# +48-999-999-999

# \d to jest dowolna cyfra
# \D dowolny znak niebędący cyfrą

wzorNumeru = re.compile(r'[+]\d{1,4}-\d{3}-\d{3}-\d{3}')
znaleziono = wzorNumeru.search("Mój numer to +48-999-999-939")
znaleziono2 = wzorNumeru.search("Mój numer to +352-959-699-999")
znaleziono3 = wzorNumeru.search("Mój numer to +7-939-979-339")

print(znaleziono.group())
print(znaleziono2.group())
print(znaleziono3.group())

wzorNumeru = re.compile(r'([+]\d{1,4})-(\d{3}-\d{3}-\d{3})')
znaleziono = wzorNumeru.search("Mój numer to +48-999-999-939")

print(znaleziono.group(1))
print(znaleziono.group(2))

wzorNumeru = re.compile(r'([+]\d{1,4}-)?\d{3}-\d{3}-\d{3}')
znaleziono = wzorNumeru.search("Mój numer to 123-999-939")
znaleziono2 = wzorNumeru.search("Mój numer to +43-999-999-939")

print(znaleziono.group())
print(znaleziono2.group())
