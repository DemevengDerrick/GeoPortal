from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    username = request.session.get('username')
    if username:
        context = {"text":f"Welcome, {username}"}
        return render(request=request, template_name="map/map.html", context=context)
    else:
        return redirect('login_page')



