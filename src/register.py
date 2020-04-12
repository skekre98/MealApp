from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

# function for form validation
def error_handler(req_list, pass2):
    errors = []

    # password did not match
    if req_list[2] != pass2:
        errors.append('- passwords did not match')
    
    # age was not a number 
    if not req_list[10].isdigit():
        errors.append('- age must be a number')
    
    # weight was not a number 
    if not req_list[3].isdigit():
        errors.append('- weight must be a number')
    
    # height was not a number 
    if not req_list[4].isdigit() or not req_list[5].isdigit():
        errors.append('- height must be a number')
    
    return errors

def ingest_register(request):
    if request.method == 'POST':
        req_list = [request.POST.get('name'), 
                    request.POST.get('email'), 
                    request.POST.get('password'), 
                    request.POST.get('weight'), 
                    request.POST.get('feet'), 
                    request.POST.get('inches'), 
                    request.POST.get('gender'), 
                    request.POST.get('goal'), 
                    request.POST.get('lifestyle'), 
                    request.POST.get('vegetarian'), 
                    request.POST.get('age')
                    ]
        
        errors = error_handler(req_list, request.POST.get('repassword'))
        if errors:
            content = {"errors": errors}
            return render(request, 'invalid_reg.html', content) 

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

        register.goal= round(float(req_list[7][:4]),4)
    
        lifestyle_dict = {'Sedentary': 1.2, 'Lightly Active': 1.375, 'Moderately Active': 1.55, 'Very Active': 1.725, 'Extremely Active': 1.9}
        register.lifestyle = round(lifestyle_dict[req_list[8]],4)

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
        cal_burned += (500*register.goal)
        register.calories_intake = int(cal_burned)

        register.save()
        
        return render(request, 'private/taste_test.html')  
    else:
        return render(request, 'register.html')