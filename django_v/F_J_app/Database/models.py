from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create models here


class Customer(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return self.username

    def register(self):
        #       if(Customer.objects.filer())
        self.save()

    def isExists(self):
        return Customer.objects.filter(email_address=self.email_address)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    cost = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    age = models.PositiveIntegerField(default=0)
    email_address = models.EmailField()
    delivery_address = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)

    def deliveryInfo(self):
        """Method saves delivery information to database"""
        self.save()


class Category:
    def __init__(self, content_type):
        self.content_type = content_type
        self.product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def productCategories(self):
        self.save()


class Order(models.Model):
    order_number = models.BigIntegerField(default=0)
    date_ordered = models.DateField(default=timezone.now)
    date_shipped = models.DateField()
    status = models.BooleanField()
    customer_name = models.ForeignKey(Delivery, on_delete=models.CASCADE)

    def PlaceOrder(self):
        """Method places an order for customer"""
        print("Order has been placed")
        self.save()

    def CancelOrder(self):
        """Method cancels an order for customer"""
        print("Order has been canceled")
        self.delete()

    def ViewOrder(self):
        """Method views the orders placed"""
        print("Display order")
        self.objects.all().values()


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} + {self.product.name}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail")

    def AddtoCart(self):
        """Adds an item to the shopping cart"""
        print("Item added to cart")
        cart = Cart(self.product, self.quantity, self.customer)
        cart.save()
