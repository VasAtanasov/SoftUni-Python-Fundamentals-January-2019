input_string = input()

chars = {}

for i in range(len(input_string)):
    char = input_string[i]

    if char not in chars:
        chars[char] = []

    chars[char].append(i)

for key, value in chars.items():
    print(f"{key}:{'/'.join(map(str, value))}")
