# Creates a customer for the database to store


class Customer:
    # initializes all class variables
    def __init__(self, username: str, password: str, email_address: str):
        self.username = username
        self.password = password
        self.email_address = email_address

    # Passes customer information to database
    def register():
        print("User registered")

    # Checks user credentials against database
    def login():
        print("Logged in")
