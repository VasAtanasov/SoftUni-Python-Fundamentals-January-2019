input_string = list(input())

for i in range(len(input_string) // 2):
    temp_char = input_string[i]
    input_string[i] = input_string[len(input_string) - i - 1]
    input_string[len(input_string) - i - 1] = temp_char

print("".join(input_string))
