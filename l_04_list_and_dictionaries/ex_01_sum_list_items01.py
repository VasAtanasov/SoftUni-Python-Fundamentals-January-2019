def sum_list(list_of_numbers):
    total_sum = 0
    for num in list_of_numbers:
        total_sum += num
    return total_sum


input_list = []

n = int(input())

for i in range(n):
    input_list.append(int(input()))

print(sum_list(input_list))
