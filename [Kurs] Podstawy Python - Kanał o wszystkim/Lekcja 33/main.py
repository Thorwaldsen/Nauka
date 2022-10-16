import re

if re.match("^[rR]ok[-_=][0-9][0-9][0-9][0-9].$", "Rok-1992!"):
    print("Dopasowano!")
else:
    print("Słowa nie dopasowano!")