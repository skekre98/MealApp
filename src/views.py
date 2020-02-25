import requests
from django.shortcuts import render
from django.http import HttpResponse

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/quickAnswer"

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "01daf6b1dfmshd1effca0f6c3b8ap1e852cjsn15c8f2f00f35"
}


# Function to render home
def home(request):
    return render(request, 'home.html')

# Function to render login page
def login(request):
    return render(request, 'login.html')

def ingest_login(request):
    # TODO
    return HttpResponse('Login ingested')

# Function to render login page
def register(request):
    return render(request, 'register.html')

def ingest_register(request):
    # TODO
    return HttpResponse('Register ingested')