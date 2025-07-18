from django.urls import path
from . import views
# create url patterns

urlpatterns = [
    path("", view=views.users, name="users")
]

