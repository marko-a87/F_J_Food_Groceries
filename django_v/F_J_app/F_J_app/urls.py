"""
URL configuration for F_J_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Authentication.views.Home import Home
from Authentication.views.Login import Login
from Authentication.views.Signup import Register
from Authentication.views.Main import Main
from Authentication.views.Delivery import Delivery
from Authentication.views.Product import Product

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("main/", Main.as_view(), name="main"),
    path("delivery/", Delivery.as_view(), name="delivery"),
    path("product/", Product.as_view(), name="product"),
]
"""
<button class='box' id='b1' onclick="location.href='Main.html'">Home</button>
            <button class='box' id='b2' onclick="location.href='product.html'">Product</button>
            <button class='box' id='b3' onclick="location.href='delivery.html'">Delivery</button>
            <button class='box' id='b4' onclick="location.href='#'">Pickup</button>
            <button class='box' id='b5' onclick="location.href='home.html'">Signin</button>
            <button class='box' id='b6' onclick="location.href='signout.html'">SignOut</button>
"""
