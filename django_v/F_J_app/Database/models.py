from django.db import models

# Create models here

class Customer(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email_address = models.CharField(max_length=100)

class Product(models.Model):
    name=  models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    cost = 

class Delivery(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(int)
    email_address = models.EmailField(True)
    delivery_address= models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)


class Order(models.Model):
    order_number = 
    date_ordered = 
    date_shipped = 
    status:  =
    customer_name =

class Cart(models.Model):