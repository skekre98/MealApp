import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from .login import ingest

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
    res = login.ingest(request)
    return HttpResponse('Login ingested')

# Function to render login page
def register(request):
    return render(request, 'register.html')

def ingest_register(request):
    # TODO
    print(request.POST)
    if request.method == 'POST':
        req_list = [request.POST.get('name'), request.POST.get('email'), request.POST.get('password'), request.POST.get('weight'), request.POST.get('height'), request.POST.get('gender'), request.POST.get('goal'), request.POST.get('lifestyle'), request.POST.get('vegetarian')]
        if all(r is not None for r in req_list):
            register=Users()
            register.name= req_list[0]
            register.email= req_list[1]
            register.password= req_list[2]
            register.weight= req_list[3]          
            register.height= req_list[4]

            str_gender = req_list[5]
            if str_gender == 'Male':
                register.gender= 0
            else:
                register.gender= 1

            register.goal= req_list[6]
      
            lifestyle_num = req_list[7]
            mult_fac = [1.2, 1.375, 1.55, 1.725, 1.9]  
            register.lifestyle = mult_fac[lifestyle_num-1]

            register.vegetarian = req_list[8]
            register.save()
            
            return render(request, 'register.html')  

    else:
            return render(request, 'register.html')