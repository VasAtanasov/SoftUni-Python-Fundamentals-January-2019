numbers = [int(num) for num in input().split(' ')]
limit = int(input())

print(" ".join(map(str, sorted(numbers, reverse=True)[:limit])))
