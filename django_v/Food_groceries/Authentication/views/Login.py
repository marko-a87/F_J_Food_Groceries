from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.views import View
from django.urls import reverse


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get("return_url")
        return render(request, "login.html")

    def post(self, request):
        # Handle login logic here
        # ...
        if Login.return_url:
            return HttpResponseRedirect(Login.return_url)
        else:
            """Testing this route"""

    #       return HttpResponseRedirect(reverse("home"))
