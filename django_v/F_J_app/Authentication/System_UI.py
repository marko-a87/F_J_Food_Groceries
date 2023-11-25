# System_UI verifies the login information of each customer class
import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir))
from Authentication.Customer import Customer


class System_UI:
    def __init__(self, status: bool):
        self.status = status

    # Verfies customer information based on whats stored in database
    def verifyLogin(self, username: str, password: str):
        # You can implement the code to verify customer login information here
        """If login status is successful then return true"""
        print("Login successful")
        """Otherwise return false"""


client = Customer()  # Creates customer instance
client.register()  # Register customer instance
client.login(client.user_name, client.password)  # login customer
"""if login is valid then set System_UI status to true"""


print(client.user_name)
