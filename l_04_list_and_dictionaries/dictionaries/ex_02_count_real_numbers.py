import re

numbers = [float(num) for num in re.split(r'\s+', input())]

counts = {}

for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

result = [f'{key} -> {counts[key]} times' for key in sorted(counts.keys())]
print("\n".join(result))
