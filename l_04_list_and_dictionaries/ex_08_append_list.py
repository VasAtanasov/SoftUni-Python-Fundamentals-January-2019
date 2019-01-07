list_of_lists = input().split('|')
list_of_lists.reverse()

result = []

for item in list_of_lists:
    result += list(map(int, list(filter(None, item.split(' ')))))

print(" ".join(map(str, result)))
