number = int(input())


def increasing_part(n):
    result = ''
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            result += repr(col) + ' '
        result = result[:-1]
        result += '\n'
    return result


def decreasing_part(n):
    result = ''
    for row in range(n, 1, -1):
        for col in range(1, row):
            result += repr(col) + ' '
        result = result[:-1]
        result += '\n'
    return result


def print_triangle(n):
    print(increasing_part(n), end="")
    print(decreasing_part(n), end="")


print_triangle(number)
