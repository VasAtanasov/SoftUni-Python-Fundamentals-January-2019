def rotate_to_right(items):
    last_element = items[len(items) - 1]
    for i in range(len(items) - 1, 0, -1):
        items[i] = items[i - 1]
    items[0] = last_element


strings = input().split(' ')

rotate_to_right(strings)
print(' '.join(strings))
