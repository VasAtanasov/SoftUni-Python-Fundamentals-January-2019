def get_sum(number, remainder):
    total_sum = 0
    while number != 0:
        total_sum += number % 10 if (number % 10) % 2 == remainder else 0
        number //= 10
    return total_sum


input_number = abs(int(input()))

print(get_sum(input_number, 0) * get_sum(input_number, 1))
