import json
import os

# A class to handle file-based storage for the library data.
class Storage:
    def __init__(self, filename):
        self.filename = filename

# Saves data to the file.
    def save(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {self.filename}")
        
# Loads data from the file.
    def load(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, 'r') as file:
            data = json.load(file)
        print(f"Data loaded from {self.filename}")
        return data
