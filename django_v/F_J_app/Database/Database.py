import os
import sys

from django.core.wsgi import get_wsgi_application
from django.urls import reverse


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "F_J_app.settings")
application = get_wsgi_application()

from Database.models import *


class Database:
    """Stores user information
    Updates user information
    Deletes user information
    Reads user information"""

    def __init__(self):
        """Initializes an empty constructor"""

    def register(self, customer: object):
        """Register customer information"""
        customer.save()

    def isExists(self, customer: object):
        return Customer.objects.filter(email_address=customer.email_address)

    def login(self, username: str, password: str):
        # Method returns a status when user puts in login credentials
        if Customer.objects.filter(username=username, password=password):
            return True
        else:
            return False

    def __str__(self):
        return self.name

    def productCategories(self, category: object):
        """Save category to the database"""
        category.save()

    def PlaceOrder(self, order: object):
        """Method places an order for customer"""
        print("Order has been placed")
        order.save()

    def CancelOrder(self, order: object):
        """Method cancels an order for customer"""
        print("Order has been canceled")
        order.delete()

    def ViewOrder(self):
        """Method views the orders placed"""
        print("Display order")
        return Order.objects.all().values()

    def __str__(self):
        return f"{self.quantity} + {self.product.name}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail")

    def AddtoCart(self):
        """Adds an item to the shopping cart"""
        print("Item added to cart")
        cart = Cart(Cart.product, Cart.quantity, Cart.customer)
        cart.save()
