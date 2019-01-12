dictionary = {}

while True:
    tokens = input()
    if 'end' == tokens:
        break

    [name, value] = tokens.split(' = ')

    if value.isdigit():
        dictionary[name] = int(value)
    elif value in dictionary:
        dictionary[name] = dictionary[value]

print(("\n".join([f'{key} === {value}' for key, value in dictionary.items()])))

