n = int(input())

wardrobe = {}

for i in range(n):
    [color, value] = filter(None, input().split(" -> "))

    if color not in wardrobe:
        wardrobe[color] = {}

    for item in value.split(','):
        if item in wardrobe[color]:
            wardrobe[color][item] += 1
        else:
            wardrobe[color][item] = 1

searched_color, searched_item, *rest = filter(None, input().split(' ', 2))

for color, data in wardrobe.items():
    print(f'{color} clothes:')
    for item, quantity in wardrobe[color].items():
        if color == searched_color and item == searched_item:
            print(f'* {item} - {quantity} (found!)')
        else:
            print(f'* {item} - {quantity}')
