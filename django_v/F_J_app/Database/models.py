from django.db import models
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

   


class Order(models.Model):
    order_number = models.BigIntegerField(default=0)
    date_ordered = models.DateField(default=timezone.now)
    date_shipped = models.DateField()
    status = models.BooleanField()
    customer_name = models.ForeignKey(Delivery, on_delete=models.CASCADE)

   


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    