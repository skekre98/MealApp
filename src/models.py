from django.db import models

class Users(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
