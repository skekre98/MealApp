from django.db import models

class Users(models.Model):
    name= models.CharField(max_length=100, default= '')
    email= models.CharField(max_length=200, default= '')
    password= models.CharField(max_length=200, default= '')
    weight= models.IntegerField(default= -1) # pounds
    height= models.IntegerField(default= -1) # inches
    gender= models.IntegerField(default= -1) # 0:M or 1:F
    goal= models.DecimalField(max_digits=5, decimal_places=5, default= -1.0) # -0.5 represents losing 1/2 pound per week
    lifestyle= models.DecimalField(max_digits=5, decimal_places=5, default= -1.0) # 1.2, 1.375, 1.55, 1.725, or 1.9
    vegetarian= models.BooleanField(default= True)
    age= models.IntegerField(default= -1)
    calories_intake = models.IntegerField(default= -1)

