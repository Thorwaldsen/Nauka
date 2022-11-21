import re

number = input()

print(re.sub("^00", "+", number))
