cities = {}

while True:
    line = input()
    if 'ready' == line:
        break

    tokens = line.split(":")
    city = tokens[0]
    transports = tokens[1].split(",")

    if city not in cities:
        cities[city] = {}

    for value in transports:
        transport, capacity = value.split("-")
        cities[city][transport] = int(capacity)

while True:
    line = input()
    if 'travel time!' == line:
        break

    city, people_count = line.split(" ")
    people_count = int(people_count)

    total_capacity = sum(capacity for capacity in cities[city].values())

    if people_count <= total_capacity:
        print(f'{city} -> all {people_count} accommodated')
    else:
        print(f'{city} -> all except {people_count - total_capacity} accommodated')
