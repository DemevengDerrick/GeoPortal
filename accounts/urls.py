from django.urls import path
from . import views

# create urls patterns

urlpatterns = [
    path('', view=views.login_page, name="login_page"),
    path('submit', view=views.login_submit, name="login_submit"),
    path('create_account', view=views.create_account, name="create_account")
]
