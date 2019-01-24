import re

matches = []

lowercase_a_m = list(map(chr, range(ord('a'), ord('m') + 1)))
lowercase_n_z = list(map(chr, range(ord('n'), ord('z') + 1)))

input_string = input()


def replace_non_alphanumeric_characters(string):
    return re.sub('[^a-z0-9]+', ' ', string)


def replace_multiple_spaces(string):
    return re.sub(' +', ' ', string)


def switch_characters(array):
    for i in range(len(array)):
        char = array[i]
        if char in lowercase_a_m:
            array[i] = lowercase_n_z[lowercase_a_m.index(char)]
        elif char in lowercase_n_z:
            array[i] = lowercase_a_m[lowercase_n_z.index(char)]
    return "".join(array)


while True:
    if "<p>" not in input_string:
        break
    start = input_string.index("<p>")
    end = input_string.index("</p>")
    if 0 <= start < end:
        match = input_string[start + len("<p>"):end]
        match = replace_non_alphanumeric_characters(match)
        match = replace_multiple_spaces(match)
        match = switch_characters(list(match))
        matches.append(match)
        input_string = input_string[end + len("<p>") + 1:]

print("".join(matches))
