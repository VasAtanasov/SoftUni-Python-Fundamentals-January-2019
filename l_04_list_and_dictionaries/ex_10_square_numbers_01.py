import math

list_numbers = list(map(int, input().split(" ")))
list_sqrt = []

for number in list_numbers:
    if number > 0 and math.sqrt(number) == int(math.sqrt(number)):
        list_sqrt.append(number)

list_sqrt.sort(reverse=True)

print(" ".join(map(str, list_sqrt)))

