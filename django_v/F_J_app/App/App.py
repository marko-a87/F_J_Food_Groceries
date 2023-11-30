import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir))

# Import the classes into the application code.
from F_J_app.Authentication.Customer import Customer
from F_J_app.Business_Logic.Category import Category
from F_J_app.Business_Logic.Order import Order
from F_J_app.Business_Logic.Product import Product
from F_J_app.Database import Database


class App:
    # Creates instances of classes for the application
    def __init__(self):
        self.Customer = Customer()
        self.Category = Category()
        self.Order = Order()
        self.Product = Product()
        self.data = Database()


def main():
    # Driver code
    JandJ_app = App()
    JandJ_app.Customer.register()  # Registers the customer
    JandJ_app.Customer.login()  # Login the customer


"""Calls main function"""
if __name__ == "__main__":
    main()
