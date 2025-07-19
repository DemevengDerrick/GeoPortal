from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users

# Create your views here.
def login_page(request):
    request.session.flush()
    return render(request, 'accounts/login.html')

def login_submit(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f'{email} : {password}')

        try:
            current_user = Users.objects.get(email=email, password=password)
            request.session['username'] = current_user.user_name
            return redirect('map')
        except Users.DoesNotExist:
            return render(request, 'accounts/login.html', context={"login_error": 'Invalid username or password!'})
    
    login_page(request)



def create_account(request):
    context = {"message": 'Account created successfully!'}
    return render(request, "accounts/create_account.html", context=context)
