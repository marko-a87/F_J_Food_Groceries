from django.db import models

# Create models here

class Customer(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email_address = models.CharField(max_length=100)

class Product(models.Model):
    name= 
    description = 
    cost = 

class Delivery(models.Model):
    name = 
    age = 
    email_address =
    delivery_address= 
    phone_number = 


class Order(models.Model):
    order_number = 
    date_ordered = 
    date_shipped = 
    status:  =
    customer_name =

class Cart(models.Model):