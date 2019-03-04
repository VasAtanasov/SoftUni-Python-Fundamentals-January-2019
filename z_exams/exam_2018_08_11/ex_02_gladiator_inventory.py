inventory = input().split(" ")


def add(element):
    if element not in inventory:
        inventory.append(element)


def delete(element):
    if element in inventory:
        inventory.remove(element)


def repair(element):
    if element in inventory:
        delete(element)
        add(element)


def upgrade(element):
    element_tokens = element.split("-")
    if element_tokens[0] in inventory:
        upgd = element_tokens[1]
        index = inventory.index(element_tokens[0])
        inventory.insert(index + 1, f"{element_tokens[0]}:{upgd}")


actions = {
    "Buy": add,
    "Trash": delete,
    "Repair": repair,
    "Upgrade": upgrade
}

while True:
    line = input()
    if "Fight!" == line:
        break

    tokens = line.split(" ")
    actions[tokens[0]](tokens[1])

print(" ".join(inventory))
