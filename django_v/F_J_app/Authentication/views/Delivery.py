from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password

# from store.models.customer import Customer
from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect


class Delivery(View):
    return_url = None

    def get(self, request):
        Delivery.return_url = request.GET.get("return_url")
        return render(
            request,
            "delivery.html",
        )
