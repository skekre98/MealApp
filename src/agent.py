import spacy
from django.shortcuts import render
from django.http import HttpResponse

g_nlp = spacy.load("en_core_web_sm")

def analyze_taste(request):
    cuisine_text = request.POST.get('cuisine')
    ing_text = request.POST.get('ingredients')
    
    return HttpResponse("Taste Analyzed")


