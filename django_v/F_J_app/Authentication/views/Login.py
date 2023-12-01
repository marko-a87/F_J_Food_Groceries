from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password

# from store.models.customer import Customer
from django.views import View
from Database.models import *
from Database.Database import *


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get("return_url")
        return render(
            request,
            "login.html",
        )


    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        # Perform login authentication using the Database class or any other authentication mechanism
        storage = Database()
        status = storage.login(email, password)

        if status:
            # Login successful, redirect to the home page or the intended return_url
            return redirect(Login.return_url or "home")
        else:
            # Login failed, you may want to display an error message or redirect to the login page
            return render(request, "login.html", {"error": "Invalid credentials"})
