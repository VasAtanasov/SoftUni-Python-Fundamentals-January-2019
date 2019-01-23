import re

PATTER = r'(?P<power>[2-9JQKA]|10)(?P<suit>[SHDC])'
input_line = input()

matches = re.finditer(PATTER, input_line)

for match in matches:
    power = match.group('power')
    suit = match.group('suit')
    print(power + suit, end=" ")
