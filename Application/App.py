import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir))

# Import the classes into the application code.
from Authentication.Customer import Customer
from Authentication.System_UI import System_UI
from Business_Logic.Category import Category
from Business_Logic.Order import Order
from Business_Logic.Product import Product
from Data_management_Security import Database


class App:
    # Creates instances of classes for the application
    def __init__(self):
        self.Customer = Customer()
        self.System_ui = System_UI()
        self.Category = Category()
        self.Order = Order()
        self.Product = Product()
        self.data = Database()


def main():
    # Driver code
    JandJ_app = App()
    JandJ_app.Customer.register()  # Registers the customer
    JandJ_app.Customer.login()  # Login the customer


if __name__ == "__main__":
    main()
