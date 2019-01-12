regions = {}


def calculate_giant_shell(shells):
    return sum(shells) - (sum(shells) // len(shells))


while True:
    in_line = input()
    if 'Aggregate' == in_line:
        break

    [region, shell] = filter(None, in_line.split(" "))

    if region not in regions:
        regions[region] = []

    if int(shell) not in regions[region]:
        regions[region].append(int(shell))

print(("\n".join(
    [f'{region} -> {", ".join(map(str, shells))} ({calculate_giant_shell(shells)})' for region, shells in
     regions.items()])))
