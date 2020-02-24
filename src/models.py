from django.db import models

class Users(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    weight= models.IntegerField() # pounds
    height= models.IntegerField() # inches
    gender= models.CharField(max_length=1) # M or F
    goal= models.DecimalField(max_digits=3, decimal_places=2) # -0.5 represents losing 1/2 pound per week
    lifestyle= models.IntegerField() # some number 1 through 5
    vegetarian= models.BooleanField()
