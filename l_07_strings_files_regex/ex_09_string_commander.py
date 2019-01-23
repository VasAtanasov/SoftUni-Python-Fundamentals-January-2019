strings_list = list(input())


def shift_list_left(array, params):
    s = int(params[0])
    s %= len(array)
    shifted_array = array[s:] + array[:s]
    return shifted_array


def shift_list_right(array, params):
    s = int(params[0])
    s %= len(array)
    s *= -1
    shifted_array = array[s:] + array[:s]
    return shifted_array


def splice(array, params):
    start_index = int(params[0])
    end_index = int(params[1])
    return array[:start_index] + array[end_index + 1:]


def insert_char(array, params):
    index = int(params[0])
    char = params[1]
    array.insert(index, char)
    return array


commands = {
    "Left": shift_list_left,
    "Right": shift_list_right,
    "Delete": splice,
    "Insert": insert_char
}

while True:
    input_command = input()
    if input_command == 'end':
        break

    tokens = input_command.split(" ")

    command = tokens[0]
    strings_list = commands[command](strings_list, tokens[1:])

print("".join(strings_list))
