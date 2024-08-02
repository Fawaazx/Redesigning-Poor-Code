from models import Book

# A class to manage books in the library.

class BookManager:
    def __init__(self):
        self.books = []

#Adds a new book to the library.
    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Added book: {new_book}")

# Lists all books in the library.
    def list_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(book)

# Updates the details of a book.
    def update_book(self, isbn, title=None, author=None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                print(f"Updated book: {book}")
                return
        print("Book not found")

# Deletes a book from the library.
    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Deleted book: {book}")
                return
        print("Book not found")

# Searches for books by given attributes.
    def search_books(self, **kwargs):
        results = []
        for book in self.books:
            if all(getattr(book, key) == value for key, value in kwargs.items()):
                results.append(book)
        return results
