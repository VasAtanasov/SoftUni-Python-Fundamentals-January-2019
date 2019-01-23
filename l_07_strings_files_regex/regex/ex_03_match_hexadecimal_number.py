import re

REGEX = "\\b(?:0x)?[0-9A-F]+\\b"

numbers = input()
matches = re.findall(REGEX, numbers)
print(" ".join(matches))
