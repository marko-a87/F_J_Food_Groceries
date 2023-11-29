import Order
import os
import sys
import Shopping_Cart

##Order_List should be initialized when the customer creates an account

class Order_List:
    def __init__(self):
        """Order_List constructor"""
        self.order_list = []
    

    def addOrder(self, order):
        """Adds an order to the list"""
        self.order_list.append(order)

    def viewOrders(self):
        """Views all orders"""
        for order in self.order_list:
            print(order)
    
    def cancelOrder(self, order):
        """Removes an order from the list"""
        if order in self.order_list:
            self.order_list.remove(order)
        print ("Order has been cancelled")