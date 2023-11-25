# Creates a customer for the database to store
import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir))
from Authentication.System_UI import System_UI


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
        print("Logged in")
        System_UI.verifyLogin(self.user_name, self.password)
        """Otherwise throw a Invalid credentials error"""
