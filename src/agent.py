import os
import spacy
import requests
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

g_nlp = spacy.load("en_core_web_sm")

def analyze_taste(request):

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/detect"
    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': settings.SPOON_KEY,
        'content-type': "application/x-www-form-urlencoded"
    }

    payload = "tedelicious%20tacos.%20Only%20cheeseburger%20with%20cheddar%20are%20better%20than%20that.%20Bu%20tomatoes%20is%20so%20good!"

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

    cuisine_text = request.POST.get('cuisine')
    ing_text = request.POST.get('ingredients')
    
    return HttpResponse("Taste Analyzed")


