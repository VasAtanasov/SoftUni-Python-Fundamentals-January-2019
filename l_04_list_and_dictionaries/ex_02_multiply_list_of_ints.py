numbers = [int(n) for n in input().split()]
p = int(input())

multiplied = [num * p for num in numbers]

print(' '.join(map(str, multiplied)))
