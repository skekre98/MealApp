import requests
from django.shortcuts import render

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/quickAnswer"

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "01daf6b1dfmshd1effca0f6c3b8ap1e852cjsn15c8f2f00f35"
}


# Function to render Django forms
def ingest(request):
    if request.method == 'POST':
        if request.POST.get('register-name'):
            # TODO
            # connect to sqlite
            # insert user info
            print('hi')
    return render(request, 'register.html')