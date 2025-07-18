from django.urls import path
from . import views

# create url patterns

urlpatterns = [
    path("", views.index, name="index")
]

