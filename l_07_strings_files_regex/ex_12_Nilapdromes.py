while True:
    input_line = input()
    if input_line == 'end':
        break

    border = ""

    for i in range(len(input_line) // 2):
        current_border = input_line[:i + 1]
        if input_line.endswith(current_border):
            border = current_border

    core = input_line[len(border):-len(border)]

    if not core:
        continue

    print(core + border + core)
