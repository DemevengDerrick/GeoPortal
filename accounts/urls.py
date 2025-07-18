from django.urls import path
from . import views

# create urls patterns

urlpatterns = [
    path('', view=views.login, name="login"),
    path('create_account', view=views.create_account, name="create_account")
]
