from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
#from store.models.customer import Customer
from django.views import View

class Login(View):
    return_url = None
    
    def get(self,request):
        Login.return_url = request.Get.get('return_url')
        return render(request,'login.html') 