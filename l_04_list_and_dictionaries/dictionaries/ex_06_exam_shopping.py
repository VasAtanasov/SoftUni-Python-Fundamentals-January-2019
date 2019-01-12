import re

stock = {}

while True:
    in_line = input()
    if 'shopping time' == in_line:
        break

    [action, product, quantity] = re.split(r'\s+', in_line)

    if product not in stock:
        stock[product] = 0

    stock[product] += int(quantity)

while True:
    in_line = input()
    if 'exam time' == in_line:
        break

    [action, product, quantity] = re.split(r'\s+', in_line)
    quantity = int(quantity)

    if product not in stock:
        print(f'{product} doesn\'t exist')
    elif stock[product] == 0:
        print(f'{product} out of stock')
    elif stock[product] < quantity:
        stock[product] = 0
    else:
        stock[product] -= quantity

print(("\n".join([f'{product} -> {quantity}' for product, quantity in stock.items() if quantity > 0])))
