import re

text = input()

diamond_pattern = '<\\w+>'

matches = re.findall(diamond_pattern, text)

result = ''
if matches:
    for match in matches:
        result += f'Found {sum(int(l) for l in match if l.isdigit())} carat diamond\n'
else:
    result = 'Better luck next time'

print(result)
