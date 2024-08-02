# A class representing a book in the library.
# title (str): The title of the book.
# author (str): The author of the book.
# isbn (str): The ISBN of the book.
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn})"

# A class representing a user of the library.
# user_id (str): The unique ID of the user.
# name (str): The name of the user.
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return f"User(user_id={self.user_id}, name={self.name})"

# A class representing a checkout of a book by a user.
# user_id (str): The ID of the user who checked out the book.
# isbn (str): The ISBN of the book that was checked out.
class Checkout:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn

    def __repr__(self):
        return f"Checkout(user_id={self.user_id}, isbn={self.isbn})"
