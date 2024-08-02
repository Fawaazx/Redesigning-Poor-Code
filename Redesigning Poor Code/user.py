from models import User
# A class to manage users in the library.
class UserManager:
    def __init__(self):
        self.users = []

# Adds a new user to the library.
    def add_user(self, user_id, name):
        new_user = User(user_id, name)
        self.users.append(new_user)
        print(f"Added user: {new_user}")

# Lists all users in the library.
    def list_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            print(user)

# Updates the details of a user.
    def update_user(self, user_id, name=None):
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                print(f"Updated user: {user}")
                return
        print("User not found")

# Deletes a user from the library.
    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print(f"Deleted user: {user}")
                return
        print("User not found")

# Searches for users by given attributes.
    def search_users(self, **kwargs):
        results = []
        for user in self.users:
            if all(getattr(user, key) == value for key, value in kwargs.items()):
                results.append(user)
        return results
