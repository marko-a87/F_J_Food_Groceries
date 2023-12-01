from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password

# from store.models.customer import Customer
from django.views import View
from Database.models import *
from Database.Database import *


class Register(View):
    return_url = None

    def get(self, request):
        Register.return_url = request.GET.get("return_url")
        return render(
            request,
            "register.html",
        )

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # Perform registration using the Database class or any other registration mechanism
        storage = Database()
        customer = Customer(username=username, password=password, email_address=email)
        storage.register(customer)

        # Optionally, you can perform login after registration
        status = storage.login(username, password)

        if status:
            # Registration and login successful, redirect to the home page or the intended return_url
            return redirect(Register.return_url or "home")
        else:
            # Registration successful but login failed, you may want to display an error message or redirect to the login page
            return render(
                request,
                "login.html",
                {"error": "Registration successful, but login failed"},
            )
