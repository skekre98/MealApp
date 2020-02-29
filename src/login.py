# Login API
from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

def user_login(request):
    # TODO
    input_email = request.POST.get('email')
    input_password = request.POST.get('password')

    try:
        user = Users.objects.get(email=input_email)
    except Exception:
        return HttpResponse("Invalid email")

    if input_password != user.password:
        return HttpResponse("Incorrect password")
    else:
        return HttpResponse("Login ingested")