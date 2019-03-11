numbers = list(map(int, filter(None, input().split(" "))))


def in_range(index, length):
    return 0 <= index < length


def set_command(array):
    output = []
    for n in array:
        if n not in output:
            output.append(n)

    if output == array:
        print("It is a set")
    else:
        print(output)


def slice_command(array, from_index, to_index):
    if not in_range(from_index, len(array)) or not in_range(to_index + 1, len(array)):
        print("IndexError caught")
    else:
        print(array[from_index:to_index + 1])


def filter_command(array, token):
    result = None
    if "odd" == token:
        result = list(filter(lambda n: n % 2 != 0, array))
    elif "even" == token:
        result = list(filter(lambda n: n % 2 == 0, array))

    if result:
        print(result)


def multiply_command(array, number):
    print(list(map(lambda n: n * number, array)))


def divide_command(array, number):
    if number == 0:
        print("ZeroDivisionError caught")
    else:
        print(list(map(lambda n: n / number, array)))


def reverse_command(array):
    copy = array[:]
    copy.reverse()
    print(copy)


def sort_command(array):
    print(sorted(array))


rounds = 0

while True:
    line = input()
    if "exhausted" == line:
        break

    tokens = list(filter(None, line.split(" ")))
    command = tokens[0]

    if "set" == command:
        set_command(numbers)
    elif "slice" == command:
        slice_command(numbers, int(tokens[1]), int(tokens[2]))
    elif "filter" == command:
        filter_command(numbers, tokens[1])
    elif "multiply" == command:
        multiply_command(numbers, int(tokens[1]))
    elif "divide" == command:
        divide_command(numbers, int(tokens[1]))
    elif "reverse" == command:
        reverse_command(numbers)
    elif "sort" == command:
        sort_command(numbers)

    rounds += 1

print(f"I beat It for {rounds} rounds!")
