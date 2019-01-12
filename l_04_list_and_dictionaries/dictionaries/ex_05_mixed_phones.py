contacts = {}

while True:
    tokens = input()
    if 'Over' == tokens:
        break

    [first_value, second_value] = tokens.split(' : ')

    if second_value.isdigit():
        contacts[first_value] = second_value
    else:
        contacts[second_value] = first_value

print(("\n".join([f'{key} -> {value}' for key, value in sorted(contacts.items())])))
