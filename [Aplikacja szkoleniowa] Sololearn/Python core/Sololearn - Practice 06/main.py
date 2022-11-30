import re

word = input()

word_lenght = len(word)

match = re.match(r"^m([a-z][a-z])e$", word)

if match:
    print("Match")
else:
    print("No match")