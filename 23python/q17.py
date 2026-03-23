#17. Implement a Library Management System that uses parameterized constructors to initialize books and members and destructors to log when books are removed.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __del__(self):
        print(f"Book '{self.title}' removed")


class Member:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Member '{self.name}' removed")


book1 = Book("Python Basics", "John")
member1 = Member("Alice")

del book1
del member1