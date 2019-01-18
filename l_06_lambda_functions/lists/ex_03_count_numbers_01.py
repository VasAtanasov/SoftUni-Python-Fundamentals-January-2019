input_numbers = [int(num) for num in input().split(' ')]

count = {}
for number in input_numbers:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

result = ''
for key in sorted(count):
    result += f'{int(key)} -> {count[key]}\n'
print(result)
