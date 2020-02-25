import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from .login import user_login

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

# Function to render login page
def register(request):
    return render(request, 'register.html')

def ingest_register(request):
    # TODO
    print(request.POST)
    if request.method == 'POST':
        req_list = [request.POST.get('name'), request.POST.get('email'), request.POST.get('password'), request.POST.get('weight'), request.POST.get('feet'), request.POST.get('inches'), request.POST.get('gender'), request.POST.get('goal'), request.POST.get('lifestyle'), request.POST.get('vegetarian'), request.POST.get('age')]
        if all(r is not None for r in req_list):
            register=Users()
            register.name= req_list[0]
            register.email= req_list[1]
            register.password= req_list[2]
            register.weight= int(req_list[3])

            ft = int(req_list[4])
            inch = int(req_list[5])      
            register.height = 12*ft + inch

            str_gender = req_list[6]
            if str_gender == 'Male':
                register.gender= 0
            else:
                register.gender= 1

            register.goal= float(req_list[7][:4])
      
            lifestyle_dict = {'Sedentary': 1.2, 'Lightly Active': 1.375, 'Moderately Active': 1.55, 'Very Active': 1.725, 'Extremely Active': 1.9}
            register.lifestyle = lifestyle_dict[req_list[8]]

            veg_res = req_list[9]
            if veg_res == 'Yes':
                register.vegetarian = True
            else:
                register.vegetarian = False

            register.age = int(req_list[10])

            cal_burned = 0
            if str_gender == 'Male':
                cal_burned = 66 + (6.23 * register.weight) + (12.7 * register.height) - (6.8 * register.age)
            else:
                cal_burned = 655 + (4.35 * register.weight) + (4.7 * register.height) - (4.7 * register.age)
            cal_burned *= register.lifestyle
            register.calories_intake = int(cal_burned + (500*register.goal))
            register.save()
            
            return render(request, 'register.html')  

    else:
            return render(request, 'register.html')