input_numbers = [int(num) for num in input().split(' ')]

occurrences = [0] * 1000

for num in input_numbers:
    occurrences[num] = occurrences[num] + 1

for i in range(len(occurrences)):
    if occurrences[i] != 0:
        print(f"{i} -> {occurrences[i]}")
