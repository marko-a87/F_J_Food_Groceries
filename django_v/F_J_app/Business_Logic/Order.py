"""Order class represents actions user can make with site"""
import random
from datetime import date

class Order:
    def __init__(
        self,
        delivery: bool, #whether the order is delivery or not (pickup)
        address: str, #address of the customer
        cost: int
    ):
        self.order_number = random.randomint(1000,9999)
        self.date_ordered = date.today()
        self.cost = cost
        self.delivery=delivery
        if delivery:
            self.estimated_delivery = date.tomorrow().tomorrow()
            self.address = address
        self.estimated_pickup = date.today()
