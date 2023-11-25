class Customer:
    # initializes all class variables
    def __init__(self, user_name: str, password: str, email_address: str):
        self.user_name = user_name
        self.password = password
        self.email_address = email_address

    def __init__(self):
        """Empty constructor"""

    def register(self):
        """Method registers customer"""
        print("User registered")
        self.user_name: str = input("Enter the username: ")
        self.password: str = input("Enter the password: ")
        self.email_address: str = input("Enter the email address: ")
        """if username, password and email_address not in database then, create a customer instance"""
        """Otherwise say that """

        """If username exists already throw a username error"""
        """If password exists already throw a password error"""
        """If email exists already throw an email error"""

    # Checks user credentials against database
    def login(self):
        """If records from customer_type matches database then login"""
        if self.verifyLogin(self.user_name, self.password):
            print("Logged in")
            return True
        else:
            """Otherwise throw a Invalid credentials error"""
            print("Invalid credentials")
            print("Try again")
            return False

    # Verfies customer information based on whats stored in database
    def verifyLogin(self, username, password):
        # You can implement the code to verify customer login information here
        """If login status is successful then return true"""
        if "Shamar" in username and "gmail" in password:
            return True
        else:
            return False


client = Customer()
client.register()
status = client.login()
