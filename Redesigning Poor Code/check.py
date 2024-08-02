from models import Checkout

# A class to manage book checkouts in the library.

class CheckoutManager:
    def __init__(self):
        self.checkouts = []

# Records a book checkout by a user.
    def checkout_book(self, user_id, isbn):
        new_checkout = Checkout(user_id, isbn)
        self.checkouts.append(new_checkout)
        print(f"Checked out book: {isbn} to user: {user_id}")
        
# Lists all book checkouts.
    def list_checkouts(self):
        if not self.checkouts:
            print("No checkouts available.")
        for checkout in self.checkouts:
            print(checkout)
