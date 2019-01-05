number = int(input())
backslashes = "\\/"


def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length / len(string_to_expand)) + 1))[:length]


def row_mid_square(n):
    return f'-{repeat_to_length(backslashes, n * 2 - 2)}-'


def mid_square(n):
    for i in range(n - 2):
        print(row_mid_square(n))


print(repeat_to_length('-', number * 2))
mid_square(number)
print(repeat_to_length('-', number * 2))
