chars = {}

max_index = 0

while True:
    input_string = input()
    if input_string == 'end':
        break

    tokens = input_string.split(":")

    char = tokens[0]
    indexes = [int(num) for num in tokens[1].split("/")]

    if char not in chars:
        chars[char] = []

    chars[char] += indexes

    if max_index < max(indexes):
        max_index = max(indexes)

strings_list = [""] * (max_index + 1)

for char, indexes in chars.items():
    for index in indexes:
        strings_list[index] = char

print("".join(strings_list))
