"""Order class represents actions user can make with site"""


class Order:
    def __init__(self, order_number, date_ordered, date_shipped, status, customer_name):
        self.order_number = order_number
        self.date_ordered = date_ordered
        self.date_shipped = date_shipped
        self.status = status
        self.customer_name = customer_name

    def PlaceOrder():
        """Method places an order for customer"""
        print("Order has been placed")

    def CancelOrder():
        """Method cancels an order for customer"""
        print("Order has been canceled")

    def ViewOrder():
        """Method views the orders placed"""
        print("Display order")
