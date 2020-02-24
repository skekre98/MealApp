from django.db import models

class Users(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    email= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
