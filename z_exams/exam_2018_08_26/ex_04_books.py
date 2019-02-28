class Book:
    def __init__(self, title, author, price, chapters=0):
        self.__title = title
        self.__author = author
        self.__price = price
        self.__chapters = chapters

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def price(self):
        return self.__price

    @property
    def chapters(self):
        return self.__chapters

    def __str__(self):
        return f"{self.title} with author {self.author}. Chapters in the book {self.chapters}"


class BookStore:
    def __init__(self):
        self.__in_stock = {}
        self.__sold = []
        self.__profit = 0

    def add_book(self, book):
        self.__in_stock[book.title] = book

    def sell_book(self, title):
        if title not in self.__in_stock:
            return False
        book = self.__in_stock[title]
        self.__profit += book.price
        self.__sold.append(book)
        return True

    def __str__(self):
        if self.__profit == 0:
            return "Bad day :("
        books = '\n'.join(map(lambda b: f"SOLD: {b}", self.__sold))
        return f"{books}\nMoney: {self.__profit:.2f}"


store = BookStore()


def is_number(number):
    try:
        float(number)
        return True
    except (TypeError, ValueError) as exe:
        return False


while True:
    line = input()
    if "on work" == line:
        break
    book_info = line.split(" -> ")
    book_params = book_info[0].split()

    if len(book_params) < 3 or not is_number(book_params[2]):
        continue

    book_title = book_params[0]
    book_author = book_params[1]
    book_price = float(book_params[2])
    if book_price <= 0:
        continue

    chapters_count = len(book_info[1].split(', '))

    book_obj = Book(book_title, book_author, book_price, chapters_count)

    store.add_book(book_obj)

while True:
    line = input()
    if "end work" == line:
        break

    if not store.sell_book(line):
        print("No such book here")

print(store)
