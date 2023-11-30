from django.db import models
<<<<<<< HEAD
from django.urls import reverse
=======
from django.utils import timezone

>>>>>>> origin/django_testing
# Create models here

class Customer(models.Model):
    name = models.CharField(max_length=50)
<<<<<<< HEAD
    age = models.PositiveIntegerField(int)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email_address = models.CharField(max_length=100)
    def __str__(self):
        return self.username
=======
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return self.username

   

>>>>>>> origin/django_testing

class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    
class Product(models.Model):
<<<<<<< HEAD
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    product_name=  models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    product_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.product_name

class Delivery(models.Model):
    email_address = models.EmailField(True)
    delivery_address= models.CharField(max_length=80)
=======
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    cost = models.FloatField(default=0.0)


class Delivery(models.Model):
    age = models.PositiveIntegerField(default=0)
    email_address = models.EmailField()
    delivery_address = models.CharField(max_length=80)
>>>>>>> origin/django_testing
    phone_number = models.CharField(max_length=20)

    def deliveryInfo(self):
        """Method saves delivery information to database"""
        self.save()


class Category:
    def __init__(self, content_type):
        self.content_type = content_type
        self.product = models.ForeignKey(Product, on_delete=models.CASCADE)

   


class Order(models.Model):
<<<<<<< HEAD
    order_number = models.IntegerField(int)
    date_ordered = models.DateField()
    date_shipped = models.DateField
    status  = models.BooleanField()
    customer_name =models.ForeignKey(Delivery, on_delete=models.CASCADE)

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.quantity} + {self.product.name}'
    def get_absolute_url(self):
        return reverse("cart:shop_cart")
=======
    order_number = models.BigIntegerField(default=0)
    date_ordered = models.DateField(default=timezone.now)
    date_shipped = models.DateField()
    status = models.BooleanField()
    customer_name = models.ForeignKey(Delivery, on_delete=models.CASCADE)

   


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    
>>>>>>> origin/django_testing
