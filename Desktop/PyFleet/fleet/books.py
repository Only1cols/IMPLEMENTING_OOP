class Book:
    category = "Fiction"  # shared class attribute

    def __init__(self, author, title):
        self.author = author  # instance attribute per object
        self.title = title

    def describe(self):  # instance method
        return f"{self.title} by {self.author}"


b1 = Book("Chinua Achebe", "Things fall apart")


print(b1.describe())
print(Book.category)
