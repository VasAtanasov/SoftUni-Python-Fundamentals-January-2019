numbers = [int(num) for num in input().split(' ') if int(num) >= 0]
numbers.reverse()

if not numbers:
    print('empty')
else:
    print(" ".join(map(str, numbers)))
