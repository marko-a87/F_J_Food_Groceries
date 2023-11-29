from django.db import models
from django.urls import reverse

# Create models here


class Customer(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return self.username

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email_address=self.email_address):
            return True
        return False


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    cost = models.FloatField()

    def __str__(self):
        return self.name

    def AddtoCart():
        """Adds an item to the shopping cart"""
        print("Item added to cart")


class Delivery(models.Model):
    age = models.PositiveIntegerField(default=0)
    email_address = models.EmailField()
    delivery_address = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)

    def deliveryInfo():
        """Method saves delivery information to database"""


class Order(models.Model):
    order_number = models.BigIntegerField()
    date_ordered = models.DateField()
    date_shipped = models.DateField()
    status = models.BooleanField()
    customer_name = models.ForeignKey(Delivery, on_delete=models.CASCADE)

    def PlaceOrder(self):
        """Method places an order for customer"""
        print("Order has been placed")
        self.save()

    def CancelOrder():
        """Method cancels an order for customer"""
        print("Order has been canceled")

    def ViewOrder():
        """Method views the orders placed"""
        print("Display order")


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} + {self.product.name}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail")
