class Ticket:
    def __init__(self, full_name, destination, card=None):
        self.__full_name = full_name
        self.__card = card
        self.__destination = destination

    @property
    def price(self):
        regular_price = sum(map(ord, (list(self.__destination)))) / 100
        if self.__card:
            return regular_price / 2
        return regular_price

    def __str__(self):
        output = f"--{self.__destination}: {self.price:.2f}lv"
        if self.__card:
            output += f" (using card {self.__card})"
        return output


def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"


cards_by_full_name = {}
tickets_by_full_name = {}
cards_by_number = {}

n = int(input())
for _ in range(n):
    first_name, last_name, card_number = input().split()
    full_name = get_full_name(first_name, last_name)

    if full_name not in cards_by_full_name:
        cards_by_full_name[full_name] = []

    cards_by_full_name[full_name].append(card_number)

    if card_number not in cards_by_number:
        cards_by_number[card_number] = full_name


def issue_regular_ticket(full_name, destination):
    tickets_by_full_name[full_name].append(Ticket(full_name, destination))


def issue_ticket_with_discount(full_name, destination, card_number):
    tickets_by_full_name[full_name].append(Ticket(full_name, destination, card_number))


while True:
    line = input()
    if "time to leave!" == line:
        break

    create_ticket, first_name, last_name, destination, card_number = line.split()

    full_name = get_full_name(first_name, last_name)

    if full_name not in cards_by_full_name:
        cards_by_full_name[full_name] = []

    if full_name not in tickets_by_full_name:
        tickets_by_full_name[full_name] = []

    cards = cards_by_full_name[full_name]

    if card_number in cards:
        issue_ticket_with_discount(full_name, destination, card_number)
        continue

    is_valid_number = sum(map(int, list(card_number))) % 7 == 0

    if not is_valid_number:
        print(f"card {card_number} is not valid!")
        issue_regular_ticket(full_name, destination)
    elif card_number in cards_by_number:
        print(f"card {card_number} already exists for another passenger!")
        issue_regular_ticket(full_name, destination)
    else:
        cards_by_number[card_number] = full_name
        cards_by_full_name[full_name].append(card_number)
        issue_ticket_with_discount(full_name, destination, card_number)
        print(f"issuing card {card_number}")


def get_sum_of_tickets(tickets):
    return sum(list(map(lambda t: t.price, tickets)))


for person, tickets in sorted(tickets_by_full_name.items(), key=lambda x: -get_sum_of_tickets(x[1])):
    print(f"{person}:")
    print("\n".join(map(str, sorted(tickets, key=lambda t: -t.price))))
    print(f"total: {get_sum_of_tickets(tickets):.2f}lv")
