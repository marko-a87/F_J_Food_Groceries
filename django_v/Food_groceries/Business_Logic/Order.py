"""

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "F_J_app.settings")
"""

import os
import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "F_J_app.settings")
application = get_wsgi_application()


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from Database.models import Cart,Order, Product, cartItem,OrderList
from Business_Logic.Shopping_Cart import Cart_Shop

class shopOrder:
    def vieworder(request):
        cart = Cart(request)
        if request.method == 'POST':
            name = request.POST.get("name")
            age = request.POST.get("age")
            phone_number = request.POST.get("phone_number")
            email_address = request.POST.get("email_address")
            delivery_address = request.POST.get("delivery_address")
        
            order = Order.objects.create(customer = request.customer, name=name, age=age, phone_number= phone_number, email_address=email_address, delivery_address= delivery_address)

            for thing in cart:
                product = thing['product']
                quantity = int(thing['quantity'])
                price = product.price * quantity

                thing = OrderList.objects.create(order=order, product=product, price=price)
            return redirect("orders.html")
        return redirect("cart.html")
