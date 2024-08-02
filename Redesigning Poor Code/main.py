from book import BookManager
from user import UserManager
from check import CheckoutManager
from storage import Storage

class LibraryManagementSystem:
    def __init__(self):
        self.book_manager = BookManager()
        self.user_manager = UserManager()
        self.checkout_manager = CheckoutManager()
        self.storage = Storage('library_data.json')
        self.load_data()

    def load_data(self):
        data = self.storage.load()
        if data:
            for book in data.get('books', []):
                self.book_manager.add_book(book['title'], book['author'], book['isbn'])
            for user in data.get('users', []):
                self.user_manager.add_user(user['user_id'], user['name'])

    def save_data(self):
        data = {
            "books": [book.__dict__ for book in self.book_manager.books],
            "users": [user.__dict__ for user in self.user_manager.users]
        }
        self.storage.save(data)

    def run(self):
        while True:
            print("\nLibrary Management System")
            print("1. Manage Books")
            print("2. Manage Users")
            print("3. Checkout Book")
            print("4. List Checkouts")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.manage_books()
            elif choice == "2":
                self.manage_users()
            elif choice == "3":
                self.checkout_book()
            elif choice == "4":
                self.list_checkouts()
            elif choice == "5":
                self.save_data()
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_books(self):
        while True:
            print("\nManage Books")
            print("1. Add Book")
            print("2. List Books")
            print("3. Update Book")
            print("4. Delete Book")
            print("5. Search Books")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                self.book_manager.add_book(title, author, isbn)
            elif choice == "2":
                self.book_manager.list_books()
            elif choice == "3":
                isbn = input("Enter book ISBN to update: ")
                title = input("Enter new title (leave blank to keep current): ")
                author = input("Enter new author (leave blank to keep current): ")
                self.book_manager.update_book(isbn, title, author)
            elif choice == "4":
                isbn = input("Enter book ISBN to delete: ")
                self.book_manager.delete_book(isbn)
            elif choice == "5":
                field = input("Search by (title/author/isbn): ")
                value = input(f"Enter {field}: ")
                results = self.book_manager.search_books(**{field: value})
                print("Search results:")
                for book in results:
                    print(book)
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_users(self):
        while True:
            print("\nManage Users")
            print("1. Add User")
            print("2. List Users")
            print("3. Update User")
            print("4. Delete User")
            print("5. Search Users")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                user_id = input("Enter user ID: ")
                name = input("Enter user name: ")
                self.user_manager.add_user(user_id, name)
            elif choice == "2":
                self.user_manager.list_users()
            elif choice == "3":
                user_id = input("Enter user ID to update: ")
                name = input("Enter new name (leave blank to keep current): ")
                self.user_manager.update_user(user_id, name)
            elif choice == "4":
                user_id = input("Enter user ID to delete: ")
                self.user_manager.delete_user(user_id)
            elif choice == "5":
                field = input("Search by (name/user_id): ")
                value = input(f"Enter {field}: ")
                results = self.user_manager.search_users(**{field: value})
                print("Search results:")
                for user in results:
                    print(user)
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    def checkout_book(self):
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkout: ")
        self.checkout_manager.checkout_book(user_id, isbn)

    def list_checkouts(self):
        self.checkout_manager.list_checkouts()

if __name__ == "__main__":
    lms = LibraryManagementSystem()
    lms.run()
