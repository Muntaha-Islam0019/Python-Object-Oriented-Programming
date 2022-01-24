# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, page_count, price):
        self.title = title
        # TODO: add properties
        self.autho = author
        self.page_count = page_count
        self.price = price
        self.__secret = "This is a secret."

    # TODO: create instance methods
    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount

# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.25)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.get_price())

# TODO: try setting the discount
print(b2.get_price())
b2.set_discount(0.25)
print(b2.get_price())

# TODO: properties with double underscores are hidden by the interpreter
# This will return an error. It's called name mangling. It adds the name of the class before the attribute. So the attribute mentioned earlier is not _Book__secret.
# print(b2.__secret)