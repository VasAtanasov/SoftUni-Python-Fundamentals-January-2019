import re

PATTER = r'(^|(?<=\s))-?[0-9]+(\.[0-9]+)?($|(?=\s))'

numbers = input()
matches = re.finditer(PATTER, numbers)
for match in matches:
    print(match.group(), end=" ")
