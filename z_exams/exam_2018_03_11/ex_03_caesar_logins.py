import re

PATTERN_VALID_LOGIN = re.compile(r"^(\\|/).+\1$")


def replace_alphanumeric_characters(string):
    return re.sub(r'[A-Za-z0-9]+', '', string)


def replace_non_alphanumeric_characters(string):
    return re.sub(r'[^A-Za-z0-9]+', '', string)


while True:
    line = input()
    if "/end/" == line:
        break

    if not PATTERN_VALID_LOGIN.match(line):
        continue

    login = replace_non_alphanumeric_characters(line)
    count_special = len(replace_alphanumeric_characters(line)) - 2
    login = "".join(list(map(lambda ch: chr(ord(ch) - count_special), list(login))))

    if not re.compile("^[A-Za-z0-9]+$").match(login):
        continue

    match = re.search(r"^([a-zA-Z0-9]+)\1([a-zA-Z0-9]+)\2\1\2$", login)

    if match:
        print(f"user: {match.group(1)}, pass: {match.group(2)}")
