import re


def map_space_symbols(string):
    string = re.sub(r"\+|%20", " ", string).strip()
    return re.sub(r" +", " ", string).strip()


while True:
    pairs = {}
    input_string = input()
    if input_string == "END":
        break

    tokens = list(filter(lambda x: "=" in x and x is not None, re.split("[&?]", input_string)))

    for token in tokens:
        pair = token.split("=")
        key = map_space_symbols(pair[0])
        value = map_space_symbols(pair[1])

        if key not in pairs:
            pairs[key] = []

        pairs[key].append(value)

    for key, value in pairs.items():
        print(f"{key}=[{', '.join(value)}]", end="")
