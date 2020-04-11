# Login API
from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

def user_login(request):
    input_email = request.POST.get('email')
    input_password = request.POST.get('password')

    try:
        user = Users.objects.get(email=input_email)
    except Exception:
        return render(request, 'invalid_login.html', {"errors":["- invalid email"]}) 

    if input_password != user.password:
        return render(request, 'invalid_login.html', {"errors":["- incorrect password"]}) 
    else:
        # TODO
        # build client portal
        return render(request, 'private/profile.html') 