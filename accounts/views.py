from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

# Create your views here.

def login(request):
    user = Users.objects.all()[0]
    context = {"user":user}
    return render(request, "accounts/login.html", context=context)

def create_account(request):
    context = {"message": 'Account created successfully!'}
    return render(request, "accounts/create_account.html", context=context)
