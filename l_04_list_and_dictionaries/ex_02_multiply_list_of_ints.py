numbers = [int(n) for n in input().split()]
p = int(input())

multiplied = []

for i in range(len(numbers)):
    multiplied.append(numbers[i] * p)

print(' '.join(map(str, multiplied)))
