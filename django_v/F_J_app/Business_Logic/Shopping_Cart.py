# Creates a customer for the database to store
import os
import sys
import Order
import Order_List
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir))
import Authentication.Customer


class Shopping_Cart:
    def __init__(self, quantity: int, totalcost: int) -> None:
        """Shopping_Cart constructor"""
        self.quantity = quantity
        self.totalcost = totalcost

    def ViewCart():
        """Views item from the cart"""
        print("Views cart items")

    def RemovefromCart():
        """Removes item from the cart"""
        print("Removes item from cart")

    def PlaceOrder(totalcost: int, delivery: bool, address: str): #Code Needs to be written to extract this information from the customer
        """Places an order for customer"""
        order= Order.Order(delivery, address, totalcost)
        Order_List.addOrder(order)
        print("Order has been placed")
        #TBD: sends message to store

print(Authentication.Customer.status)
