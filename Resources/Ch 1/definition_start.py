# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    # Initializer, not constructor
    def __init__(self, title) -> None:
        self.title = title


# TODO: create instances of the class
b1 = Book("Harry Potter")
b2 = Book("Feluda")

# TODO: print the class and property
print(b1)
print(b1.title)