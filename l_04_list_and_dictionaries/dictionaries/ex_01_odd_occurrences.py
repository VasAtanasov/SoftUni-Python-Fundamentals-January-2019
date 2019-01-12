import re

words = list(map(lambda a: a.lower(), re.split(r'\s+', input())))

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

counts = {key: value for key, value in counts.items() if value % 2 == 1}

print(", ".join(counts.keys()))
