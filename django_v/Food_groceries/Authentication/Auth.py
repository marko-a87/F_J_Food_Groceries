""""Use django.contrib.auth to authorize a customer"""

"""

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "F_J_app.settings")
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "F_J_app.settings")
application = get_wsgi_application()


from Database.models import *
from Database.Database import *


class Auth:
    # initializes all class variables
    def __init(self):
        """Initializes empty constructor"""
        print("Constructor initialized")

    def register(self):
        """Method registers customer"""
        self.name: str = input("Enter your full name:")
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


"""Once the register button is called do this"""
"""auth = Auth()
auth.register()
c = Customer(
    name=auth.name,
    username=auth.user_name,
    password=auth.password,
    email_address=auth.email_address,
)
c.save()"""


def main():
    storage = Database()

    customer = Customer(
        username=input("Enter a username:"),
        password=storage.hashPassword(input("Enter a password")),
        email_address=input("Enter a email address"),
    )

    storage.register(customer)
    status = storage.login(input("Enter the username:"), input("Enter the password:"))
    if status:
        print("Logged in successfully")
    else:
        print("Not logged in")


if __name__ == "__main__":
    main()
