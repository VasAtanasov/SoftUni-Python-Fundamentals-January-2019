import re

REGEX = r"([0-9]+[A-Z][a-z]+(?:[0-9]|[A-z]){2,})"
n = int(input())

robots = []

is_manager = False
is_chain = True
manager = None

for _ in range(n):
    line = input()

    match = re.findall(REGEX, line)

    if not match:
        continue

    first = match[0]
    last = match[- 1]

    if len(robots) > 0 and first != robots[len(robots) - 1]:
        is_chain = False
        break

    if len(match) == 1 and line.endswith("!!"):
        is_manager = True
        manager = first
        if manager not in robots:
            robots.append(manager)
        continue

    if first not in robots:
        robots.append(first)

    if last not in robots:
        robots.append(last)

if is_chain:
    if is_manager:
        print(f"Found the manager!: {manager}")
    else:
        print("Did not find the manager!")
else:
    print("Broke the chain!")
print(f"Chain: {'->'.join(robots)}")
