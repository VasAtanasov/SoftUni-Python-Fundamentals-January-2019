def get_sum(number, remainder):
    total_sum = 0
    for i in range(len(number)):
        num = int(number[i])
        total_sum += (num if num % 2 == remainder else 0)
    return total_sum


input_number = input()
input_number = input_number[1:] if input_number.startswith("-") else input_number

print(get_sum(input_number, 0) * get_sum(input_number, 1))
