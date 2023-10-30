from django.db import models
# Create your models here.

class Login(models.Model):
    user_name=models.CharField(max_length=25)
    password=models.CharField(max_length=25)

class Signup(models.Model):
    user_name=models.CharField(max_length=25)
    password=models.CharField(max_length=25)