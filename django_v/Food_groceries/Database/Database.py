import os
from django.contrib.auth.hashers import make_password, check_password


# Get the directory of the current script
<<<<<<< HEAD:django_v/Food_groceries/Database/Database.py
=======
script_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir))

>>>>>>> functionalities:django_v/F_J_app/Database/Database.py
from Database.models import *
from django.contrib.auth.hashers import make_password, check_password


class Database:
    """Stores user information
    Updates user information
    Deletes user information
    Reads user information"""

    def __init__(self):
        """Initializes an empty constructor"""

    def register(self, customer: object):
        """Register customer information"""
        if self.isExists(customer):
            print("Account already exists")
        else:
            customer.save()

    def isExists(self, customer: object):
        if Customer.objects.filter(email_address=customer.email_address):
            return True
        elif Customer.objects.filter(username=customer.username):
            return True
        # elif Customer.objects.filter(password = match)
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

    def hashPassword(self, password):
        hashed_pwd = make_password(password)
        return hashed_pwd

    def login(self, email: str, entered_password: str):
        # Retrieve the customer from the database based on the username
        try:
            customer = Customer.objects.get(email_address=email)

        except Customer.DoesNotExist:
            return False  # User does not exist

        # Check if entered_password matches the stored hashed password
        return check_password(entered_password, customer.password)

<<<<<<< HEAD:django_v/Food_groceries/Database/Database.py
    def matchPasswords(self, entered_password, hashed_password):
        return check_password(entered_password, hashed_password)
=======

"""
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
    print("Not logged in")"""
>>>>>>> functionalities:django_v/F_J_app/Database/Database.py
