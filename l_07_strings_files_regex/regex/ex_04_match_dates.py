import re

REGEX = r"\b(?P<day>[0-9]{2})([.\\/-])(?P<month>[A-Z][a-z]{2})\2(?P<year>[0-9]{4})\b"

dates = input()
matches = re.finditer(REGEX, dates)

for match in matches:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")
