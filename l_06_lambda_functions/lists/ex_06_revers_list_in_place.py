numbers = [int(num) for num in input().split(' ')]

for i in range(len(numbers) // 2):
    temp = numbers[i]
    numbers[i] = numbers[- 1 - i]
    numbers[- 1 - i] = temp

print(" ".join(map(str, numbers)))
