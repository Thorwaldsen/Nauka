import re
Id = input()

right_format = re.match("^[A-Z][A-Z][0-9][0-9]$", Id)

if right_format:
    print("Searching")
else:
    print("Wrong format")