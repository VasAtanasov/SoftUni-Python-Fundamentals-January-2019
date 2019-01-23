import re

REGEX = r"\+359( |-)2\1[0-9]{3}\1[0-9]{4}\b"
phone_numbers = input()
matches = re.finditer(REGEX, phone_numbers)
phones = [match.group() for match in matches]

print(" ".join(phones))
