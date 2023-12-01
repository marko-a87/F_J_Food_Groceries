""""Use django.contrib.auth to authorize a customer"""

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
# Creates a customer for the database to store


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
from django.contrib import messages
from django.db import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from Database.models import Cart, Product, cartItem

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir))

class Cart_Shop:

    def productlist(request):
        productlist = Product.objects.all()
        return render(request, "product.html", {"products":productlist})
    
    @login_required
    def viewCart(request):
        cart= request.customer.cart
        cartlist = cartItem.objects.filter(cart = cart)
        totalprice = sum(citem.product.cost * citem.quantity for citem in cartlist)
        holder = {"cart items": cartlist, "totalprice": totalprice }
        return render(request, "cart/shop_cart.html", holder)
    
    @login_required
    def add_product_to_cart(request, productid):
        product = Product.objects.get(pid = productid)
        cart, created = Cart.objects.get_or_create(customer = request.customer)
        cartlist, pitem = cartItem.objects.get_or_create(cart=cart, product=product)
        if not pitem:
            cartlist.quantity+=1
            cartlist.save()
            messages.success(request, "This product is added to your cart")
        return redirect("productlist")
    @login_required
    def remove_product_from_cart(request, productid):
        cartlist = get_object_or_404(Cart, id = productid)
    
        if cartlist.customer == request.customer:
            cartlist.delete()
            messages.success(request, "This product has been removed")
        return redirect("cart:viewCart")
