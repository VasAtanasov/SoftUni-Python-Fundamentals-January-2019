key = input()
value = input()
n = int(input())

result = {}

for i in range(n):
    tokens = input().split(' => ')
    currentKey = tokens[0]
    if key not in currentKey:
        continue
    if currentKey not in result:
        result[currentKey] = []
    result[currentKey] = list(filter(lambda a: value in a, tokens[1].split(";")))

for k, v in result.items():
    print(k + ":")
    if len(v) > 0:
        print("\n".join(map(lambda a: f'-{a}', v)))
