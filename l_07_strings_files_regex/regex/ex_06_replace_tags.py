import re

PATTERN = r"<a ?href=.*?>.*?<\/a>"

while True:
    input_string = input()
    if input_string == 'end':
        break

    matches = re.finditer(PATTERN, input_string)

    for match in matches:
        new_tag = match.group().replace("<a", "[URL").replace("</a", "[/URL").replace(">", "]")
        input_string = input_string.replace(match.group(), new_tag)

    print(input_string)
