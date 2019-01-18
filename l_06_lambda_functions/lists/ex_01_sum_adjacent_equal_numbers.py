numbers = [float(num) for num in input().split(' ')]

isEqualPares = True
while isEqualPares:
    isEqualPares = False
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            numbers_sum = numbers[i] + numbers[i + 1]
            numbers[i] = numbers_sum
            numbers.pop(i + 1)
            isEqualPares = True
            break

print(" ".join(map(str, numbers)))
