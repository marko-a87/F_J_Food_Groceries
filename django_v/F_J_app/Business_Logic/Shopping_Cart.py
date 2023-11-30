# Creates a customer for the database to store
import os
import sys

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from Database.models import Cart

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(script_dir))

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from Database.models import Cart

class Cart_Shop:
    @login_required
    def cart_view(request):
        cartlist = Cart.objects.filter(customer = request.customer)
        totalprice = sum(citem.product.product_cost * citem.quantity for citem in cartlist)
        holder = {"cart items": cartlist, "totalprice": totalprice }
        return render(request, "cart/shop_cart.html", holder)
    @login_required
    def add_product_to_cart(request, product_name):
        cartlist = Cart.objects.filter(customer = request.customer, product=product_name)
        if cartlist:
            cartlist.quantity+=1
            cartlist.save()
            messages.success(request, "This product is added to your cart")
        else:
            Cart.objects.create(customer = request.customer, product=product_name)
            messages.success(request, "This product is added to your cart")
        return redirect("cart:cart_view")
    @login_required
    def remove_product_from_cart(request, item_id):
        cartlist = get_object_or_404(Cart, id = item_id)
    
        if cartlist.customer == request.customer:
            cartlist.delete()
            messages.success(request, "This product has been removed")
        return redirect("cart:cart_view")

<<<<<<< HEAD
   
=======
    def ViewCart():
        """Views item from the cart"""
        print("Views cart items")

    def RemovefromCart():
        """Removes item from the cart"""
        print("Removes item from cart")

    # Creates a customer for the database to store
    @login_required
    def cart_view(request):
        cartlist = Cart.objects.filter(customer=request.customer)
        totalprice = sum(
            citem.product.product_cost * citem.quantity for citem in cartlist
        )
        holder = {"cart items": cartlist, "totalprice": totalprice}
        return render(request, "cart/shop_cart.html", holder)

    @login_required
    def add_product_to_cart(request, product_name):
        cartlist = Cart.objects.filter(customer=request.customer, product=product_name)
        if cartlist:
            cartlist.quantity += 1
            cartlist.save()
            messages.success(request, "This product is added to your cart")
        else:
            Cart.objects.create(customer=request.customer, product=product_name)
            messages.success(request, "This product is added to your cart")
        return redirect("cart:cart_view")

    @login_required
    def remove_product_from_cart(request, item_id):
        cartlist = get_object_or_404(Cart, id=item_id)

        if cartlist.customer == request.customer:
            cartlist.delete()
            messages.success(request, "This product has been removed")
        return redirect("cart:cart_view")


print(Authentication.Customer.status)
>>>>>>> origin/django_testing
