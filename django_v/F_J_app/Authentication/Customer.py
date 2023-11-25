# Creates a customer for the database to store


class Customer:
    # initializes all class variables
    def __init__(self, name: str, password: str, email_address: str):
        self.name = name
        self.password = password
        self.email_address = email_address

    def register():
        """Method registers customer"""
        print("User registered")
        name: str = input("")
        password: str = input("")
        email_address: str = input("")
        customer_type = Customer(name, password, email_address)

    # Checks user credentials against database
    def login():
        """If records from customer_type matches database then login"""
        if customer_type == True:
            print("Logged in")
        else:
            print("Invalid credentials")
