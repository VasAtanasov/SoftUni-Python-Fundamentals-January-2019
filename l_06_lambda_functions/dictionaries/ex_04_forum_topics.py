topics = {}

while True:
    line = input()
    if 'filter' == line:
        break
    tokens = line.split(' -> ')
    topic = tokens[0]
    tags = tokens[1].split(", ")

    if topic not in topics:
        topics[topic] = []

    for tag in tags:
        if tag not in topics[topic]:
            topics[topic].append(tag)

tags = input().split(", ")

for key, value in topics.items():
    if all(elem in value for elem in tags):
        print(f'{key} | {", ".join(map(lambda a: f"#{a}", value))}')
