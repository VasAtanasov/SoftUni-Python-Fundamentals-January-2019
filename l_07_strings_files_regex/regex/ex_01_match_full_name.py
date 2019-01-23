import re

names = input()
REGEX = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

matches = re.findall(REGEX, names)
print(" ".join(matches))
