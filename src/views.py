import requests
from django.shortcuts import render

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/quickAnswer"

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "01daf6b1dfmshd1effca0f6c3b8ap1e852cjsn15c8f2f00f35"
}


# Function to render Django forms
def query(request):
    # querystring = {"q":"How much vitamin c is in 2 apples%3F"}
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    return render(request, 'index.html')
