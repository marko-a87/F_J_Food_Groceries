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


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    cost = models.FloatField(default=0.0)
    image = models.ImageField()


class Order(models.Model):
    ORDERED = "ordered"
    SHIPPED = "shipped"
    STATUS_TYPE = (
        (ORDERED, "Ordered"), 
        (SHIPPED, "Shipped")
    )
    customer = models.ForeignKey(Customer, related_name="orders", blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=100)
    delivery_address = models.CharField(max_length=80)

    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    amountpaid= models.IntegerField(blank= True, null= True)

    status = models.CharField(max_length=20, choices=STATUS_TYPE, default=ORDERED)

    def deliveryInfo(self):
        """Method saves delivery information to database"""
        self.save()


class Category:
    def __init__(self, content_type):
        self.content_type = content_type
        self.product = models.ForeignKey(Product, on_delete=models.CASCADE)


class OrderList(models.Model):
    order = models.ForeignKey(Order, related_name="products", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="products", on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)


class cartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="cartItem")

Customer.cart=property(lambda u:Cart.objects.get_or_create(customer=u)[0])
