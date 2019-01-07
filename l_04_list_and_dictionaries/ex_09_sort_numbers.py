numbers = [int(num) for num in input().split(' ')]
numbers.sort()

print(" <= ".join(map(str, numbers)))
