from django.db import models

# Create models here

class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(int)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email_address = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Product(models.Model):
    name=  models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    cost = models.FloatField()
    def __str__(self):
        return self.name

class Delivery(models.Model):
    email_address = models.EmailField(True)
    delivery_address= models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)


class Order(models.Model):
    order_number = models.IntegerField(int)
    date_ordered = models.DateField()
    date_shipped = models.DateField
    status  = models.BooleanField()
    customer_name =models.ForeignKey(Delivery, on_delete=models.CASCADE)
