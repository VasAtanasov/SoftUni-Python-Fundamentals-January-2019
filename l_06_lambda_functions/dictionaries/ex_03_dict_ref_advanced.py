dictionary = {}

while True:
    tokens = input()
    if 'end' == tokens:
        break

    name, value = tokens.split(' -> ')

    debug = ""

    if not value.isalpha():
        if name not in dictionary:
            dictionary[name] = []
        dictionary[name] += [int(num) for num in value.split(', ')]
    elif value in dictionary:
        dictionary[name] = []
        dictionary[name] += dictionary[value]

print(("\n".join([f'{key} === {", ".join(map(str, value))}' for key, value in dictionary.items()])))
