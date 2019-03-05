from collections import OrderedDict


class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price


class PC:
    def __init__(self, name, model, price):
        self.__name = name
        self.__model = model
        self.__price = price
        self.__products = []

    @property
    def total_price(self):
        return sum(list(map(lambda p: p.price, self.__products))) + self.__price

    def add(self, product):
        self.__products.append(product)

    def remove(self, product_name):
        self.__products = list(filter(lambda p: p.name != product_name, self.__products))

    def __str__(self):
        header = f"PC: {self.__name} {self.__model} {self.total_price:.2f}\n"
        if not self.__products:
            return header + "--- Products: None"
        else:
            return header + f"--- Products: " + ", ".join(list(map(lambda p: p.name, self.__products)))


products = OrderedDict()
pcs = OrderedDict()

while True:
    line = input()
    if "PC" == line:
        break
    name, price = line.split(' ')
    products[name] = Product(name=name, price=float(price))


def add_pc(name, model, price):
    if name not in pcs:
        pcs[name] = PC(name=name, model=model, price=float(price))


def remove_pc(name):
    pcs.pop(name, None)


def add_product(pc_name, product_name):
    if pc_name in pcs and product_name in products:
        pcs[pc_name].add(products[product_name])


def remove_product(pc_name, product_name):
    if pc_name in pcs and product_name in products:
        pcs[pc_name].remove(product_name)


def print_pcs():
    for pc in pcs.values():
        print(pc)


actions = {
    "ADDPC": add_pc,
    "REMOVEPC": remove_pc,
    "ADDPRODUCT": add_product,
    "REMOVEPRODUCT": remove_product,
    "PRINT": print_pcs,
}

while True:
    line = input()
    if "END" == line:
        break
    tokens = line.split(" ")
    actions[tokens[0]](*tokens[1:])
