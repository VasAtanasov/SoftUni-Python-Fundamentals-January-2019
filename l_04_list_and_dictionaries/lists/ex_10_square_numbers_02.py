import math

list_data = list(map(int, input().split()))

sqrt_list = [x for x in list_data if x > 0 and math.sqrt(x) == int(math.sqrt(x))]
print(*sorted(sqrt_list, reverse=True))
