class Book:
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = float(price)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        names = author.split()
        if len(names) == 2 and names[1][0].isdigit():
            raise Exception("Author not valid!")
        self.__author = author

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if len(title) < 3:
            raise Exception("Title not valid!")
        self.__title = title

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise Exception("Price not valid!")
        self.__price = price

    def __str__(self):
        return f"Type: {self.__class__.__name__}\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}"


class GoldenEditionBook(Book):
    def __init__(self, author, title, price):
        Book.__init__(self, author, title, price)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise Exception("Price not valid!")
        self.__price = price + ((price * 30) / 100)


try:
    author = input()
    title = input()
    price = input()

    book = Book(author, title, price)
    golden_edition_book = GoldenEditionBook(author=author, title=title, price=price)

    print(book)
    print()
    print(golden_edition_book)

except Exception as exe:
    print(exe)
