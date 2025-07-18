from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(verbose_name= "Firstname", max_length=200)
    last_name = models.CharField(verbose_name= "Lastname", max_length=200)
    user_name = models.CharField(verbose_name= "Username", max_length=200)
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(verbose_name= "Password", max_length=200)

    def __str__(self):
        return f'User: {self.user_name}'