# Creates a customer for the database to store


class Customer:
    # initializes all class variables
    def __init__(self, name, age, phone_number, email_address, delivery_address):
        self.name = str(name)
        self.age = int(age)
        self.email_address = str(email_address)
        self.phone_number = str(phone_number)
        self.delivery_address = str(delivery_address)

    # Passes customer information to database
    def register():
        print("User registered")

    # Checks user credentials against database
    def login():
        print("Logged in")
