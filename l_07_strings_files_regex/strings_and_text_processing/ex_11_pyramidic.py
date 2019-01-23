lines = int(input())

input_lines = []

for line in range(lines):
    input_lines.append(input())

best_pyramid = []

for row in range(len(input_lines)):
    for col in range(len(input_lines[row])):
        current_char = input_lines[row][col]
        current_pyramid = [current_char]

        for i in range(row + 1, len(input_lines)):
            next_line = list(filter(lambda char: char == current_char, input_lines[i]))
            current_base = current_pyramid[-1]
            if len(current_base) + 2 <= len(next_line):
                current_pyramid.append(current_base + current_char * 2)

        if len(best_pyramid) <= len(current_pyramid):
            best_pyramid = current_pyramid

print("\n".join(best_pyramid))
