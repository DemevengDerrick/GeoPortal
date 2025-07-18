from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def users(response):
    return HttpResponse("Below is the list of all users")